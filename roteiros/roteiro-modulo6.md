# Roteiro do módulo 6

Análise exploratória de dados. Encontro 7, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

Começa a nota 2.

## Antes da aula

Material do professor: `slides/modulo6-analise-exploratoria.html`, este roteiro e `scripts/atividade_modulo6.py`.

Publicado na turma virtual: o script e o lembrete de que a base tratada precisa estar em `dados/` e as três perguntas de gestão escritas.

Rode o script sobre a base de reserva antes da aula, para conhecer a saída que a turma vai ver. O script é determinístico e não usa modelo, então o resultado do seu teste é exatamente o que aparecerá na tela dos alunos com o mesmo arquivo.

Prepare uma base de reserva com defeitos plantados: uma coluna com valores em branco, uma com vírgula decimal, dois valores mil vezes maiores por unidade trocada, um valor negativo impossível e uma linha duplicada. É o material que faz o ciclo 6.3 funcionar mesmo para quem trouxe uma base limpa demais.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura e visão geral | 10 min | 1 a 2 |
| Ciclo 6.1 | 45 min | 3 a 8 |
| Ciclo 6.2 | 55 min | 9 a 14 |
| Intervalo | 15 min | |
| Ciclo 6.3 | 50 min | 15 a 21 |
| Intervalo | 10 min | |
| Ciclo 6.4 | 50 min | 22 a 27 |
| Fechamento | 15 min | 28 a 31 |

## Ciclo 6.1 — Da pergunta de gestão à pergunta de dados

Teoria, 18 min. Análise exploratória e análise confirmatória (Tukey, 1977), com o problema das comparações múltiplas: em 20 comparações sem efeito real, a 5% de significância, a chance de ao menos um falso positivo é 64%. A pergunta de gestão e a pergunta de dados, com a definição da medida em numerador, denominador, período e recorte.

Demonstração, 7 min. A tradução de uma pergunta, com a instrução que proíbe calcular antes de listar o que falta.

Prática, 15 min. Três perguntas de gestão, traduzidas.

Entrega, 5 min. `entregas/modulo6-ciclo1-perguntas.md`.

O critério que separa pergunta boa de pergunta ruim é se alguém decide algo com a resposta. Aplique em voz alta a duas ou três perguntas da turma: a maioria vira pedido de estatística descritiva sem destinatário, e a correção em público ensina mais que o slide.

O "não calcule nada ainda" da instrução é deliberado. Sem ele o modelo entrega um número e o aluno aceita a definição implícita que ele usou, que é justamente a decisão que deveria ser do administrador.

## Ciclo 6.2 — Perfil da base

Teoria, 20 min. Os quatro passos antes de qualquer gráfico. Média, mediana e a distância entre elas.

Demonstração, 8 min. O script perfilando a base de reserva na projeção.

Prática, 22 min. Cada aluno perfila a própria base, lê o perfil inteiro e pede a interpretação ao agente.

Entrega, 5 min. `entregas/modulo6-ciclo2-perfil.md`.

Vale mostrar na projeção a linha da coluna de custo da base de reserva, em que a média fica muito acima da mediana por causa dos dois valores de unidade trocada. É a demonstração mais eficiente do módulo, e antecipa o ciclo seguinte.

O script não usa o modelo. Diga isso: cálculo determinístico dá sempre o mesmo resultado, e por isso o perfil é auditável de um jeito que a resposta de um modelo não é. O modelo entra depois, para interpretar.

Quem trouxe arquivo que o script não abre tem o defeito no arquivo, não no script. A mensagem informa o que foi tentado. Corrigir separador ou codificação é parte da atividade.

## Ciclo 6.3 — Valores ausentes e atípicos

Teoria, 22 min. Os três mecanismos de ausência do formulário e a terminologia de Rubin (1976): ausente ao acaso (MCAR), por regra (ausência estrutural) e com viés (MAR ou MNAR). O exemplo numérico do slide 17, em que a ausência com viés inverte a conclusão e o preenchimento pela média não corrige. A árvore de classificação do valor atípico e as cercas de Tukey, que são o critério do script.

Demonstração, 6 min. O script apontando os casos e criando o formulário de decisão.

Prática, 17 min. Cada aluno decide sobre cada caso, com a razão escrita.

Entrega, 5 min. `entregas/modulo6-tratamento.csv`.

O ausente com viés é o conteúdo mais importante do ciclo e o menos intuitivo. Use o exemplo do slide 17: a unidade Norte parece custar 100 e o Sul 150, mas os meses caros do Norte não foram lançados e o custo real do Norte é 200. Preencher os vazios pela média leva o Norte a 116,7 e mantém a conclusão invertida.

O script recusa duas coisas: decisão sem razão escrita, e exclusão de um valor classificado como realidade. A segunda regra existe porque excluir o que atrapalha a média é o atalho mais comum e o mais grave. A alternativa legítima é separar em análise própria e dizer que se fez isso.

## Ciclo 6.4 — Conferência dos números calculados pelo agente

Teoria, 20 min. Os dois caminhos do número calculado pelo agente (escrito na resposta ou produzido por script) e o tipo de erro de cada um. As quatro conferências e o campo correspondente no log.

Demonstração, 6 min. A instrução que pede o script junto do número, com as linhas descartadas e o total antes do filtro.

Prática, 19 min. Cinco números calculados e conferidos, registrados no log.

Entrega, 5 min. `entregas/modulo6-log-verificacao.csv`.

O ponto que precisa ficar: quando o agente escreve e executa um script, o risco muda de lugar. Sai do cálculo, que passa a ser confiável, e vai para o filtro aplicado. Por isso a instrução pede as linhas descartadas e o total antes do filtro.

O script marca com aviso, e não com erro, o número que ninguém recalculou na mão. É a conferência mais barata que existe e a mais ignorada.

Cinco números que passam nas quatro conferências na primeira tentativa é improvável. Se acontecer na turma inteira, o mais provável é que as conferências não tenham sido feitas.

## O que sai deste encontro

Três perguntas de gestão traduzidas em perguntas de dados, o perfil completo da base, o tratamento de ausentes e atípicos com razão registrada, e cinco números com log de verificação. É o começo da nota 2.

## Avisos no fechamento

Deixar a base tratada em `dados/`, com o arquivo original preservado ao lado. No encontro 8 as duas bases viram tabelas ligadas por uma chave.

Escrever cinco perguntas que só podem ser respondidas cruzando as duas bases. São elas que viram consultas.

A entrega B1, no encontro 9, reúne o trabalho dos encontros 7, 8 e 9. Quem atrasar aqui chega sem base para consultar.
