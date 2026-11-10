# Roteiro do módulo 4

Do prompt ao artefato: arquivos, agentes e configuração. Encontro 5, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

## Antes da aula

Material do professor: `slides/modulo4-do-prompt-ao-artefato.html`, este roteiro e `scripts/atividade_modulo4.py`.

Publicado na turma virtual: o script e o lembrete de trazer um documento da própria área, em PDF ou Word, sem dado pessoal de terceiro.

Prepare um documento de reserva, com dez a quinze páginas, para quem esquecer. Um edital de pregão publicado no Portal de Compras serve bem: é público, tem obrigações claras e rende os três estágios da cadeia do ciclo 4.4.

Teste obrigatório numa máquina do laboratório, na semana da aula. O ciclo 4.3 depende de rede, e a rede é o que mais varia:

1. Instale o MCP gravando o opencode.json do slide 25 na raiz de um projeto de teste e confirme que as quinze ferramentas aparecem (no terminal, `opencode mcp list` mostra o servidor). Isso exige Node.js instalado e acesso ao registro de pacotes npm.
2. Rode `python atividade_modulo4.py apis testar` e anote quais das oito fontes a rede do CCET alcança. Rode também `apis cnpj 06279103000119`, a consulta usada nos slides 25 e 27.
3. O arquivo de configuração é o `opencode.json` na raiz do projeto, ao lado do AGENTS.md, com o bloco `mcp` (documentação em opencode.ai/docs/mcp-servers, consultada em 2 nov. 2026). A versão de setembro do slide trazia o bloco `mcpServers`, formato de outros programas que o opencode não lê.

Se o laboratório bloquear a instalação do MCP ou os domínios das APIs, o ciclo continua funcionando: a atividade foi desenhada para que o diagnóstico de bloqueio seja parte da entrega. Mas você precisa saber disso antes da aula, não durante.

Confira antes da aula quais alunos ainda não têm o AGENTS.md preenchido do encontro 3. Sem ele, o ciclo 4.2 não funciona, e a correção é rápida se feita antes.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura e visão geral | 10 min | 1 a 2 |
| Ciclo 4.1 | 48 min | 3 a 10 |
| Ciclo 4.2 | 45 min | 11 a 18 |
| Intervalo | 15 min | |
| Ciclo 4.3 | 75 min | 19 a 30 |
| Intervalo | 10 min | |
| Ciclo 4.4 | 40 min | 31 a 36 |
| Fechamento e vocabulário | 15 min | 37 a 42 |

O deck foi refeito para uma turma sem contato anterior com o tema. Entraram cinco slides de conceito, com a tarja CONCEITO, que definem cada termo antes do primeiro uso: artefato, HTML, API, JSON e MCP. Dois slides de vocabulário fecham o encontro.

Na revisão de 2 nov. 2026 o deck passou de 40 para 42 slides. Novos: 14, o que a segunda rodada mostra (exemplo numérico do registro e Gloaguen et al., 2026, arXiv:2602.11988), e 16, o registro das rodadas e o comando conferir, com saída real do script sobre um registro com uma linha incompleta. Os slides de conceito mantêm a analogia PARA FIXAR, e as comparações de regra vaga e regra testável (slide 13) e de pedido único e cadeia (slide 32) usam o mesmo componente lado a lado do módulo 3.

O ciclo 4.3 concentra quatro desses conceitos e é o mais pesado do encontro em vocabulário novo. A ordem é deliberada: primeiro a API, que é o que existe de fato; depois o JSON, que é o formato em que o dado chega; só então o MCP, que é o embrulho por cima. Quem inverte essa ordem ensina a sigla e não o conceito, e a turma sai achando que MCP é uma fonte de dados.

A analogia do balcão dos fundos, no slide da API, resolve o conceito para a maior parte da turma. A do funcionário novo que ganha acesso a mais um sistema, no slide do MCP, evita a confusão entre dar ferramenta e ficar mais inteligente.

## Ciclo 4.1 — Gerar documentos na pasta do projeto

Conceito, 6 min. O que é um artefato, slide 4. A frase que resume o ciclo está ali: uma tarde de conversa com o modelo pode terminar sem nenhum artefato, e é assim que o trabalho se perde.

Teoria, 12 min. Resposta na tela e arquivo na pasta, slide 5, em dois caminhos. A tabela dos quatro formatos, slide 6, com a coluna sobre o que o histórico mostra. O que é HTML, slide 7, com o arquivo por dentro e a página no navegador, antes da demonstração que gera um arquivo desses.

Demonstração, 7 min. O glossário em HTML, aberto no navegador ali mesmo. Peça para ordenar a tabela por subárea, para mostrar que o arquivo é editado e não recriado. A versão anterior pedia uma coluna com o ano de surgimento de cada conceito, dado sujeito a confabulação, e foi trocada.

Prática, 18 min. Cada aluno gera o glossário da própria área e revisa as doze definições.

Entrega, 5 min. `entregas/glossario.html`.

A instrução da demonstração proíbe o autor de referência de propósito. Explique por quê: é exatamente onde a alucinação apareceria, e o aluno acrescenta depois, conferindo. Três conceitos com autor conferido bastam.

## Ciclo 4.2 — AGENTS.md: configurar o comportamento

Teoria, 15 min. A instrução que vale em toda sessão da pasta, slide 12, com o que segue para o modelo a cada pedido e a situação do formato AGENTS.md em nov. 2026 (Agentic AI Foundation, Linux Foundation). A regra testável, slide 13. O que a segunda rodada mostra, slide 14.

Demonstração, 6 min. O script `iniciar`, slide 15, que guarda a cópia da versão 1 e prepara as três tarefas. O registro e o comando `conferir`, slide 16, que recusa a linha sem o que saiu fora e sem o ajuste.

Prática, 19 min. Duas rodadas de três tarefas, com correção do arquivo entre elas.

Entrega, 5 min. `AGENTS.md`, `entregas/modulo4-registro.csv` e o relatório gerado.

O critério de que uma regra precisa poder ser violada é o conteúdo central do ciclo. Peça em voz alta que alguém leia uma regra sua e pergunte à turma como ela seria violada. Regra que ninguém consegue violar é intenção, não regra.

O script compara o AGENTS.md com a cópia da versão 1 e aponta se o arquivo não mudou. Quem defender que a versão 1 já estava perfeita precisa escrever isso no relatório, com as notas da rodada 1 sustentando o argumento.

Resultado esperado, se a cota acabar: a rodada 1 é a prioridade. Quem não conseguir rodar a segunda completa em casa e registra a indisponibilidade.

## Ciclo 4.3 — Estender o agente: um MCP e as APIs públicas

Conceito, 12 min. O que é uma API, slide 20, com a anatomia da URL do IBGE e a analogia do balcão dos fundos. Depois o JSON, slide 21, lendo em voz alta o par nome e valor do exemplo de São Luís e a mesma linha no CSV do script. Só então as três formas de estender, slide 22, com os arquivos que o opencode lê (AGENTS.md, SKILL.md e o bloco mcp do opencode.json), e o que é um MCP, slide 23, com a analogia do funcionário novo que ganha acesso a mais um sistema.

Teoria, 5 min. O diagrama do slide 24, com os dois caminhos até a BrasilAPI na consulta de CNPJ. Pelo MCP, o modelo escolhe a ferramenta e o argumento, e pelo script a URL fica impressa. O servidor MCP só empacota APIs que já existem, e é isso que o aluno leva para a reunião com fornecedor.

Demonstração da instalação, 12 min. Grave o opencode.json do slide 25, reinicie e confirme que as quinze ferramentas apareceram. Faça a primeira consulta com o número na instrução, CNPJ 06.279.103/0001-19, da UFMA, e peça ao agente o argumento que ele passou à ferramenta. Sem o número, o modelo pode completar um CNPJ por conta própria.

Teoria, 8 min. A tabela das oito fontes do comando apis, slide 26. Todas abrem sem cadastro. Portal da Transparência e DataJud ficam fora da aula porque cada aluno precisaria da própria chave.

Demonstração do que está por baixo, 8 min. Rode `apis testar` e depois `apis cnpj 06279103000119`, slide 27, que mostra as saídas reais obtidas em 2 nov. 2026 numa rede que bloqueou os oito domínios. Escreva a URL no quadro. A ferramenta consultar_cnpj do brasil-data-mcp consulta a mesma BrasilAPI. Em `apis municipios MA` o script chama o IBGE direto, enquanto o MCP usa a BrasilAPI, segundo o README do servidor. O dado tem a mesma origem e a URL é outra.

Teoria, 5 min. As quatro perguntas de decisão, em árvore, slide 28. A pergunta sobre exportar o dado periodicamente vem antes da conexão.

Prática, 20 min. Instalação, diagnóstico, consulta pelas duas vias e ficha de decisão.

Entrega, 5 min. `entregas/modulo4-ciclo3-decisao.md`, `dados/api-diagnostico.md` e os arquivos de resposta.

Três coisas para conduzir bem.

A ordem importa: MCP primeiro, API depois. O aluno vê a mágica, e então descobre que embaixo dela havia um endereço que ele mesmo poderia ter chamado. Invertendo a ordem, a aula vira introdução a protocolo HTTP e perde a turma.

A instalação vai falhar em algumas máquinas. Isso é normal e está previsto: a entrega aceita o registro da falha, e o script funciona sem o MCP. Não pare a turma para resolver caso individual, e não deixe ninguém parado esperando: quem travou segue pelo script.

A pergunta sobre quem responde pelo acesso costuma ser ignorada. Insista: é a que separa um administrador de um entusiasta. Conectar um agente ao sistema da organização é decisão de segurança da informação, e o aluno vai ser o gestor que assina ou não assina essa decisão.

Ressalva sobre o material: os endereços das oito fontes foram tirados da documentação de cada uma. Em 2 nov. 2026, `apis testar` foi rodado no contêiner da revisão e no computador do professor, e as duas redes recusaram os oito domínios no proxy (HTTP 403 no túnel, registrado pelo script como URLError). A documentação conferida na mesma data indica três pontos. O Banco Central limita, desde 26 mar. 2025, a consulta ao SGS a dez anos por chamada, e o script respeita o limite porque começa em 01/01/2026. No PNCP, a modalidade é obrigatória em contratacoes/publicacao e a página vai até 50 registros, como o script envia. O endpoint taxas da BrasilAPI devolve nome e valor sem data de referência. O teste na máquina do laboratório, descrito em Antes da aula, continua sendo o que confirma que as chamadas funcionam.

## Ciclo 4.4 — Tarefas encadeadas e subagentes

Teoria, 15 min. Por que quebrar em etapas. As quatro regras de uma cadeia.

Demonstração, 5 min. As três instruções em sequência sobre o documento do professor.

Prática, 15 min. Cada aluno roda a cadeia no próprio documento.

Entrega, 5 min. `entregas/modulo4-cadeia.md` e o procedimento no caderno.

Exija que os três critérios de aceitação sejam escritos antes de rodar. Quem escrever depois produz critérios que a resposta já cumpre, e o exercício perde o sentido.

Três etapas custam três pedidos. Avise antes: a cadeia se roda uma vez, com o documento certo, e não como teste.

## O que sai deste encontro

Um glossário em HTML, um AGENTS.md testado em duas rodadas, um MCP instalado com a mesma consulta feita também pela API, um diagnóstico do que a rede do laboratório bloqueia, uma ficha de decisão sobre estender ou não a ferramenta, e uma cadeia de três etapas documentada.

## Avisos no fechamento

O encontro 6 fecha a nota 1 com a entrega A2. Liste em voz alta o que ela reúne: mapa de tarefas do módulo 1, diário e par de prompts do módulo 3, AGENTS.md do módulo 4, e o mapa de dados que será feito no próprio encontro 6.

A organização do projeto precisa estar definida. Depois do encontro 6, mudar custa refazer o mapa de dados.

Trazer uma planilha ou base da organização escolhida, com pelo menos vinte linhas e sem dado pessoal identificável. Quem não tiver, traz o endereço de uma base pública.
