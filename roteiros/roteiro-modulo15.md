# Roteiro do módulo 15

Projeto integrador. Encontro 16, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

Último encontro. Fecha a entrega C2, que vale 60% da nota 3, e encerra a disciplina.

## Antes da aula

Material do professor: `slides/modulo15-projeto-integrador.html`, este roteiro e `scripts/atividade_modulo15.py`.

Publicado na turma virtual: o script, a estrutura dos quatro blocos da apresentação e o lembrete de que a demonstração ao vivo é obrigatória, incluindo o caso com dado errado.

Monte a ordem das apresentações antes da aula e publique. Sorteio feito na hora consome dez minutos e deixa a turma inteira ansiosa até o fim.

Confira a sala: projeção, tomada, e um plano para quem for apresentar de máquina própria. Perder cinco minutos por apresentação em troca de cabo derruba o encontro inteiro.

Prepare a lista de pendências por aluno, da última rodada de `c1` e `conferir`. O ciclo 15.1 depende dela.

Atenção ao comando `c2` antes da aula. Nos encontros 10 e 11 ele procura arquivos cujo nome começa por `entregas/modulo9-ciclo4` e `entregas/modulo10-ciclo3`, nomes que nenhum deck nem script anterior manda criar. As entregas desses ciclos são `entregas/modulo9-fluxo.csv` e `entregas/modulo9-relatorio.md` (módulo 9) e `entregas/modulo10-codificacao.csv` e `entregas/modulo10-livro-de-codigos.md` (módulo 10). No encontro 4, o prefixo `entregas/modulo3-ciclo` só encontra `modulo3-ciclo1-variacao.md` e não o diário de alucinação. Sem ajuste na lista `ENTREGAS` do script, quem fez tudo vê os encontros 10 e 11 como ausentes. Decida antes do encontro se corrige o script ou se confere esses encontros à mão. A dúvida 5 do slide 25 orienta o aluno a mostrar o arquivo e o commit.

O tempo das apresentações depende do tamanho da turma. O roteiro abaixo prevê duas rodadas somando 130 minutos, o que comporta cerca de doze apresentações de dez minutos com transição. Turma maior exige apresentação em dupla ou corte para sete minutos, decidido e avisado antes, e não no dia.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura | 5 min | 1 a 2 |
| Ciclo 15.1 | 40 min | 3 a 8 |
| Ciclo 15.2 | 70 min | 9 a 14 |
| Intervalo | 15 min | |
| Ciclo 15.3 | 60 min | 15 a 17 |
| Ciclo 15.4 | 40 min | 18 a 22 |
| Encerramento | 10 min | 23 a 26 |

O deck foi revisado em novembro de 2026 e passou de 20 para 26 slides. Os slides novos são a linha do semestre (4), as demonstrações dos comandos c2, pares e portfolio (6, 13 e 20), o slide sobre o caso com dado errado (11) e os próximos passos depois da disciplina (24).

## Ciclo 15.1 — Conferência da C2 e últimas correções

Teoria e demonstração, 5 min. O semestre na pasta (slide 4): os quinze encontros por nota, as seis entregas e o arquivo que o `c2` procura em cada encontro. O que a C2 avalia no produto, no caminho e na apresentação, com a evidência na pasta e o critério comum às seis entregas (slide 5). A saída do `c2` sobre uma pasta de teste, com o encontro 15 parcial e o 16 ausente (slide 6).

Prática, 35 min. Cada aluno roda `c2`, confere o conteúdo com `c1` do módulo 13 e `conferir` do módulo 14, corrige com um commit por correção e cria o roteiro com o comando `apresentacao` (slides 7 e 8).

Entrega, incluída na prática.

Entregue a lista de pendências impressa no início. O aluno que descobre a pendência pelo papel corrige em dez minutos; o que descobre pelo script no meio da apresentação, não corrige.

Deixe claro, uma vez, que esta é a última janela do semestre. Depois disso a nota fecha com o que estiver na pasta.

Quem estiver com tudo em ordem usa o tempo para ensaiar a demonstração. Peça que rode o caso com dado errado ao menos uma vez antes de apresentar.

## Ciclo 15.2 — Apresentações, primeira rodada

Teoria e demonstração, 5 min. Os quatro blocos com o tempo e os campos de `entregas/roteiro-apresentacao.md` (slide 10). Validação de entrada, sintática e semântica, com o produto ilustrativo de pedidos ao almoxarifado (slide 11, conceito da OWASP). A avaliação por pares com respostas aceitas e recusadas pelo script (slide 12, Topping, 1998, e Hattie e Timperley, 2007). A saída do comando `pares` sobre um formulário incompleto (slide 13). Com quatro slides, os slides 11 e 13 podem ser mostrados em ritmo rápido.

Prática, 65 min. Apresentações.

Cronômetro visível, com aviso aos oito minutos. Corte aos dez, com gentileza e sem exceção, porque a exceção da primeira apresentação vira o padrão de todas.

Duas perguntas por apresentação, no máximo. As demais ficam para o intervalo.

O bloco 4, o que ainda não funciona, é o que a turma tende a pular. Se alguém pular, pergunte. É a parte que mais diferencia as apresentações.

Quando uma demonstração falhar ao vivo, deixe a pessoa ler a mensagem de erro e dizer o que faria. Isso vale mais que a demonstração que corre sem susto, e diga isso à turma na hora.

Circule olhando os formulários de pares. Justificativa em branco ou "ficou bom" precisa ser cobrada no momento, porque depois ninguém lembra do detalhe.

## Ciclo 15.3 — Apresentações, segunda rodada

Prática, 55 min. Mesmo formato.

Entrega, 5 min. `entregas/roteiro-apresentacao.md` e `entregas/avaliacao-pares.md`, com a rodada de `pares` para conferência.

Quem já apresentou costuma dar a melhor devolutiva, porque reconhece o problema do outro. Aponte isso para incentivar a segunda rodada de avaliações.

A ideia que cada aluno leva de cada produto assistido é um campo do formulário e serve ao fechamento do ciclo 15.4. Colete duas ou três em voz alta antes do intervalo.

## Ciclo 15.4 — O portfólio e o que continua

Teoria, 15 min. O que continua depois da disciplina (slide 19): o que funciona sem modelo, o que depende de prática e o que muda com as ferramentas. A caixa datada traz a situação em 02/11/2026 dos modelos gratuitos do OpenCode Zen e do PL 2338/2023. Reconfira as duas informações antes da aula.

Demonstração e prática, 25 min. A saída do comando `portfolio` e a estrutura de `saidas/portfolio.md` (slide 20). Cada aluno roda `portfolio`, confere a lista e escreve as três frases nos campos `o_que_ficou_pronto`, `o_que_eu_usaria_de_novo` e `o_que_eu_abandonaria` (slide 21). A entrega C2 está no slide 22.

O índice gerado costuma surpreender a turma pelo tamanho. Vale projetar o de um voluntário: quinze encontros produzem cerca de trinta arquivos, e quase ninguém percebeu isso acontecendo.

A frase sobre o que abandonaria é a mais difícil e a mais honesta. Aceite respostas que critiquem a disciplina, e anote as recorrentes para o semestre seguinte.

O aviso final é prático: a máquina do laboratório pode ser restaurada, o repositório no GitHub não. Peça que cada aluno confira, ali mesmo, que o repositório remoto está atualizado.

O encerramento (slides 23 a 26) tem o balanço do semestre por nota, com os arquivos de referência e a conferência adotada em cada bloco, os próximos passos depois da disciplina, as dúvidas frequentes e o slide final.

## O que sai deste encontro

A C2 conferida. A apresentação feita, com demonstração ao vivo e o que não funciona dito. O formulário de avaliação por pares com justificativas escritas. O portfólio do semestre com as três frases do aluno.

## Depois do semestre

Guarde os formulários de avaliação por pares. Eles são a melhor fonte sobre o que a turma entendeu, melhor que a nota das entregas, porque mostram o que um aluno consegue reconhecer no trabalho do outro.

Anote as respostas recorrentes de "o que eu abandonaria". São o insumo direto para o ajuste dos módulos no semestre seguinte.

Registre também quantos alunos ficaram sem cota do modelo em cada encontro. Se o número crescer, os ciclos de prática precisam de mais atividade sem modelo, e os scripts já foram escritos para isso.
