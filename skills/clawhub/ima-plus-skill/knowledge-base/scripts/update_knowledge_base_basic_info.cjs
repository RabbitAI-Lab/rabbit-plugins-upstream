#!/usr/bin/env node
'use strict';

/**
 * 修改知识库基本信息（封装 openapi/wiki/v1/update_knowledge_base_basic_info）
 * 按提供的字段自动推导 update_fields（1-名称 2-封面 3-简介 4-推荐问题）。
 *
 * Usage:
 *   node update_knowledge_base_basic_info.cjs --path "我的知识库" --name "新名称"
 *   node update_knowledge_base_basic_info.cjs --kb-name "我的知识库" --description "新简介" --recommended-questions "问题1,问题2"
 */

const path = require('node:path');
const { imaApi } = require(path.join(__dirname, '..', '..', 'ima_api.cjs'));
const { resolveKbId: __resKb, resolvePathStr: __resPath, withPathRetry: __withRetry } = require(path.join(__dirname, '..', '..', 'resolve_path.cjs'));

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
async function resolveKbId(args, extra) {
  // 统一解析：--path "知识库名/文件夹..." 优先；兼容 --kb / --kb-name
  if (args.path) {
    const r = await __resPath(args.path, extra || {});
    if (extra && extra.needFolder) return r;
    return r.kb_id;
  }
  const r = await __resKb(args);
  return (r && typeof r === 'object') ? (extra && extra.needFolder ? r : r.kb_id) : r;
}

async function main() {
  const args = parseArgs(process.argv);
  await __withRetry(args, async () => {
    const kbId = await resolveKbId(args);
    const body = { id: kbId, update_fields: [] };
    if (args['current-name']) body.current_name = args['current-name'];
    if (args.name) { body.update_fields.push(1); body.name = args.name; }
    if (args['cover-url']) { body.update_fields.push(2); body.cover_url = args['cover-url']; }
    if (args.description) { body.update_fields.push(3); body.description = args.description; }
    if (args['recommended-questions']) {
      body.update_fields.push(4);
      body.recommended_questions = String(args['recommended-questions']).split(',').map((s) => s.trim()).filter(Boolean);
    }
    if (args['update-fields']) {
      body.update_fields = String(args['update-fields']).split(',').map((s) => Number(s.trim())).filter((n) => [1, 2, 3, 4].includes(n));
    }
    if (!body.update_fields.length) {
      console.error('[error] 至少提供一个要更新的字段：--name / --cover-url / --description / --recommended-questions');
      process.exit(1);
    }
    log('⏳', `更新知识库 ${kbId} 字段 [${body.update_fields.join(',')}]…`);
    await call('openapi/wiki/v1/update_knowledge_base_basic_info', body);
    log('✅', '知识库信息更新成功');
  });
}

main().catch((err) => { console.error(`[error] ${err.message}`); process.exit(1); });
