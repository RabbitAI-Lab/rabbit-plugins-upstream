// 在当前已填好内容的发布页上：关弹窗 -> 原创 -> 合集 -> 点「暂存离开」存草稿
// 用法: EP=29 node xhs-save-draft.js   （EP 只用于日志与截图命名）
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const SHOT = '/Users/jx/Downloads/.workbuddy/macros/shots';
const sleep = ms => new Promise(r => setTimeout(r, ms));
const fail = m => { throw new Error('【中止】' + m); };

const EP = process.env.EP || '?';
const COLLECTION = process.env.COLLECTION || '怎么活得更好';
const CLOSE_OTHER = process.env.CLOSE_OTHER === '1';

const markByText = (page, txt, id) => page.evaluate((t, i) => {
  const el = Array.from(document.querySelectorAll('button, div, span, a'))
    .find(e => (e.textContent || '').replace(/\s+/g, '').trim() === t && e.children.length <= 2 && e.offsetParent !== null);
  if (!el) return false;
  el.scrollIntoView({ block: 'center' });
  el.id = i;
  return true;
}, txt, id);

(async () => {
  const browser = await puppeteer.connect({ browserURL: 'http://127.0.0.1:9222', protocolTimeout: 120000 });
  const pages = (await browser.pages()).filter(p => p.url().includes('creator.xiaohongshu.com/publish'));
  if (!pages.length) fail('没有发布页');

  // 选一个标题非空、且没有被弹窗遮罩卡住的页面
  let page = null, pageTitle = '';
  const cand = [];
  for (const p of pages) {
    const s = await p.evaluate(() => ({
      t: (document.querySelector('input[placeholder*="填写标题"]') || {}).value || '',
      mask: !!document.querySelector('.d-modal-mask')
    })).catch(() => null);
    if (s && s.t.trim()) cand.push({ p, ...s });
  }
  if (!cand.length) fail('没有已填内容的发布页');
  const clean = cand.find(c => !c.mask) || cand[0];
  page = clean.p; pageTitle = clean.t;
  console.log('使用页面 | 标题:', pageTitle, '| 初始遮罩:', clean.mask);

  // 关闭标题相同的重复页面（避免误操作两条一样的内容）
  for (const c of cand) {
    if (c.p === page) continue;
    if (c.t === pageTitle) { try { await c.p.close(); console.log('已关闭重复页面'); } catch (e) {} }
  }
  await page.bringToFront();
  await sleep(1200);

  // 1. 关闭挡路的弹窗（章节弹窗会留一个 d-modal-mask 盖住底部按钮区）
  const hasMask = () => page.evaluate(() => !!document.querySelector('.d-modal-mask') ||
    !!Array.from(document.querySelectorAll('.d-modal')).find(m => m.offsetParent !== null));
  for (let i = 0; i < 4; i++) {
    if (!(await hasMask())) break;
    const act = await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('button'))
        .filter(b => b.offsetParent !== null);
      const cancel = btns.find(b => /^取消$/.test((b.innerText || b.textContent || '').trim()));
      if (cancel) { cancel.click(); return 'cancel'; }
      const close = document.querySelector('.d-modal [class*=close], .d-modal-close');
      if (close) { close.click(); return 'close'; }
      return 'none';
    });
    console.log('  关弹窗:', act);
    await sleep(1600);
  }
  if (await hasMask()) {
    await page.evaluate(() => {
      document.querySelectorAll('.d-modal-mask').forEach(e => e.remove());
      document.querySelectorAll('.d-modal').forEach(e => e.remove());
    });
    await sleep(800);
    console.log('  兜底：已移除 modal DOM');
  }
  console.log('遮罩状态:', (await hasMask()) ? '仍在（可能影响点击）' : '已清除');

  // 2. 原创声明
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
      await sleep(1800);
      if (await page.evaluate(() => !!document.querySelector('.d-modal'))) {
        await page.evaluate(() => { const b = document.querySelector('.d-modal .d-checkbox'); if (b) b.id = 'xhs-cb'; });
        await page.click('#xhs-cb');
        await sleep(700);
        if (await markByText(page, '声明原创', 'xhs-orig-ok')) { await page.click('#xhs-orig-ok'); await sleep(2200); }
      }
    }
    origOn = await page.evaluate(() => {
      const s = document.querySelector('.original-wrapper .d-switch-simulator');
      return s ? !/unchecked/.test(s.className) : false;
    });
  } catch (e) { console.log('⚠️ 原创异常:', e.message.split('\n')[0]); }
  console.log('原创:', origOn ? '✓' : '✗');

  // 3. 合集
  let colOk = false;
  try {
    const now = await page.evaluate(() => {
      const w = document.querySelector('.collection-plugin-wrapper');
      return w ? (w.innerText || '').replace(/\s+/g, ' ') : '';
    });
    if (!now.includes(COLLECTION)) {
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
    const after = await page.evaluate(() => {
      const w = document.querySelector('.collection-plugin-wrapper');
      return w ? (w.innerText || '').replace(/\s+/g, ' ').slice(0, 60) : '';
    });
    colOk = after.includes(COLLECTION);
    console.log('合集:', colOk ? '✓' : '✗ ' + after);
  } catch (e) { console.log('⚠️ 合集异常:', e.message.split('\n')[0]); }

  // 4. 读按钮文案
  const attrs = await page.evaluate(() => {
    const h = document.querySelector('xhs-publish-btn');
    if (!h) return null;
    const o = {};
    for (const a of h.attributes) o[a.name] = a.value;
    const r = h.getBoundingClientRect();
    o._rect = { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
    return o;
  });
  console.log('按钮属性:', JSON.stringify(attrs));
  if (!attrs || attrs['is-save-draft'] !== 'true') fail('无可存草稿按钮');

  // 5. CDP 文本搜索定位「暂存离开/暂存草稿」
  const cdp = await page.createCDPSession();
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  const saveText = attrs['save-text'] || '暂存离开';
  console.log('搜索按钮文本:', saveText);

  // 文本搜索进不去闭包 shadow DOM -> getNodeForLocation 坐标扫描（穿透 shadow）
  // 底部按钮实测：button.ce-btn.white = 暂存离开；button.ce-btn.bg-red = 发布（绝不能点）
  const vp = await page.evaluate(() => ({ vw: window.innerWidth, vh: window.innerHeight }));
  await cdp.send('DOM.getDocument', { depth: 1, pierce: true });   // 必须先建节点树，否则 getNodeForLocation 拿不到
  const y0 = Math.max(0, attrs._rect.y - 4);
  const y1 = Math.min(vp.vh - 2, attrs._rect.y + attrs._rect.h + 8);
  console.log(`扫描 y ${y0}~${y1}（视口 ${vp.vw}x${vp.vh}）`);
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
  list.forEach(b => console.log(`  x ${b.x1}~${b.x2} y ${b.y1}~${b.y2} 点${b.n} ${b.red ? '🔴发布(禁点)' : '⚪暂存离开'} :: ${b.key.slice(0, 70)}`));

  const secondary = list.filter(b => !b.red && b.n >= 5);
  if (!secondary.length) fail('未找到「暂存离开」按钮（非 bg-red 的 ce-btn）');
  const pick = secondary.sort((a, b) => b.n - a.n)[0];
  if (pick.red) fail('安全闸：选中了发布按钮，已中止');
  const target = { cx: Math.round((pick.x1 + pick.x2) / 2), cy: Math.round((pick.y1 + pick.y2) / 2), label: '暂存离开' };
  console.log('点击位置:', target.cx, target.cy);
  if (process.env.DRY === '1') { console.log('DRY=1 只扫描不点击'); await browser.disconnect(); return; }

  await cdp.send('Input.dispatchMouseEvent', { type: 'mouseMoved', x: target.cx, y: target.cy, button: 'none', clickCount: 0 });
  await sleep(300);
  await cdp.send('Input.dispatchMouseEvent', { type: 'mousePressed', x: target.cx, y: target.cy, button: 'left', clickCount: 1 });
  await sleep(100);
  await cdp.send('Input.dispatchMouseEvent', { type: 'mouseReleased', x: target.cx, y: target.cy, button: 'left', clickCount: 1 });
  console.log('>>> 已点击', saveText);

  // 6. 判定
  let done = false;
  for (let i = 1; i <= 14; i++) {
    await sleep(2500);
    const st = await page.evaluate(() => ({
      toast: (() => {
        const t = document.body.innerText || '';
        const m = t.match(/[^\n]*(保存成功|已保存|草稿|存入)[^\n]*/g);
        return m ? m.slice(0, 2).join(' | ').slice(0, 120) : '';
      })(),
      inEditor: !!document.querySelector('div.tiptap.ProseMirror[contenteditable="true"]'),
      url: location.href.slice(0, 70)
    }));
    if (st.toast) console.log('    提示:', st.toast);
    if (!st.inEditor) { done = true; console.log('✅ ep' + EP + ' 已离开编辑器'); break; }
  }
  if (!done) console.log('⚠️ 仍在编辑器，状态未确认');
  await page.screenshot({ path: `${SHOT}/xhs-ep${EP}-save-done.png` });
  if (!done) { await browser.disconnect(); process.exit(2); }   // 供批处理判断成败

  if (CLOSE_OTHER) {
    for (const p of pages) { if (p !== page) { try { await p.close(); console.log('关闭多余发布页'); } catch (e) {} } }
  }
  await browser.disconnect();
})().catch(e => { console.error('FATAL ep' + EP + ': ' + e.message); process.exit(1); });
