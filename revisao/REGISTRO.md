# Registro de revisões do material 2026.2

Estado de cada deck e histórico das revisões. O padrão e o procedimento estão em `revisao/GUIA-DE-REVISAO.md`. Atualize este arquivo ao fim de cada sessão de revisão.

## Estado por módulo

Os sinais vêm de `python revisao/auditar_texto.py`, rodado em 2 nov. 2026. Elementos visuais conta os slides com diagrama, fluxo ou tabela anotada.

| Mód. | Enc. | Deck | Slides | Sinais | Elementos visuais | Situação |
|---|---|---|---|---|---|---|
| 1 | 2 | Transformação digital | 34 | 2 | nenhum | ajustes pontuais em set. 2026, revisão pelo padrão pendente |
| 2 | 3 | Ambiente de trabalho digital | 46 | 8 | nenhum | revisado em set. 2026 para turma sem contato prévio, linguagem pendente |
| 3 | 4 | IA e engenharia de prompt | 42 | 13 | nenhum | revisado em set. 2026 para turma sem contato prévio, linguagem e atualização sobre IA pendentes |
| 4 | 5 | Do prompt ao artefato | 40 | 8 | nenhum | revisado em set. 2026 para turma sem contato prévio, linguagem pendente |
| 5 | 6 | Dados na Administração | 32 | 0 | 11 | revisado em 2 nov. 2026, slides 6 a 32 (ver abaixo) |
| 6 | 7 | Análise exploratória | 31 | 2 | 15 | revisado em 2 nov. 2026, deck inteiro (ver abaixo). Os dois sinais restantes são falsos positivos: "significativa" como termo estatístico e o separador ';' na saída do script |
| 7 | 8 | Dados estruturados e consulta | 29 | 17 | nenhum | pendente, próximo da fila |
| 8 | 9 | Visualização e painéis | 29 | 15 | nenhum | pendente |
| 9 | 10 | Automação | 29 | 10 | nenhum | pendente |
| 10 | 11 | Pesquisa e análise qualitativa | 29 | 10 | nenhum | pendente |
| 11 | 12 | Aprendizado de máquina | 27 | 5 | nenhum | pendente |
| 12 | 13 | Governança, LGPD e cibersegurança | 27 | 9 | nenhum | pendente. Já distingue anonimização de pseudonimização, coerente com o módulo 5 |
| 13 | 14 | Decisão apoiada por IA | 26 | 6 | nenhum | pendente |
| 14 | 15 | Produto digital e ágil | 25 | 4 | nenhum | pendente |
| 15 | 16 | Projeto integrador | 20 | 7 | nenhum | pendente |

Ordem sugerida: seguir o calendário dos encontros (módulo 7 em diante) e depois voltar aos módulos 1 a 4, que já passaram por uma revisão de conteúdo em setembro.

Em 2 nov. 2026 os marcadores de tempo foram retirados de todos os decks (ver histórico). A contagem de slides acima já reflete o estado posterior.

## Histórico

### 2 nov. 2026, marcadores de tempo retirados de todos os decks

Pedido do professor: os slides não devem mostrar tempo. Em todos os 15 decks foram retirados o "~N min" dos cartões da visão geral, o "~N minutos" dos divisores e os minutos da linha de etapas dos divisores, que passou a mostrar só "Teoria · Demonstração · Prática · Entrega". O subtítulo das práticas passou de "N minutos, individual" para "Individual" (e variantes como "Turma inteira"). No módulo 15, "a ordem dos seus 35 minutos" virou "a ordem das correções". Ficaram, por serem conteúdo e não marcação de aula, os tempos do roteiro de apresentação do projeto integrador (2, 2, 4 e 2 min no módulo 15). Os tempos continuam nos roteiros do professor.

### 2 nov. 2026, módulo 6 (encontro 7), deck inteiro

Pedido do professor: revisar o módulo 6 pelo mesmo padrão do módulo 5. Todos os slides depois da capa foram reescritos. O deck passou de 30 para 31 slides.

Mudanças de conteúdo:

- slide 4: exploratória e confirmatória com referência a Tukey (1977) e o problema das comparações múltiplas quantificado (1 − 0,95²⁰ = 64%), com figura de 20 cruzamentos
- slide 5: fluxo decisão, pergunta de gestão, pergunta de dados e verificação na base, com a ficha da medida (numerador, denominador, período, recorte)
- slide 11: média e mediana com o exemplo de 101 contratos desenhado e a conta explícita (R$ 108.910), mediana apresentada como medida resistente
- slide 16: as três classificações do formulário do script ligadas à terminologia de Rubin (1976): MCAR, ausência estrutural, MAR ou MNAR
- slide 17 (novo): exemplo numérico em que a ausência com viés inverte a conclusão (Norte 100 observado, 200 real, Sul 150) e o preenchimento pela média (116,7) não corrige
- slide 18: árvore de decisão do valor atípico, com a definição das cercas de Tukey (Q1 − 1,5 × AIQ, Q3 + 1,5 × AIQ), que é o critério do script
- slide 23: os dois caminhos do número calculado pelo agente (escrito na resposta ou produzido por script) e onde o erro aparece em cada um
- slide 24: as quatro conferências ligadas aos campos do log. A afirmação anterior de que estavam "em ordem de custo" era inconsistente e saiu
- slides 12, 19 e 25: saídas ilustrativas no formato real do script, em bloco de terminal
- slide 30: pergunta nova sobre preencher vazios com a média
- `\n` literais, ponto e vírgula e paralelismos removidos

Os rótulos do formulário (ausente ao acaso, por regra, com viés, erro de registro, unidade trocada, realidade) e as decisões aceitas (manter, corrigir, separar, excluir, não preencher) foram mantidos exatamente como o script os valida.

Roteiro: tabela de distribuição renumerada (6.1 slides 3 a 8, 6.2 9 a 14, 6.3 15 a 21, 6.4 22 a 27, fechamento 28 a 31), títulos dos ciclos e textos de teoria atualizados.

Conferência: renderização com Liberation Sans e DejaVu Sans, sem estouro relevante.

### 2 nov. 2026, módulo 5 (encontro 6), slides 6 a 32

Pedido do professor: linguagem com cara de modelo de linguagem, inadequada para material acadêmico, poucos elementos visuais e conteúdo sobre IA a atualizar. Revisão a partir do slide 6. O deck passou de 29 para 32 slides.

Slides novos:

- 6, "Onde o agente de IA acerta e onde erra com dados": matriz de quatro tarefas com desempenho, falha característica e controle, mais a definição de saída estruturada
- 18, "As dimensões aplicadas a uma base de fornecedores": base fictícia anotada, com o cálculo da completude (338 ÷ 400 = 84,5%)
- 21, "O que o agente envia ao provedor do modelo": fluxo pasta, agente e provedor, retenção e uso de dados pelos modelos gratuitos, transferência internacional (LGPD, art. 33)

Correções de conteúdo:

- qualidade de dados passou de cinco para seis dimensões (validade incluída), com fonte DAMA UK (2013)
- LGPD: troca de nome por código reclassificada como pseudonimização (arts. 12 e 13), minimização apresentada como princípio da necessidade (art. 6º, III)
- API: menção aos conectores padronizados (MCP)
- cruzamento e diagnóstico de qualidade pedidos como script gravado em `saidas/`
- `\n` literais removidos dos slides de cruzamento

Elementos visuais acrescentados: matriz de tarefas (6), tabela de inventário com lacunas (7), fluxo da linhagem com barra de rastreabilidade (11), eixo de dependência (12), diagrama de cruzamento com códigos IBGE (13), grade das seis dimensões (17), base anotada (18), diagrama de governança (19), fluxo até o provedor (21), ficha do mapa de dados (25), sequência dos comandos do script (26).

Roteiro: tabela de distribuição do tempo renumerada (ciclo 5.1 slides 3 a 9, 5.2 10 a 15, 5.3 16 a 23, 5.4 24 a 28, fechamento 29 a 32) e menções aos slides 6, 20 e 21.

Fontes consultadas: OpenCode Zen, seção Privacy (opencode.ai/docs/zen), 2 nov. 2026. Ficha do PL 2338/2023 no Senado. IBGE Cidades para os códigos 2111201 e 2107506.

Conferência: renderização com Liberation Sans e DejaVu Sans. Falta conferir no laboratório com a Segoe UI, em especial os slides 6 e 13, que são os mais cheios.

### Set. 2026, histórico anterior (git)

- 31 ago.: material completo dos 15 módulos (4b9c99f)
- 1º set.: módulo 2 revisado para turma sem contato prévio (a374d7f). Módulos 3 e 4 no mesmo sentido (4083a3c)
- 14 set.: ajustes no módulo 3 e no roteiro 3 (7a074f5, 5efb7a9). README e modelo de AGENTS.md para os alunos (7709dbd)
- 15 set.: ajustes pequenos em quase todos os decks (e882102). Links do README para o GitHub Pages (600fbc3)

## Pendências fora dos decks

- Em 2 nov. 2026 os decks (e os dois .pptx antigos) foram movidos para `slides/` e os scripts das atividades para `scripts/`. Na mesma data, os roteiros foram para `roteiros/`. Foram atualizados `index.html`, `README.md`, `indice-material-2026-2.md`, os roteiros e as ferramentas de `revisao/`. Os scripts receberam um ajuste de poucas linhas que muda o diretório de trabalho para a raiz quando estão em `scripts/`. O texto dos decks continua dizendo "execute atividade_moduloN.py", porque na turma o script é copiado para a raiz do projeto do aluno. Os endereços antigos do GitHub Pages (sem `slides/`) deixam de funcionar depois do próximo push.

- Alterações sem commit em 2 nov. 2026: ajustes de exemplos numéricos nos decks 4, 6, 7, 8, 10, 11 e 13, a revisão do módulo 5 e a pasta `revisao/`. A pasta `estilo-vale/` e o arquivo `justificativa-diarias-passagens-fora-prazo.docx` também estão fora do controle de versão. Decidir o que entra no repositório público antes do próximo commit.
- `build_moduloN.js` e `tema_ufma.js` não estão na pasta. Se forem recuperados, portar a revisão do módulo 5 antes de gerar os decks de novo.
- Antes de cada semestre, reconferir a política dos modelos gratuitos do OpenCode Zen e a situação do PL 2338/2023.
