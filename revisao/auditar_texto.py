# -*- coding: utf-8 -*-
"""Auditoria de linguagem dos decks HTML da DECC0294.

Conta, por deck e por slide, os sinais de texto com cara de modelo de
linguagem definidos em revisao/GUIA-DE-REVISAO.md. Só usa a biblioteca padrão.

Uso, a partir da pasta material-2026-2:
    python revisao/auditar_texto.py              resumo de todos os decks
    python revisao/auditar_texto.py 6            detalhe do módulo 6, slide a slide
    python revisao/auditar_texto.py 6 --desde 6  detalhe a partir do slide 6

A contagem é um indicador para priorizar a revisão. Ela não substitui a
leitura: frase de efeito sem palavra proibida passa pelo filtro.
"""
import glob
import html
import os
import re
import sys

PASTA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PALAVRAS = [
    "abrangente", "crucial", "dinâmico", "disruptiv", "eficaz", "eficiente",
    "essencial", "estratégic", "fundamental", "inovador", "poderos", "robust",
    "significativ", "valios", "vital", "transformador", "revolucion", "impressionante",
    "destacar", "ressaltar", "enfatizar", "potencializ", "fomentar", "alavanc",
    "cenário", "panorama", "insight", "sinergia", "jornada", "mergulh",
    "além disso", "adicionalmente", "notavelmente", "portanto", "contudo",
    "frequentemente", "consequentemente", "sem dúvida", "na verdade",
    "é importante", "vale destacar", "vale lembrar", "lembre-se",
    "mudou o jogo", "virou o jogo", "o segredo",
]

PADROES = [
    (r"—|–", "travessão"),
    (r";", "ponto e vírgula"),
    (r"\bnão é [^.]{1,60}, é\b", "paralelismo 'não é X, é Y'"),
    (r"\bnão [^.]{1,50}, e sim\b", "paralelismo 'não X, e sim Y'"),
    (r"\bnão apenas\b|\bmas também\b", "'não apenas... mas também'"),
    (r"\bvale mais (que|do que)\b", "frase de efeito 'vale mais que'"),
    (r"\bé o (achado|produto|ponto|segredo)\b", "aforismo 'é o achado/produto'"),
    (r"\\n", "\\n literal no texto"),
]


def slides_do_deck(caminho):
    s = open(caminho, encoding="utf-8").read()
    pos = [m.start() for m in re.finditer(r'<section class="slide ', s)]
    fim = s.find('<div id="barra">')
    pos.append(fim if fim > 0 else len(s))
    out = []
    for a, b in zip(pos, pos[1:]):
        t = s[a:b]
        t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S)
        t = re.sub(r"<[^>]+>", " ", t)
        t = html.unescape(re.sub(r"\s+", " ", t))
        out.append(t)
    return out


def sinais(texto):
    achados = []
    baixo = texto.lower()
    for p in PALAVRAS:
        n = baixo.count(p)
        if n:
            achados.append((p, n))
    for rx, nome in PADROES:
        n = len(re.findall(rx, texto, flags=re.I))
        if n:
            achados.append((nome, n))
    return achados


def numero(caminho):
    m = re.search(r"modulo(\d+)-", os.path.basename(caminho))
    return int(m.group(1)) if m else 0


def main():
    args = sys.argv[1:]
    decks = sorted(glob.glob(os.path.join(PASTA, "slides", "modulo*-*.html")), key=numero)
    if not args:
        print("%-48s %7s %8s" % ("deck", "slides", "sinais"))
        for d in decks:
            sl = slides_do_deck(d)
            total = sum(n for t in sl for _, n in sinais(t))
            print("%-48s %7d %8d" % (os.path.basename(d), len(sl), total))
        return
    alvo = int(args[0])
    desde = int(args[args.index("--desde") + 1]) if "--desde" in args else 1
    d = [x for x in decks if numero(x) == alvo][0]
    print(os.path.basename(d))
    for k, t in enumerate(slides_do_deck(d), 1):
        if k < desde:
            continue
        a = sinais(t)
        if a:
            print("  slide %2d: %s" % (k, ", ".join("%s (%d)" % x for x in a)))


if __name__ == "__main__":
    main()
