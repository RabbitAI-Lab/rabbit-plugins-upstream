#!/usr/bin/env node
/**
 * seed43.mjs — 为 #43 受控验证播种全部隔离测试库（仅 fs 写，不 spawn 子进程）。
 * 沙箱约束：node→node 子进程 EBUSY，故所有 CLI 调用改由 bash 顶层驱动（见 val43.sh）。
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const RUN = path.join(HERE, 'run43');

const reset = (d) => { fs.rmSync(d, { recursive: true, force: true }); fs.mkdirSync(d, { recursive: true }); };
const writeJsonl = (p, a) => { fs.mkdirSync(path.dirname(p), { recursive: true }); fs.writeFileSync(p, a.map((o) => JSON.stringify(o)).join('\n') + '\n'); };
const mk = ({ id, signals, strategy, anti = [], category = 'repair' }) => ({
	type: 'Gene', schema_version: '1.13.0', id, category,
	signals_match: signals,
	strategy: Array.isArray(strategy) ? strategy : [strategy],
	anti_patterns: anti,
	constraints: { max_files: 12, forbidden_paths: ['.git', 'node_modules'] },
	validation: [], summary: 'val43 test gene',
	generation_meta: { source: 'val43' },
	claims: [{ predicate: 'output_contract', kind: 'behavioral' }],
	scope: { signals: signals.map((s) => `capability:${s}`) },
	asset_id: `sha256:${id}`,
});
const seed = (dir, genes, approve = true) => {
	reset(dir);
	writeJsonl(path.join(dir, 'genes.jsonl'), genes);
	writeJsonl(path.join(dir, 'review.jsonl'), genes.map((g) => ({
		assetId: g.asset_id, state: approve ? 'approved' : 'quarantined', reason: 'val43', at: new Date().toISOString(),
	})));
};

reset(RUN);

// B：GBK / JSON / 不对靶
seed(path.join(RUN, 'storeB'), [
	mk({ id: 'gene_test_gbk', signals: ['read', 'encoding-error'], strategy: "FIX: read the file with encoding='gbk' to avoid UnicodeDecodeError" }),
	mk({ id: 'gene_test_json', signals: ['read', 'invalid-json'], strategy: 'FIX: parse each line with json.loads and skip malformed lines' }),
	mk({ id: 'gene_test_file', signals: ['file-not-found'], strategy: 'FIX: list the directory before assuming a path exists' }),
]);
reset(path.join(RUN, 'hitsB'));          // 空命中库 = scale-0

// C：负载均衡偏置（等分基因；strategy 须含修法信号词，否则被召回守卫整体过滤）
seed(path.join(RUN, 'storeC'), [
	mk({ id: 'gene_test_hot', signals: ['alpha'], strategy: 'FIX: use alpha method' }),
	mk({ id: 'gene_test_cold', signals: ['bravo'], strategy: 'FIX: use bravo method' }),
]);
reset(path.join(RUN, 'hitsC0'));
reset(path.join(RUN, 'hitsC1'));
writeJsonl(path.join(RUN, 'hitsC1', 'hits.jsonl'),
	Array.from({ length: 10 }, () => ({ ts: new Date().toISOString(), gene_id: 'gene_test_hot', asset_id: 'sha256:gene_test_hot' })));

// D/E：真冲突 / 单基因
// anti_patterns 用**单个 token**（'utf-8'）——这是 geneConflicts 的实际触发面：
// 它做的是「anti_pattern 整串 ∈ 对方 token 集」的成员判断，多词短语/连字符标签不会命中。
const geneP = mk({ id: 'gene_test_conf_p', signals: ['read', 'encoding-error'], strategy: "FIX: read the file with encoding='gbk'", anti: ['utf-8'] });
seed(path.join(RUN, 'storeD'), [
	geneP,
	mk({ id: 'gene_test_conf_q', signals: ['read', 'invalid-json'], strategy: 'FIX: just use the default utf-8 encoding, it works fine' }),
]);
seed(path.join(RUN, 'storeE'), [geneP]);
reset(path.join(RUN, 'hitsD'));

// F：复合 token anti_patterns（保守不误判）
seed(path.join(RUN, 'storeF'), [
	mk({ id: 'gene_test_blind_p', signals: ['read', 'encoding-error'], strategy: "FIX: read with encoding='gbk'", anti: ['assume-default-utf8'] }),
	mk({ id: 'gene_test_blind_q', signals: ['read', 'invalid-json'], strategy: 'FIX: just use the default utf-8 encoding, it works fine' }),
]);

// G/H：质量守卫 / 审核门
seed(path.join(RUN, 'storeG'), [
	mk({ id: 'gene_test_narr', signals: ['read', 'encoding-error'], strategy: 'Now I understand the context, let me read the file with gbk encoding and report the total' }),
]);
seed(path.join(RUN, 'storeH'), [
	mk({ id: 'gene_test_gbk', signals: ['read', 'encoding-error'], strategy: "FIX: read the file with encoding='gbk' to avoid UnicodeDecodeError" }),
], false); // quarantined

// I：审核语义（last-write-wins）——approved 后被 quarantine 的资产不得再视为可注入
reset(path.join(RUN, 'storeI'));
writeJsonl(path.join(RUN, 'storeI', 'genes.jsonl'), [
	mk({ id: 'gene_test_kept', signals: ['read', 'encoding-error'], strategy: "FIX: read with encoding='gbk'" }),
	mk({ id: 'gene_test_revoked', signals: ['read', 'invalid-json'], strategy: 'FIX: skip malformed json lines' }),
]);
writeJsonl(path.join(RUN, 'storeI', 'review.jsonl'), [
	{ assetId: 'sha256:gene_test_kept', state: 'approved', reason: 'val43', at: new Date().toISOString() },
	{ assetId: 'sha256:gene_test_revoked', state: 'approved', reason: 'val43', at: new Date().toISOString() },
	{ assetId: 'sha256:gene_test_revoked', state: 'quarantined', reason: 'val43 revoked', at: new Date().toISOString() },
]);

// A：引导式沉淀（CLI 自行建库）
reset(path.join(RUN, 'storeA'));
reset(path.join(RUN, 'storeA2'));

console.log('seeded ->', RUN);
