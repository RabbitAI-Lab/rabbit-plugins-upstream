// 一次性抓：服务端笔记全量（已发布/审核中/未通过）+ 草稿箱 → nm-now.json / drafts.json
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const b = await puppeteer.connect({ browserURL: 'http://127.0.0.1:9222', protocolTimeout: 240000 });
  const all = await b.pages();
  let page = all.find(p => p.url().includes('creator.xiaohongshu.com')) || await b.newPage();
  await page.setViewport({ width: 1440, height: 900 });

  let baseHeaders = null;
  page.on('request', req => {
    if (req.url().includes('/note/user/posted') && !baseHeaders) baseHeaders = req.headers();
  });

  await page.goto('https://creator.xiaohongshu.com/new/note-manager?source=official', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await sleep(10000);

  // 1) 服务端笔记：按 tab 取（0 全部 / 1 已发布 / 2 审核中 / 3 未通过）
  const notes = await page.evaluate(async (BH) => {
    const keep = ['authorization', 'referer', 'x-s-common', 'user-agent', 'accept', 'x-b3-traceid', 'x-xray-traceid'];
    const H = {};
    for (const k of keep) if (BH[k]) H[k] = BH[k];
    const out = [];
    for (const tab of [0, 1, 2, 3]) {
      for (let p = 0; p < 8; p++) {
        const path = '/api/galaxy/v2/creator/note/user/posted?tab=' + tab + '&page=' + p;
        let sig = null;
        try { sig = window._webmsxyw(path, undefined); } catch (e) { try { sig = window._webmsxyw(path, {}); } catch (e2) {} }
        if (!sig) { out.push({ tab, page: p, err: 'nosig' }); break; }
        try {
          const r = await fetch(path, { credentials: 'include', headers: Object.assign({}, H, sig) });
          const j = await r.json();
          const list = (j && j.data && j.data.notes) || [];
          list.forEach(x => out.push({
            tab,
            // 🔴 tab=0 返回 display_title，tab=1/2/3 返回 title，两个都要兜
            title: x.title || x.display_title || '',
            time: x.time || '',
            state: x.noteState || x.state || x.status || x.permission_code || '',
            id: x.noteId || x.id || ''
          }));
          if (!list.length) break;
        } catch (e) { out.push({ tab, page: p, err: String(e).slice(0, 80) }); break; }
      }
    }
    return out;
  }, baseHeaders || {});

  const errs = notes.filter(n => n.err);
  const real = notes.filter(n => !n.err && n.title);
  console.log('服务端笔记条数:', real.length, '| 异常:', errs.length ? JSON.stringify(errs.slice(0, 3)) : '无');
  const TABNAME = { 1: '已发布', 2: '审核中', 3: '未通过' };
  real.forEach(n => console.log(`  [${TABNAME[n.tab] || n.tab}] ${n.time} | ${n.title}`));
  fs.writeFileSync('/Users/jx/Downloads/.workbuddy/macros/nm-now.json', JSON.stringify(real, null, 2));

  // 2) 草稿箱
  await page.goto('https://creator.xiaohongshu.com/publish/publish?source=official', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await sleep(7000);
  await page.evaluate(() => {
    const hit = Array.from(document.querySelectorAll('*'))
      .find(e => e.children.length === 0 && /^草稿箱\(\d+\)$/.test((e.textContent || '').trim()));
    if (hit) hit.click();
  });
  await sleep(7000);
  const drafts = await page.evaluate(() => Array.from(document.querySelectorAll('.draft-item')).map(c => {
    const t = (c.innerText || '').replace(/\s+/g, ' ').trim();
    const date = (t.match(/保存于(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})/) || [])[1] || '';
    const title = t.replace(/^\d{1,2}:\d{2}(:\d{2})?\s*/, '').replace(/\s*保存于.*$/, '').replace(/\s*(编辑|删除)\s*$/, '').trim();
    return { title, saveAt: date };
  }));
  console.log('\n草稿箱条数:', drafts.length);
  drafts.forEach((d, i) => console.log(`  ${String(i).padStart(2)} | ${d.saveAt} | ${d.title}`));
  fs.writeFileSync('/Users/jx/Downloads/.workbuddy/macros/drafts.json', JSON.stringify(drafts, null, 2));

  console.log('\n已写入 nm-now.json / drafts.json');
  await b.disconnect();
})().catch(e => { console.log('ERR', e.message.split('\n')[0]); process.exit(1); });
