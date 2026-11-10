# Roteiro do módulo 8

Visualização de dados e painéis. Encontro 9, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

Este encontro fecha a entrega B1, que vale 60% da nota 2.

## Antes da aula

Material do professor: `slides/modulo8-visualizacao-e-paineis.html`, este roteiro e `scripts/atividade_modulo8.py`.

Publicado na turma virtual: o script e o lembrete de trazer um gráfico ruim e de escolher três dos cinco indicadores do encontro 8.

Gere um painel de teste antes da aula, com a base de reserva, e projete-o no ciclo 8.3. Ver o resultado pronto antes de construir encurta a prática em dez minutos.

Separe dois ou três gráficos ruins de fontes públicas, caso a turma traga poucos. Relatório de gestão de órgão público e apresentação de resultado de empresa listada rendem exemplos fartos, e o fato de serem públicos evita constrangimento com material de estágio.

Confira quem ficou pendente nos encontros 7 e 8. A B1 reúne os três encontros, e o script vai apontar item por item no último ciclo.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura e visão geral | 10 min | 1 a 2 |
| Ciclo 8.1 | 45 min | 3 a 9 |
| Ciclo 8.2 | 50 min | 10 a 16 |
| Intervalo | 15 min | |
| Ciclo 8.3 | 55 min | 17 a 22 |
| Intervalo | 10 min | |
| Ciclo 8.4 | 50 min | 23 a 27 |
| Fechamento | 15 min | 28 a 31 |

## Ciclo 8.1 — Por que a maioria dos gráficos falha

Teoria, 18 min. O gráfico responde a uma pergunta de gestão, com o mesmo conjunto de números antes e depois do título-conclusão (slide 4). Os cinco defeitos frequentes e a proporção dados-tinta de Tufte (slide 5). Exemplo numérico do eixo cortado, com o fator de distorção (slide 6, novo).

Demonstração, 10 min. A turma escolhe o pior gráfico trazido e ele é refeito na projeção, começando pela pergunta e pelo título-conclusão. Se o agente redesenhar, o slide 7 traz a instrução com o script gravado em saidas/.

Prática, 12 min. Cada aluno reconstrói o próprio.

Entrega, 5 min. `entregas/modulo8-ciclo1-reconstrucao.md`.

O teste do título escrito antes do gráfico é o conteúdo central do ciclo. Aplique na demonstração em voz alta: se ninguém consegue escrever a frase afirmativa, o diagnóstico é que falta análise, e não desenho.

O corte do eixo em gráfico de barras é o defeito que mais aparece e o que mais distorce. O slide 6 mostra a mesma série com e sem base no zero.

## Ciclo 8.2 — Forma, escala e cor

Teoria, 30 min. As cinco comparações e a forma de cada uma (slide 11). A ordem de precisão de leitura de Cleveland e McGill, 1984 (slide 12, novo). As três decisões de escala, com o exemplo de valor absoluto e taxa (slide 13). Os três usos da cor e o contraste mínimo da WCAG 2.2, com a razão de contraste de cada cor da paleta UFMA (slide 14).

Prática, 15 min. Cada aluno escolhe a forma dos cinco indicadores do encontro 8 e escreve o título-conclusão de cada um.

Entrega, 5 min. `entregas/modulo8-ciclo2-formas.md`.

O par valor absoluto contra taxa é o que mais muda conclusão em gestão pública. A unidade maior sempre tem mais atendimentos; por atendimento, pode ser a mais barata. Peça um exemplo da turma.

O histograma quase nunca aparece em relatório de gestão e é o que revela se a média representa o conjunto. Vale um minuto a mais.

Indicador sem título-conclusão não entra no painel. A regra é do script e é o filtro de qualidade do encontro.

## Ciclo 8.3 — Do dado ao painel que abre no navegador

Teoria, 18 min. Os elementos de um painel, apontados sobre a imagem do painel que o script gera, com a definição de Few, 2006 (slide 18). Comparação entre o HTML do script, o Power BI e o Data Studio, antigo Looker Studio, com custo e requisitos do Copilot consultados em 2 nov. 2026 (slide 19).

Demonstração, 7 min. O painel de teste que você gerou antes da aula, aberto na projeção. O slide 20 mostra as nove colunas do formulário e as regras de recusa do script.

Prática, 25 min. Cada aluno preenche os indicadores, exporta a série e gera o painel.

Entrega, 5 min. `entregas/painel.html`.

O quarto elemento, a fonte de cada número no próprio painel, é o que quase todo painel esquece. É o mapa de dados do encontro 6 chegando à tela de quem decide, e o script recusa indicador sem fonte.

Quem gerar o painel e vir número diferente da consulta quase sempre tem filtro de período diferente entre o SQL e o que escreveu no formulário. Essa é a primeira coisa a checar.

## Ciclo 8.4 — O painel do projeto e a entrega B1

Teoria, 10 min. De quem é o painel: três destinatários de uma secretaria fictícia, a decisão de cada um e a regra de corte (slide 24).

Demonstração, 5 min. Os dois comandos de conferência, com saída ilustrativa do b1 (slide 25).

Prática, 30 min. Painel final e fechamento da B1.

Entrega, 5 min. Repositório publicado com a mensagem "entrega B1".

A regra de que o indicador sobre o que o destinatário não pode mudar não entra é a mais útil do ciclo, e a que mais reduz painel inchado. Aplique a dois painéis da turma em voz alta.

Reserve os últimos vinte minutos para o comando `b1`. Ele percorre doze itens dos encontros 7, 8 e 9 e imprime o caminho de cada arquivo esperado. Quem rodar cedo tem tempo de corrigir.

## O que sai deste encontro

Um gráfico reconstruído, a escolha de forma justificada para cinco indicadores, e o painel do projeto com destinatário declarado. Somados aos encontros 7 e 8, fecham a B1.

## Avisos no fechamento

Retomar o mapa de tarefas do módulo 1: a tarefa em primeiro lugar na ordem de ataque é o objeto do encontro 10.

Trazer um documento que se refaz todo mês, com dois exemplares de meses diferentes se possível, e a anotação de quanto tempo ele leva hoje.

Deixar o painel funcionando: regerar o painel com dado novo é um exemplo de fluxo repetível para o encontro 10 (slide 29).
