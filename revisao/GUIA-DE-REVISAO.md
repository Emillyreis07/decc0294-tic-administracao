# Guia de revisão dos decks da DECC0294

Este guia registra o padrão adotado na revisão do material de 2026.2 e o procedimento para continuar o trabalho em qualquer sessão, com ou sem o mesmo assistente. O registro do que já foi feito e do que falta está em `revisao/REGISTRO.md`.

O padrão foi aplicado pela primeira vez no módulo 5 (slides 6 a 32), em 2 de novembro de 2026. Esse deck serve de referência para os demais.

## O que a revisão busca

A revisão tem três objetivos, definidos pelo professor.

1. Linguagem adequada a material acadêmico. O texto dos slides apresentava marcas de redação por modelo de linguagem: frases de efeito, paralelismos, aforismos e vocabulário promocional. O conceito deve aparecer de forma consistente e compreensível para a turma, sem perder a precisão técnica.
2. Mais elementos visuais. Esquemas, fluxos, tabelas anotadas e diagramas no lugar de parte dos cartões só de texto.
3. Conteúdo atualizado sobre modelos de linguagem e agentes de IA, com fonte verificável e data de consulta quando a informação muda com o tempo.

## Onde editar

Organização da pasta: os decks ficam em `slides/`, os scripts das atividades em `scripts/`, os roteiros em `roteiros/` e as ferramentas de revisão em `revisao/`. Os scripts gravam nas pastas de trabalho da raiz (`dados/`, `entregas/`, `saidas/`) mesmo quando chamados de dentro de `scripts/`.

Os decks são HTML de arquivo único. O `indice-material-2026-2.md` menciona `build_moduloN.js` e `tema_ufma.js`, mas esses geradores não estão nesta pasta. Por isso a edição é feita direto no HTML. Se os geradores forem recuperados, a revisão do módulo 5 precisa ser portada para eles antes de qualquer nova geração, sob pena de perda.

Cada slide é um `<section class="slide ...">` dentro de `<div id="palco">`. Há quatro tipos: `capa`, `conteudo`, `divisor` e `fim`. Nos slides de conteúdo, a área útil é a `div.corpo` (1168 × 444 px, de 180 px a 624 px do topo). O rodapé traz `<span class="pag">N / TOTAL</span>`, e a barra de navegação no fim do arquivo traz `<span>/ TOTAL</span>`. Ao inserir ou remover slides, as duas numerações e o atributo `data-i` precisam ser refeitos.

## Padrão de texto

As regras abaixo resumem as preferências de escrita do professor aplicadas a slides.

Construções a eliminar:

- travessão (— ou –) e ponto e vírgula
- paralelismos do tipo "não é X, é Y", "não X, e sim Y", "não apenas X, mas também Y"
- aforismos e frases de efeito: "o NÃO INFORMADO é o produto", "vale mais que a lista de certezas", "é um achado, não um fracasso", "mudou o jogo", "mata a discussão"
- vocabulário promocional ou vago: crucial, essencial, fundamental, valioso, robusto, eficaz, estratégico, significativo, cenário, panorama, insight, além disso, portanto, contudo, frequentemente
- negrito para ênfase no meio do texto e títulos em caixa de título (usar apenas a inicial maiúscula)

O que entra no lugar:

- definição do conceito com o termo técnico da área e, quando houver, o equivalente em inglês entre parênteses: linhagem de dados (data lineage), confabulação, saída estruturada (structured output), curador de dados (data steward)
- regra, medida ou critério verificável: "valores preenchidos ÷ total de registros, por coluna"
- exemplo concreto da administração brasileira, com números quando possível
- fonte citada no próprio slide, em `p.fonte-nota` ou dentro da caixa de definição: DAMA UK (2013), Lei nº 13.709/2018 com artigo, documentação oficial com data de consulta

Exemplos tirados do módulo 5:

| Antes | Depois |
|---|---|
| O NÃO INFORMADO é o produto. Cada lacuna é uma pergunta a fazer na organização. | Cada célula NÃO INFORMADO indica uma pergunta a levar ao setor que responde pela fonte. Ela reaparece no mapa de dados do ciclo 5.4. |
| Alto, e é aqui que a IA generativa mudou o jogo: extrair estrutura de texto ficou barato. | Alto. Os modelos de linguagem atuais extraem campos de texto quando recebem a lista de campos, o que reduziu o custo desta etapa. A conferência continua manual. |
| Substitua o nome por um código antes de usar. (sob o título Anonimização) | Trocar o nome por um código é pseudonimização. O dado continua pessoal enquanto existir a tabela de correspondência. |
| O agente não conhece a sua organização. Tudo que ele souber além do que você disse é invenção. | O agente conhece da organização apenas o que está na instrução. Qualquer detalhe que ele acrescente é confabulação. |

O imperativo continua adequado nos slides de prática e entrega, porque são instruções ao aluno.

Os slides não trazem marcadores de tempo (minutos por ciclo, por etapa ou por prática). Os tempos ficam só no roteiro do professor. Os divisores mostram apenas as etapas do ciclo (Teoria · Demonstração · Prática · Entrega) e o subtítulo das práticas indica só a forma de trabalho (Individual, Turma inteira).

## Conteúdo técnico sobre IA

Pontos que o módulo 5 passou a tratar e que devem permanecer coerentes nos demais decks:

- Desempenho dos agentes por tipo de tarefa (slide 6 do módulo 5): extração com esquema e escrita de script funcionam com controle. Cálculo escrito na resposta é irregular. Descrição de algo que o modelo não recebeu produz confabulação.
- Todo cálculo é pedido como script gravado em `saidas/`, lido antes do uso e conferido em dois números à mão. O módulo 6 já segue esse padrão.
- Saída estruturada assegura o formato dos campos e não verifica o conteúdo.
- O conteúdo que o agente lê é enviado ao servidor do provedor do modelo. Parte dos modelos gratuitos do OpenCode Zen declara uso dos dados para aprimoramento. Envio de dado pessoal ao exterior é transferência internacional (LGPD, art. 33).
- Agentes acessam sistemas por conectores padronizados, como o Model Context Protocol (MCP).

Informações que mudam com o tempo e precisam ser reconferidas antes de cada semestre: lista e política de privacidade dos modelos gratuitos (opencode.ai/docs/zen), situação do PL 2338/2023 na Câmara, regulamentação da ANPD sobre IA. Ao atualizar, registrar a data de consulta no slide.

## Componentes visuais disponíveis

Os módulos 5 e 6 têm, no fim do bloco `<style>`, a seção `/* ---- componentes acrescentados na revisão de nov. 2026 ---- */`. A versão do módulo 6 é a mais completa, porque inclui também o `pre.terminal`. Para usar os componentes em outro deck, copie essa seção do módulo 6 inteira (até o fim do `<style>`) para o deck de destino.

| Classe | Uso | Exemplo no módulo 5 |
|---|---|---|
| `.tab` e `.tab.apertada` | tabela de dados ou matriz comparativa. `td.lac` destaca célula, `.chip.ok/.med/.ruim` classifica | slides 6, 7, 18 |
| `.fluxo` com `.etapa` | sequência de etapas com setas, `--n` define o número de colunas e `--cor` a cor de cada etapa | slides 11, 26 |
| `.trilha` | barra em gradiente com rótulos, para grandezas que variam ao longo de um fluxo | slide 11 |
| `.def` | caixa de definição de conceito, com fonte | slides 6, 11 |
| `.eixo` | eixo ordenador acima de cartões | slide 12 |
| `.cards.baixos` | cartões com texto menor, para caber sob um eixo ou nota | slides 12, 20 |
| `.duascol` com `.col` | duas colunas, proporção em `--esq` e `--dir` | slides 13, 18, 19 |
| `.caixa.vinho/.dourado/.teal` | nota lateral curta com rótulo | slides 7, 13, 18, 19, 26 |
| `.grade` com `.dim` | seis blocos com definição e medida | slide 17 |
| `.legenda` e `.badge` | legenda numerada ligada a marcas na tabela | slide 18 |
| `.ficha` com `.grupo` | registro de campos agrupados por função | slide 25 |
| `svg.fig` | diagrama em SVG inline, com cores da paleta UFMA | slides 13, 19, 21 |
| `p.fonte-nota` | linha de fonte no pé da área útil | slides 17, 20, 21 |
| `pre.terminal` com `.hl` | saída de script ou de terminal, com linha destacada (definida no módulo 6) | módulo 6, slides 12, 19, 25 |

Paleta: vinho `#8D0333`, dourado `#D4B277`, verde-azulado `#0AB0AB`, amarelo `#FEC84D`, cinza de texto `#6B6B6B`. Linhas tracejadas em `#C9962E`.

Diagramas em SVG usam `viewBox` com a largura em pixels igual à largura que ocuparão no slide (1168 para a largura total), para que o tamanho da fonte no SVG corresponda ao tamanho real.

## Procedimento

1. Rodar `python revisao/auditar_texto.py` para ver o número de sinais por deck e `python revisao/auditar_texto.py N --desde S` para o detalhe de um deck. A contagem indica prioridade. A leitura do deck inteiro continua necessária, porque frase de efeito sem palavra proibida passa pelo filtro.
2. Ler o roteiro do módulo e o script `scripts/atividade_moduloN.py`. Nomes de arquivos, comandos, colunas e regras de recusa citados nos slides precisam coincidir com o script.
3. Pesquisar o que mudou no tema desde a produção do material e registrar a fonte.
4. Reescrever os slides e acrescentar os elementos visuais. Manter a estrutura de ciclo: teoria, demonstração, prática e entrega.
5. Refazer a numeração (`pag`, `data-i`, total na barra) se o número de slides mudou.
6. Rodar `node revisao/conferir_slides.js slides/moduloN-....html` e abrir as imagens geradas. Testar também com `"DejaVu Sans"` como terceiro argumento, que é mais larga que a Segoe UI e dá margem de segurança.
7. Atualizar a tabela "Distribuição do tempo" do `roteiros/roteiro-moduloN.md` com a nova numeração dos slides e as menções a conteúdo novo.
8. Atualizar `revisao/REGISTRO.md`.
9. Fazer o commit no GitHub Desktop com uma mensagem que indique o módulo e o escopo, por exemplo "Modulo 6 revisado: linguagem, esquemas e conteudo de IA".

## Conferência final

- nenhum elemento passa da área útil ou da margem direita
- títulos em uma linha, subtítulo em uma linha
- `auditar_texto.py` sem sinais nos slides revisados
- nomes de arquivos e comandos iguais aos do script da atividade
- toda informação datada tem fonte e data de consulta
- roteiro e registro atualizados
