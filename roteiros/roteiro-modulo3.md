# Roteiro do módulo 3

Inteligência artificial, modelos de linguagem e engenharia de prompt. Encontro 4, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

## Antes da aula

Material do professor: `slides/modulo3-ia-e-engenharia-de-prompt.html`, este roteiro e `scripts/atividade_modulo3.py`.

Publicado na turma virtual com uma semana de antecedência: o capítulo 1 de Taulli, o script e o aviso de que cada aluno precisa trazer uma referência bibliográfica que use em algum trabalho seu.

Antes do encontro, confira quem ficou pendente na entrega A1 do encontro 3. Aluno sem repositório não consegue gravar nada hoje, e o problema se agrava a cada semana.

Teste o roteiro na semana da aula, não no início do semestre: o provedor gratuito muda de modelo e de limite sem aviso.

Desde a revisão de novembro de 2026 os slides não trazem marcadores de tempo. Os tempos por etapa ficam neste roteiro.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura e visão geral | 10 min | 1 a 2 |
| Ciclo 3.1 | 50 min | 3 a 14 |
| Ciclo 3.2 | 55 min | 15 a 22 |
| Intervalo | 15 min | |
| Ciclo 3.3 | 55 min | 23 a 30 |
| Intervalo | 10 min | |
| Ciclo 3.4 | 45 min | 31 a 38 |
| Fechamento e vocabulário | 15 min | 39 a 44 |

Revisão de novembro de 2026: o deck passou de 42 para 44 slides. Entraram três slides de teoria com diagrama no ciclo 3.1, sobre tokens e previsão do próximo token (7), o que ocupa a janela de contexto (10) e o ciclo do agente com ferramentas e o MCP (11). O antigo slide sobre o que o modelo faz foi absorvido pelo slide 7. Os slides de conceito estão em 4, 6, 9, 16 e 24, e o vocabulário em 40 e 41. As informações datadas (janelas de contexto, datas de corte, MCP, recomendações de prompt da Anthropic, OpenAI e Google, teste SimpleQA) foram conferidas em 02/11/2026 e precisam ser reconferidas antes de cada semestre.

O deck foi refeito para uma turma sem contato anterior com o tema. Entraram cinco slides de conceito, com a tarja CONCEITO, que definem cada termo antes do primeiro uso: inteligência artificial, treinamento e data de corte, sessão e janela de contexto, alucinação, engenharia de prompt. Entrou também um slide sobre onde se confere cada tipo de afirmação, com o procedimento concreto para artigo, lei, número e sistema. Dois slides de vocabulário fecham o encontro.

Nos slides de conceito, a frase grande no topo é a definição, os quatro pontos abaixo a sustentam e a caixa dourada no pé traz a analogia. Leia a analogia em voz alta e peça um exemplo da turma antes de avançar. São eles que seguram o resto do encontro numa turma que nunca ouviu falar do assunto.

## Ciclo 3.1 — O que é IA e o que é um modelo de linguagem

Teoria, 25 min. As três técnicas chamadas de IA, em tabela (slide 5). Tokens e previsão do próximo token (slide 7). O que o mecanismo explica no uso diário (slide 8). O que ocupa a janela de contexto, com a compactação do opencode (slide 10). O ciclo do agente com ferramentas e o MCP (slide 11). Com oito slides de teoria, os slides 10 e 11 podem ser apresentados de forma breve, porque os módulos 5, 10 e 4 retomam janela, conectores e agente.

Demonstração, 8 min. A mesma instrução rodada duas vezes, em sessões separadas, com as duas respostas gravadas em arquivo.

Prática, 12 min. Cada aluno repete com um conceito da própria área.

Entrega, 5 min. `entregas/modulo3-ciclo1-variacao.md`.

Os três slides de conceito do ciclo, 4, 6 e 9, sustentam tudo o que vem depois. O de treinamento explica por que ele não consegue abrir a fonte e traz a data de corte e os modelos de raciocínio. O de sessão e janela de contexto explica por que a demonstração exige sessões separadas e por que ele esquece uma regra dada no início da conversa, agora com a compactação do opencode. Não passe rápido por eles para ganhar tempo: o tempo se perde depois, em dúvida repetida.

Ponto de atenção: alguém vai concluir que a variação torna a ferramenta inútil. A resposta é que variação de redação não é o problema; variação de fato é. O exercício serve para separar as duas.

## Ciclo 3.2 — Alucinação e verificação

Conceito, 8 min. O que é alucinação, também chamada confabulação, slide 16. Os quatro pontos seguem esta ordem: sem intenção de enganar, sem aviso no texto, concentrada no que sustenta decisão e presente também nos modelos novos. O último muda o comportamento do aluno, porque mostra que a conferência não depende da versão do modelo.

Teoria, 15 min. Os quatro tipos de erro com o rótulo aceito pelo script, slide 17. Por que acontece e o que reduz, slide 18, com o gráfico do teste SimpleQA publicado pela OpenAI em 05/09/2025, em que o modelo que se abstém mais erra menos com acerto parecido. Depois, onde se confere cada tipo de afirmação, slide 19, que é o slide mais operacional do encontro: título entre aspas no Google Acadêmico, DOI em doi.org, artigo no texto compilado do Planalto, número no órgão que o produz, procedimento no próprio sistema. Boa parte da turma nunca conferiu uma referência dessa forma.

Demonstração, 7 min. A instrução com e sem a autorização do NÃO SEI, sobre a referência que o aluno trouxe. Vale rodar as duas versões na projeção: a diferença costuma ser visível.

Prática, 20 min. Cinco casos no diário, com o script.

Entrega, 5 min. `entregas/modulo3-diario-de-alucinacao.csv` e o `.md` gerado.

O script exige pelo menos três tipos diferentes de erro entre os cinco casos e recusa a coluna de conferência preenchida com "pesquisei". Ele aceita os rótulos e os vereditos só sem acento (por exemplo, nao verificavel), e os slides 17 e 21 mostram isso, este último com a saída real do comando conferir. A recusa gera reclamação e faz parte do exercício, porque a nota recai sobre a conferência.

Resultado esperado, caso a cota acabe: o aluno registra os casos que conseguiu, anota a indisponibilidade e completa os demais em casa. O mínimo de três tipos continua valendo.

## Ciclo 3.3 — Os quatro elementos de um prompt

Teoria, 22 min. Papel, contexto, instrução e formato num prompt anotado (slide 25). O prompt fraco e o forte lado a lado (slide 26). Os quatro erros que estragam um prompt bom, com a base na documentação da Anthropic e do Google (slide 27). O slide de conceito (24) apresenta também a engenharia de contexto.

Demonstração, 13 min. O slide 28 já traz um prompt fraco e sua versão forte, prontos, sobre um edital de compras. Projete os dois, rode as duas versões ao vivo e compare o que muda na resposta com a turma.

Prática, 15 min. A tarefa agora é fixa para toda a turma, um parecer sobre terceirizar a limpeza de um prédio público, para o professor poder comparar os pares entre si. Cada aluno inventa o órgão e o papel que dão contexto, e escreve o próprio par de prompts.

Entrega, 5 min. `prompts/modulo3-par-de-prompts.md`.

Este é o ciclo mais produtivo do módulo e o que mais rende em qualidade de trabalho no resto do semestre. Se algum ciclo precisar ceder tempo, não seja este.

## Ciclo 3.4 — Técnicas e quando cada uma vale

Teoria, 18 min. Exemplos, passo a passo, do simples ao complexo, com a coluna sobre modelos de raciocínio (slide 32): a OpenAI recomenda não pedir passo a passo a esses modelos, e a Anthropic prefere instrução geral a roteiro escrito à mão. Verificação em cadeia e consistência (slide 33), com a ressalva de que número repetido nas execuções também precisa de fonte. Depois, dois slides de fecho: escolher a técnica pelo erro que ela evita (34) e a pergunta entre trocar de técnica ou trocar de modelo, com o esforço de raciocínio (35).

Demonstração, 6 min. O slide 36 já traz as duas instruções prontas, sem exemplos e com exemplos, cada uma gravando num arquivo de nome diferente (classificacao-sem-exemplos.csv e classificacao-com-exemplos.csv). As três demandas a classificar estão escritas no próprio prompt, não dependem de nenhum arquivo de dados. Rode as duas e abra os arquivos lado a lado.

Prática, 16 min. Três técnicas, um arquivo por técnica em prompts/, e uma delas repetida em outro modelo por quem tiver acesso.

Entrega, 5 min. Três arquivos em `prompts/`.

O critério de escolha é o tipo de erro, não o custo. Isso foi decidido assim porque o aluno pode trocar de provedor durante o semestre, e um critério ancorado em cota deixaria de valer no dia em que ele mudasse. O tipo de erro que cada técnica evita continua valendo em qualquer modelo.

O slide sobre trocar de modelo é o mais importante do ciclo. A ordem que ele fixa é instrução, técnica, modelo. Aluno que troca de modelo antes de corrigir a instrução nunca descobre onde estava o problema, e leva esse hábito para a organização onde vai trabalhar.

Se parte da turma estiver em provedores diferentes, aproveite: peça que dois alunos com modelos distintos leiam em voz alta o resultado da mesma instrução. A comparação em sala rende mais que qualquer slide.

## O que sai deste encontro

Uma comparação de variação, um diário de alucinação com cinco casos, um par de prompts e o início do caderno de prompts. Os três primeiros compõem a entrega A2, avaliada no encontro 6.

## Avisos no fechamento

Gravar e publicar antes de sair da sala, com a mensagem "entregas do modulo 3".

Trazer um documento da própria área para o encontro 5: edital, contrato, relatório ou regulamento, em PDF ou Word, sem dado pessoal de terceiro.

A escolha da organização do projeto precisa estar fechada até o encontro 6.
