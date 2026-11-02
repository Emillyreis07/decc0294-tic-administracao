# Roteiro do módulo 7

Dados estruturados e consulta. Encontro 8, cerca de 4 horas.
DECC0294, UFMA, Curso de Administração, 2026.2.

## Antes da aula

Material do professor: `slides/modulo7-dados-estruturados-e-consulta.html`, este roteiro e `scripts/atividade_modulo7.py`.

Publicado na turma virtual: o script e o lembrete de que as duas bases precisam estar em `dados/` e as cinco perguntas escritas.

Rode o script sobre a base de reserva antes da aula: crie o banco, faça uma consulta e uma junção. Você vai precisar conhecer a saída, e a demonstração do ciclo 7.4 depende de uma junção que dê certo na projeção.

Prepare também uma segunda tabela de referência com uma chave repetida, para demonstrar a junção que multiplica linhas. É a demonstração mais valiosa do encontro e não acontece sozinha se as bases estiverem bem formadas.

## Distribuição do tempo

| Bloco | Duração | Slides |
|---|---|---|
| Abertura e visão geral | 10 min | 1 a 2 |
| Ciclo 7.1 | 45 min | 3 a 9 |
| Ciclo 7.2 | 50 min | 10 a 15 |
| Intervalo | 15 min | |
| Ciclo 7.3 | 60 min | 16 a 22 |
| Intervalo | 10 min | |
| Ciclo 7.4 | 45 min | 23 a 27 |
| Fechamento | 15 min | 28 a 31 |

## Ciclo 7.1 — Da planilha à tabela

Teoria, 18 min. Planilha, tabela e banco relacional (Codd, 1970). Os quatro problemas que a planilha não resolve, com o termo técnico de cada um. Tipo declarado e valor gravado (slide 6): no SQLite o tipo da coluna é uma preferência (afinidade de tipo), e o script cria a coluna como número quando 90% ou mais dos valores preenchidos são números, grava vazio no lugar dos demais e não conta a linha como rejeitada. O mesmo slide mostra o valor 1.234 lido como 1,234 e o CNPJ que perde os zeros à esquerda.

Demonstração, 7 min. O script criando o banco na projeção, com as contagens e a conferência de COUNT(coluna) contra os vazios do perfil.

Prática, 15 min. Cada aluno cria o banco com as próprias bases.

Entrega, 5 min. `entregas/modulo7-ciclo1-banco.md`.

O slide dos quatro problemas costuma gerar reconhecimento imediato em quem trabalha. O PROCV como tecnologia crítica da organização é a frase que a turma repete depois.

A conferência de contagem contra o perfil do encontro 7 é obrigatória. Diferença sem explicação invalida tudo que vier no resto do encontro, e é melhor descobrir agora.

Coluna de valor que o script tipou como TEXT é vírgula decimal de novo. Corrigir o CSV e recriar o banco leva dois minutos; consultar um banco mal tipado custa o encontro inteiro.

## Ciclo 7.2 — Modelo relacional em linguagem de gestor

Teoria, 25 min. Entidade, atributo e relação, com o diagrama das tabelas usadas nas demonstrações (Chen, 1976). Chave primária e chave estrangeira, o agrupamento pelo nome que divide São Luís em quatro grupos e o CNPJ alfanumérico, emitido desde julho de 2026 (IN RFB nº 2.229/2024). Os três tipos de relação e o efeito de cada um na contagem da junção.

Prática, 20 min. Cada aluno modela as próprias tabelas e gera o diagrama.

Entrega, 5 min. `entregas/modulo7-ciclo2-modelo.md`.

Este ciclo não tem demonstração de propósito: a competência é escrever a relação nos dois sentidos, e isso se faz com caneta antes de se fazer com ferramenta.

Retome o cruzamento que falhou no encontro 6. A causa era chave de texto, e o slide da chave explica por quê. A ligação entre os dois encontros é o que fixa o conteúdo.

Aluno cujas bases não têm chave comum tem o principal achado do ciclo, e não um problema. A solução, criar a correspondência à mão numa terceira tabela, é o que se faz na organização real.

## Ciclo 7.3 — Perguntas de negócio viram consultas

Teoria, 25 min. As cinco partes de uma consulta e a ordem em que o banco as executa. Os três erros que produzem número errado plausível e o conceito de granularidade (Kimball e Ross, 2013). O acerto dos modelos ao escrever SQL no teste BIRD (slide 19): 80,04% para o melhor modelo único em junho de 2026, contra 92,96% de especialistas humanos. Uma consulta em cinco ainda sai errada e roda sem mensagem de erro.

Demonstração, 10 min. A sequência completa: esquema, pedido ao agente, leitura da consulta, execução. O script mostra só as linhas do resultado, então a contagem antes e depois do filtro sai de duas consultas COUNT(*), sem e com o WHERE.

Prática, 20 min. Cinco perguntas viradas em consultas.

Entrega, 5 min. `entregas/modulo7-consultas.csv`.

Insista na leitura da consulta antes de executar. O aluno que não entende o filtro não pode aceitar o número, e a leitura das cinco partes é ensinável em dez minutos.

O script bloqueia comandos que não sejam de leitura. Isso evita que uma instrução mal formulada apague a tabela no meio da aula.

O script recusa entrega sem a contagem antes e depois do filtro. É onde o número errado se esconde, e é a conferência que o encontro passado já ensinou.

## Ciclo 7.4 — Juntar fontes sem inventar linha

Teoria, 12 min. As três formas de juntar e a contagem esperada de cada uma. A diferença entre a junção interna, que é a do comando juntar, e a junção à esquerda, que o aluno pode pedir pelo comando sql.

Demonstração, 8 min. A junção com a tabela de chave repetida que você preparou. A contagem cresce na tela, e é isso que fica.

Prática, 20 min. Cada aluno junta as próprias tabelas e explica as linhas sem par.

Entrega, 5 min. `entregas/modulo7-ciclo4-juncao.md`.

A regra é simples e vale para o resto da vida profissional: se a junção aumentou a contagem, a chave não era única e qualquer soma sobre o resultado está inflada. O script informa quantas chaves se repetem, o que encurta a investigação.

## O que sai deste encontro

Um banco com as duas bases tipadas, o modelo com chaves e relações, cinco consultas com SQL gravado e contagem conferida, e a junção validada. Tudo compõe a entrega B1 do encontro 9.

## Avisos no fechamento

Escolher três dos cinco indicadores para o painel, e anotar a razão da escolha.

Trazer um gráfico ruim de relatório, jornal ou apresentação, para ser reconstruído em sala.

A entrega B1 reúne os encontros 7, 8 e 9. Quem está atrasado precisa acertar esta semana, porque o painel se constrói sobre estas consultas.
