# Roteiro do módulo 10

Pesquisa, documentos longos e análise qualitativa. Encontro 11, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

Este encontro fecha a entrega B2, que vale 40% da nota 2, e com ela a nota 2 inteira.

## Antes da aula

Material do professor: `slides/modulo10-pesquisa-e-analise-qualitativa.html`, este roteiro e `scripts/atividade_modulo10.py`.

Publicado na turma virtual, com pelo menos uma semana de antecedência: o pedido de que cada aluno traga um documento longo do próprio setor, com dez páginas ou mais, e um arquivo de respostas abertas em CSV, se tiver acesso a um. Relatório de gestão, plano diretor, edital, contrato e ata de reunião longa servem.

Material de reserva, obrigatório: um relatório de gestão público em PDF e um CSV de respostas abertas de pesquisa de satisfação, com pelo menos 40 linhas. Todo semestre parte da turma chega sem documento, e sem reserva esses alunos ficam parados.

Rode `python atividade_modulo10.py codificar <csv>` antes da aula sobre o CSV de reserva, para conhecer a amostra de 20 que o script sorteia. A semente é fixa, então a amostra da sua aula é a mesma da sua preparação.

Selecione uma lei ou norma que a turma conheça, para o ciclo 10.4. Lei 8.666 e Lei 14.133 são úteis porque muito aluno já ouviu falar e quase ninguém leu, e porque o modelo confunde as duas com frequência, o que é exatamente o que o ciclo quer mostrar.

Confira quem está pendente na B1 e nos encontros 9 e 10. A nota 2 fecha aqui.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura e visão geral | 10 min | 1 a 2 |
| Ciclo 10.1 | 50 min | 3 a 8 |
| Ciclo 10.2 | 45 min | 9 a 15 |
| Intervalo | 15 min | |
| Ciclo 10.3 | 55 min | 16 a 22 |
| Intervalo | 10 min | |
| Ciclo 10.4 | 50 min | 23 a 26 |
| Fechamento e B2 | 15 min | 27 a 31 |

## Ciclo 10.1 — Leitura em camadas de documento longo

Teoria, 20 min. Slide 4: por que o resumo sem pergunta falha, com a janela de contexto e a queda de acerto quando a informação está no meio de um texto longo (Liu et al., 2024. Hong, Troynikov e Huber, 2025). Slide 5: as quatro camadas (mapa, extração com trecho de origem, análise sobre a lista, síntese), cada uma com o seu arquivo em saidas/ e a síntese em entregas/modulo10-ciclo1-sintese.md.

Demonstração, 12 min. As quatro camadas aplicadas ao relatório de reserva, na projeção. Mostre a extração pedindo o trecho de origem junto de cada afirmação e depois procure o trecho no documento, na frente da turma. O slide 6 traz um exemplo ilustrativo com um trecho que não existe no contrato.

Prática, 13 min. Cada aluno aplica as camadas ao documento que trouxe.

Entrega, 5 min. `entregas/modulo10-ciclo1-sintese.md`.

O trecho de origem é o item central do encontro inteiro. Afirmação sem trecho localizável no documento é descartada. Faça uma verificação ao vivo que falhe, se aparecer uma, e não conserte o slide para esconder isso.

Documento longo consome contexto. Com modelo gratuito, oriente a trabalhar por seção e não pelo arquivo inteiro. Duas requisições longas por aluno bastam neste ciclo.

## Ciclo 10.2 — Comparação setorial com fontes verificadas

Teoria, 20 min. Slide 10: os três defeitos (período, medida e fonte secundária). Slide 11, novo: exemplo numérico com três municípios fictícios em que a ordem da despesa com saúde por habitante se inverte entre despesa empenhada e despesa paga (Lei 4.320/1964, arts. 58, 63 e 64). Slide 12: o procedimento em quatro passos. Slide 13: demonstração dos comandos fontes e conferir, dentro do tempo de teoria. Avise que, antes do ciclo 10.3, o conferir acusa também a falta da codificação e do livro de códigos.

Prática, 20 min. Cada aluno monta a comparação de três organizações do setor que escolheu, com ficha de fonte para cada número.

Entrega, 5 min. `entregas/modulo10-ciclo2-comparacao.md`.

Número sem ano e sem fonte sai da tabela. Essa é a regra e ela reprova mais linhas do que a turma espera. Avise antes, para o aluno não montar quinze linhas e perder dez.

`atividade_modulo10.py fontes` cria a ficha em branco. O aluno preenche uma por número, não uma por organização.

## Ciclo 10.3 — Análise de conteúdo de respostas abertas

Teoria, 20 min. Slide 17: o livro de códigos (Bardin, 1977), com um exemplo de categoria e as regras de exaustividade e exclusão mútua. Slide 18: a dupla codificação em fluxo, com o limite de 70% do script e dois estudos sobre modelo de linguagem como codificador (Gilardi, Alizadeh e Kubli, 2023. Reiss, 2023). Slide 19, novo: concordância ao acaso e kappa de Cohen, calculado à mão sobre os 20 casos fictícios da demonstração (75% de concordância, kappa de 0,65).

Demonstração, 10 min. `codificar` sobre o CSV de reserva na projeção. O script detecta a coluna de texto mais longa, sorteia 20 respostas com semente fixa e monta as duas rodadas.

Prática, 20 min. Em duplas: cada aluno codifica as mesmas 20 respostas, sem olhar o do colega, e depois roda `concordancia`.

Entrega, 5 min. `entregas/modulo10-ciclo3-codificacao.md`.

O limite de 70% de concordância não é nota, é gatilho. Abaixo dele o script exige o campo `divergencia_examinada`, e é ali que o aprendizado acontece: quase sempre a definição da categoria estava ambígua, não o colega estava errado.

Duplas com concordância de 100% na primeira rodada costumam ter categorias amplas demais ("positivo", "negativo"). Vale conferir uma delas em voz alta.

Este ciclo não usa modelo de linguagem em nenhum passo. É proposital: a turma precisa ver que categorizar é trabalho de julgamento e que o modelo, quando entra, entra depois do livro de códigos pronto.

## Ciclo 10.4 — Legislação e o teste de alucinação jurídica

Teoria, 15 min. Slide 24: numeração, vigência e aplicação, com exemplos da Lei 14.133/2021 (definição de pregão no art. 6º, XLI, revogação da Lei 8.666/1993 em 30/12/2023, valor do art. 75, II, atualizado para R$ 65.492,11 pelo Decreto 12.807/2025), o estudo de Dahl et al. (2024) e a multa aplicada pelo TSE por julgados inexistentes gerados por IA. Slide 25: demonstração do teste em três passos (instrução com texto literal e NÃO SEI, conferência no Planalto, classificação em confirmado, dispositivo errado, redação desatualizada ou inexistente), dentro do tempo de teoria.

Prática, 25 min. Cada aluno faz o teste sobre a lei escolhida e registra o que passou e o que não passou.

Entrega, 10 min. `entregas/modulo10-ciclo4-legislacao.md` e depois `python atividade_modulo10.py b2`.

O aluno que não encontrar nenhum erro deve escrever isso, e não inventar um. O resultado honesto do teste é o resultado.

Reserve os últimos dez minutos para a rodada `b2` de cada aluno. O script lista item por item o que falta da nota 2 inteira, e é melhor descobrir isso em sala do que na semana seguinte.

## O que sai deste encontro

Uma síntese em quatro camadas com trechos de origem. Uma comparação de três organizações com ficha de fonte por número. Um livro de códigos com dupla codificação e concordância medida. Um teste de alucinação jurídica documentado.

Com a B2 fechada, a nota 2 está completa. O bloco seguinte, encontros 12 a 16, é o da nota 3.

## Avisos no fechamento

O encontro 12 trata de aprendizado de máquina. Cada aluno precisa trazer uma base própria em CSV com pelo menos 30 linhas e três colunas de número, uma delas sendo algo que faça sentido prever. A base do encontro 7 serve, se tiver colunas numéricas suficientes.

Quem não tiver base usa a de reserva, mas perde o vínculo com o próprio trabalho, que é o que dá sentido ao ciclo 11.4.
