#!/usr/bin/env node
'use strict';

/**
 * 修改知识库权限（封装 openapi/wiki/v1/update_knowledge_base_permission）
 * 按提供的字段自动推导 update_fields（1-导出状态 2-加入类型）。
 *
 * Usage:
 *   node update_knowledge_base_permission.cjs --kb <kb_id> --visible-export-status 3
 *   node update_knowledge_base_permission.cjs --kb-name "我的知识库" --join-type 1
 *
 * visible_export_status: 1-不可查看不可导出, 2-可查看不可导出, 3-可查看可导出
 * join_type:            1-直接加入, 2-管理员批准加入, 3-付费加入
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
  const body = { id: kbId, update_fields: [] };
  if (args.name) body.name = args.name;
  if (args['visible-export-status'] !== undefined) {
    body.update_fields.push(1);
    body.visible_export_status = Number(args['visible-export-status']);
  }
  if (args['join-type'] !== undefined) {
    body.update_fields.push(2);
    body.join_type = Number(args['join-type']);
  }
  if (args['update-fields']) {
    body.update_fields = String(args['update-fields']).split(',').map((s) => Number(s.trim())).filter((n) => [1, 2].includes(n));
  }
  if (!body.update_fields.length) {
    console.error('[error] 至少提供一个要更新的权限字段：--visible-export-status / --join-type');
    process.exit(1);
  }
  log('⏳', `更新知识库 ${kbId} 权限字段 [${body.update_fields.join(',')}]…`);
  await call('openapi/wiki/v1/update_knowledge_base_permission', body);
  log('✅', '知识库权限更新成功');
}

main().catch((err) => { console.error(`[error] ${err.message}`); process.exit(1); });
