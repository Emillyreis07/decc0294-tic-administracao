// Conferência visual dos decks HTML da DECC0294.
//
// Abre o deck no Chromium, grava uma imagem por slide e lista os elementos
// que ultrapassam a área útil (.corpo) ou a margem direita do slide.
//
// Requisito: Node e Playwright com Chromium
//   npm install playwright && npx playwright install chromium
//
// Uso, a partir da pasta material-2026-2:
//   node revisao/conferir_slides.js slides/modulo5-dados-na-administracao.html
//   node revisao/conferir_slides.js slides/modulo5-dados-na-administracao.html saidas/imagens "Liberation Sans"
//
// O terceiro argumento força uma fonte. Sem ele, vale a fonte do sistema
// (Segoe UI no Windows do laboratório). Testar também com uma fonte mais
// larga, como "DejaVu Sans", dá margem de segurança.
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

(async () => {
  const deck = path.resolve(process.argv[2]);
  const pasta = process.argv[3] || 'saidas/conferencia-slides';
  const fonte = process.argv[4] || '';
  fs.mkdirSync(pasta, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  await p.goto('file://' + deck);
  await p.addStyleTag({ content: '#barra,#ajuda{display:none!important}' });
  if (fonte) await p.addStyleTag({ content: `html,body,.fig text{font-family:"${fonte}",sans-serif!important}` });
  const n = await p.$$eval('.slide', s => s.length);
  const relatorio = [];
  for (let i = 0; i < n; i++) {
    await p.evaluate(i => { location.hash = i + 1; }, i);
    await p.waitForTimeout(80);
    const r = await p.evaluate(i => {
      const s = document.querySelectorAll('.slide')[i];
      s.style.transform = 'none';
      const sb = s.getBoundingClientRect();
      const corpo = s.querySelector('.corpo');
      const lim = corpo ? corpo.getBoundingClientRect().bottom : sb.bottom;
      const out = [];
      s.querySelectorAll('.corpo *').forEach(e => {
        if (e.closest('svg') && e.tagName !== 'svg') return;
        if (e.classList.contains('fonte-nota')) return;
        const b = e.getBoundingClientRect();
        if (b.height === 0) return;
        if (b.bottom > lim + 4) out.push(`${e.tagName}.${e.className} passa ${Math.round(b.bottom - lim)}px abaixo do corpo`);
        if (b.right > sb.right - 40) out.push(`${e.tagName}.${e.className} passa da margem direita`);
      });
      const sub = s.querySelector('.conteudo .sub');
      if (sub && sub.getBoundingClientRect().height > 30) out.push('subtítulo em duas linhas');
      const h2 = s.querySelector('.conteudo h2');
      if (h2 && h2.getBoundingClientRect().height > 50) out.push('título em duas linhas');
      return [...new Set(out)].slice(0, 5);
    }, i);
    if (r.length) relatorio.push(`slide ${i + 1}: ${r.join(' | ')}`);
    await p.screenshot({ path: path.join(pasta, `slide${String(i + 1).padStart(2, '0')}.png`) });
  }
  console.log(relatorio.join('\n') || 'Nenhum estouro encontrado.');
  console.log(`${n} imagens em ${pasta}`);
  await b.close();
})();
