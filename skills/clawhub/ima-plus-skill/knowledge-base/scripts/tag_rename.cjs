#!/usr/bin/env node
'use strict';

/**
 * 重命名标签（封装 openapi/wiki/v1/tag_rename）；所有打了旧标签的文件自动迁移到新名。
 * ⚠️ 若新名已存在会自动合并（旧标签关联并入新标签并删除旧标签），调用前应确认。
 *
 * Usage:
 *   node tag_rename.cjs --kb <kb_id> --old-tag-name "旧名" --new-tag-name "新名"
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
  if (!args['old-tag-name']) { console.error('[error] 缺少必需参数 --old-tag-name <旧标签名>'); process.exit(1); }
  if (!args['new-tag-name']) { console.error('[error] 缺少必需参数 --new-tag-name <新标签名>'); process.exit(1); }
  const kbId = await resolveKbId(args);
  const body = { knowledge_base_id: kbId, old_tag_name: args['old-tag-name'], new_tag_name: args['new-tag-name'] };
  log('⏳', `重命名标签「${args['old-tag-name']}」→「${args['new-tag-name']}」…`);
  await call('openapi/wiki/v1/tag_rename', body);
  log('✅', `标签已重命名（若新名已存在则自动合并）`);
}

main().catch((err) => { console.error(`[error] ${err.message}`); process.exit(1); });
