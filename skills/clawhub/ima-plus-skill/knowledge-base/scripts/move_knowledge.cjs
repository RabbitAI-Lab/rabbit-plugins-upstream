#!/usr/bin/env node
'use strict';

/**
 * 移动文件到其他知识库/文件夹（封装 openapi/wiki/v1/move_knowledge）
 * 注意：不支持文件夹的移动，只能移动文件。
 *
 * Usage:
 *   node move_knowledge.cjs --src-kb <src_kb_id> --dst-kb <dst_kb_id> --media-id <media_id>
 *   node move_knowledge.cjs --src-kb <src_kb_id> --dst-kb <dst_kb_id> --media-id id1,id2,id3 [--dst-folder <folder_id>]
 *   node move_knowledge.cjs --src-kb-name "源库" --dst-kb-name "目标库" --media-id <media_id>
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
    if (next && !next.startsWith('--')) {
      args[key] = next;
      i++;
    } else {
      args[key] = true;
    }
  }
  return args;
}

function log(step, msg) {
  console.log(`${step} ${msg}`);
}

async function call(apiPath, body) {
  const raw = await imaApi(apiPath, body);
  let json;
  try {
    json = JSON.parse(raw);
  } catch {
    throw new Error(`接口 ${apiPath} 返回非 JSON：${raw}`);
  }
  if (json.code !== 0) {
    throw new Error(`接口 ${apiPath} 失败 (code=${json.code}): ${json.msg || ''}`);
  }
  return json;
}

// 解析知识库 ID：必须显式指定（--<flag> 或 --<flag>-name）
async function resolveKbId(flag, args, label) {
  const direct = args[flag];
  if (direct) return direct;
  const nameVal = args[`${flag}-name`];
  if (nameVal) {
    const resp = await call('openapi/wiki/v1/search_knowledge_base', {
      query: nameVal,
      cursor: '',
      limit: 20,
    });
    const list = (resp.data && resp.data.info_list) || [];
    const hit =
      list.find((k) => k.kb_name === nameVal) ||
      list.find((k) => (k.kb_name || '').includes(nameVal));
    if (!hit) throw new Error(`未找到名称包含「${nameVal}」的知识库`);
    log('🔎', `按名称匹配到${label}知识库：${hit.kb_name}`);
    return hit.kb_id;
  }
  throw new Error(
    `必须显式指定${label}知识库：用 --${flag} <knowledge_base_id> 或 --${flag}-name <知识库名称> 传入。`
  );
}

async function main() {
  const args = parseArgs(process.argv);
  if (!args['media-id']) {
    console.error('[error] 缺少必需参数 --media-id <media_id>（多个用逗号分隔）');
    process.exit(1);
  }
  const mediaIds = String(args['media-id'])
    .split(',')
    .map((s) => s.trim())
    .filter(Boolean);
  if (mediaIds.length === 0) {
    console.error('[error] --media-id 为空');
    process.exit(1);
  }

  log('⏳', '定位源/目标知识库…');
  const srcKb = await resolveKbId('src-kb', args, '源');
  const dstKb = await resolveKbId('dst-kb', args, '目标');

  const body = {
    src_knowledge_base_id: srcKb,
    dst_knowledge_base_id: dstKb,
    infos: mediaIds.map((id) => ({ media_id: id })),
  };
  if (args['dst-folder']) body.dst_folder_id = args['dst-folder'];

  log('⏳', `移动 ${mediaIds.length} 个文件：${srcKb} → ${dstKb}…`);
  const resp = await call('openapi/wiki/v1/move_knowledge', body);
  const results = (resp.data && resp.data.move_results) || {};
  log('✅', '移动完成，逐文件结果：');
  console.log(JSON.stringify(results, null, 2));
}

main().catch((err) => {
  console.error(`[error] ${err.message}`);
  process.exit(1);
});
