#!/usr/bin/env node
'use strict';

/**
 * 列出 / 搜索知识库中的标签（封装 openapi/wiki/v1/tag_list）
 *
 * Usage:
 *   node tag_list.cjs --kb <kb_id>
 *   node tag_list.cjs --kb-name "我的知识库" --keyword "重要" --limit 50
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
async function resolveKbId(args) {
  if (args.kb) return args.kb;
  if (args['kb-name']) {
    const resp = await call('openapi/wiki/v1/search_knowledge_base', { query: args['kb-name'], cursor: '', limit: 20 });
    const list = (resp.data && resp.data.info_list) || [];
    const hit = list.find((k) => k.kb_name === args['kb-name']) || list.find((k) => (k.kb_name || '').includes(args['kb-name']));
    if (!hit) throw new Error(`未找到名称包含「${args['kb-name']}」的知识库`);
    log('🔎', `按名称匹配到知识库：${hit.kb_name}`);
    return hit.kb_id;
  }
  throw new Error('必须显式指定目标知识库：用 --kb <knowledge_base_id> 或 --kb-name <知识库名称> 传入。');
}

async function main() {
  const args = parseArgs(process.argv);
  const kbId = await resolveKbId(args);
  const body = { knowledge_base_id: kbId, cursor: args.cursor || '', limit: Number(args.limit) || 50 };
  if (args.keyword) body.keyword = args.keyword;

  log('⏳', `列出知识库 ${kbId} 的标签…`);
  const resp = await call('openapi/wiki/v1/tag_list', body);
  const data = resp.data || {};
  const items = data.items || [];
  log('✅', `共 ${items.length} 个标签：`);
  for (const it of items) console.log(`  - ${it.tag_name}`);
  if (data.next_cursor) log('➡️', `还有更多，翻页用 --cursor ${data.next_cursor}`);
}

main().catch((err) => { console.error(`[error] ${err.message}`); process.exit(1); });
