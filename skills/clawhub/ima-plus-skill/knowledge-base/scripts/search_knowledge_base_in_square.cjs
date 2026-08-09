#!/usr/bin/env node
'use strict';

/**
 * 在知识库广场发现/搜索公开知识库（封装 openapi/wiki/v1/search_knowledge_base_in_square）
 * 用于加入知识库前定位目标（返回 kb_id + 名称）。
 *
 * Usage:
 *   node search_knowledge_base_in_square.cjs --question "Python 教程"
 *   node search_knowledge_base_in_square.cjs --question "AI" --limit 20 --cursor "<next_cursor>"
 */

const path = require('node:path');
const { imaApi } = require(path.join(__dirname, '..', '..', 'ima_api.cjs'));

function parseArgs(argv) {
  const args = {};
  for (let i = 2; i < argv.length; i++) {
    const tok = argv[i];
    if (!tok.startsWith('--')) continue;
    const key = tok.replace(/^--/, '');
    const next = argv[i + 1];
    if (next && !next.startsWith('--')) { args[key] = next; i++; }
    else { args[key] = true; }
  }
  return args;
}
function log(step, msg) { console.log(`${step} ${msg}`); }
async function call(apiPath, body) {
  const raw = await imaApi(apiPath, body);
  let json;
  try { json = JSON.parse(raw); } catch { throw new Error(`接口 ${apiPath} 返回非 JSON：${raw}`); }
  if (json.code !== 0) throw new Error(`接口 ${apiPath} 失败 (code=${json.code}): ${json.msg || ''}`);
  return json;
}

async function main() {
  const args = parseArgs(process.argv);
  if (!args.question) { console.error('[error] 缺少必需参数 --question <搜索关键词>'); process.exit(1); }
  const body = {
    question: args.question,
    cursor: args.cursor || '',
    limit: Number(args.limit) || 20,
  };
  log('⏳', `在广场搜索「${args.question}」…`);
  const resp = await call('openapi/wiki/v1/search_knowledge_base_in_square', body);
  const data = resp.data || {};
  const items = data.items || [];
  log('✅', `找到 ${items.length} 个公开知识库：`);
  for (const it of items) {
    console.log(`  📚 ${it.kb_name}  (id=${it.kb_id}, 成员=${it.member_count}, 内容=${it.content_count}, 创建者=${it.creator})`);
  }
  if (data.next_cursor) log('➡️', `还有更多，翻页用 --cursor ${data.next_cursor}`);
  else log('➡️', '已到末尾');
}

main().catch((err) => { console.error(`[error] ${err.message}`); process.exit(1); });
