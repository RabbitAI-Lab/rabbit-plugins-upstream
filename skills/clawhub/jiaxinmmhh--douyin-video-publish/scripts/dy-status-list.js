// 抖音内容管理：按审核状态筛选（待发布）并抓列表
const puppeteer = require('puppeteer-core');
const CDP = 'http://127.0.0.1:9222';
const sleep = ms => new Promise(r => setTimeout(r, ms));
const STATUS = process.argv[2] || '待发布';

(async () => {
  const browser = await puppeteer.connect({ browserURL: CDP, defaultViewport: { width: 1440, height: 900 }, protocolTimeout: 300000 });
  const all = await browser.pages();
  const page = all.filter(p => p.url().includes('creator.douyin.com/creator-micro/content/manage')).pop() || await browser.newPage();
  if (!page.url().includes('/content/manage')) {
    try { await page.goto('https://creator.douyin.com/creator-micro/content/manage', { waitUntil: 'domcontentloaded', timeout: 60000 }); } catch (e) {}
    await sleep(8000);
  }
  await page.bringToFront();
  await sleep(2500);

  // 点「审核状态」按钮（抖音自研组件，文本可能带图标）
  const btn = await page.evaluate(() => {
    const cands = Array.from(document.querySelectorAll('*')).filter(e => {
      const t = (e.innerText || '').trim();
      return t.startsWith('审核状态') && t.length < 20 && e.offsetParent !== null && e.children.length <= 3;
    });
    if (!cands.length) return null;
    cands.sort((a, b) => a.getBoundingClientRect().width - b.getBoundingClientRect().width);
    const b = cands[0];
    const r = b.getBoundingClientRect();
    return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2), t: b.innerText.trim(), tag: b.tagName, w: Math.round(r.width) };
  });
  console.log('审核状态按钮:', JSON.stringify(btn));
  if (!btn) { await browser.disconnect(); return; }
  await page.mouse.click(btn.x, btn.y);
  await sleep(2500);

  const opts = await page.evaluate(() => {
    const res = [];
    document.querySelectorAll('[class*="select-option"]').forEach(e => {
      if (e.offsetParent === null) return;
      const t = (e.innerText || '').trim();
      if (!t || t.length > 6) return;
      const r = e.getBoundingClientRect();
      if (r.width < 5 || r.height < 10 || r.height > 60) return;
      res.push({ t, cls: String(e.className).slice(0, 70), x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) });
    });
    return res;
  });
  console.log('筛选选项:', JSON.stringify(opts.map(o => `${o.t}@${o.y}`)));
  const pick = opts.find(o => o.t === STATUS);
  if (!pick) { console.log('未找到选项', STATUS); await browser.disconnect(); return; }
  await page.mouse.click(pick.x, pick.y);
  await sleep(5000);

  // 抓列表
  for (let i = 0; i < 6; i++) { await page.evaluate(() => window.scrollBy(0, 900)); await sleep(1300); }
  const items = await page.evaluate(() => {
    const lines = document.body.innerText.split('\n').map(s => s.trim()).filter(Boolean);
    const out = [];
    for (let i = 0; i < lines.length; i++) {
      const m = lines[i].match(/^(\d{4})年(\d{2})月(\d{2})日\s+(\d{2}:\d{2})/);
      if (m) out.push({ time: `${m[1]}-${m[2]}-${m[3]} ${m[4]}`, title: (lines[i - 1] || '').slice(0, 60), status: (lines[i].match(/待发布|审核中|已发布|未通过/) || [''])[0] });
    }
    return out;
  });
  console.log(`=== ${STATUS}: ${items.length} 条 ===`);
  items.forEach((o, i) => console.log(`${i + 1}. [${o.time}] ${o.status} | ${o.title}`));
  await page.screenshot({ path: `/Users/jx/Downloads/.workbuddy/macros/dy-status-${STATUS}.png` });
  await browser.disconnect();
})().catch(e => { console.error('ERR', e.stack || e.message); process.exit(1); });
