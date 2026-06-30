#!/usr/bin/env python3
"""
Servidor backend para o Sistema de Gestão de Escala Don Garcia.
Armazena todos os dados (setores, funcionários, escalas) em um arquivo JSON.
Todos os dispositivos que acessam o link compartilham os mesmos dados automaticamente.
"""
import json
import os
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "dados_nuvem.json")
INDEX_FILE = os.path.join(BASE_DIR, "index.html")
PORT = 8099

# Lock para evitar conflito de escrita simultânea (até 3 pessoas)
_lock = threading.Lock()


def ler_dados():
    """Lê os dados do arquivo JSON. Retorna estrutura vazia se não existir."""
    if not os.path.exists(DATA_FILE):
        return {"setores": [], "funcionarios": [], "escalas": [], "versao": 0}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"setores": [], "funcionarios": [], "escalas": [], "versao": 0}


def salvar_dados(dados):
    """Salva os dados no arquivo JSON de forma atômica."""
    with _lock:
        atual = ler_dados()
        # Incrementa versão para o sistema de sincronização detectar mudanças
        dados["versao"] = atual.get("versao", 0) + 1
        tmp = DATA_FILE + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        os.replace(tmp, DATA_FILE)
        return dados["versao"]


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass  # silencia logs

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
        # Serve o index.html na raiz
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
                # Mantém apenas as chaves esperadas
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
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Servidor Don Garcia rodando na porta {PORT}")
    print(f"Arquivo de dados: {DATA_FILE}")
    server.serve_forever()


if __name__ == "__main__":
    main()
