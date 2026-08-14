#!/usr/bin/env node
'use strict';

/**
 * 在 IMA 知识库里创建文件夹（封装 openapi/wiki/v1/create_folder）
 *
 * Usage:
 *   node create_folder.cjs --kb <knowledge_base_id> --name "新文件夹"
 *   node create_folder.cjs --kb-name "我的知识库" --name "新文件夹"
 *   node create_folder.cjs --kb <kb_id> --name "子文件夹" --folder <parent_folder_id>
 *
 * 必须显式指定目标知识库（--kb 或 --kb-name），脚本不替用户选库。
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

// 解析知识库 ID：必须显式指定（--kb 或 --kb-name）
async function resolveKbId(args) {
  if (args.kb) return args.kb;
  if (args['kb-name']) {
    const resp = await call('openapi/wiki/v1/search_knowledge_base', {
      query: args['kb-name'],
      cursor: '',
      limit: 20,
    });
    const list = (resp.data && resp.data.info_list) || [];
    const hit =
      list.find((k) => k.kb_name === args['kb-name']) ||
      list.find((k) => (k.kb_name || '').includes(args['kb-name']));
    if (!hit) throw new Error(`未找到名称包含「${args['kb-name']}」的知识库`);
    log('🔎', `按名称匹配到知识库：${hit.kb_name}`);
    return hit.kb_id;
  }
  throw new Error(
    '必须显式指定目标知识库：用 --kb <knowledge_base_id> 或 --kb-name <知识库名称> 传入。'
  );
}

async function main() {
  const args = parseArgs(process.argv);
  if (!args.name) {
    console.error('[error] 缺少必需参数 --name <文件夹名称>');
    process.exit(1);
  }
  const folderName = args.name;
  const parentFolderId = args.folder;

  log('⏳', '定位目标知识库…');
  const kbId = await resolveKbId(args);

  const body = { knowledge_base_id: kbId, name: folderName };
  if (parentFolderId) body.folder_id = parentFolderId;

  log('⏳', `在知识库 ${kbId} 创建文件夹「${folderName}」…`);
  const resp = await call('openapi/wiki/v1/create_folder', body);
  const mediaId = (resp.data && resp.data.media_id) || '';
  log('✅', `文件夹创建成功：media_id=${mediaId}（即 folder_id）`);
}

main().catch((err) => {
  console.error(`[error] ${err.message}`);
  process.exit(1);
});
