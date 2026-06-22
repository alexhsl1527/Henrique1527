# 🌐 Como Hospedar o Sistema Online (Grátis)

Este guia mostra 3 formas **gratuitas** de colocar o sistema na internet para acessar de qualquer lugar.

---

## 🥇 Opção 1: Netlify Drop (MAIS FÁCIL - 1 minuto)

### Passo a passo:

1. **Baixe o arquivo** `index.html` (clique no ícone "Files" no canto superior direito)

2. **Abra** [app.netlify.com/drop](https://app.netlify.com/drop) no navegador

3. **Arraste** o arquivo `index.html` para a área indicada na tela

4. **Pronto!** Netlify gera automaticamente um domínio (ex: `https://escala-dongarcia-xyz123.netlify.app`)

5. **Copie o link** e compartilhe com sua equipe

### ✅ Vantagens:
- Não precisa criar conta
- Domínio gerado automaticamente
- SSL/HTTPS incluído
- Atualização: basta arrastar o arquivo novamente

### 📝 Opcional: Personalizar domínio
- Crie uma conta gratuita no Netlify
- No painel do site, clique em "Domain settings"
- Escolha um nome personalizado (ex: `escala-dongarcia.netlify.app`)

---

## 🥈 Opção 2: GitHub Pages (recomendado para controle de versões)

### Passo a passo:

1. **Crie uma conta** em [github.com](https://github.com) (se ainda não tiver)

2. **Crie um novo repositório**:
   - Clique no botão **"New"** (verde, canto superior direito)
   - Nome: `escala-don-garcia`
   - Marque como **Public**
   - Clique em **"Create repository"**

3. **Faça upload do arquivo**:
   - Na página do repositório, clique em **"uploading an existing file"**
   - Arraste o arquivo `index.html`
   - Clique em **"Commit changes"** (botão verde)

4. **Ative o GitHub Pages**:
   - No repositório, clique em **Settings** (aba no topo)
   - No menu lateral, clique em **Pages**
   - Em "Source", selecione **"main"** branch
   - Clique em **"Save"**

5. **Aguarde 1 minuto** e acesse seu site em:
   ```
   https://[seu-usuario].github.io/escala-don-garcia/
   ```
   (Substitua `[seu-usuario]` pelo seu nome de usuário do GitHub)

### ✅ Vantagens:
- Controle de versões (histórico de mudanças)
- Domínio .github.io profissional
- 100% gratuito e ilimitado
- SSL/HTTPS incluído

---

## 🥉 Opção 3: Vercel (alternativa rápida)

### Passo a passo:

1. **Crie uma conta** em [vercel.com](https://vercel.com) (pode usar conta do GitHub)

2. **Clique** em **"Add New Project"**

3. **Arraste** a pasta `gestao_escala_don_garcia` (ou apenas o `index.html`)

4. **Clique** em **"Deploy"**

5. **Pronto!** Domínio gerado automaticamente (ex: `escala-dongarcia.vercel.app`)

### ✅ Vantagens:
- Deploy automático
- Domínio .vercel.app
- SSL/HTTPS incluído
- Fácil de atualizar

---

## 📱 Usando o Sistema Hospedado

Depois de hospedar, você pode:

1. **Acessar de qualquer máquina**: basta abrir o link no navegador

2. **Compartilhar com a equipe**:
   - Copie o domínio (ex: `https://escala-dongarcia.netlify.app`)
   - Envie para os colegas via WhatsApp/email
   - Cada um abre no próprio computador

3. **Sincronizar dados entre máquinas**:
   - Na **Máquina 1**: preencha setores, funcionários e escalas
   - Clique em **🔗 Compartilhar** no Dashboard
   - Copie o link gerado
   - Na **Máquina 2**: abra o link de compartilhamento
   - Todos os dados serão importados automaticamente!

4. **Manter sincronizado** (processo manual):
   - Sempre que fizer mudanças, clique em **🔗 Compartilhar**
   - Envie o novo link para a equipe
   - Eles abrem o link para atualizar os dados

---

## ⚠️ Importante

### Dados Locais vs. Hospedado

- **Dados ficam salvos no navegador de cada máquina** (localStorage)
- **Compartilhamento é manual** via link gerado
- Para sincronização automática, seria necessário um backend (banco de dados na nuvem)

### Fluxo de Trabalho Recomendado (3 pessoas):

**Opção A - Pessoa principal atualiza**:
1. Uma pessoa fica responsável por gerenciar os dados
2. Essa pessoa cria/edita escalas
3. Usa **🔗 Compartilhar** para gerar link atualizado
4. Envia o link para os outros 2 via WhatsApp
5. Os outros abrem o link para ver os dados mais recentes

**Opção B - Backup antes de editar**:
1. Antes de qualquer edição, clique em **🔗 Compartilhar** e salve o link (backup)
2. Faça as mudanças
3. Clique em **🔗 Compartilhar** novamente e envie o novo link
4. Se der algum problema, use o link de backup para restaurar

---

## 🆘 Problemas Comuns

### "Meus dados sumiram quando troquei de navegador"
- Os dados ficam salvos **no navegador específico** (Chrome, Edge, etc.)
- Solução: Use **🔗 Compartilhar** antes de trocar e abra o link no novo navegador

### "Quero transferir para outro computador"
- Use **🔗 Compartilhar** → copie o link → abra no outro computador

### "Link de compartilhamento não funciona"
- Certifique-se de copiar o link **completo** (pode ser muito longo)
- Ou use o QR Code (mais fácil para celular)

### "Quero um domínio próprio (ex: escalas.dongarcia.com)"
- Isso requer registrar um domínio (~R$40/ano)
- Após hospedar no Netlify/Vercel, você pode configurar domínio customizado no painel

---

## 💡 Dicas

- **Salve o link do site hospedado** nos favoritos do navegador
- **Use o botão Compartilhar** regularmente para fazer backup dos dados
- **Teste primeiro localmente** (abrindo o index.html) antes de hospedar
- **Se trabalham no mesmo computador**, não precisa hospedar — basta abrir o index.html

---

Qualquer dúvida, consulte o [README.md](README.md) principal!
