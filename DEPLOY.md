# 🚀 Deploy Permanente no Render.com (GRÁTIS)

Este guia mostra como colocar o sistema online **permanentemente** e de graça.

---

## 📋 Passo a Passo (5 minutos)

### 1️⃣ Baixar os arquivos do sistema

Clique no ícone **"Files"** no canto superior direito desta conversa e baixe a pasta `gestao_escala_don_garcia` completa.

### 2️⃣ Criar conta no GitHub (se não tiver)

1. Acesse [github.com](https://github.com)
2. Clique em **"Sign up"**
3. Preencha email, senha e username
4. Verifique o email

### 3️⃣ Criar repositório no GitHub

1. No GitHub, clique no botão **"+"** (canto superior direito) → **"New repository"**
2. Nome: `escala-don-garcia`
3. Marque como **Public** (público)
4. Clique em **"Create repository"**
5. Na tela que abrir, clique em **"uploading an existing file"**
6. Arraste **TODOS os arquivos** da pasta `gestao_escala_don_garcia` que você baixou:
   - index.html
   - server.py
   - requirements.txt
   - render.yaml
   - README.md
   - etc.
7. Clique em **"Commit changes"**

### 4️⃣ Criar conta no Render (deploy grátis)

1. Acesse [render.com](https://render.com)
2. Clique em **"Get Started"** (ou "Sign in")
3. Escolha **"Sign in with GitHub"** (conecta automaticamente)
4. Autorize o Render a acessar seus repositórios

### 5️⃣ Fazer o deploy

1. No painel do Render, clique em **"New +"** → **"Web Service"**
2. Conecte seu repositório do GitHub `escala-don-garcia`
3. O Render vai detectar automaticamente as configurações (pelo `render.yaml`)
4. Confirme:
   - Name: `escala-don-garcia` (ou qualquer nome)
   - Plan: **Free** (grátis)
5. Clique em **"Create Web Service"**
6. Aguarde 2-3 minutos enquanto o Render faz o deploy

### 6️⃣ Pegar o link permanente

Após o deploy terminar, você verá:
```
Your service is live at https://escala-don-garcia.onrender.com
```

**Esse é seu link permanente!** 🎉

---

## ✅ Pronto!

Agora o sistema está online 24/7, permanentemente. Características:

- ✅ **Link nunca expira**: `https://seu-nome.onrender.com`
- ✅ **Sincronização automática** entre todos os dispositivos
- ✅ **Até 3 pessoas** podem usar ao mesmo tempo
- ✅ **Dados salvos na nuvem** de verdade
- ✅ **100% gratuito** (plano Free do Render)

⚠️ **Única limitação do plano grátis**: Se ninguém acessar o site por 15 minutos, o servidor "hiberna" (desliga para economizar). Quando alguém acessar de novo, ele acorda em ~30 segundos. Os dados **NÃO** são perdidos.

---

## 🔧 Se Tiver Problemas

### "Meu deploy falhou"
- Verifique se você enviou **TODOS** os arquivos para o GitHub (principalmente `server.py` e `render.yaml`)
- Certifique-se que o repositório é **público**

### "Link não abre"
- Aguarde 2-3 minutos após o deploy terminar
- Se mostrar "Service starting...", aguarde mais 30 segundos

### "Dados não sincronizam"
- Verifique se o rodapé do menu mostra "☁️ Sincronizado na nuvem"
- Se mostrar "⚠️ Sem conexão", pode ser que o servidor esteja hibernando. Aguarde 30s e recarregue a página.

---

## 💡 Alternativas

Se não quiser usar GitHub + Render, pode usar:

### Opção B: Railway.app
1. Acesse [railway.app](https://railway.app)
2. Login com GitHub
3. "New Project" → "Deploy from GitHub repo"
4. Mesmo processo, mais rápido

### Opção C: Pythonanywhere (mais simples, mas limitado)
1. Acesse [pythonanywhere.com](https://pythonanywhere.com)
2. Crie conta gratuita
3. Upload dos arquivos via Web Files
4. Configure Web App com `server.py`

---

## 📞 Suporte

Se tiver dificuldade em qualquer passo, me avise que te ajudo!
