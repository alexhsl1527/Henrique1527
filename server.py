#!/usr/bin/env python3
"""
Servidor backend para o Sistema de Gestão de Escala Don Garcia.

ARMAZENAMENTO PERMANENTE:
Os dados (setores, funcionários, escalas) são guardados no próprio repositório
do GitHub (arquivo dados_nuvem.json), usando a API do GitHub. Assim os dados
NUNCA se perdem, mesmo quando o servidor do Render hiberna e reinicia (o disco
do plano grátis do Render é temporário e apaga arquivos locais a cada restart).

Configuração via variáveis de ambiente (definidas no painel do Render):
  GITHUB_TOKEN  -> token de acesso pessoal do GitHub (obrigatório p/ salvar)
  GITHUB_REPO   -> "usuario/repositorio" (ex: alexhsl1527/Henrique1527)
  GITHUB_BRANCH -> branch (padrão: main)
  DATA_PATH     -> caminho do arquivo de dados no repo (padrão: dados_nuvem.json)

Se GITHUB_TOKEN não estiver definido, cai para um arquivo local (modo teste).
"""
import json
import os
import base64
import threading
import urllib.request
import urllib.error
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "dados_nuvem.json")
INDEX_FILE = os.path.join(BASE_DIR, "index.html")
PORT = int(os.environ.get("PORT", 8099))

# --- Configuração do GitHub como armazenamento permanente ---
GH_TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()
GH_REPO = os.environ.get("GITHUB_REPO", "alexhsl1527/Henrique1527").strip()
GH_BRANCH = os.environ.get("GITHUB_BRANCH", "main").strip()
GH_PATH = os.environ.get("DATA_PATH", "dados_nuvem.json").strip()
GH_API = f"https://api.github.com/repos/{GH_REPO}/contents/{GH_PATH}"

_lock = threading.Lock()

# Cache em memória: serve leituras rápidas e guarda o "sha" do arquivo no GitHub
# (necessário para atualizar o arquivo). Também reduz o número de chamadas à API.
_cache = {"dados": None, "sha": None}

ESTRUTURA_VAZIA = {"setores": [], "funcionarios": [], "escalas": [], "versao": 0}


# ------------------------------------------------------------------
# Camada de armazenamento no GitHub
# ------------------------------------------------------------------
def _gh_request(method, url, body=None):
    """Faz uma requisição autenticada à API do GitHub."""
    headers = {
        "Authorization": f"Bearer {GH_TOKEN}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "don-garcia-app",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    if data is not None:
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _gh_ler():
    """Lê dados_nuvem.json do GitHub. Guarda o sha no cache. Retorna (dados, ok)."""
    try:
        url = f"{GH_API}?ref={GH_BRANCH}"
        info = _gh_request("GET", url)
        conteudo = base64.b64decode(info["content"]).decode("utf-8")
        dados = json.loads(conteudo)
        _cache["sha"] = info.get("sha")
        # garante chaves
        for k in ESTRUTURA_VAZIA:
            dados.setdefault(k, ESTRUTURA_VAZIA[k] if not isinstance(ESTRUTURA_VAZIA[k], list) else [])
        return dados, True
    except urllib.error.HTTPError as e:
        if e.code == 404:
            # arquivo ainda não existe no repo
            _cache["sha"] = None
            return dict(ESTRUTURA_VAZIA), True
        print(f"[GitHub] erro ao ler: {e}")
        return None, False
    except Exception as e:
        print(f"[GitHub] erro ao ler: {e}")
        return None, False


def _gh_salvar(dados):
    """Grava dados_nuvem.json no GitHub (cria ou atualiza). Retorna True/False."""
    try:
        conteudo = json.dumps(dados, ensure_ascii=False, indent=2)
        b64 = base64.b64encode(conteudo.encode("utf-8")).decode("ascii")
        body = {
            "message": f"Atualiza dados (versao {dados.get('versao')})",
            "content": b64,
            "branch": GH_BRANCH,
        }
        if _cache.get("sha"):
            body["sha"] = _cache["sha"]
        info = _gh_request("PUT", GH_API, body)
        _cache["sha"] = info.get("content", {}).get("sha")
        return True
    except urllib.error.HTTPError as e:
        # conflito de sha (outra escrita simultânea): recarrega sha e tenta 1x
        if e.code in (409, 422):
            _gh_ler()
            try:
                if _cache.get("sha"):
                    body["sha"] = _cache["sha"]
                info = _gh_request("PUT", GH_API, body)
                _cache["sha"] = info.get("content", {}).get("sha")
                return True
            except Exception as e2:
                print(f"[GitHub] erro ao salvar (retry): {e2}")
                return False
        print(f"[GitHub] erro ao salvar: {e}")
        return False
    except Exception as e:
        print(f"[GitHub] erro ao salvar: {e}")
        return False


# ------------------------------------------------------------------
# Camada de armazenamento local (fallback quando não há token)
# ------------------------------------------------------------------
def _local_ler():
    if not os.path.exists(DATA_FILE):
        return dict(ESTRUTURA_VAZIA)
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return dict(ESTRUTURA_VAZIA)


def _local_salvar(dados):
    tmp = DATA_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    os.replace(tmp, DATA_FILE)
    return True


# ------------------------------------------------------------------
# Interface unificada de dados
# ------------------------------------------------------------------
def ler_dados():
    """Retorna os dados atuais (do cache, senão do GitHub/local)."""
    if _cache["dados"] is not None:
        return _cache["dados"]
    if GH_TOKEN:
        dados, ok = _gh_ler()
        if not ok:
            dados = _local_ler()  # fallback de emergência
    else:
        dados = _local_ler()
    _cache["dados"] = dados
    return dados


def salvar_dados(dados):
    """Salva os dados de forma permanente e incrementa a versão."""
    with _lock:
        atual = ler_dados()
        dados["versao"] = atual.get("versao", 0) + 1
        _cache["dados"] = dados  # atualiza cache imediatamente
        # sempre grava uma cópia local (backup rápido)
        try:
            _local_salvar(dados)
        except Exception:
            pass
        # grava no GitHub (permanente)
        if GH_TOKEN:
            _gh_salvar(dados)
        return dados["versao"]


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def _json(self, obj, status=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self._cors()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        if self.path.startswith("/api/data"):
            self._json(ler_dados())
            return
        if self.path.startswith("/api/versao"):
            self._json({"versao": ler_dados().get("versao", 0)})
            return
        if self.path.startswith("/api/status"):
            self._json({"github": bool(GH_TOKEN), "repo": GH_REPO})
            return
        if self.path in ("/", "/index.html"):
            try:
                with open(INDEX_FILE, "rb") as f:
                    body = f.read()
                self.send_response(200)
                self._cors()
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            except Exception:
                self.send_error(404)
            return
        self.send_error(404)

    def do_POST(self):
        if self.path.startswith("/api/data"):
            try:
                length = int(self.headers.get("Content-Length", 0))
                raw = self.rfile.read(length)
                dados = json.loads(raw.decode("utf-8"))
                limpo = {
                    "setores": dados.get("setores", []),
                    "funcionarios": dados.get("funcionarios", []),
                    "escalas": dados.get("escalas", []),
                }
                versao = salvar_dados(limpo)
                self._json({"success": True, "versao": versao})
            except Exception as e:
                self._json({"success": False, "error": str(e)}, status=500)
            return
        self.send_error(404)


def main():
    # pré-carrega os dados na inicialização
    ler_dados()
    modo = "GitHub (permanente)" if GH_TOKEN else "arquivo local (teste)"
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Servidor Don Garcia na porta {PORT} | armazenamento: {modo}")
    server.serve_forever()


if __name__ == "__main__":
    main()
