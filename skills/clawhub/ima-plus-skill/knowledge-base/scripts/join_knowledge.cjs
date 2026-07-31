#!/usr/bin/env node
'use strict';

/**
 * 加入知识库（封装 openapi/wiki/v1/join_knowledge）
 * 通常通过 search_knowledge_base_in_square 找到目标知识库 ID 后再加入。
 *
 * Usage:
 *   node join_knowledge.cjs --kb <knowledge_base_id> --name "知识库名称"
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
  if (!args.kb) { console.error('[error] 缺少必需参数 --kb <knowledge_base_id>'); process.exit(1); }
  if (!args.name) { console.error('[error] 缺少必需参数 --name <知识库名称>'); process.exit(1); }
  const body = { knowledge_base_id: args.kb, name: args.name };
  log('⏳', `加入知识库「${args.name}」(${args.kb})…`);
  await call('openapi/wiki/v1/join_knowledge', body);
  log('✅', `已加入知识库：${args.name}`);
}

main().catch((err) => { console.error(`[error] ${err.message}`); process.exit(1); });
