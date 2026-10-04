#!/usr/bin/env node
/** e43.mjs — A9 端到端：用 A4 产出的**真实引导草稿**（其 anti_patterns 来自 ANTI_TOKENS）
 *  与一条语义冲突的 utf-8 基因组成 storeJ，供 bash 跑 recall 验证守卫会剔除冲突者。 */
import fs from 'node:fs';
import path from 'node:path';

const RUN = process.argv[2];
const read = (p) => { try { return fs.readFileSync(p, 'utf8').split('\n').map((s) => s.trim()).filter(Boolean).map((s) => JSON.parse(s)); } catch { return []; } };
const src = read(path.join(RUN, 'storeA', 'genes.jsonl'));
if (!src.length) { console.log('E9 0 no-guided-gene'); process.exit(0); }
const g = src[0];
const mk = (id, strategy, anti = []) => ({
	type: 'Gene', schema_version: '1.13.0', id, category: 'repair',
	signals_match: ['read', 'encoding-error'], strategy: [strategy], anti_patterns: anti,
	constraints: { max_files: 12, forbidden_paths: ['.git', 'node_modules'] }, validation: [],
	summary: 'e43', generation_meta: { source: 'e43' },
	claims: [{ predicate: 'output_contract', kind: 'behavioral' }],
	scope: { signals: ['capability:read'] }, asset_id: `sha256:${id}`,
});
const dir = path.join(RUN, 'storeJ');
fs.rmSync(dir, { recursive: true, force: true });
fs.mkdirSync(dir, { recursive: true });
const genes = [
	{ ...g, id: 'gene_e2e_guided' },                                                    // 保留 A4 草稿的 anti_patterns
	mk('gene_e2e_conflict', 'FIX: just use the default utf-8 encoding, it works fine'), // 与之冲突
];
fs.writeFileSync(path.join(dir, 'genes.jsonl'), genes.map((x) => JSON.stringify(x)).join('\n') + '\n');
fs.writeFileSync(path.join(dir, 'review.jsonl'),
	genes.map((x) => JSON.stringify({ assetId: x.asset_id, state: 'approved', reason: 'e43', at: new Date().toISOString() })).join('\n') + '\n');
console.log('E9 seeded', dir, '| guided anti =', JSON.stringify(g.anti_patterns));
