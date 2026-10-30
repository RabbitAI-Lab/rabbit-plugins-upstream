// 抓草稿箱列表 -> drafts.json
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const b = await puppeteer.connect({ browserURL: 'http://127.0.0.1:9222', protocolTimeout: 120000 });
  const all = await b.pages();
  let page = all.find(p => p.url().includes('creator.xiaohongshu.com')) || await b.newPage();
  await page.setViewport({ width: 1440, height: 900 });

  await page.goto('https://creator.xiaohongshu.com/publish/publish?source=official', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await sleep(6000);
  await page.evaluate(() => {
    const hit = Array.from(document.querySelectorAll('*'))
      .find(e => e.children.length === 0 && /^草稿箱\(\d+\)$/.test((e.textContent || '').trim()));
    if (hit) hit.click();
  });
  await sleep(6000);

  const drafts = await page.evaluate(() => Array.from(document.querySelectorAll('.draft-item')).map(c => {
    const t = (c.innerText || '').replace(/\s+/g, ' ').trim();
    const date = (t.match(/保存于(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})/) || [])[1] || '';
    const title = t.replace(/^\d{1,2}:\d{2}(:\d{2})?\s*/, '').replace(/\s*保存于.*$/, '').replace(/\s*(编辑|删除)\s*$/, '').trim();
    return { title, saveAt: date, raw: t.slice(0, 90) };
  }));
  console.log('草稿总数:', drafts.length);
  drafts.forEach((d, i) => console.log(String(i).padStart(2) + ' | ' + d.saveAt + ' | ' + d.title));
  fs.writeFileSync('/Users/jx/Downloads/.workbuddy/macros/drafts.json', JSON.stringify(drafts, null, 2));
  console.log('\n已写入 drafts.json');
  await b.disconnect();
})().catch(e => { console.log('ERR', e.message.split('\n')[0]); process.exit(1); });
