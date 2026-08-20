#!/usr/bin/env node
'use strict';

/**
 * 重命名知识库中的文件或文件夹（封装 openapi/wiki/v1/rename_knowledge）
 *
 * Usage:
 *   node rename_knowledge.cjs --path "我的知识库" --media-id <media_id> --name "新名称"
 *   node rename_knowledge.cjs --kb-name "我的知识库" --media-id <media_id> --name "新名称"
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

// 解析知识库 ID：必须显式指定（--kb 或 --kb-name）
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
    if (!args['media-id']) {
      console.error('[error] 缺少必需参数 --media-id <media_id>');
      process.exit(1);
    }
    if (!args.name) {
      console.error('[error] 缺少必需参数 --name <新名称>');
      process.exit(1);
    }

    log('⏳', '定位目标知识库…');
    const kbId = await resolveKbId(args);

    const body = { knowledge_base_id: kbId, media_id: args['media-id'], name: args.name };
    log('⏳', `重命名 media_id=${args['media-id']} → 「${args.name}」…`);
    await call('openapi/wiki/v1/rename_knowledge', body);
    log('✅', `重命名成功：${args['media-id']} → ${args.name}`);
  });
}

main().catch((err) => {
  console.error(`[error] ${err.message}`);
  process.exit(1);
});
