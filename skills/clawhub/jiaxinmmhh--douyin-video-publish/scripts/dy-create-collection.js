// 抖音：创建作品合集
// 用法: NAME="标题" DESC="简介" COVER=/path/cover.png node dy-create-collection.js
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const CDP = 'http://127.0.0.1:9222';
const sleep = ms => new Promise(r => setTimeout(r, ms));
const fail = m => { throw new Error('【中止】' + m); };

const NAME = process.env.NAME || '怎么活得更好';
const DESC = process.env.DESC || '人生下半场的另一种可能。每期搬来一位创作者的真实样本，拆开看他们怎么想、怎么选，又是怎么一天天过下来的。';
const COVER = process.env.COVER || '/Users/jx/Downloads/.workbuddy/macros/dy-col-cover.png';
const DRY = process.env.DRY === '1';

(async () => {
  if (NAME.length > 20) fail(`合集标题 ${NAME.length} 字，超过抖音 20 字上限`);
  if (DESC.length > 200) fail(`合集简介 ${DESC.length} 字，超过 200 字上限`);
  if (!fs.existsSync(COVER)) fail('封面不存在: ' + COVER);

  const browser = await puppeteer.connect({ browserURL: CDP, defaultViewport: { width: 1440, height: 900 }, protocolTimeout: 300000 });
  const page = await browser.newPage();
  try { await page.goto('https://creator.douyin.com/creator-micro/content/manage', { waitUntil: 'domcontentloaded', timeout: 60000 }); } catch (e) {}
  await sleep(7000);
  console.log('url:', page.url());

  // 进入「作品合集」tab
  await page.mouse.click(367, 125).catch(() => {});
  await sleep(3000);

  // 点「自定义创建合集」
  let opened = false;
  for (let i = 0; i < 3; i++) {
    const btn = await page.evaluate(() => {
      const el = Array.from(document.querySelectorAll('*')).find(e => (e.innerText || '').trim() === '自定义创建合集' && e.children.length <= 2 && e.offsetParent !== null);
      if (!el) return null;
      el.scrollIntoView({ block: 'center' });
      const r = el.getBoundingClientRect();
      return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
    });
    if (!btn) { // 表单可能已打开
      const has = await page.evaluate(() => document.body.innerText.includes('合集标题'));
      if (has) { opened = true; break; }
      await sleep(2000); continue;
    }
    await page.mouse.click(btn.x, btn.y);
    await sleep(3000);
    opened = await page.evaluate(() => document.body.innerText.includes('合集标题'));
    if (opened) break;
  }
  if (!opened) fail('未能打开创建合集表单');
  console.log('✅ 表单已打开');

  // 注入标题 / 简介
  await page.evaluate((n, d) => {
    const setValue = (el, v) => {
      const proto = el.tagName === 'TEXTAREA' ? window.HTMLTextAreaElement : window.HTMLInputElement;
      Object.getOwnPropertyDescriptor(proto.prototype, 'value').set.call(el, v);
      el.dispatchEvent(new Event('input', { bubbles: true }));
    };
    const t = Array.from(document.querySelectorAll('input[type=text]')).find(i => (i.placeholder || '').includes('合集'));
    const a = document.querySelector('textarea');
    if (t) setValue(t, n);
    if (a) setValue(a, d);
  }, NAME, DESC);
  await sleep(1000);

  const filled = await page.evaluate(() => {
    const t = Array.from(document.querySelectorAll('input[type=text]')).find(i => (i.placeholder || '').includes('合集'));
    const a = document.querySelector('textarea');
    return { title: t ? t.value : null, desc: a ? a.value : null, counter: (document.body.innerText.match(/(\d+)\/20/) || [])[0] || '' };
  });
  console.log('填充结果:', JSON.stringify(filled));

  // 上传封面
  const fi = await page.$('input[type=file]');
  if (!fi) fail('找不到封面上传 input');
  await fi.uploadFile(COVER);
  console.log('封面已注入，等待裁剪弹窗...');
  await sleep(4000);

  // 上传后弹出裁剪窗 → 点「保存」
  const crop = await page.evaluate(() => {
    const b = Array.from(document.querySelectorAll('button')).find(x => (x.innerText || '').trim() === '保存' && x.offsetParent !== null);
    if (!b) return null;
    const r = b.getBoundingClientRect();
    return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
  });
  console.log('裁剪保存按钮:', JSON.stringify(crop));
  if (crop) {
    await page.mouse.click(crop.x, crop.y);
    await sleep(4000);
  } else {
    console.log('⚠️ 未见裁剪弹窗，可能已直接上传');
  }

  let coverOk = false;
  for (let i = 0; i < 20; i++) {
    await sleep(2000);
    coverOk = await page.evaluate(() => {
      const t = document.body.innerText;
      const hasCrop = Array.from(document.querySelectorAll('button')).some(x => (x.innerText || '').trim() === '保存' && x.offsetParent !== null);
      const thumb = Array.from(document.querySelectorAll('img')).some(i => i.naturalWidth > 0 && /blob:|\.png|\.jpg/i.test(i.src) && i.getBoundingClientRect().width > 30);
      return { hasCrop, thumb };
    });
    if (!coverOk.hasCrop && coverOk.thumb) { coverOk = true; break; }
  }
  console.log(coverOk === true ? '✅ 封面上传完成' : '⚠️ 封面状态未确认: ' + JSON.stringify(coverOk));
  await page.screenshot({ path: '/Users/jx/Downloads/.workbuddy/macros/dy-col-filled.png' });

  if (DRY) { console.log('DRY=1，不点创建'); await browser.disconnect(); return; }

  // 点「创建」
  const mk = await page.evaluate(() => {
    const b = Array.from(document.querySelectorAll('button')).find(x => (x.innerText || '').trim() === '创建');
    if (!b) return null;
    b.scrollIntoView({ block: 'center' });
    const r = b.getBoundingClientRect();
    return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2), disabled: b.disabled };
  });
  console.log('创建按钮:', JSON.stringify(mk));
  if (!mk) fail('找不到创建按钮');
  if (mk.disabled) fail('创建按钮不可用，检查必填项');
  await page.mouse.click(mk.x, mk.y);
  await sleep(6000);

  const after = await page.evaluate(() => document.body.innerText.slice(0, 600));
  console.log('=== 创建后页面 ===\n' + after);
  await page.screenshot({ path: '/Users/jx/Downloads/.workbuddy/macros/dy-col-created.png' });
  await browser.disconnect();
})().catch(e => { console.error('ERR', e.stack || e.message); process.exit(1); });
