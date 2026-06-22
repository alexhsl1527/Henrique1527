# Gestão de Escala Don Garcia

Sistema completo de gerenciamento de escalas de trabalho para restaurante, 100% offline, em HTML/CSS/JavaScript puro com persistência via `localStorage`.

## Como usar
Basta abrir o arquivo `index.html` em qualquer navegador moderno. Não requer servidor nem instalação.

## Funcionalidades
- **Dashboard** com indicadores (setores, funcionários, escalas) e explicação das jornadas.
- **Cadastro de Setores** (CRUD). Remover um setor remove funcionários e escalas vinculados.
  - **Horários padrão por turno**: cada setor pré-cadastra entrada/saída para a jornada de **7h20** e para a jornada de **10h**, em cada turno (ex.: Almoço, Janta). Esses horários são aplicados automaticamente ao gerar a escala.
- **Cadastro de Funcionários** (CRUD) com setor, turno predominante manual e filtro por setor.
  - **Horário personalizado (opcional)**: cada colaborador pode ter horários próprios (entrada/saída para 7h20 e 10h) que substituem o padrão do setor. Se não definido, usa o padrão do setor.
- **Geração de Escalas em 3 passos**: período → parâmetros por colaborador (turno, folga semanal, domingo de folga, calendário de dias de jornada contínua 10h) → tabela mensal editável célula a célula. Cada dia de trabalho exibe o **horário de entrada e saída**, recalculado automaticamente ao trocar turno/jornada e ajustável manualmente por dia.
- **Visualização de Escalas** com tabela colorida, horários de entrada/saída por dia, horas semanais (Semana 1-5 + Total) e contagem de funcionários por dia.
- **Exportação para PDF** (jsPDF via CDN) com tabela colorida, turnos, **horários de entrada/saída**, horas semanais, legenda e abreviações dos dias (Seg–Dom).

## Hierarquia de horários
1. **Horário personalizado do colaborador** (se preenchido) — tem prioridade.
2. **Horário padrão do setor** para o turno correspondente.
3. Ajuste manual direto na célula da escala (sobrepõe os anteriores apenas naquele dia).

## Regras de negócio
- Escala 6x1 (6 dias de trabalho, 1 de folga).
- Jornada padrão: 7h20 trabalho + 30min intervalo.
- Jornada contínua: 10h trabalho + 2h intervalo.
- 1 domingo de folga por mês garantido.

## Tecnologias
HTML5, CSS3, JavaScript puro, localStorage, jsPDF (CDN). Arquivo único auto-contido.
