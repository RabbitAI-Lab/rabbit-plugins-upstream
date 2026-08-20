#!/usr/bin/env node
'use strict';

/**
 * 在 IMA 知识库里创建文件夹（封装 openapi/wiki/v1/create_folder）
 *
 * Usage:
 *   node create_folder.cjs --path "我的知识库" --name "新文件夹"
 *   node create_folder.cjs --kb-name "我的知识库" --name "新文件夹"
 *   node create_folder.cjs --path "我的知识库/父文件夹" --name "子文件夹"
 *
 * 必须显式指定目标知识库（--kb 或 --kb-name），脚本不替用户选库。
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
    if (!args.name) {
      console.error('[error] 缺少必需参数 --name <文件夹名称>');
      process.exit(1);
    }
    const folderName = args.name;
    let parentFolderId = args.folder;

    log('⏳', '定位目标知识库…');
    // --path "知识库名/父夹路径" 时：父夹由路径解析得出
    let kbId;
    if (args.path) {
      const r = await resolveKbId(args, { needFolder: true });
      kbId = r.kb_id;
      if (r.folder_id && !parentFolderId) parentFolderId = r.folder_id;
    } else {
      kbId = await resolveKbId(args);
    }

    const body = { knowledge_base_id: kbId, name: folderName };
    if (parentFolderId) body.folder_id = parentFolderId;

    log('⏳', `在知识库 ${kbId} 创建文件夹「${folderName}」…`);
    const resp = await call('openapi/wiki/v1/create_folder', body);
    const mediaId = (resp.data && resp.data.media_id) || '';
    log('✅', `文件夹创建成功：media_id=${mediaId}（即 folder_id）`);
  });
}

main().catch((err) => {
  console.error(`[error] ${err.message}`);
  process.exit(1);
});
