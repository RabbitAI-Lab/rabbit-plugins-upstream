#!/usr/bin/env node
/**
 * anti_analysis.mjs — P1⑤ 冲突守卫：匹配器方案的量化对比（只读分析）
 *
 * 用法：node anti_analysis.mjs <store_dir>
 *
 * 对「可召回基因集」（approved(LWW) ∩ 修法守卫 ∩ 非叙述）做两两检查，
 * 分别统计 4 种匹配器各能检出多少冲突对，用于回答"是否收紧"。
 *
 * 注：REPAIR_SIGNAL_RE / NARRATION_RE 与 evolver-recall.mjs 逐字一致（此处为分析镜像，
 *     仅用于确定候选集；不参与任何生产逻辑）。
 */
import fs from 'node:fs';
import path from 'node:path';

const store = process.argv[2];
if (!store) { console.error('用法: node anti_analysis.mjs <store_dir>'); process.exit(2); }
const readJsonl = (p) => {
	const out = [];
	let raw = '';
	try { raw = fs.readFileSync(p, 'utf8'); } catch { return out; }
	for (const line of raw.split('\n')) {
		const s = line.trim(); if (!s) continue;
		try { out.push(JSON.parse(s)); } catch { /* 坏行跳过 */ }
	}
	return out;
};

const REPAIR_SIGNAL_RE = /error|exception|traceback|failed|invalid|cannot|unable|missing|not found|wrong|instead|avoid|fix|encoding\s*[=:]|errors\s*=|utf-?8|gbk|gb18030|latin-1|\brb\b|except|skip/i;
const NARRATION_RE = /^\s*(now i (understand|see|have|know|remember|need|can)|let me\b|i'?(ll|ve|m)\b|i will\b|here'?s\b|done[.!\u2026]|confirmed[:.]|the output matches|to summarize|summarize\b|first,? i\b|next,? i\b|alright\b|okay\b)/i;

const genes = readJsonl(path.join(store, 'genes.jsonl'));
const review = readJsonl(path.join(store, 'review.jsonl'));
const latest = new Map();
for (const r of review) if (r && r.assetId) latest.set(String(r.assetId).replace(/^"|"$/g, ''), r.state);
const approved = new Set([...latest].filter(([, s]) => typeof s === 'string' && s.toLowerCase().includes('approv')).map(([a]) => a));

const toks = (s) => new Set(String(s || '').toLowerCase().match(/[a-z0-9_.-]+/g) || []);
const norm = (s) => String(s || '').replace(/\s+/g, ' ').trim().toLowerCase();
// 简单停用词（仅分析用；与 recall 的 STOP_WORDS 同源子集）
const STOP = new Set(['the', 'and', 'for', 'with', 'that', 'this', 'from', 'not', 'are', 'use', 'using', 'default', 'file', 'files', 'error', 'a', 'an', 'of', 'to', 'in', 'on', 'it', 'is', 'be']);

const recallable = genes.filter((g) => {
	const st = Array.isArray(g.strategy) ? g.strategy : null;
	if (!st || !st.length) return false;
	if (!g.asset_id || !approved.has(g.asset_id)) return false;
	const text = st.join(' ').replace(/\s+/g, ' ').trim();
	if (!REPAIR_SIGNAL_RE.test(text)) return false;
	if (NARRATION_RE.test(String(st[0] ?? '').trim())) return false;
	g.__text = text;
	return true;
});

console.log('store                     :', store);
console.log('genes total               :', genes.length);
console.log('approved (LWW)            :', approved.size);
console.log('recallable (approved∩guard):', recallable.length);
const withAnti = recallable.filter((g) => Array.isArray(g.anti_patterns) && g.anti_patterns.length);
console.log('recallable w/ anti_patterns:', withAnti.length);

const distinct = new Map();
for (const g of recallable) for (const a of (g.anti_patterns || [])) distinct.set(a, (distinct.get(a) || 0) + 1);
console.log('distinct anti_patterns    :', distinct.size);
for (const [a, c] of [...distinct].sort((x, y) => y[1] - x[1])) {
	console.log(`   [${c}] ${JSON.stringify(a)}  → tokens=${[...toks(a)].join('|')}`);
}

// ── 四种匹配器 ──
// M0 现行：anti_pattern 整串 ∈ 对方 token 集（单 token 才可能命中）
const M0 = (a, b) => (a.anti_patterns || []).some((ap) => toks(b.__text).has(String(ap).toLowerCase()))
	|| (b.anti_patterns || []).some((bp) => toks(a.__text).has(String(bp).toLowerCase()));
// M1 子串：归一化文本包含归一化 anti_pattern（顺序必须一致）
const M1 = (a, b) => (a.anti_patterns || []).some((ap) => norm(b.__text).includes(norm(ap)))
	|| (b.anti_patterns || []).some((bp) => norm(a.__text).includes(norm(bp)));
// M2 全 token 子集（≥2 有效 token 全在对方文本中）
const contentToks = (s) => [...toks(s)].filter((t) => !STOP.has(t) && t.length >= 3);
const M2 = (a, b) => {
	const bT = new Set(contentToks(b.__text)), aT = new Set(contentToks(a.__text));
	for (const ap of (a.anti_patterns || [])) { const t = contentToks(ap); if (t.length >= 2 && t.every((x) => bT.has(x))) return true; }
	for (const bp of (b.anti_patterns || [])) { const t = contentToks(bp); if (t.length >= 2 && t.every((x) => aT.has(x))) return true; }
	return false;
};
// M3 部分重叠（≥2 有效 token 重叠）
const M3 = (a, b) => {
	const bT = new Set(contentToks(b.__text)), aT = new Set(contentToks(a.__text));
	const ov = (ap, T) => contentToks(ap).filter((x) => T.has(x)).length;
	for (const ap of (a.anti_patterns || [])) if (ov(ap, bT) >= 2) return true;
	for (const bp of (b.anti_patterns || [])) if (ov(bp, aT) >= 2) return true;
	return false;
};

const pairs = [];
for (let i = 0; i < recallable.length; i++) for (let j = i + 1; j < recallable.length; j++) pairs.push([recallable[i], recallable[j]]);
const hits = { M0: [], M1: [], M2: [], M3: [] };
for (const [a, b] of pairs) for (const k of ['M0', 'M1', 'M2', 'M3']) if ({ M0, M1, M2, M3 }[k](a, b)) hits[k].push([a, b]);

console.log('\n候选对总数                :', pairs.length);
console.log('M0 现行(整串∈token集)     :', hits.M0.length);
console.log('M1 子串(顺序一致)         :', hits.M1.length);
console.log('M2 全token子集(≥2)        :', hits.M2.length);
console.log('M3 部分重叠(≥2)           :', hits.M3.length);
for (const k of ['M0', 'M1', 'M2', 'M3']) {
	for (const [a, b] of hits[k].slice(0, 8)) {
		console.log(`  ${k}: ${a.id} (anti=${JSON.stringify(a.anti_patterns)}) ↔ ${b.id}`);
	}
}
