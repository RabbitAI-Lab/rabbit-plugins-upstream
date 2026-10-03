#!/usr/bin/env node
/** review_semantics.mjs — 对靶核验审核台账语义：ever-approved vs latest-approved（last-write-wins） */
import fs from 'node:fs';

const p = process.argv[2] || '/root/.evomap/assets/review.jsonl';
let raw = '';
try { raw = fs.readFileSync(p, 'utf8'); } catch (e) { console.log('READ_FAIL', e.message); process.exit(1); }
const recs = raw.split('\n').map((s) => s.trim()).filter(Boolean)
	.map((s) => { try { return JSON.parse(s); } catch { return null; } }).filter(Boolean);

const ever = new Set();
const latest = new Map();
for (const r of recs) {
	if (/approv/i.test(String(r.state || ''))) ever.add(r.assetId);
	latest.set(r.assetId, r.state); // 后写覆盖前写
}
const lw = [...latest].filter(([, s]) => /approv/i.test(String(s || ''))).map(([a]) => a);
const revoked = [...ever].filter((a) => !lw.includes(a));

console.log('records               :', recs.length);
console.log('ever-approved  (旧语义):', ever.size);
console.log('latest-approved(新语义):', lw.length);
console.log('approved-then-revoked :', revoked.length);
for (const a of revoked.slice(0, 20)) console.log('  revoked:', a, '-> latest state:', latest.get(a));
