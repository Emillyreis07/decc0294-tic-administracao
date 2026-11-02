# Roteiro do módulo 11

Aprendizado de máquina e analytics para a decisão. Encontro 12, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

Este encontro abre o bloco da nota 3 e não tem entrega avaliada. Ele existe para que a turma saiba o que um modelo preditivo faz, o que ele não faz e quando a resposta certa é não usar modelo nenhum.

## Antes da aula

Material do professor: `slides/modulo11-aprendizado-de-maquina.html`, este roteiro e `scripts/atividade_modulo11.py`.

Publicado na turma virtual: o script e o pedido de base própria em CSV, com pelo menos 30 linhas e três colunas de número, uma delas sendo algo que faça sentido prever.

Base de reserva, obrigatória: um CSV com cerca de 40 linhas, uma coluna alvo e duas ou três preditoras com relação real, para quem chegar sem base. Dados públicos de município servem: população, receita, despesa, número de servidores.

Rode `python atividade_modulo11.py prever <base> <alvo>` antes da aula, com a base de reserva, e guarde a saída. O ciclo 11.4 fica mais curto se a turma já viu o formato do relatório.

Prepare também um caso em que o modelo perde para o palpite simples. Basta rodar `prever` usando uma coluna que não tem relação com o alvo. Esse caso é o mais importante da aula e não pode faltar: é ele que separa a turma que entendeu da que decorou.

Este encontro usa pouco ou nenhum modelo de linguagem. O script faz a conta sozinho, sem biblioteca externa. Diga isso à turma no início, porque quem está com cota estourada da semana costuma chegar preocupado.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura e visão geral | 10 min | 1 a 2 |
| Ciclo 11.1 | 45 min | 3 a 8 |
| Ciclo 11.2 | 50 min | 9 a 13 |
| Intervalo | 15 min | |
| Ciclo 11.3 | 45 min | 14 a 19 |
| Intervalo | 10 min | |
| Ciclo 11.4 | 60 min | 20 a 25 |
| Fechamento | 15 min | 26 a 29 |

## Ciclo 11.1 — Descritiva, preditiva e prescritiva

Teoria, 20 min. Slides 4 e 5. As três camadas de analytics em tabela (slide 4), com técnica típica, o que cada uma entrega e um exemplo ilustrativo de ouvidoria lido nas três camadas (1.109 atendimentos em setembro, estimativa de 1.150 para dezembro, 8 atendentes), com a definição de Sharda, Delen e Turban (2019, cap. 1). As quatro perguntas do gestor em tabela (slide 5), com o que pedir a quem propõe o modelo e o sinal de alerta de cada uma: erro comparado com quê, dados de treino, custo de cada direção do erro, quem responde (LGPD, art. 20).

Demonstração, 8 min. Slide 6. Cinco perguntas de uma ouvidoria classificadas pelo agente (saída ilustrativa), com variável a prever e palpite simples, e a instrução "não proponha algoritmo". Se houver tempo, repita com a base do encontro 9 na projeção.

Prática, 12 min. Cada aluno classifica cinco perguntas do próprio setor nas três categorias.

Entrega, 5 min. `entregas/modulo11-ciclo1-classificacao.md`.

Quase toda pergunta que a turma traz como preditiva é descritiva mal formulada. "Quantos atendimentos vamos ter" costuma ser "quantos tivemos e a série está subindo". Aponte isso, porque a maior parte das decisões de gestão se resolve na camada descritiva e não precisa de modelo.

A pergunta "comparado com quê" volta no ciclo 11.4 como o palpite simples. Plante ela aqui.

## Ciclo 11.2 — Os três tipos de aprendizado

Teoria, 30 min. Slides 10 e 11. Supervisionado, não supervisionado e por reforço em tabela (slide 10), com o que existe na base, o que cada um produz, um exemplo de gestão e como se avalia, e a definição de aprendizado de máquina de Mitchell (1997), com Taulli (2020, cap. 3). Os quatro problemas anteriores ao algoritmo (slide 11): rótulo ausente, viés do histórico (triagem de currículos da Amazon, Dastin, 2018), vazamento de dados (Kaufman et al., 2012) e avaliação no que o modelo já viu. O vazamento aparece com saída real do script sobre uma base ilustrativa de 40 unidades: prever custo_total com custo_pessoal dá 94,9% de ganho sobre o palpite, contra 70,6% com atendimentos.

Prática, 15 min. Cada aluno escolhe a abordagem para o problema que trouxe e justifica em duas frases.

Entrega, 5 min. `entregas/modulo11-ciclo2-abordagem.md`.

A variável que é consequência do alvo é o erro mais silencioso e o mais fácil de demonstrar. Prever faturamento usando comissão paga dá um modelo quase perfeito e inútil, porque a comissão só existe depois da venda. Peça à turma para procurar uma dessas na base própria.

O viés do passado merece um exemplo de seleção de pessoal ou de concessão de benefício, porque volta no módulo 12 junto com a LGPD.

## Ciclo 11.3 — Aprendizado profundo e IA generativa

Teoria, 25 min. Slides 15 a 17. O que o aprendizado profundo mudou, em diagrama comparando características escolhidas por especialista e camadas que aprendem as características (slide 15), com o ImageNet de 2012 (15,3% contra 26,2% de erro, Krizhevsky et al., 2012) e o resultado de Grinsztajn et al. (2022) sobre dados tabulares. Como se treina um modelo de linguagem (slide 16, novo): pré-treinamento autossupervisionado, ajuste por instrução supervisionado e reforço por preferência humana (Ouyang et al., 2022) e por resposta conferível nos modelos de raciocínio (DeepSeek-AI, 2025), ligados à confabulação e à regra do cálculo por script. Quando a explicação é exigível, em tabela (slide 17): decisão só automatizada sobre pessoa (LGPD, art. 20, caput e § 1º), ato administrativo que nega direito (Lei 9.784/1999, art. 50, e Lei 14.133/2021, art. 5º) e decisão sobre agregado. O veto mantido em 2019 à revisão por pessoa natural, Rudin (2019) sobre modelos interpretáveis e a situação do PL 2338/2023 (aguarda parecer na comissão especial da Câmara, consulta em 2/11/2026).

Prática, 15 min. Cada aluno analisa um caso do próprio setor, aplica as quatro perguntas e situa o caso na tabela do slide 17.

Entrega, 5 min. `entregas/modulo11-ciclo3-caso.md`.

A distinção útil é entre decisão que afeta uma pessoa identificada e decisão que afeta um agregado. Prever demanda de estoque não pede explicação individual; negar um benefício pede.

O direito à revisão do artigo 20 é sobre decisão automatizada que afeta interesses do titular. Leia o texto na tela em vez de parafrasear, porque a paráfrase costuma ampliar o alcance do artigo.

## Ciclo 11.4 — Um modelo simples sobre a sua base

Teoria, 12 min. Slides 21 e 22. O palpite simples como régua, com o cálculo do erro médio absoluto em cinco casos ilustrativos (4,2 contra 13,2, redução de 68,2%) e o caso da categoria mais comum (slide 21). A separação treino e teste em diagrama com a regra do script (slide 22, novo): linhas com célula vazia descartadas, embaralhamento com semente 42, 70% para treino, palpite igual à média do treino, e as recusas do comando `prever`.

Demonstração, 10 min. Slide 23. Duas execuções de `prever` sobre a base ilustrativa de 40 unidades: `atendimentos` ganha do palpite (70,6%) e `area_m2` perde. Repita na projeção com a base de reserva, cujos números serão outros, incluindo o caso em que o modelo perde para o palpite simples.

Prática, 30 min. Slide 24. Cada aluno roda `iniciar`, preenche `modelo/ficha-modelo.md`, roda `prever` com uma e depois com duas preditoras, escreve a seção Leitura do resultado e roda `conferir`. O `resultado.md` guarda só a última execução, por isso a versão entregue é rodada por último e a comparação vai para a Leitura.

Entrega, 8 min. `modelo/ficha-modelo.md` e `modelo/resultado.md`.

O script recusa a conferência se o custo de errar para mais e o de errar para menos estiverem com a mesma resposta, e se o aluno declarar que usaria o modelo depois de ele ter perdido do palpite simples sem escrever a ressalva. As duas recusas são o conteúdo do ciclo.

O campo `o_modelo_ganhou_do_palpite_simples` precisa de `sim` ou `nao` sem acento. O script compara com o `resultado.md`, que grava `nao`, e recusa `não` como divergência. O deck avisa disso no slide 25 e nas dúvidas frequentes (slide 28).

Modelo que perde para a média é resultado válido e deve ser dito assim em voz alta, várias vezes. Aluno que troca de coluna até "dar certo" está aprendendo o hábito errado.

A leitura do coeficiente descreve a base e não prova causa. Repita isso ao ver o primeiro aluno escrever "cada vendedor a mais gera tantos reais".

## O que sai deste encontro

Cinco perguntas classificadas nas três camadas de análise. Uma abordagem de aprendizado escolhida e justificada. Um caso do setor analisado quanto à exigência de explicação. Um modelo treinado sobre base própria, comparado com o palpite simples e lido em duas frases.

## Avisos no fechamento

O encontro 13 trata de governança de dados, LGPD e cibersegurança. Cada aluno precisa levantar, antes da aula, quais dados pessoais passam pelas mãos dele no trabalho ou no estágio, e por onde eles circulam. Basta uma lista, sem nenhum dado real anotado.

Deixe claro que ninguém deve trazer arquivo com dado pessoal de terceiro para a sala. A lista é de tipos de dado e de caminhos, não de conteúdo.
