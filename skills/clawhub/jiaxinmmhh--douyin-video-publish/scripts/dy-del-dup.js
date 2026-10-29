// 删除重复的预约作品（默认 DRY，DEL=1 才真删）
// 用法: KW="成年人缺的不是目标" IDX=2 node dy-del-dup.js [DEL=1]
const puppeteer = require('puppeteer-core');
const CDP = 'http://127.0.0.1:9222';
const sleep = ms => new Promise(r => setTimeout(r, ms));
const KW = process.env.KW || '成年人缺的不是目标';
const IDX = parseInt(process.env.IDX || '2', 10);   // 删第几条（从 1 数）
const DEL = process.env.DEL === '1';

(async () => {
  const browser = await puppeteer.connect({ browserURL: CDP, defaultViewport: { width: 1440, height: 900 }, protocolTimeout: 300000 });
  const page = await browser.newPage();
  try { await page.goto('https://creator.douyin.com/creator-micro/content/manage', { waitUntil: 'domcontentloaded', timeout: 60000 }); } catch (e) {}
  await sleep(9000);
  await page.bringToFront();

  // 搜索
  const si = await page.evaluate(() => {
    const i = Array.from(document.querySelectorAll('input')).find(x => (x.placeholder || '').includes('搜索') && x.offsetParent !== null);
    if (!i) return null;
    const r = i.getBoundingClientRect();
    return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
  });
  if (!si) throw new Error('无搜索框');
  await page.mouse.click(si.x, si.y);
  await sleep(400);
  await page.keyboard.type(KW, { delay: 40 });
  await page.keyboard.press('Enter');
  await sleep(5000);

  // 定位第 IDX 个「删除作品」
  const del = await page.evaluate((idx) => {
    const btns = Array.from(document.querySelectorAll('*')).filter(e => {
      const t = (e.innerText || '').trim();
      return t === '删除作品' && e.offsetParent !== null && e.children.length <= 2;
    });
    if (btns.length < idx) return { found: false, count: btns.length };
    const b = btns[idx - 1];
    const r = b.getBoundingClientRect();
    return { found: true, count: btns.length, x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
  }, IDX);
  console.log('删除作品按钮:', JSON.stringify(del));
  if (!del.found) { await browser.disconnect(); return; }
  await page.mouse.click(del.x, del.y);
  await sleep(2500);

  const dlg = await page.evaluate(() => {
    const modals = Array.from(document.querySelectorAll('[class*="modal"], [class*="Modal"], [class*="dialog"], [class*="Dialog"], [class*="popover"]'))
      .filter(e => e.offsetParent !== null && (e.innerText || '').trim());
    const btns = Array.from(document.querySelectorAll('button, [class*="btn"]'))
      .filter(b => b.offsetParent !== null && (b.innerText || '').trim())
      .map(b => (b.innerText || '').trim());
    return { modals: modals.map(m => (m.innerText || '').trim().replace(/\n+/g, ' | ').slice(0, 200)).slice(0, 4), btns: [...new Set(btns)] };
  });
  console.log('=== 弹窗 ==='); console.log(JSON.stringify(dlg, null, 1));
  await page.screenshot({ path: '/Users/jx/Downloads/.workbuddy/macros/dy-del-confirm.png' });

  if (!DEL) { console.log('DRY 模式，未确认删除'); await browser.disconnect(); return; }

  // 点确认
  const cfm = await page.evaluate(() => {
    const b = Array.from(document.querySelectorAll('button, [class*="btn"]'))
      .find(x => x.offsetParent !== null && /^(确认|确定|删除)$/.test((x.innerText || '').trim()));
    if (!b) return null;
    const r = b.getBoundingClientRect();
    return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2), t: b.innerText.trim() };
  });
  console.log('确认按钮:', JSON.stringify(cfm));
  if (!cfm) { console.log('未找到确认按钮'); await browser.disconnect(); return; }
  await page.mouse.click(cfm.x, cfm.y);
  await sleep(5000);
  const after = await page.evaluate(() => document.body.innerText.slice(0, 400));
  console.log('=== 删除后 ==='); console.log(after);
  await page.screenshot({ path: '/Users/jx/Downloads/.workbuddy/macros/dy-del-done.png' });
  await browser.disconnect();
})().catch(e => { console.error('ERR', e.stack || e.message); process.exit(1); });
