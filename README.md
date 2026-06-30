# 🍽️ Gestão de Escala Don Garcia

Sistema completo de gerenciamento de escalas de trabalho para restaurantes, funcionando **100% offline** no navegador com opção de **compartilhamento entre máquinas**.

## ✨ Funcionalidades

### 📊 Dashboard
- Indicadores: total de setores, funcionários e escalas
- Últimas escalas geradas
- Distribuição de funcionários por setor
- Atalhos rápidos

### 🏢 Gestão de Setores
- CRUD completo (Criar, Ler, Atualizar, Deletar)
- **Horários pré-cadastrados por turno**: defina entrada/saída para jornada padrão (7h20) e contínua (10h) de cada turno (ex: Almoço, Janta)
- Deleção em cascata (aviso se houver funcionários ou escalas vinculadas)

### 👥 Gestão de Funcionários
- CRUD completo com vinculação a setores
- Turno padrão do colaborador
- **Horários personalizados opcionais**: permite sobrescrever os horários do setor para colaboradores específicos
- Badge visual indicando horário personalizado
- Filtro por setor
- Contagem total

### 📅 Geração de Escalas (3 Passos)
1. **Selecionar setor + mês/ano**
2. **Configurar cada colaborador**:
   - Turno padrão
   - Dia da semana de folga
   - Domingo de folga garantido (escolha qual ou automático)
   - Marcar dias de jornada de 10h (calendário visual)
3. **Tabela editável** com visualização completa:
   - Cores por turno (Almoço, Janta, Folga, Domingo)
   - Horários de entrada e saída em cada dia
   - Jornada (7h20 ou 10h)
   - Edição célula por célula (turno, jornada, folga)
   - **Ajuste manual de horários** por dia (sobrescreve setor/colaborador)
   - Cálculo automático de horas semanais (Semana 1-5 + Total)
   - Contador de pessoas trabalhando por dia

### ☁️ Sincronização Automática na Nuvem (NOVO!)
- **Tudo é salvo automaticamente no servidor** — não precisa fazer nada
- **Todos os dispositivos compartilham os mesmos dados**: cadastre em um computador e aparece em todos os outros
- **Atualização automática a cada 5 segundos**: mudanças feitas por outra pessoa aparecem na sua tela sozinhas
- **Indicador de status** no rodapé: "☁️ Sincronizado na nuvem" / "⚠️ Sem conexão"
- **Funciona para até 3 pessoas** ao mesmo tempo
- Como funciona:
  - O sistema roda em um servidor (`server.py`) que guarda os dados em `dados_nuvem.json`
  - Ao abrir o link, o sistema carrega os dados do servidor
  - A cada alteração, salva automaticamente no servidor
  - A cada 5 segundos, verifica se outra pessoa mudou algo e atualiza a tela

### 🔗 Compartilhamento de Dados (backup/transferência)
- **Gera link com todos os dados** (setores + funcionários + escalas) codificados na URL
- **QR Code** para escaneamento rápido
- Útil para backup ou transferir dados para um sistema rodando em modo local (offline)

### 📄 Exportação PDF
- Layout profissional em paisagem (A4)
- Cabeçalho com nome do setor e mês/ano
- Todas as informações da escala:
  - Nome do colaborador
  - Turnos e jornadas
  - **Horários de entrada e saída por dia**
  - Horas semanais e total mensal
  - Contagem de trabalhadores por dia
- Legenda com cores e explicações
- Paginação automática
- Nome do arquivo: `Escala_Setor_Mês_Ano.pdf`

## 🎨 Regras de Negócio

- **Regime 6x1**: 6 dias de trabalho, 1 folga semanal
- **Jornada Padrão**: 7h20 + 30min intervalo = 8h (turno normal)
- **Jornada Contínua**: 10h + 2h intervalo = 12h (dias específicos marcados no calendário)
- **Folga Domingo**: Todo colaborador tem direito a 1 domingo de folga por mês (configurável qual ou automático para o 2º domingo)

## ⚙️ Hierarquia de Horários (entrada/saída)

Os horários de cada dia são resolvidos na seguinte ordem de prioridade:

1. **Ajuste manual na célula** (se houver) — prioridade máxima, permite ajustes dia-a-dia
2. **Horário personalizado do colaborador** (se houver) — sobrescreve o padrão do setor
3. **Horário padrão do setor** para aquele turno e jornada — base para todos

### Exemplo prático:
- **Setor Cozinha** tem horário "Almoço 7h20": 09:00-16:50
- **Colaborador Ana** usa o horário do setor (não tem personalizado): **09:00-16:50**
- **Colaborador Bruno** tem horário personalizado "Janta": 18:00-01:50 — **18:00-01:50** (ignora setor)
- **Dia 15 de Ana** foi ajustado manualmente para 10:00-17:50 — **10:00-17:50** (apenas nesse dia)

## 🚀 Como Usar

### Opção 1: Uso Local (offline)
1. Baixe o arquivo `index.html` (ícone "Files" no canto superior direito)
2. Abra diretamente no navegador (Chrome, Edge, Firefox)
3. Todos os dados ficam salvos no `localStorage` do navegador

### Opção 2: Compartilhar entre Máquinas
1. No Dashboard, clique em **🔗 Compartilhar**
2. Copie o link gerado (ou escaneie o QR Code)
3. Abra o link em qualquer outro computador/celular
4. Os dados serão importados automaticamente!

### Opção 3: Hospedar Online (acesso público)

Para que o sistema fique disponível na internet com um domínio público, você pode hospedar gratuitamente:

#### GitHub Pages (recomendado - domínio .github.io)
1. Crie uma conta em [github.com](https://github.com)
2. Crie um novo repositório público (nome: `escala-don-garcia`)
3. Faça upload do arquivo `index.html`
4. Vá em Settings → Pages → Source: "main branch"
5. Seu site estará em: `https://seuusuario.github.io/escala-don-garcia`

#### Netlify Drop (mais fácil - domínio .netlify.app)
1. Acesse [app.netlify.com/drop](https://app.netlify.com/drop)
2. Arraste o arquivo `index.html` para a tela
3. Pronto! Domínio gerado automaticamente (ex: `escala-dongarcia.netlify.app`)

#### Vercel (alternativa - domínio .vercel.app)
1. Crie conta em [vercel.com](https://vercel.com)
2. Clique em "Add New Project" → "Import Git Repository" ou arraste a pasta
3. Deploy automático

**Importante**: Após hospedar online, o link de compartilhamento funcionará com o domínio público (ex: `https://escala-dongarcia.netlify.app?dados=...`), permitindo que qualquer pessoa com o link acesse de qualquer lugar.

## 💾 Armazenamento de Dados

- **Local**: Dados salvos no `localStorage` do navegador (persistem entre sessões)
- **Compartilhamento**: Dados codificados em Base64 na URL (até ~2MB, suporta centenas de funcionários e escalas)
- **Backup**: Use a função "Compartilhar" e salve o link como backup — basta abri-lo para restaurar tudo

## 📋 Estrutura de Dados

```javascript
// localStorage keys:
dg_setores      // Array de setores com horários
dg_funcionarios // Array de funcionários (com horário opcional)
dg_escalas      // Array de escalas geradas

// Exemplo de setor com horários:
{
  id: "s1",
  nome: "Cozinha",
  horarios: [
    {turno: "Almoço", entP: "09:00", saiP: "16:50", ent10: "09:00", sai10: "21:00"},
    {turno: "Janta", entP: "17:00", saiP: "00:50", ent10: "15:00", sai10: "03:00"}
  ]
}

// Exemplo de funcionário com horário personalizado:
{
  id: "f1",
  nome: "João",
  setorId: "s1",
  turno: "Almoço",
  horario: {  // OPCIONAL - sobrescreve setor
    entP: "10:00", saiP: "17:50",
    ent10: "10:00", sai10: "22:00"
  }
}
```

## 🛠️ Tecnologias

- HTML5 + CSS3 (variáveis CSS)
- JavaScript Vanilla (sem frameworks)
- [jsPDF](https://github.com/parallax/jsPDF) - Geração de PDF
- [QRCode.js](https://github.com/davidshimjs/qrcodejs) - Geração de QR Code
- localStorage API - Persistência local

## 📝 Changelog

### v1.3.0 (22/06/2026)
- ✨ Compartilhamento de dados via URL/QR Code
- 🔗 Sincronização manual entre máquinas sem backend
- 📱 QR Code para transferência rápida via celular

### v1.2.0
- ✨ Horários de entrada/saída por setor e colaborador
- 🕒 Hierarquia de horários (célula > colaborador > setor)
- 📄 Horários no PDF (entrada e saída em cada dia)
- 🐛 Fix: backfill automático de horários no PDF

### v1.1.0
- ✨ Jornada de 10h configurável por dia no calendário
- 📊 Cálculo de horas semanais e total mensal
- 🎨 Melhorias visuais no dashboard

### v1.0.0
- 🎉 Lançamento inicial
- Dashboard, CRUD setores/funcionários
- Geração de escala em 3 passos
- Exportação PDF

## 📄 Licença

Projeto desenvolvido para **Don Garcia Restaurante**. Código aberto para uso interno.

---

**© 2026 Don Garcia • Sistema 100% Offline**
