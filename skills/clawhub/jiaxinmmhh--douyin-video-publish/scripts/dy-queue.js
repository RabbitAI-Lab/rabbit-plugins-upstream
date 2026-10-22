// 抖音：按审核状态筛选 + 卡片式滚动累积抓取（对账用）
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const CDP = 'http://127.0.0.1:9222';
const sleep = ms => new Promise(r => setTimeout(r, ms));
const STATUS = process.argv[2] || '审核中';
const OUT = `/Users/jx/Downloads/.workbuddy/macros/dy-list-${STATUS}.json`;

(async () => {
  const browser = await puppeteer.connect({ browserURL: CDP, defaultViewport: { width: 1440, height: 900 }, protocolTimeout: 300000 });
  const page = await browser.newPage();
  try { await page.goto('https://creator.douyin.com/creator-micro/content/manage', { waitUntil: 'domcontentloaded', timeout: 60000 }); } catch (e) {}
  await sleep(9000);
  await page.bringToFront();

  // 切筛选
  const btn = await page.evaluate(() => {
    const c = Array.from(document.querySelectorAll('*')).filter(e => {
      const t = (e.innerText || '').trim();
      return t.startsWith('审核状态') && t.length < 20 && e.offsetParent !== null && e.children.length <= 3;
    });
    if (!c.length) return null;
    c.sort((a, b) => a.getBoundingClientRect().width - b.getBoundingClientRect().width);
    const r = c[0].getBoundingClientRect();
    return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
  });
  if (!btn) throw new Error('无审核状态按钮');
  await page.mouse.click(btn.x, btn.y);
  await sleep(2500);
  const opt = await page.evaluate((s) => {
    const o = Array.from(document.querySelectorAll('[class*="select-option"]')).find(e => e.offsetParent !== null && (e.innerText || '').trim() === s);
    if (!o) return null;
    const r = o.getBoundingClientRect();
    return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
  }, STATUS);
  if (!opt) throw new Error('无选项 ' + STATUS);
  await page.mouse.click(opt.x, opt.y);
  await sleep(5000);

  // 卡片式抓取 + 滚动累积
  const seen = new Map();
  const grab = async () => {
    const batch = await page.evaluate(() => {
      const cards = [];
      document.querySelectorAll('*').forEach(el => {
        if (el.children.length < 3 || el.children.length > 60) return;
        const t = el.innerText || '';
        if (!t.includes('删除作品') || !/\d{4}年\d{2}月\d{2}日/.test(t)) return;
        cards.push(el);
      });
      const uniq = cards.filter(el => !cards.some(o => o !== el && el.contains(o)));
      return uniq.map(el => {
        const m = (el.innerText.match(/(\d{4})年(\d{2})月(\d{2})日\s+(\d{2}:\d{2})/) || []).slice(1);
        const lines = el.innerText.split('\n').map(s => s.trim()).filter(Boolean);
        return { dt: m.join('-'), lines: lines.slice(0, 4), status: (el.innerText.match(/待发布|审核中|已发布|未通过/) || ['?'])[0] };
      });
    });
    for (const b of batch) if (b.dt && !seen.has(b.dt)) seen.set(b.dt, b);
    return batch.length;
  };

  await grab();
  for (let i = 0; i < 25; i++) {
    const before = seen.size;
    await page.evaluate(() => {
      window.scrollBy(0, 700);
      let best = null;
      document.querySelectorAll('div').forEach(c => { if (c.scrollHeight > c.clientHeight + 50 && c.clientHeight > 300) best = c; });
      if (best) best.scrollTop = best.scrollTop + 700;
    });
    await sleep(1400);
    await grab();
    if (i % 5 === 4) console.log(`  已抓 ${seen.size} 条`);
    if (seen.size === before && i > 10) break;
  }

  const list = [...seen.values()].sort((a, b) => a.dt.localeCompare(b.dt));
  fs.writeFileSync(OUT, JSON.stringify(list, null, 1));
  console.log(`=== ${STATUS}: ${list.length} 条 ===`);
  list.forEach((o, i) => console.log(`${String(i + 1).padStart(2)}. [${o.dt}] ${o.status} | ${(o.lines[0] || '').slice(0, 60)}`));
  await browser.disconnect();
})().catch(e => { console.error('ERR', e.stack || e.message); process.exit(1); });
