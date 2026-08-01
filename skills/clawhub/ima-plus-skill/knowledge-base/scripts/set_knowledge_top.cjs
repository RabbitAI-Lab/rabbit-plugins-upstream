#!/usr/bin/env node
'use strict';

/**
 * 置顶 / 取消置顶知识库内的内容（封装 openapi/wiki/v1/set_knowledge_top）
 * 注意：不适用于名称为"某某的知识库"的个人知识库。
 *
 * Usage:
 *   node set_knowledge_top.cjs --kb <kb_id> --media-id <media_id> --is-top true
 *   node set_knowledge_top.cjs --kb-name "我的知识库" --media-id <media_id> --is-top false
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
  if (!args['media-id']) { console.error('[error] 缺少必需参数 --media-id <media_id>'); process.exit(1); }
  if (args['is-top'] === undefined) { console.error('[error] 缺少必需参数 --is-top <true|false>'); process.exit(1); }
  const isTop = args['is-top'] === 'true' || args['is-top'] === '1';
  const kbId = await resolveKbId(args);
  const body = { knowledge_base_id: kbId, media_id: args['media-id'], is_top: isTop };
  log('⏳', `设置置顶 media_id=${args['media-id']} → is_top=${isTop}…`);
  await call('openapi/wiki/v1/set_knowledge_top', body);
  log('✅', `置顶状态已更新：${isTop ? '已置顶' : '已取消置顶'}`);
}

main().catch((err) => { console.error(`[error] ${err.message}`); process.exit(1); });
