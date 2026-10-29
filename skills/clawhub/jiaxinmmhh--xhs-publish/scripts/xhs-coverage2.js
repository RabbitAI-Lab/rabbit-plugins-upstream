// 覆盖矩阵：本地各系列文案 vs 服务端已发布 vs 草稿箱
// 用法: node xhs-coverage2.js
const fs = require('fs');
const D = '/Users/jx/Downloads';

const HEAD = '(?:##\\s*标题|【标题】)';
function titleOf(dir) {
  const f = `${D}/${dir}/xhs-copy.txt`;
  if (!fs.existsSync(f)) return null;
  const t = fs.readFileSync(f, 'utf8');
  return ((t.match(new RegExp(HEAD + '\\s*\\n(.+)')) || [])[1] || '').trim();
}
// 归一化：去空白 + 去标点 + 全角转半角
const norm = s => (s || '').replace(/[\s\u3000]/g, '')
  .replace(/[，。！？、：；“”「」（）()【】《》,.!?:;"'_-]/g, '');
// 模糊匹配：包含关系 或 前 8 字相同
function match(a, b) {
  const x = norm(a), y = norm(b);
  if (!x || !y) return false;
  if (x === y) return true;
  if (x.includes(y) || y.includes(x)) return true;
  return x.slice(0, 8) === y.slice(0, 8);
}

const nm = JSON.parse(fs.readFileSync('/Users/jx/Downloads/.workbuddy/macros/nm-now.json', 'utf8'));
const drafts = JSON.parse(fs.readFileSync('/Users/jx/Downloads/.workbuddy/macros/drafts.json', 'utf8'));
const published = nm.filter(n => n.tab === 1);
const failed = nm.filter(n => n.tab === 3);
const reviewing = nm.filter(n => n.tab === 2);

const series = [
  { key: 'xip', label: 'xip（怎么活得更好 / 系列二?）', n: 30 },
  { key: 'xip3', label: 'xip3（怎么赚得更聪明 / 系列三）', n: 15 }
];

const report = {};
for (const s of series) {
  const rows = [];
  for (let i = 1; i <= s.n; i++) {
    const ep = String(i).padStart(2, '0');
    const dir = `${s.key}-ep${ep}`;
    const t = titleOf(dir);
    if (!t) { rows.push({ ep, title: '(无文案)', status: 'NOSRC' }); continue; }
    let status = 'MISSING';
    if (published.find(p => match(p.title, t))) status = 'PUBLISHED';
    else if (drafts.find(d => match(d.title, t))) status = 'DRAFT';
    else if (failed.find(p => match(p.title, t))) status = 'FAILED';
    else if (reviewing.find(p => match(p.title, t))) status = 'REVIEWING';
    rows.push({ ep, title: t, status });
  }
  report[s.key] = { label: s.label, rows };
}

const LABEL = { PUBLISHED: '已发布', DRAFT: '草稿箱', FAILED: '未通过', REVIEWING: '审核中', MISSING: '❌两头都没有', NOSRC: '⚠️缺文案' };
for (const s of series) {
  const r = report[s.key];
  const c = {};
  r.rows.forEach(x => c[x.status] = (c[x.status] || 0) + 1);
  console.log(`\n===== ${r.label} =====`);
  console.log('已发布', c.PUBLISHED || 0, '| 草稿', c.DRAFT || 0, '| 未通过', c.FAILED || 0, '| 审核中', c.REVIEWING || 0, '| 缺失', c.MISSING || 0, '| 无文案', c.NOSRC || 0);
  r.rows.forEach(x => console.log(`  ep${x.ep} [${LABEL[x.status]}] ${x.title}`));
  const miss = r.rows.filter(x => x.status === 'MISSING');
  if (miss.length) {
    console.log('  --- 需要补发到草稿箱 ---');
    miss.forEach(x => console.log(`     ${s.key} ep${x.ep} | ${x.title}`));
  }
}
// 检查视频是否齐全
console.log('\n===== 缺失条目视频检查 =====');
for (const s of series) {
  report[s.key].rows.filter(x => x.status === 'MISSING').forEach(x => {
    const v = `${D}/${s.key}-ep${x.ep}/output.mp4`;
    console.log(`  ${s.key}-ep${x.ep}: ${fs.existsSync(v) ? '✅ 有视频 ' + Math.round(fs.statSync(v).size / 1048576) + 'MB' : '❌ 无 output.mp4'}`);
  });
}
fs.writeFileSync('/Users/jx/Downloads/.workbuddy/macros/coverage2.json', JSON.stringify(report, null, 2));
console.log('\n已写入 coverage2.json');
