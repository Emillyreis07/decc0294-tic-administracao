# Roteiro do módulo 2

Ambiente de trabalho digital. Encontro 3, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

Este é o encontro crítico do semestre. Ao final dele todo aluno precisa sair com opencode desktop instalado, conta criada, pasta do projeto montada e repositório publicado. Quem não sair assim não acompanha os encontros seguintes.

## Antes da aula, obrigatoriamente

Teste de sanidade numa máquina do laboratório, com o técnico presente, cronometrando:

1. Baixar e instalar o opencode desktop. Anote se o antivírus bloqueia e o que foi preciso fazer.
2. Criar conta e autenticar o modelo gratuito. Anote o tempo e o limite de cota informado.
3. Baixar e instalar o GitHub Desktop. Criar conta, adicionar uma pasta, gravar e publicar.
4. Verificar se as máquinas são restauradas a cada uso. Se forem, providenciar imagem com os dois aplicativos ou combinar reinstalação no início da aula.
5. Conferir em opencode.ai/docs/zen a lista de modelos gratuitos e a política de dados de cada um. O slide 26 reproduz a consulta de 02/11/2026 e indica GLM-5.3-Flash Free e DeepSeek V4.1 Flash Free, que declaram retenção zero. Se a lista mudou, ajuste os slides 26 e 28.
6. Verificar se a conexão da conta no OpenCode Zen pede cartão de crédito para liberar os modelos gratuitos. O slide 28 orienta o aluno a parar e chamar o professor se isso acontecer.
7. Fazer dez pedidos seguidos de máquinas diferentes do laboratório. Relatos de outubro de 2026 descrevem bloqueio temporário dos modelos gratuitos quando muitos pedidos saem da mesma rede.
8. No GitHub Desktop, criar o repositório a partir de uma pasta já montada pelo script (File, Add local repository, link create a repository) e confirmar que o Initial commit inclui os arquivos existentes e não sobrescreve o README.

O tempo medido nesse teste decide se o ciclo 2.4 cabe nos 65 minutos previstos. Se passar de 25 minutos por máquina, reduza o ciclo 2.1 e transfira o tempo.

Providencie também: os endereços de download escritos na turma virtual, um monitor circulando pela sala e a instrução de como adicionar o professor como colaborador no repositório.

Os slides não trazem marcadores de tempo. Os tempos por etapa ficam neste roteiro, que é material de preparação e não de consulta durante a aula.

## Material

Deck `slides/modulo2-ambiente-de-trabalho-digital.html`, este roteiro e o arquivo `scripts/atividade_modulo2.py`, publicado na turma virtual antes da aula.

O deck foi refeito em setembro para uma turma sem contato anterior com o tema e revisado em novembro de 2026 (linguagem, esquemas e atualização das ferramentas, com fonte e data de consulta nos slides). Os slides marcados com a tarja CONCEITO definem cada termo antes do primeiro uso: infraestrutura de TI, programa, arquivo e sistema, nuvem, arquivo e caminho, texto puro, modelo de linguagem, agente, AGENTS.md, controle de versão e a diferença entre git, GitHub Desktop, GitHub e repositório. Dois slides de vocabulário fecham o encontro, com vinte termos e a definição de cada um.

Os slides de conceito são para ler em voz alta e discutir, não para passar rápido. A frase grande no topo é a definição; os quatro pontos abaixo são o que a sustenta; a caixa dourada no pé é a analogia, que é o que a turma vai lembrar na semana seguinte. Peça um exemplo da turma em cada analogia antes de avançar.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura, visão geral e combinado | 10 min | 1 a 3 |
| Ciclo 2.1 | 52 min | 4 a 12 |
| Ciclo 2.2 | 50 min | 13 a 21 |
| Intervalo | 15 min | |
| Ciclo 2.3 | 67 min | 22 a 32 |
| Intervalo | 10 min | |
| Ciclo 2.4 | 70 min | 33 a 40 |
| Fechamento e vocabulário | 15 min | 41 a 46 |

O slide 3 é o combinado de abertura: toda palavra técnica é definida antes de ser usada, ninguém precisa saber programar e a pergunta que parece óbvia deve ser feita. Leia os quatro pontos em voz alta. Numa turma que nunca viu o tema, esse minuto reduz a quantidade de gente que fica calada com dúvida.

## Ciclo 2.1 — Infraestrutura de TI: o que roda onde

Conceito, 12 min. O que é infraestrutura de TI, slide 5, com equipamento, programa, rede e dado. Depois a separação entre programa, arquivo e sistema, slide 6, agora em tabela com exemplos (SIGAA, SIAFI, SEI).

Teoria, 15 min. Os três lugares onde um programa roda, slide 7, com diagrama da rede da organização e do data center do fornecedor e tabela de onde fica o dado, quem mantém e o que acontece sem internet. O slide 8 define computação em nuvem com base em Mell e Grance (NIST SP 800-145, 2011) e é o mais importante do ciclo: a turma chega achando que nuvem é uma abstração e sai sabendo que é o data center de uma empresa com contrato. O slide 9 traz o custo total de propriedade com exemplo numérico ilustrativo (protocolo eletrônico de uma prefeitura, R$ 500 mil em cinco anos, dos quais R$ 150 mil, 30%, aparecem na proposta comercial).

Demonstração, 5 min. A própria ferramenta da disciplina submetida à pergunta, slide 10: o programa roda na máquina, o conteúdo lido pelo agente vai ao servidor do provedor nos EUA ou na União Europeia, e o envio de dado pessoal ao exterior é transferência internacional (LGPD, art. 33, e Resolução CD/ANPD nº 19/2024).

Prática, 15 min. Cada aluno escolhe um sistema que usa e responde às três perguntas.

Entrega, 5 min. Ficha de infraestrutura, salva depois que a pasta existir.

Este ciclo é o mais compressível do encontro. Se o teste de sanidade indicou instalação demorada, corte o slide 9, o do custo total, que é o único que não é pré-requisito de nada adiante. Os slides de conceito não se cortam: sem eles, o ciclo 2.3 não se sustenta.

## Ciclo 2.2 — A pasta do projeto

Conceito, 10 min. Arquivo, pasta e caminho, slide 14. É o slide mais elementar do encontro e o mais decisivo: sem ele, nenhuma instrução ao agente funciona, porque o aluno não sabe citar um arquivo. Escreva um caminho no quadro, dados/vendas-2025.csv, e peça que alguém leia em voz alta o que ele significa.

Teoria, 15 min. Conversa, pasta e repositório, slide 15, em tabela com a definição de reprodutibilidade. A estrutura padrão, slide 16, em árvore: quatro pastas (dados, prompts, saidas, entregas), README.md, AGENTS.md e .gitignore, mais os arquivos LEIA-ME.md e .manter que o comando criar grava dentro das pastas. O deck anterior falava em cinco pastas, e o script cria quatro. Texto puro e arquivo fechado, slide 17, com o mesmo conteúdo visto no Bloco de Notas em .md e em .docx. Os formatos, slide 18, em tabela, com a nota sobre o separador do CSV no Excel em português.

Demonstração, 8 min. O professor executa `atividade_modulo2.py criar` na projeção. O slide 19 mostra a saída real do comando numa pasta vazia.

Ponto a decidir: a prática do slide 20 pede que cada aluno rode o comando criar, mas o opencode só é instalado no ciclo 2.3. O slide orienta quem ainda não tiver o opencode a rodar o comando logo após a instalação. Se o laboratório tiver Python, a alternativa é executar o script com duplo clique.

Prática, 12 min. Cada aluno cria a pasta, roda o script e preenche o README.

Entrega, 5 min. Estrutura criada e README preenchido.

Ponto de atenção: nome de pasta com espaço e acento causa problema o semestre inteiro. Insista no padrão minúsculas com hífen no momento em que a turma criar a pasta.

## Ciclo 2.3 — opencode desktop: instalação e primeiro uso

Conceito, 12 min. O que é um modelo de linguagem, slide 23, na versão curta: ele prevê a continuação provável do texto e não consulta uma base de verdades. Depois, o que é um agente, slide 24, com a diferença entre ser o carregador de informação e ser o revisor.

A analogia do estagiário, no slide 23, costuma resolver o conceito para a turma inteira. Não a substitua por uma explicação técnica. O slide usa o termo confabulação, com alucinação entre parênteses, como os módulos 5 e 6.

Teoria, 8 min. O que o opencode faz, slide 25, em fluxo (lê, grava, executa, você confere) com os modos build e plan. Os modelos gratuitos do OpenCode Zen e a política de dados de cada um, slide 26, com a cota e o que fazer quando o modelo parar (consulta de 02/11/2026).

Demonstração e instalação assistida, 22 min. O esquema da tela do opencode desktop, slide 27, e os seis passos do slide 28, com toda a turma acompanhando na própria máquina. Monitor circulando. Ninguém avança sozinho.

Demonstração da primeira instrução, 5 min. O pedido do slide 29, que lê um arquivo da pasta e grava outro.

Conceito do AGENTS.md, slide 30, com as quatro seções na mesma ordem e com os mesmos títulos que o script procura. Leia a instrução em voz alta apontando as três partes: o arquivo citado pelo caminho, o formato pedido e a proibição no fim.

Prática, 15 min. Cada aluno preenche o AGENTS.md e testa com três pedidos, slide 31, com exemplo ilustrativo preenchido. O script considera curta demais a seção com menos de 25 caracteres fora do comentário entre parênteses e só reconhece os títulos numerados originais. No mesmo momento, o aluno preenche no README a ferramenta e o modelo usados, o quarto PREENCHER do arquivo.

Entrega, 5 min. AGENTS.md preenchido e três testes salvos em `prompts/`.

Resultado esperado, se a cota do modelo falhar em parte da turma: os alunos afetados escrevem o AGENTS.md mesmo assim e fazem os três testes na aula seguinte. Registram a indisponibilidade na entrega. A instalação e a autenticação são o que não pode ficar pendente.

## Ciclo 2.4 — GitHub Desktop e a entrega A1

Conceito, 10 min. O que é versionar, slide 34, começando pela pilha de relatorio-final-v3 que todo mundo tem. Depois o slide 35, em tabela, com git, GitHub Desktop, GitHub e repositório, que é onde a turma se perde na primeira semana: um é o programa, outro é a tela com botões, outro é o site e o último é a sua pasta com histórico.

Teoria, 10 min. Os quatro gestos, slide 36, em diagrama (pasta de trabalho, histórico local, GitHub) com os nomes em inglês porque é assim que estão nos botões. O antigo slide dos três problemas que o versionamento resolve foi incorporado aos slides 15 e 34. O que nunca vai para o repositório, slide 38, em tabela com os padrões do .gitignore que o script grava e o limite de 100 MB por arquivo do GitHub.

Demonstração e execução assistida, 30 min. Os seis passos do slide 37, com a turma acompanhando. Este é o trecho em que o encontro trava ou não trava. Ao criar o repositório a partir da pasta, o GitHub Desktop grava sozinho a versão Initial commit. Insista em deixar desmarcado Initialize this repository with a README e Git ignore em None, porque o script já criou esses arquivos.

Conferência, 15 min. Cada aluno roda `atividade_modulo2.py conferir` e corrige o que o script apontar, slide 39. O script verifica nove itens e escreve `entregas/A1-relatorio.md`. Logo após o Initial commit e a publicação, a saída mostra 8 de 9, porque o item de duas versões gravadas exige um segundo commit. Cada execução reescreve o relatório, e por isso nome e matrícula são preenchidos depois da última execução, antes do commit com a mensagem entrega A1.

Entrega, 5 min. Endereço do repositório enviado na turma virtual, ainda em sala.

Ordem de resolução quando alguém trava: primeiro o que impede publicar, depois o preenchimento de arquivos. Um aluno com AGENTS.md incompleto resolve em casa. Um aluno sem conta no GitHub não resolve.

## Os nove itens que o script confere

Estrutura de pastas, README preenchido, AGENTS.md com as quatro seções, as quatro entregas do módulo 1 na pasta certa, ficha do ciclo 2.1, .gitignore presente, pasta sob controle de versão, ao menos duas versões gravadas e repositório publicado.

O script lê o estado do repositório direto dos arquivos internos do git, sem depender de comando. Funciona mesmo sem git instalado no caminho do sistema. A contagem de versões vem do registro local (.git/logs/HEAD). Num repositório clonado em outra máquina, esse registro começa vazio e o item de duas versões aparece como pendente, mesmo com o histórico completo no GitHub.

## O vocabulário do fim

Os slides 42 e 43 trazem os vinte termos do encontro com uma linha de definição em cada. Não são para explicar de novo: são para o aluno fotografar e consultar durante o semestre. Reserve dois minutos, diga isso com essas palavras e siga.

Se algum termo gerar dúvida ali, é sinal de que o slide de conceito correspondente passou rápido demais. Anote qual foi e ajuste o ritmo no próximo semestre.

## Problemas conhecidos

Antivírus bloqueia o instalador. Não autorizar por conta própria: chamar o professor, que resolve com o técnico.

E-mail de confirmação não chega. Verificar spam, esperar cinco minutos, trocar de endereço e seguir.

Agente diz que não encontra o arquivo. Quase sempre a pasta aberta não é a do projeto.

GitHub Desktop não deixa publicar. Faltou autenticar, ou não há nenhuma versão gravada ainda.

Cota do modelo esgotada. Trocar para o outro modelo indicado no slide 26. Se persistir, registrar na entrega e seguir com o roteiro.

GitHub pede verificação em duas etapas. A exigência vale para contas selecionadas por atividade de contribuição, com 45 dias para ativar (docs.github.com, consulta em 02/11/2026). Orientar o uso de aplicativo autenticador e a guarda dos códigos de recuperação fora do repositório.

O slide 44 reúne estes problemas em tabela, com causa provável e providência.

## Depois da aula

Confira os repositórios recebidos antes do encontro 4 e identifique quem ficou pendente. Quem não publicou precisa resolver na semana, com atendimento fora de aula. Não deixe passar para o encontro 5: o módulo 3 já grava trabalho na pasta.
