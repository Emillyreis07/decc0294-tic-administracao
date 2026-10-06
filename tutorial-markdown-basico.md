# Tutorial Básico de Markdown — DECC0294

> Guia rápido para alunos de Administração. Leia em 15 minutos e pratique junto.
> Este próprio arquivo é um exemplo: tudo que você vê aqui foi feito só com Markdown.

## 1. O que é e para que serve aqui

Markdown é um jeito simples de formatar texto usando só caracteres do teclado.

Na disciplina você vai usá-lo em:

- `entregas/*.md` — mapas, relatórios e painéis gerados pelos scripts
- `prompts/` — caderno de prompts
- GitHub — README e visualização das entregas

Você escreve texto puro e o GitHub, o VS Code ou o navegador transformam em documento formatado.

## 2. Como visualizar

1. **VS Code:** abra o `.md` e aperte `Ctrl + Shift + V` para pré-visualizar lado a lado.
2. **GitHub:** basta abrir o arquivo no repositório, ele já renderiza.
3. **Navegador:** arraste o `.md` para sites como `stackedit.io` se precisar.

Não precisa instalar nada.

## 3. Sintaxe essencial

### 3.1 Títulos

```markdown
# Título 1 — nome do trabalho
## Seção 2 — ex: Ordem de ataque
### Subseção 3 — ex: Tarefa detalhada
```

Use um único `#` por arquivo. O resto organiza com `##` e `###`.

### 3.2 Parágrafos, quebras e linhas

Um parágrafo é só texto. Deixe **uma linha em branco** entre parágrafos.

Para linha horizontal de separação:
```markdown
---
```

### 3.3 Ênfase

```markdown
**negrito** para resultado importante
*itálico* para termo estrangeiro, ex: *backlog*
`código ou nome de arquivo`, ex: `atividade_modulo1.py`
```

Resultado: **negrito**, *itálico*, `código`.

### 3.4 Listas

Não ordenada — para itens sem ordem:

```markdown
- Consolidar planilhas de frequência
- Conferir notas fiscais do mês
- Responder fornecedores no e-mail
```

Ordenada — para passo a passo:

```markdown
1. Execute `python atividade_modulo1.py iniciar`
2. Preencha o CSV no Excel
3. Execute `python atividade_modulo1.py conferir`
```

Lista de tarefas (checklist):

```markdown
- [x] Levantar 10 tarefas do setor
- [ ] Estimar esforço 1 a 5
- [ ] Declarar base da estimativa
```

Resultado:

- [x] Levantar 10 tarefas do setor
- [ ] Estimar esforço 1 a 5
- [ ] Declarar base da estimativa

### 3.5 Citação e alerta

```markdown
> Escreva aqui, em uma frase, o que você faria na segunda-feira.
```

Resultado:

> Escreva aqui, em uma frase, o que você faria na segunda-feira.

### 3.6 Links e imagens

```markdown
[Página da disciplina](https://tadeugomes.github.io/decc0294-tic-administracao/)
![Logotipo da UFMA](logo-ufma.png)
```

O primeiro vira link clicável. O segundo exibe imagem (o arquivo precisa estar na mesma pasta).

### 3.7 Tabelas

Tabelas são muito usadas nos mapas dos módulos 1 e 6:

```markdown
| # | Tarefa | Esforço | Ganho (h/mês) | Risco |
|---|---|---|---|---|
| 1 | Consolidar planilhas de frequência | 2 | 6 | 2 |
| 2 | Conferir notas fiscais do mês | 3 | 4 | 4 |
```

Resultado:

| # | Tarefa | Esforço | Ganho (h/mês) | Risco |
|---|---|---|---|---|
| 1 | Consolidar planilhas de frequência | 2 | 6 | 2 |
| 2 | Conferir notas fiscais do mês | 3 | 4 | 4 |

Dica: alinhe com `|:---|` à esquerda, `|:---:|` centro, `|---:|` à direita.

### 3.8 Código

Uma linha: `python atividade_modulo6.py perfil`

Bloco com linguagem para colorir:

````markdown
```python
total_ganho = sum(t["ganho"] for t in tarefas[:3])
print(total_ganho)
```
````

## 4. Exemplo completo aplicado à Administração

Abaixo, um mini-relatório como os que você entrega:

---

# Mapa de tarefas automatizáveis — Exemplo

Módulo 1, ciclo 1.4. Aluna: Maria Silva, Mat. 2026001234.

## 1. Ordem de ataque

Tarefas ordenadas por **ganho / esforço**, excluídas as de risco alto.

| # | Tarefa | Destino | Esforço | Ganho (h/mês) |
|---|---|---|---|---|
| 1 | Consolidar planilhas de frequência das 4 unidades | automatizar | 2 | 6 |
| 2 | Gerar recibos mensais de estágio | automatizar | 1 | 3 |

As três primeiras somam **9 horas por mês** de ganho estimado.

## 2. Primeira ação

> Na segunda-feira, vou padronizar a planilha de frequência em um único modelo antes de automatizar.

## 3. Declaração de uso de IA

Ferramenta e modelo usados: Opencode + Muse Spark.
As classificações foram revisadas por mim e as divergências estão anotadas.

---

## 5. Erros comuns (e como evitar)

1. **Esquecer a linha em branco** antes de lista ou título — o texto gruda.
2. **Número sem base declarada não conta** — sempre explique: *leva 1h30 por unidade*.
3. **Tabela quebrada** — toda linha precisa do mesmo número de `|`.
4. **Acentos no nome do arquivo** — prefira `modulo1-mapa.md`, sem espaço nem ç.
5. **Apagar o exemplo sem substituir** — o script `conferir` reclama de arquivo vazio.

## 6. Mini-exercício de 5 minutos

1. Crie um arquivo `meu-teste.md` na pasta `saidas/`.
2. Copie o modelo abaixo, preencha e pré-visualize com `Ctrl + Shift + V`:

```markdown
# Meu primeiro Markdown
Nome: ______________________________

## Minhas 3 tarefas de hoje
- [ ] Tarefa 1: __________
- [ ] Tarefa 2: __________
- [ ] Tarefa 3: __________

## Prioridade
| Tarefa | Esforço 1-5 | Ganho h/mês |
|---|---|---|
| __________ |  |  |

> Minha primeira ação na segunda-feira: __________
```

3. Apague `saidas/meu-teste.md` depois do teste, para não poluir a entrega.

## 7. Para ir além

- Guia oficial: <https://www.markdownguide.org/basic-syntax/>
- Na disciplina: abra qualquer `entregas/modulo1-mapa-de-tarefas.md` gerado pelo script e compare o `.csv` com o `.md` — é a mesma informação, em dois formatos.

*Arquivo criado como exemplo para a turma DECC0294 2026.2 — UFMA Administração. Licença CC BY 4.0.*
