// 抖音：上传 + 填标题/简介/话题 + 合集 + 定时发布
//
// 用法: node dy-publish.js --ep 02 --time "2026-10-15 07:00" [--dry]
//       node dy-publish.js --file a.mp4 --title "标题" --desc "正文" --topics "#a #b" --time "..." [--dry]
//
// 退出码: 0 成功 | 1 失败 | 2 参数错误 | 4 超出14天窗口
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const CDP = 'http://127.0.0.1:9222';
const sleep = ms => new Promise(r => setTimeout(r, ms));
const fail = (m, code = 1) => { const e = new Error('【中止】' + m); e.code = code; throw e; };

const arg = (k, d) => { const i = process.argv.indexOf('--' + k); return i >= 0 ? process.argv[i + 1] : d; };
const has = k => process.argv.includes('--' + k);

// ---------- 输入 ----------
let VIDEO, TITLE, BODY, TOPICS, ALBUM = '怎么活得更好', TIME, DRY = has('dry');
const EP = arg('ep');
TIME = arg('time');
if (EP) {
  const dir = `/Users/jx/Downloads/xip-ep${EP}`;
  VIDEO = `${dir}/output.mp4`;
  const c = fs.readFileSync(`${dir}/xhs-copy.txt`, 'utf8');
  TITLE = (c.match(/## 标题\n(.+)/) || [])[1].trim();
  BODY = (c.match(/## 正文\n([\s\S]*?)\n## 话题标签/) || [])[1].trim();
  TOPICS = ((c.match(/## 话题标签\n([\s\S]*)$/) || [])[1] || '').split('\n').map(s => s.trim()).filter(s => s.startsWith('#'));
} else {
  VIDEO = arg('file'); TITLE = arg('title'); BODY = arg('desc', '');
  TOPICS = (arg('topics', '').match(/#\S+/g) || []);
}
ALBUM = arg('album', ALBUM);

// ---------- 校验 ----------
if (!VIDEO || !fs.existsSync(VIDEO)) fail('视频不存在: ' + VIDEO, 2);
if (!TITLE) fail('缺标题', 2);
if (TITLE.length > 30) fail(`标题 ${TITLE.length} 字 > 30`, 2);
const DESC_FULL = (BODY + (TOPICS.length ? '\n' + TOPICS.join(' ') : '')).trim();
if (DESC_FULL.length > 1000) fail(`简介 ${DESC_FULL.length} 字 > 1000`, 2);

if (TIME) {
  const t = new Date(TIME.replace(' ', 'T') + ':00');
  const now = Date.now();
  const diffH = (t.getTime() - now) / 3600000;
  if (Number.isNaN(t.getTime())) fail('时间格式错误，需 YYYY-MM-DD HH:mm', 2);
  if (diffH < 2) fail(`定时 ${TIME} 距今不足 2 小时（抖音下限）`, 4);
  if (diffH > 14 * 24) fail(`定时 ${TIME} 超出 14 天窗口（抖音上限）`, 4);
}

const mb = Math.round(fs.statSync(VIDEO).size / 1048576);
console.log(`=== ep${EP || '-'} | ${TITLE} (${TITLE.length}字) | 简介 ${DESC_FULL.length}字 | 话题 ${TOPICS.length} | ${mb}MB ===`);
console.log(`>>> ${DRY ? 'DRY-RUN 演练（不提交）' : '正式发布'} | 定时 ${TIME || '立即'} | 合集 ${ALBUM}`);

// ---------- 主流程 ----------
(async () => {
  const browser = await puppeteer.connect({ browserURL: CDP, defaultViewport: { width: 1440, height: 900 }, protocolTimeout: 600000 });
  // 清掉遗留的上传/发布页 tab，避免堆积
  for (const p of await browser.pages()) {
    if (/creator\.douyin\.com\/creator-micro\/content\/(upload|post)/.test(p.url())) {
      try { await p.close(); } catch (e) {}
    }
  }
  const page = await browser.newPage();
  await page.setRequestInterception(false);
  await page.goto('https://creator.douyin.com/creator-micro/content/upload', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await sleep(6000);

  const input = await page.$('input[type=file]');
  if (!input) fail('找不到上传 input（是否掉登录？）', 3);
  await input.uploadFile(VIDEO);
  console.log('  ① 视频已注入，等待上传...');

  // 等上传完成（关键：必须等"取消上传"进度浮层消失，否则它会遮挡后续点击）
  let ok = false;
  for (let i = 0; i < 120; i++) {
    await sleep(3000);
    const st = await page.evaluate(() => {
      const t = document.body.innerText;
      return {
        uploading: t.includes('取消上传'),
        done: t.includes('重新上传'),
        hasForm: t.includes('发布设置'),
        prog: (t.match(/(\d{1,3})%/) || [])[0] || '',
      };
    });
    if (i % 3 === 0 || st.prog || st.done) console.log(`     ${i * 3}s ${st.prog} 上传中=${st.uploading} 完成=${st.done}`);
    if (st.done && !st.uploading) { ok = true; break; }
  }
  if (!ok) fail('上传超时或未完成');
  await sleep(4000);
  console.log('  ② 上传完成，表单就绪');

  // ---- 标题 ----
  await page.evaluate((t) => {
    const el = document.querySelector('input[placeholder*="作品标题"]')
      || Array.from(document.querySelectorAll('input[type=text]')).find(x => x.offsetParent !== null);
    el.focus();
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, t);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  }, TITLE);
  await sleep(800);

  // ---- 简介 + 话题 ----
  await page.evaluate(() => { const e = document.querySelector('[contenteditable="true"]'); e.scrollIntoView({ block: 'center' }); e.focus(); });
  await sleep(500);
  const cdp = await page.createCDPSession();
  await cdp.send('Input.insertText', { text: DESC_FULL });
  await sleep(1500);
  console.log('  ③ 标题/简介已填');

  // ---- 合集 ----
  if (ALBUM) {
    // 先关掉可能遮挡的浮层（"视频预览功能…我知道了"）
    await page.evaluate(() => {
      const b = Array.from(document.querySelectorAll('button, div, span'))
        .find(e => (e.innerText || '').trim() === '我知道了' && e.offsetParent !== null);
      if (b) b.click();
    });
    await sleep(800);

    let picked = false;
    for (let attempt = 1; attempt <= 4 && !picked; attempt++) {
      // 用元素句柄点击（比坐标点击可靠）
      // 注意：页面上有两个下拉——左边"合集"(类型) 和 右边"请选择合集"(真正要点的那个)
      const handles = await page.$$('.semi-select');
      let target = null;
      for (const h of handles) {
        const txt = (await h.evaluate(e => (e.innerText || '')).catch(() => '')).trim();
        if (txt.includes('请选择合集') || txt.includes(ALBUM)) { target = h; break; }
      }
      if (!target) fail('找不到合集下拉控件');
      await target.evaluate(e => e.scrollIntoView({ block: 'center' })).catch(() => {});
      await sleep(500);

      let opened = false;
      try {
        await target.click();
        opened = true;
      } catch (e) {
        console.log('     句柄点击失败:', e.message.slice(0, 60));
      }
      await sleep(2200);

      let opt = await page.evaluate((alb) => {
        const o = Array.from(document.querySelectorAll('.semi-select-option'))
          .find(e => e.offsetParent !== null && (e.innerText || '').includes(alb));
        if (!o) return null;
        const r = o.getBoundingClientRect();
        return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
      }, ALBUM);

      if (!opt) {
        // 兜底：直接 DOM click 展开再找
        await page.evaluate(() => {
          const el = Array.from(document.querySelectorAll('.semi-select')).find(s => (s.innerText || '').includes('合集'));
          if (el) el.querySelector('.semi-select-selection')?.dispatchEvent(new MouseEvent('mousedown', { bubbles: true }));
        });
        await sleep(1800);
        opt = await page.evaluate((alb) => {
          const o = Array.from(document.querySelectorAll('.semi-select-option'))
            .find(e => e.offsetParent !== null && (e.innerText || '').includes(alb));
          if (!o) return null;
          const r = o.getBoundingClientRect();
          return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
        }, ALBUM);
      }

      if (opt) {
        await page.mouse.click(opt.x, opt.y);
        await sleep(2000);
        const got = await page.evaluate(() => {
          const el = Array.from(document.querySelectorAll('.semi-select-selection-text'))
            .map(s => s.innerText.trim()).join('|');
          return el;
        });
        if (got.includes(ALBUM)) { picked = true; console.log('  ④ 合集已选:', ALBUM); break; }
        console.log(`     第${attempt}次点选后回读"${got}"，重试`);
      } else {
        console.log(`     第${attempt}次下拉未展开(opened=${opened})，重试`);
      }
      await page.keyboard.press('Escape');
      await sleep(1000);
    }
    if (!picked) fail('合集未选中: ' + ALBUM);
  }

  // ---- 定时 ----
  if (TIME) {
    const rad = await page.evaluate(() => {
      const el = Array.from(document.querySelectorAll('span,label,div')).find(e => (e.innerText || '').replace(/\s+/g, '') === '定时发布' && e.offsetParent !== null);
      if (!el) return null;
      el.scrollIntoView({ block: 'center' });
      const t = el.closest('label') || el;
      const r = t.getBoundingClientRect();
      return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
    });
    if (!rad) fail('找不到定时发布选项');
    await page.mouse.click(rad.x, rad.y);
    await sleep(2000);
    await page.evaluate((v) => {
      const el = document.querySelector('.semi-datepicker input.semi-input');
      el.focus();
      Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
      el.dispatchEvent(new Event('input', { bubbles: true }));
    }, TIME);
    await sleep(600);
    await page.keyboard.press('Enter');
    await sleep(1500);
    const v = await page.$eval('.semi-datepicker input.semi-input', e => e.value).catch(() => null);
    if (v !== TIME) fail(`定时回填校验失败：期望 ${TIME} 实得 ${v}`);
    console.log('  ⑤ 定时已设:', v);
  }

  // ---- 提交前校验 ----
  const check = await page.evaluate(() => {
    const t = document.querySelector('input[placeholder*="作品标题"]');
    const e = document.querySelector('[contenteditable="true"]');
    const out = {
      title: t ? t.value : null,
      descLen: (e.innerText || '').length,
      descCount: (document.body.innerText.match(/(\d+)\s*\/\s*1000/) || [])[0] || '',
      album: (Array.from(document.querySelectorAll('.semi-select-selection-text')).map(s => s.innerText.trim()).join('|') || '').slice(0, 60),
      time: (() => { const d = document.querySelector('.semi-datepicker input.semi-input'); return d ? d.value : null; })(),
    };
    return out;
  });
  if (check.title !== TITLE) fail(`标题回读不符：期望「${TITLE}」实得「${check.title}」`);
  if (TIME && check.time !== TIME) fail(`定时回读不符：期望 ${TIME} 实得 ${check.time}`);
  console.log('  ✅ 提交前校验:', JSON.stringify(check));
  await page.screenshot({ path: `/Users/jx/Downloads/.workbuddy/macros/dy-before-${EP || 'x'}.png`, fullPage: true });

  if (DRY) { console.log('=== DRY-RUN 结束，未提交 ==='); await browser.disconnect(); return; }

  // ---- 发布 ----
  const pub = await page.evaluate(() => {
    const b = Array.from(document.querySelectorAll('button')).find(x => (x.innerText || '').trim() === '发布' && x.offsetParent !== null && !x.disabled);
    if (!b) return null;
    b.scrollIntoView({ block: 'center' });
    const r = b.getBoundingClientRect();
    return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
  });
  if (!pub) fail('找不到发布按钮');
  await page.mouse.click(pub.x, pub.y);
  console.log('  ⑥ 已点击发布，观察反馈...');

  // 观察 toast / modal / 二次确认
  for (let i = 0; i < 12; i++) {
    await sleep(2500);
    const fb = await page.evaluate(() => {
      const toast = Array.from(document.querySelectorAll('[class*="toast"], [class*="Toast"], [class*="message"], [class*="notice"], [class*="tip"]'))
        .filter(e => e.offsetParent !== null && (e.innerText || '').trim())
        .map(e => (e.innerText || '').trim().slice(0, 120));
      const modal = Array.from(document.querySelectorAll('[class*="modal"], [class*="Modal"], [class*="dialog"]'))
        .filter(e => e.offsetParent !== null && (e.innerText || '').trim())
        .map(e => (e.innerText || '').trim().replace(/\n+/g, ' | ').slice(0, 200));
      const btns = Array.from(document.querySelectorAll('button')).filter(b => b.offsetParent !== null).map(b => (b.innerText || '').trim()).filter(Boolean);
      return { url: location.href.replace('https://creator.douyin.com/creator-micro/', ''), toast: [...new Set(toast)], modal: [...new Set(modal)].slice(0, 3), btns: [...new Set(btns)].slice(0, 12) };
    });
    console.log(`     ${i * 2.5}s url=${fb.url}` + (fb.toast.length ? ` toast=${JSON.stringify(fb.toast)}` : '') + (fb.modal.length ? ` modal=${JSON.stringify(fb.modal)}` : ''));
    if (fb.url.includes('/content/manage') || fb.url.includes('/content/post')) {
      if (fb.toast.length || fb.modal.length) { console.log('     按钮:', JSON.stringify(fb.btns)); }
    }
    if (fb.toast.length) break;
  }

  const after = await page.evaluate(() => ({ url: location.href, txt: document.body.innerText.slice(0, 300) }));
  console.log('=== 最终 url ===', after.url);
  await page.screenshot({ path: `/Users/jx/Downloads/.workbuddy/macros/dy-after-${EP || 'x'}.png` });
  await browser.disconnect();
})().catch(e => { console.error('ERR', e.message); process.exit(e.code || 1); });
