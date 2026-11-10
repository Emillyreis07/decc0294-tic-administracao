# Roteiro do módulo 9

Automação de documentos e processos. Encontro 10, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

Este encontro não tem entrega avaliada própria. O que se produz aqui entra na entrega B2, conferida no encontro 11 pelo comando `b2` do script do módulo 10, que percorre os encontros 10 e 11. É o encontro em que a turma sai do relatório pontual e passa para o fluxo repetível.

## Antes da aula

Material do professor: `slides/modulo9-automacao.html`, este roteiro e `scripts/atividade_modulo9.py`.

Publicado na turma virtual: o script e o pedido de que cada aluno traga uma tarefa que ele mesmo repete, com periodicidade e tempo gasto. Sem a tarefa trazida, o aluno passa o primeiro ciclo procurando assunto.

Rode `python atividade_modulo9.py iniciar` e depois `gerar` uma vez antes da aula, com um modelo de duas variáveis e três linhas de dados. Ver o arquivo saindo pronto três vezes é o que convence a turma de que o modelo com variáveis não é firula.

Prepare uma planilha de exemplo com uma coluna faltando de propósito, para a demonstração do ciclo 9.2. O script recusa a geração quando um marcador não tem coluna, e essa recusa é conteúdo, não defeito.

Separe também um caso local de automação que deu errado. Sistema que emitiu ofício com nome trocado, boleto duplicado, e-mail em massa com campo não preenchido. O ciclo 9.3 depende de um exemplo concreto de erro em escala.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura e visão geral | 10 min | 1 a 2 |
| Ciclo 9.1 | 45 min | 3 a 9 |
| Ciclo 9.2 | 55 min | 10 a 16 |
| Intervalo | 15 min | |
| Ciclo 9.3 | 45 min | 17 a 22 |
| Intervalo | 10 min | |
| Ciclo 9.4 | 55 min | 23 a 27 |
| Fechamento | 15 min | 28 a 31 |

## Ciclo 9.1 — O que é automatizável

Teoria, 15 min. Slides 4 a 6. Coleta, produção e decisão (slide 4), com dois casos brasileiros: o Alice (CGU e TCU), que automatiza coleta e produção de alertas e deixa a decisão com a auditoria, e a concessão automática do INSS, em que a decisão é automatizada e o TCU determinou ajustes (Acórdão 1.498/2026-Plenário). Os quatro sinais de tarefa automatizável em tabela com pergunta de verificação e exemplos (slide 5, novo): entrada previsível, regra escrita, saída conferível, repetição com frequência conhecida. O método de decomposição em quatro etapas (slide 6).

Demonstração, 10 min. Slide 7. O relatório mensal da ouvidoria (exemplo ilustrativo) decomposto em oito passos, 120 minutos por execução, com 45% em coleta, 35% em produção e 20% em decisão. A instrução pede a soma por classe em script gravado em saidas/, conferida à mão.

Prática, 15 min. Cada aluno decompõe a tarefa que trouxe.

Entrega, 5 min. `entregas/modulo9-ciclo1-decomposicao.md`.

O erro comum é decompor em três passos genéricos ("coletar, analisar, escrever"). Peça grão fino: de onde vem cada número, quem abre qual arquivo, qual é a ordem. Um aluno que escreve oito passos aprendeu mais do que um que escreveu três.

O julgamento não sai da lista. Ele é marcado como julgamento e continua com o humano. Essa marcação é o que separa automação de terceirização de responsabilidade.

## Ciclo 9.2 — Modelos de documento com variáveis

Teoria, 20 min. Slides 11 a 13. O modelo com `[VARIAVEIS]` em diagrama (modelo, tabela, script, três documentos) e a definição de modelo com variáveis, ligada à mala direta (slide 11). Substituição por script e redação pelo agente comparadas (slide 12, novo): repetibilidade, falha característica, para onde vão os dados e conferência necessária. As quatro regras sobre um trecho anotado do modelo (slide 13): nome descritivo em maiúsculas e sem acento (o script só reconhece A a Z, algarismos e sublinhado), nenhum número no texto fixo, regra para dado ausente, responsável e data de revisão no topo.

Demonstração, 15 min. Slide 14. Um modelo executado três vezes com dados diferentes, na projeção, incluindo a execução com a coluna faltando, para que a turma veja o script recusar e depois preencher com `NAO INFORMADO` e o aviso no topo.

Prática, 15 min. Cada aluno escreve o próprio modelo e roda `gerar` sobre a base que trouxe.

Entrega, 5 min. `entregas/modulo9-ciclo2-modelo.md` e os três documentos gerados.

O aviso de valor ausente é o ponto do ciclo. Documento gerado com buraco silencioso é pior que documento não gerado, porque circula com aparência de completo. Diga isso enquanto o banner aparece na tela.

Este é o ciclo mais longo do encontro e o que mais consome cota do modelo gratuito. Duas requisições longas por aluno bastam. O restante é o script, que não usa modelo nenhum.

## Ciclo 9.3 — Automação de processos e seus limites

Teoria, 25 min. Slides 18 a 20. API, RPA e agentes de uso do computador comparados (slide 18), com a definição de RPA da IEEE 2755-2017, Taulli (2020, cap. 5) e os resultados do OSWorld. O ponto de conferência humana em diagrama, antes do passo irreversível, com onde, o quê, quem e o que fazer se falhar (slide 19). Quando não automatizar, em quatro situações (slide 20): baixa frequência, regra instável, processo em mudança e decisão sobre direito de pessoa (LGPD, art. 20), com a previsão do Gartner sobre projetos de IA agêntica.

Prática, 15 min. Cada aluno declara o ponto de conferência do fluxo que está montando e escreve o que a pessoa confere ali, em uma frase verificável.

Entrega, 5 min. `entregas/modulo9-ciclo3-conferencia.md` e as quatro linhas correspondentes de `entregas/modulo9-fluxo.csv`.

"O gestor revisa" não é ponto de conferência. "O coordenador confere se o total do relatório bate com o extrato do mês" é. Exija o segundo formato.

O caso local de erro em escala entra aqui. A pergunta para a turma é onde estaria o ponto de conferência que teria pegado aquele erro, e por que ele não existia.

## Ciclo 9.4 — Um fluxo repetível e medido

Teoria, 15 min. Slides 24 e 25. Os cinco itens da documentação e quem preenche cada um no relatório gerado pelo script (slide 24), com a definição de ponto de equilíbrio. A demonstração do comando `conferir` (slide 25), com a saída do script, o gráfico de minutos acumulados e a comparação com a estimativa do módulo 1, entra no tempo da teoria.

Prática, 30 min. Cada aluno preenche a ficha do fluxo e roda `conferir`. O script calcula em quantas execuções a automação se paga e recusa a entrega se o responsável for "a equipe".

Entrega, 10 min. `entregas/modulo9-fluxo.csv` e `entregas/modulo9-relatorio.md`, gerado pelo comando `conferir`.

O ponto de equilíbrio é a defesa do aluno diante de uma chefia. Quatro horas de construção, vinte minutos economizados por semana, doze execuções para pagar, três meses. Esse cálculo cabe em um e-mail e é o que aprova ou reprova a ideia.

Nome e cargo de responsável são obrigatórios porque fluxo sem dono para de funcionar no primeiro mês em que ninguém roda. O script recusa "a equipe" de propósito.

## O que sai deste encontro

Uma tarefa decomposta em passos com marcação de julgamento. Um modelo de instrução com variáveis, testado em três casos. Um ponto de conferência humana declarado. Um fluxo documentado com ganho medido e ponto de equilíbrio calculado.

Esses quatro arquivos são a matéria-prima do módulo 14 e do projeto integrador. Quem sai daqui sem eles chega ao encontro 15 sem processo para transformar em produto.

## Avisos no fechamento

O encontro 11 fecha a entrega B2, que vale 40% da nota 2. Cada aluno precisa trazer um documento longo do próprio setor, com no mínimo dez páginas, e um arquivo com respostas abertas, se tiver. Sem os dois, o encontro 11 roda com material de reserva e o aluno perde o vínculo com o trabalho dele.

Quem ficou pendente na B1 tem até o encontro 11 para regularizar. Diga isso com a lista na mão.
