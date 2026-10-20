// 用站内搜索核查某标题是否重复
const puppeteer = require('puppeteer-core');
const CDP = 'http://127.0.0.1:9222';
const sleep = ms => new Promise(r => setTimeout(r, ms));
const KW = process.argv[2] || '成年人缺的不是目标';

(async () => {
  const browser = await puppeteer.connect({ browserURL: CDP, defaultViewport: { width: 1440, height: 900 }, protocolTimeout: 300000 });
  const page = await browser.newPage();
  try { await page.goto('https://creator.douyin.com/creator-micro/content/manage', { waitUntil: 'domcontentloaded', timeout: 60000 }); } catch (e) {}
  await sleep(9000);
  await page.bringToFront();

  // 找到搜索输入框
  const si = await page.evaluate(() => {
    const i = Array.from(document.querySelectorAll('input')).find(x => (x.placeholder || '').includes('搜索') && x.offsetParent !== null);
    if (!i) return null;
    const r = i.getBoundingClientRect();
    return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2), ph: i.placeholder };
  });
  console.log('搜索框:', JSON.stringify(si));
  if (!si) { await browser.disconnect(); return; }
  await page.mouse.click(si.x, si.y);
  await sleep(500);
  await page.keyboard.type(KW, { delay: 50 });
  await page.keyboard.press('Enter');
  await sleep(5000);

  const res = await page.evaluate(() => {
    const txt = document.body.innerText;
    const ts = txt.match(/\d{4}年\d{2}月\d{2}日\s+\d{2}:\d{2}/g) || [];
    const counter = (txt.match(/作品\s*[（(]\s*\d+\s*[)）]/) || [])[0] || '';
    return { counter, times: ts, count: ts.length, deleteCount: (txt.match(/删除作品/g) || []).length, snippet: txt.slice(0, 800) };
  });
  console.log('counter:', res.counter, '| 时间戳:', JSON.stringify(res.times), '| 删除作品x', res.deleteCount);
  console.log('--- 片段 ---'); console.log(res.snippet);
  await page.screenshot({ path: '/Users/jx/Downloads/.workbuddy/macros/dy-search.png' });
  await browser.disconnect();
})().catch(e => { console.error('ERR', e.stack || e.message); process.exit(1); });
