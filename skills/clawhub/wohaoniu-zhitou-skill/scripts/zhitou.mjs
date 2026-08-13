#!/usr/bin/env node
/**
 * 我好牛AI智投 · Skill 命令行(零依赖,Node ≥18)。
 *   node scripts/zhitou.mjs geo "<品牌>" ["<品类>"]
 *   node scripts/zhitou.mjs hooks "<产品与人群描述>"
 *   node scripts/zhitou.mjs script "<素材需求>"
 *   node scripts/zhitou.mjs credits
 * 成功:stdout 输出结果;失败:stderr 输出中文原因,退出码 1。
 */
const BASE = (process.env.WOHAONIU_BASE_URL || 'https://ai.wohaoniu.com').replace(/\/$/, '');
const KEY = process.env.WOHAONIU_API_KEY || '';

const die = (msg) => {
  console.error(msg);
  process.exit(1);
};

if (!KEY) die('未配置 WOHAONIU_API_KEY —— 到 https://ai.wohaoniu.com → 个人中心 → 开放接口 生成密钥后配置到环境变量。');

async function call(path, body) {
  const res = await fetch(BASE + path, {
    method: body ? 'POST' : 'GET',
    headers: { 'content-type': 'application/json', authorization: `Bearer ${KEY}` },
    body: body ? JSON.stringify(body) : undefined,
    signal: AbortSignal.timeout(110_000),
  });
  const data = await res.json().catch(() => ({}));
  if (res.status === 401) die('API Key 无效或已吊销 —— 到 ai.wohaoniu.com 个人中心重新生成。');
  if (res.status === 402) die((data.error || '次数不足') + '\n购买:https://ai.wohaoniu.com/credits');
  if (res.status === 429) die(data.error || '调用太频繁,请稍后再试。');
  if (!res.ok || data.ok === false) die(data.error || `调用失败(HTTP ${res.status})`);
  return data;
}

const [cmd, a1, a2] = process.argv.slice(2);

if (cmd === 'geo') {
  if (!a1) die('用法:zhitou.mjs geo "<品牌名>" ["<品类>"]');
  const d = await call('/api/open/geo-check', { brand: a1, category: a2 || undefined });
  const m = d.metrics || {};
  console.log(`品牌「${d.brand}」AI 可见度(${m.model || '多模型'},共 ${m.total} 题):`);
  console.log(`  提及率 ${m.mentionRate}% · 首推率 ${m.firstRate}% · 竞品拦截率 ${m.interceptRate}% · 平均排名 ${m.avgRank ?? '—'}`);
  if (m.sentiment) console.log(`  情感:正面 ${m.sentiment.positive} / 中性 ${m.sentiment.neutral} / 负面 ${m.sentiment.negative}`);
  if (Array.isArray(m.competitorShare) && m.competitorShare.length) {
    console.log(`  竞品出现:${m.competitorShare.slice(0, 5).map((c) => `${c.name}×${c.hits}`).join('、')}`);
  }
  console.log(`完整报告:${d.reportUrl}`);
} else if (cmd === 'hooks') {
  if (!a1) die('用法:zhitou.mjs hooks "<产品与人群描述>"');
  const d = await call('/api/open/ad-hooks', { product: a1 });
  console.log(d.text);
} else if (cmd === 'script') {
  if (!a1) die('用法:zhitou.mjs script "<素材需求:产品/卖点/人群/平台>"');
  const d = await call('/api/open/ad-script', { brief: a1 });
  console.log(d.text);
} else if (cmd === 'credits') {
  const d = await call('/api/open/credits');
  console.log(`次数余额:${d.balance}(购买:${d.buyUrl})`);
} else {
  die('用法:zhitou.mjs <geo|hooks|script|credits> …');
}
