// 上传一期到小红书【草稿箱】（不定时、不发布）
// 用法: EP=29 node xhs-draft-ep.js
// 注：playwright 的 connectOverCDP 在本机 Chrome(54 target) 下握手会卡死，改用 puppeteer-core。
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const SHOT = '/Users/jx/Downloads/.workbuddy/macros/shots';
const sleep = ms => new Promise(r => setTimeout(r, ms));
const fail = m => { throw new Error('【中止】' + m); };

const EP = process.env.EP;
// SERIES: 目录前缀，默认 xip（系列一《怎么活得更好》）；系列三用 SERIES=xip3
const SERIES = process.env.SERIES || 'xip';
const COLLECTION = process.env.COLLECTION || '怎么活得更好';
const NO_CHAPTER = process.env.NO_CHAPTER === '1';   // 章节生成会长时间占用页面主线程，长视频可跳过

const VIDEO = `/Users/jx/Downloads/${SERIES}-ep${EP}/output.mp4`;
const COPY = `/Users/jx/Downloads/${SERIES}-ep${EP}/xhs-copy.txt`;
const EDITOR = 'div.tiptap.ProseMirror[contenteditable="true"]';

// 兼容两种文案格式：
//   系列一 markdown 式  ## 标题 / ## 正文 / ## 话题标签（话题一行一个）
//   系列三 方括号式    【标题】/【正文】/【话题标签】（话题一行空格分隔）
const HEAD = '(?:##\\s*标题|【标题】)';
const BODY = '(?:##\\s*正文|【正文】)';
const TAGS = '(?:##\\s*话题标签|【话题标签】)';
function parseCopy(file) {
  const t = fs.readFileSync(file, 'utf8');
  const title = ((t.match(new RegExp(HEAD + '\\s*\\n(.+)')) || [])[1] || '').trim();
  const body = ((t.match(new RegExp(BODY + '\\s*\\n([\\s\\S]*?)\\n\\s*' + TAGS)) || [])[1] || '').trim();
  const tagBlock = ((t.match(new RegExp(TAGS + '\\s*\\n([\\s\\S]*)$')) || [])[1] || '');
  const topics = tagBlock.split(/[\s\n]+/).map(s => s.trim()).filter(s => s.startsWith('#'));
  return { title, body, topics };
}

// 给"文本精确等于 txt 且子节点很少"的元素打 id，返回是否成功
const markByText = (page, txt, id) => page.evaluate((t, i) => {
  const el = Array.from(document.querySelectorAll('button, div, span, a'))
    .find(e => (e.textContent || '').replace(/\s+/g, '').trim() === t && e.children.length <= 2 && e.offsetParent !== null);
  if (!el) return false;
  el.scrollIntoView({ block: 'center' });
  el.id = i;
  return true;
}, txt, id);

(async () => {
  if (!fs.existsSync(VIDEO)) fail('视频不存在: ' + VIDEO);
  if (!fs.existsSync(COPY)) fail('文案不存在: ' + COPY);
  const { title, body, topics } = parseCopy(COPY);
  const mb = Math.round(fs.statSync(VIDEO).size / 1048576);
  console.log(`=== ep${EP} 草稿 === ${title} | 正文 ${body.length} 字 | 话题 ${topics.length} | 视频 ${mb}MB`);

  const browser = await puppeteer.connect({ browserURL: 'http://127.0.0.1:9222', protocolTimeout: 300000 });

  // 1. 找到可复用的空白发布页；否则清掉所有 creator 页（含草稿箱页）后新建一个，避免标签页堆积
  const allPages = await browser.pages();
  const creatorPages = allPages.filter(p => p.url().includes('creator.xiaohongshu.com'));
  let page = null;
  for (const p of creatorPages) {
    if (!p.url().includes('/publish/publish')) continue;
    const blank = await p.evaluate(() =>
      !!document.querySelector('input.upload-input') && !document.querySelector('input[placeholder*="填写标题"]')).catch(() => false);
    if (blank) { page = p; console.log('复用空白发布页'); break; }
  }
  if (!page) {
    for (const p of creatorPages) { try { await p.close(); } catch (e) {} }
    page = await browser.newPage();
    await page.goto('https://creator.xiaohongshu.com/publish/publish?source=official', { waitUntil: 'domcontentloaded' });
    await sleep(7000);
  }
  await page.bringToFront();
  await sleep(1000);

  const input = await page.$('input.upload-input');
  if (!input) fail('找不到上传输入框');
  await input.uploadFile(VIDEO);
  console.log('已选择文件，等待上传/转码…');

  let upOk = false;
  for (let i = 0; i < 100; i++) {
    await sleep(6000);
    const st = await page.evaluate(() => ({
      ready: !!document.querySelector('input[placeholder*="填写标题"]'),
      err: (() => {
        const t = document.body.innerText || '';
        const m = t.match(/[^\n]*(时长|过大|不支持|失败|超出|超过|限制)[^\n]*/g);
        return m ? m.slice(0, 3).join(' | ').slice(0, 200) : '';
      })()
    }));
    if (st.ready) { upOk = true; break; }
    if (st.err) console.log('  页面提示:', st.err);
    if (i % 5 === 4) console.log('  …已等 ' + ((i + 1) * 6) + 's');
  }
  if (!upOk) fail('上传/转码超时');
  console.log('上传完成');

  // 2. 标题
  await page.evaluate(t => {
    const el = document.querySelector('input[placeholder*="填写标题"]');
    el.focus();
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, t);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  }, title);
  await sleep(600);

  // 3. 正文
  await page.evaluate(sel => {
    const el = document.querySelector(sel);
    el.focus();
    document.execCommand('selectAll', false, null);
    document.execCommand('delete', false, null);
  }, EDITOR);
  await sleep(400);
  await page.evaluate((sel, text) => {
    const el = document.querySelector(sel);
    el.focus();
    document.execCommand('insertText', false, text);
  }, EDITOR, body);
  await sleep(1200);

  // 4. 话题：键盘精确点选
  const topicsOk = [];
  for (const topic of topics) {
    const kw = topic.replace(/^#/, '');
    let ok = false;
    for (let attempt = 1; attempt <= 2 && !ok; attempt++) {
      await page.evaluate(sel => {
        const el = document.querySelector(sel);
        el.focus();
        document.execCommand('insertText', false, '  ');
      }, EDITOR);
      await sleep(250);
      await page.evaluate((sel, k) => {
        const el = document.querySelector(sel);
        el.focus();
        document.execCommand('insertText', false, '#' + k);
      }, EDITOR, kw);
      await sleep(1900);
      const candidates = await page.evaluate(() => {
        const boxes = Array.from(document.querySelectorAll('.items')).filter(b => b.offsetParent !== null);
        const box = boxes[boxes.length - 1];
        return box ? Array.from(box.querySelectorAll('.item')).map(i => {
          const n = i.querySelector('.name');
          return n ? n.innerText.trim() : '';
        }) : [];
      });
      const idx = candidates.indexOf(topic);
      if (idx < 0) break;
      for (let i = 0; i < idx; i++) { await page.keyboard.press('ArrowDown'); await sleep(150); }
      await sleep(300);
      await page.keyboard.press('Enter');
      await sleep(1300);
      const last = await page.evaluate(sel => {
        const chips = document.querySelectorAll(sel + ' a.tiptap-topic');
        if (!chips.length) return null;
        try { return JSON.parse(chips[chips.length - 1].getAttribute('data-topic')).name; } catch (e) { return null; }
      }, EDITOR);
      if (last === kw) ok = true;
      else { await page.keyboard.down('Meta'); await page.keyboard.press('KeyZ'); await page.keyboard.up('Meta'); await sleep(800); await page.keyboard.down('Meta'); await page.keyboard.press('KeyZ'); await page.keyboard.up('Meta'); await sleep(800); }
    }
    topicsOk.push((ok ? '✓' : '✗') + topic);
  }
  console.log('话题:', topicsOk.join(' '));

  // 5. 智能章节（失败不阻断存草稿）
  if (NO_CHAPTER) {
    console.log('章节: 已按 NO_CHAPTER 跳过');
  } else {
    try {
      if (await page.$('button.smart-generate-btn')) {
        await page.click('button.smart-generate-btn');
        let got = false;
        for (let i = 1; i <= 15; i++) {
          await sleep(5000);
          got = await page.evaluate(() => /已为你生成章节/.test(document.body.innerText));
          if (got) break;
        }
        if (got && await markByText(page, '保存章节', 'xhs-save-ch')) {
          await page.click('#xhs-save-ch');
          await sleep(3000);
          console.log('章节: 已保存');
        } else { console.log('⚠️ 章节未生成（草稿可后续手动生成）'); }
      } else { console.log('⚠️ 无章节按钮'); }
    } catch (e) { console.log('⚠️ 章节步骤异常，继续:', e.message.split('\n')[0]); }
  }

  // 6. 原创声明（失败不阻断）
  let origOn = false;
  try {
  const origSt = await page.evaluate(() => {
    const w = document.querySelector('.original-wrapper');
    if (!w) return null;
    w.scrollIntoView({ block: 'center' });
    const sim = w.querySelector('.d-switch-simulator');
    return { unchecked: /unchecked/.test(sim ? sim.className : '') };
  });
  if (origSt && origSt.unchecked) {
    await page.evaluate(() => { document.querySelector('.original-wrapper .d-switch').id = 'xhs-orig-sw'; });
    await page.click('#xhs-orig-sw');
    await sleep(1800);
    if (await page.evaluate(() => !!document.querySelector('.d-modal'))) {
      await page.evaluate(() => { const b = document.querySelector('.d-modal .d-checkbox'); if (b) b.id = 'xhs-cb'; });
      await page.click('#xhs-cb');
      await sleep(700);
      if (await markByText(page, '声明原创', 'xhs-orig-ok')) {
        await page.click('#xhs-orig-ok');
        await sleep(2200);
      }
    }
  }
  origOn = await page.evaluate(() => {
    const s = document.querySelector('.original-wrapper .d-switch-simulator');
    return s ? !/unchecked/.test(s.className) : false;
  });
  } catch (e) { console.log('⚠️ 原创步骤异常，继续:', e.message.split('\n')[0]); }
  console.log('原创:', origOn ? '✓' : '✗（草稿可后续补）');

  // 7. 合集（失败不阻断）
  let colOk = false;
  try {
  const colNow = await page.evaluate(() => {
    const w = document.querySelector('.collection-plugin-wrapper');
    return w ? (w.innerText || '').replace(/\s+/g, ' ') : '';
  });
  if (!colNow.includes(COLLECTION)) {
    if (await markByText(page, '选择合集', 'xhs-pick-col')) {
      await page.click('#xhs-pick-col');
      await sleep(2200);
      const picked = await page.evaluate(n => {
        const pop = document.querySelector('.collection-plugin-popover');
        const item = pop && Array.from(pop.querySelectorAll('.item, .item-label')).find(e =>
          (e.textContent || '').replace(/\s+/g, '').trim() === n);
        if (!item) return false;
        item.id = 'xhs-col-item';
        return true;
      }, COLLECTION);
      if (picked) { await page.click('#xhs-col-item'); await sleep(2000); }
    }
  }
  const colAfter = await page.evaluate(() => {
    const w = document.querySelector('.collection-plugin-wrapper');
    return w ? (w.innerText || '').replace(/\s+/g, ' ').slice(0, 60) : '';
  });
  colOk = colAfter.includes(COLLECTION);
  console.log('合集:', colOk ? '✓' : '✗ ' + colAfter);
  } catch (e) { console.log('⚠️ 合集步骤异常，继续:', e.message.split('\n')[0]); }

  // 8. 内容校验（草稿不校验定时）
  const final = await page.evaluate(() => ({
    title: (document.querySelector('input[placeholder*="填写标题"]') || {}).value || '',
    bodyLen: ((document.querySelector('div.tiptap.ProseMirror') || {}).innerText || '').length,
    topics: document.querySelectorAll('div.tiptap.ProseMirror a.tiptap-topic').length
  }));
  console.log('校验:', JSON.stringify(final));
  if (final.title !== title) fail('标题不符');
  if (final.bodyLen < 50) fail('正文过短: ' + final.bodyLen);
  await page.screenshot({ path: `${SHOT}/xhs-ep${EP}-draft-ready.png` });

  // 9. 存草稿交给专用脚本（按钮在闭包 shadow DOM 里，逻辑已在 xhs-save-draft.js 验证）
  console.log('✅ ep' + EP + ' 内容已就绪，下一步: EP=' + EP + ' node xhs-save-draft.js');
  await browser.disconnect();
})().catch(e => { console.error('FATAL ep' + EP + ': ' + e.message); process.exit(1); });
