// 打开草稿箱里已有的一条草稿 -> 补「原创声明」与「合集」-> 再存回草稿
// 用法: SERIES=xip3 EP=10 COLLECTION="怎么赚得更聪明" node xhs-fix-draft.js
// 用于补救批量入库时因主线程超时漏掉原创/合集的条目
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const SHOT = '/Users/jx/Downloads/.workbuddy/macros/shots';
const sleep = ms => new Promise(r => setTimeout(r, ms));
const fail = m => { throw new Error('【中止】' + m); };

const EP = process.env.EP;
const SERIES = process.env.SERIES || 'xip';
const COLLECTION = process.env.COLLECTION || '怎么活得更好';
const COPY = `/Users/jx/Downloads/${SERIES}-ep${EP}/xhs-copy.txt`;

const HEAD = '(?:##\\s*标题|【标题】)';
function readTitle(file) {
  const t = fs.readFileSync(file, 'utf8');
  return ((t.match(new RegExp(HEAD + '\\s*\\n(.+)')) || [])[1] || '').trim();
}

const markByText = (page, txt, id) => page.evaluate((t, i) => {
  const el = Array.from(document.querySelectorAll('button, div, span, a'))
    .find(e => (e.textContent || '').replace(/\s+/g, '').trim() === t && e.children.length <= 2 && e.offsetParent !== null);
  if (!el) return false;
  el.scrollIntoView({ block: 'center' });
  el.id = i;
  return true;
}, txt, id);

(async () => {
  const title = readTitle(COPY);
  console.log(`=== 修 ep${EP} === ${title} | 合集 ${COLLECTION}`);

  const browser = await puppeteer.connect({ browserURL: 'http://127.0.0.1:9222', protocolTimeout: 600000 });
  const all = await browser.pages();
  // 关掉多余 creator 页，避免标签堆积拖慢主线程
  const creators = all.filter(p => p.url().includes('creator.xiaohongshu.com'));
  for (let i = 1; i < creators.length; i++) { try { await creators[i].close(); } catch (e) {} }
  let page = creators[0] || await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });

  // 1. 进发布页 -> 草稿箱
  await page.goto('https://creator.xiaohongshu.com/publish/publish?source=official', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await sleep(7000);
  await page.evaluate(() => {
    const hit = Array.from(document.querySelectorAll('*'))
      .find(e => e.children.length === 0 && /^草稿箱\(\d+\)$/.test((e.textContent || '').trim()));
    if (hit) hit.click();
  });
  await sleep(6000);

  // 2. 按标题定位条目并点「编辑」
  const clicked = await page.evaluate(t => {
    const items = Array.from(document.querySelectorAll('.draft-item'));
    const hit = items.find(c => (c.innerText || '').includes(t));
    if (!hit) return { ok: false, n: items.length };
    const btn = Array.from(hit.querySelectorAll('*')).find(e =>
      e.children.length === 0 && /^编辑$/.test((e.textContent || '').trim()) && e.offsetParent !== null);
    (btn || hit).click();
    return { ok: true, via: btn ? '编辑按钮' : '卡片', n: items.length };
  }, title);
  if (!clicked.ok) fail(`草稿箱里没找到「${title}」（共 ${clicked.n} 条）`);
  console.log('已点击条目:', JSON.stringify(clicked));

  // 3. 等编辑页就绪
  let ready = false;
  for (let i = 0; i < 40; i++) {
    await sleep(5000);
    const st = await page.evaluate(() => ({
      t: (document.querySelector('input[placeholder*="填写标题"]') || {}).value || '',
      ed: !!document.querySelector('div.tiptap.ProseMirror[contenteditable="true"]')
    })).catch(() => ({ t: '', ed: false }));
    if (st.ed && st.t.trim() === title) { ready = true; break; }
    if (i % 4 === 3) console.log('  …等编辑页 ' + ((i + 1) * 5) + 's, 当前标题=' + JSON.stringify(st.t.slice(0, 20)));
  }
  if (!ready) fail('编辑页未就绪');
  console.log('编辑页就绪');
  await sleep(3000);

  // 4. 原创声明
  let origOn = false;
  try {
    const st = await page.evaluate(() => {
      const w = document.querySelector('.original-wrapper');
      if (!w) return null;
      w.scrollIntoView({ block: 'center' });
      const sim = w.querySelector('.d-switch-simulator');
      return { unchecked: /unchecked/.test(sim ? sim.className : '') };
    });
    if (st && st.unchecked) {
      await page.evaluate(() => { document.querySelector('.original-wrapper .d-switch').id = 'xhs-orig-sw'; });
      await page.click('#xhs-orig-sw');
      await sleep(2000);
      if (await page.evaluate(() => !!document.querySelector('.d-modal'))) {
        await page.evaluate(() => { const b = document.querySelector('.d-modal .d-checkbox'); if (b) b.id = 'xhs-cb'; });
        await page.click('#xhs-cb');
        await sleep(800);
        if (await markByText(page, '声明原创', 'xhs-orig-ok')) { await page.click('#xhs-orig-ok'); await sleep(2500); }
      }
    }
    origOn = await page.evaluate(() => {
      const s = document.querySelector('.original-wrapper .d-switch-simulator');
      return s ? !/unchecked/.test(s.className) : false;
    });
  } catch (e) { console.log('⚠️ 原创异常:', e.message.split('\n')[0]); }
  console.log('原创:', origOn ? '✓' : '✗');

  // 5. 合集
  let colOk = false;
  try {
    const now = await page.evaluate(() => {
      const w = document.querySelector('.collection-plugin-wrapper');
      if (w) w.scrollIntoView({ block: 'center' });
      return w ? (w.innerText || '').replace(/\s+/g, ' ') : '';
    });
    console.log('  合集当前:', now.slice(0, 40));
    if (!now.includes(COLLECTION)) {
      if (await markByText(page, '选择合集', 'xhs-pick-col')) {
        await page.click('#xhs-pick-col');
        await sleep(2500);
        const picked = await page.evaluate(n => {
          const pop = document.querySelector('.collection-plugin-popover');
          const item = pop && Array.from(pop.querySelectorAll('.item, .item-label')).find(e =>
            (e.textContent || '').replace(/\s+/g, '').trim() === n);
          if (!item) return false;
          item.id = 'xhs-col-item';
          return true;
        }, COLLECTION);
        if (picked) { await page.click('#xhs-col-item'); await sleep(2500); }
        else console.log('  ⚠️ 弹层里没找到合集项');
      } else { console.log('  ⚠️ 没找到「选择合集」按钮'); }
    }
    colOk = await page.evaluate(n => {
      const w = document.querySelector('.collection-plugin-wrapper');
      return w ? (w.innerText || '').replace(/\s+/g, ' ').includes(n) : false;
    }, COLLECTION);
  } catch (e) { console.log('⚠️ 合集异常:', e.message.split('\n')[0]); }
  console.log('合集:', colOk ? '✓' : '✗');

  await page.screenshot({ path: `${SHOT}/xhs-fix-${SERIES}-ep${EP}.png` });
  if (!origOn && !colOk) { console.log('两项都没补上，不点保存（避免无意义改动）'); await browser.disconnect(); process.exit(2); }

  // 6. 点「暂存离开」——底部按钮在闭包 shadow DOM，用 CDP 坐标扫描，绝不点 bg-red
  const attrs = await page.evaluate(() => {
    const h = document.querySelector('xhs-publish-btn');
    if (!h) return null;
    const o = {};
    for (const a of h.attributes) o[a.name] = a.value;
    const r = h.getBoundingClientRect();
    o._rect = { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
    return o;
  });
  if (!attrs || attrs['is-save-draft'] !== 'true') fail('无可存草稿按钮');

  const cdp = await page.createCDPSession();
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  const vp = await page.evaluate(() => ({ vw: window.innerWidth, vh: window.innerHeight }));
  await cdp.send('DOM.getDocument', { depth: 1, pierce: true });
  const y0 = Math.max(0, attrs._rect.y - 4);
  const y1 = Math.min(vp.vh - 2, attrs._rect.y + attrs._rect.h + 8);
  const buttons = {};
  for (let y = y0; y <= y1; y += 4) {
    for (let x = 2; x < vp.vw - 2; x += 12) {
      let nodeId = null;
      try { nodeId = (await cdp.send('DOM.getNodeForLocation', { x, y, includeUserAgentShadowDOM: true })).nodeId; } catch (e) { continue; }
      if (!nodeId) continue;
      let node = null;
      try { node = (await cdp.send('DOM.describeNode', { nodeId, depth: 0, pierce: true })).node; } catch (e) { continue; }
      if ((node.localName || '').toLowerCase() !== 'button') continue;
      const key = (node.attributes || []).join(' ');
      if (!/ce-btn/.test(key)) continue;
      if (!buttons[key]) buttons[key] = { xs: [], ys: [] };
      buttons[key].xs.push(x); buttons[key].ys.push(y);
    }
  }
  const list = Object.keys(buttons).map(k => ({
    key: k,
    x1: Math.min(...buttons[k].xs), x2: Math.max(...buttons[k].xs),
    y1: Math.min(...buttons[k].ys), y2: Math.max(...buttons[k].ys),
    n: buttons[k].xs.length,
    red: /bg-red/.test(k)
  })).sort((a, b) => a.x1 - b.x1);
  console.log('扫描到 ce-btn:');
  list.forEach(b => console.log(`  x ${b.x1}~${b.x2} 点${b.n} ${b.red ? '🔴发布(禁点)' : '⚪暂存离开'}`));

  const secondary = list.filter(b => !b.red && b.n >= 5);
  if (!secondary.length) fail('未找到「暂存离开」按钮');
  const pick = secondary.sort((a, b) => b.n - a.n)[0];
  if (pick.red) fail('安全闸：选中了发布按钮，已中止');
  const cx = Math.round((pick.x1 + pick.x2) / 2), cy = Math.round((pick.y1 + pick.y2) / 2);
  console.log('点击位置:', cx, cy);
  if (process.env.DRY === '1') { console.log('DRY=1 不点击'); await browser.disconnect(); return; }

  await cdp.send('Input.dispatchMouseEvent', { type: 'mouseMoved', x: cx, y: cy, button: 'none', clickCount: 0 });
  await sleep(300);
  await cdp.send('Input.dispatchMouseEvent', { type: 'mousePressed', x: cx, y: cy, button: 'left', clickCount: 1 });
  await sleep(100);
  await cdp.send('Input.dispatchMouseEvent', { type: 'mouseReleased', x: cx, y: cy, button: 'left', clickCount: 1 });
  console.log('>>> 已点击 暂存离开');

  let done = false;
  for (let i = 1; i <= 16; i++) {
    await sleep(2500);
    const st = await page.evaluate(() => ({
      toast: (() => {
        const t = document.body.innerText || '';
        const m = t.match(/[^\n]*(保存成功|已保存|草稿|存入)[^\n]*/g);
        return m ? m.slice(0, 2).join(' | ').slice(0, 120) : '';
      })(),
      inEditor: !!document.querySelector('div.tiptap.ProseMirror[contenteditable="true"]')
    })).catch(() => ({ toast: '', inEditor: false }));
    if (st.toast) console.log('    提示:', st.toast);
    if (!st.inEditor) { done = true; console.log(`✅ ep${EP} 已保存并离开编辑器`); break; }
  }
  if (!done) console.log('⚠️ 仍在编辑器，状态未确认');
  await browser.disconnect();
  if (!done) process.exit(2);
})().catch(e => { console.error('FATAL ep' + EP + ': ' + e.message); process.exit(1); });
