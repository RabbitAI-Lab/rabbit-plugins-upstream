#!/usr/bin/env node
'use strict';

/**
 * 批量更新知识条目的访问权限状态（封装 openapi/wiki/v1/update_knowledge_access_status）
 *
 * Usage:
 *   node update_knowledge_access_status.cjs --kb <kb_id> --media-id <media_id> --access-status 3
 *   node update_knowledge_access_status.cjs --kb <kb_id> --media-id id1,id2,id3 --access-status 2
 *
 * access_status: 1-不可查看不可导出, 2-可查看不可导出, 3-可查看可导出
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
  if (!args['media-id']) { console.error('[error] 缺少必需参数 --media-id <media_id>（多个用逗号分隔，最多10个）'); process.exit(1); }
  if (args['access-status'] === undefined) { console.error('[error] 缺少必需参数 --access-status <1|2|3>'); process.exit(1); }
  const accessStatus = Number(args['access-status']);
  if (![1, 2, 3].includes(accessStatus)) throw new Error(`--access-status 必须是 1/2/3，收到 ${args['access-status']}`);
  const mediaIds = String(args['media-id']).split(',').map((s) => s.trim()).filter(Boolean);
  if (mediaIds.length === 0) { console.error('[error] --media-id 为空'); process.exit(1); }
  if (mediaIds.length > 10) { console.error('[error] infos 最多 10 个'); process.exit(1); }
  const kbId = await resolveKbId(args);
  const body = {
    knowledge_base_id: kbId,
    infos: mediaIds.map((id) => ({ media_id: id })),
    access_status: accessStatus,
  };
  log('⏳', `更新 ${mediaIds.length} 个条目的访问状态 → ${accessStatus}…`);
  await call('openapi/wiki/v1/update_knowledge_access_status', body);
  log('✅', '访问状态更新成功');
}

main().catch((err) => { console.error(`[error] ${err.message}`); process.exit(1); });
