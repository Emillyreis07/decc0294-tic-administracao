# Roteiro do módulo 1

Transformação digital e o trabalho do administrador. Encontro 2, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

## Antes da aula

Material do professor: deck `slides/modulo1-transformacao-digital.html`, este roteiro e o arquivo `scripts/atividade_modulo1.py`.

Material publicado na turma virtual, com uma semana de antecedência: o capítulo 1 de Schwab, o script `atividade_modulo1.py` (em `scripts/` no repositório) e este roteiro.

Não há instalação neste encontro. Os alunos precisam apenas de navegador e de um editor de planilha. O opencode desktop é instalado no encontro 3, e neste módulo o professor conduz as demonstrações na projeção.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura e visão geral | 10 min | 1 a 2 |
| Ciclo 1.1 | 50 min | 3 a 10 |
| Intervalo | 15 min | |
| Ciclo 1.2 | 50 min | 11 a 17 |
| Ciclo 1.3 | 55 min | 18 a 25 |
| Intervalo | 10 min | |
| Ciclo 1.4 | 45 min | 26 a 31 |
| Fechamento | 15 min | 32 a 36 |

Deck revisado em 2 nov. 2026 (36 slides). Slides novos: 6, velocidade de adoção da IA generativa, e 20, quanto do trabalho a IA generativa alcança. Os dados de adoção e de trabalho por plataforma têm data de consulta no próprio slide e devem ser reconferidos antes de cada semestre.

## Ciclo 1.1. A quarta revolução industrial

Teoria, 20 min. As quatro revoluções e o que cada uma transferiu para a máquina (slide 4). A definição de Schwab e as três características que ele usa, velocidade, amplitude e profundidade, e impacto sistêmico (slide 5). A versão anterior do deck trocava o impacto sistêmico por uma terceira característica chamada profundidade. A velocidade com número, pela adoção da IA generativa nos EUA (Bick, Blandin e Deming, 2025) e no Brasil (TIC Domicílios 2025) (slide 6). As fragilidades do argumento, com a produtividade por hora de Gordon (2016) (slide 7).

Demonstração, 10 min. O professor projeta uma sessão e dá a instrução do slide 8. Mostra a resposta e abre uma das fontes citadas no navegador, ao vivo. A tabela do slide é ilustrativa e apresenta as três marcas da conferência (existe e traz o dado, existe e não traz o dado, não encontrada) e a definição de confabulação.

Prática, 15 min. Cada aluno escolhe uma afirmação e repete o procedimento.

Entrega, 5 min. Ficha de verificação em `entregas/modulo1-ciclo1-verificacao.md`.

Resultado esperado, caso o modelo não responda: o exercício continua sem ele. O aluno escolhe a afirmação, escreve quais indicadores permitiriam testá-la e procura a fonte sozinho. Registra na ficha que a cota estava indisponível.

Ponto de atenção: alguém vai perguntar se pode usar o Perplexity ou outro serviço. Pode, desde que registre qual usou.

## Ciclo 1.2. Sociedade informacional e a empresa brasileira

Teoria, 20 min. Sociedade informacional em Castells (1996) e três mudanças na empresa (slide 12). A plataforma como mercado de dois lados, com os números do IBGE sobre trabalho por plataforma em 2024 e a disputa sobre o vínculo (slide 13). Antes da aula, conferir se o STF concluiu o Tema 1291. O recorte brasileiro com a TIC Empresas 2025 por porte e setor, a PNAD Contínua TIC 2025 e a Pintec Semestral 2024 (slide 14).

Demonstração, 10 min. A instrução do slide 15, que pede a fonte antes do número, com as três fontes públicas que o assistente deveria listar. Explicar por que a ordem do pedido muda o resultado.

Prática, 15 min. Dois setores, uma fonte, expectativa registrada antes.

Entrega, 5 min. `entregas/modulo1-ciclo2-comparacao.md`.

Fontes que funcionam bem nesta atividade: TIC Domicílios e TIC Empresas (indicador H9, uso de IA por porte e setor), do Cetic.br, PNAD Contínua TIC e Pintec Semestral, do IBGE.

Resultado esperado: a maioria descobre que a diferença entre setores é maior do que imaginava, e que a média nacional esconde essa diferença. Se ninguém chegar lá, o professor projeta uma comparação pronta e discute.

## Ciclo 1.3. Automação do trabalho medida por tarefa

Teoria, 25 min. Tarefa e ocupação, com as estimativas de Frey e Osborne (2013), Arntz, Gregory e Zierahn (2016) e Nedelkoska e Quintini (2018) (slide 19). A exposição à IA generativa medida por tarefa em Eloundou et al. (2024), OIT e NASK (2025), Gmyrek, Winkler e Garganta (2024) e Brynjolfsson, Li e Raymond (2025) (slide 20). Os três destinos (slide 21) e os quatro critérios em tabela, com a referência a Autor, Levy e Murnane (2003) (slide 22).

Demonstração, 10 min. Classificação das dez tarefas do assistente administrativo, com o pedido de incerteza ao final (slide 23). As tarefas do exemplo reaparecem na matriz do slide 28.

Prática, 15 min. Cada aluno escolhe um cargo que conhece e lista dez tarefas.

Entrega, 5 min. `entregas/modulo1-ciclo3-tarefas.md`.

Ponto de atenção: metade da turma escreve "cuidar do setor" como tarefa. Corrija na hora, no primeiro caso, para toda a turma ouvir. Tarefa tem verbo no infinitivo e objeto definido.

## Ciclo 1.4. Mapa de tarefas automatizáveis

Teoria, 12 min. Esforço, ganho e risco, com a linha de exemplo do formulário calculada (slide 27). A ordem de ataque na matriz ganho por esforço, com as dez tarefas ilustrativas (slide 28).

Demonstração, 8 min. O professor executa `atividade_modulo1.py iniciar` na projeção e mostra o formulário criado. O slide 29 traz a saída real do `conferir` sobre as dez tarefas ilustrativas.

Prática, 20 min. Cada aluno preenche as suas dez tarefas e roda `conferir`.

Entrega, 5 min. `entregas/modulo1-mapa-de-tarefas.csv` e `entregas/modulo1-mapa-de-tarefas.md`.

O script recusa o preenchimento quando a coluna `base_da_estimativa` está vazia ou curta. Isso é deliberado e vai gerar reclamação. A resposta é a do slide de entrega: número sem base declarada não conta.

## O que sai deste encontro

Quatro arquivos, que no encontro 3 entram na pasta do projeto e compõem a entrega A1. Além deles, a rotina que vai se repetir o semestre inteiro: pedir, conferir contra a fonte, registrar o que estava errado.

## Avisos a dar no fechamento

O encontro 3 tem a primeira entrega avaliada, feita em sala. Quem faltar fica sem o ambiente montado e não acompanha os encontros seguintes.

Cada aluno precisa chegar com acesso a um e-mail que consiga abrir na aula, para confirmar a conta do GitHub.
