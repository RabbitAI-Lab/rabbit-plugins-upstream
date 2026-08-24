#!/usr/bin/env node
'use strict';

/**
 * 递归列举知识库全部文件目录（含任意层级子文件夹）
 *
 * 用于「打包导出」「全量盘点」「批量处理」等需要先拿到完整文件清单的场景。
 * 输出全部条目的目录树：文件夹(media_type=99) 与 文件(非99)，含路径 / media_id / media_type。
 *
 * 用法:
 *   node list_all_files.cjs --path "我的知识库"
 *   node list_all_files.cjs --kb-name "谈水君的知识库"
 *   node list_all_files.cjs --path "我的知识库" --json
 *   node list_all_files.cjs --path "我的知识库" --with-url      # 额外逐个 get_media_info 获取下载链接(较慢)
 */

const fs = require('node:fs');
const path = require('node:path');
const { imaApi } = require(path.join(__dirname, '..', '..', 'ima_api.cjs'));
const { resolveKbId: __resKb, resolvePathStr: __resPath, withPathRetry: __withRetry } = require(path.join(__dirname, '..', '..', 'resolve_path.cjs'));

const MEDIA_TYPE_NAME = {
  1: 'PDF', 2: '网页', 3: 'Word', 4: 'PPT', 5: 'Excel', 6: '公众号',
  7: 'Markdown', 9: '图片', 11: '笔记', 12: 'QA', 13: 'TXT', 14: 'Xmind',
  15: '录音', 16: '网页视频', 17: '对话', 18: '视频', 19: '播客', 20: 'HTML', 99: '文件夹',
};

function parseArgs(argv) {
  const args = {};
  for (let i = 2; i < argv.length; i++) {
    const tok = argv[i];
    if (!tok.startsWith('--')) continue;
    const key = tok.replace(/^--/, '');
    const next = argv[i + 1];
    if (next && !next.startsWith('--')) { args[key] = next; i++; }
    else args[key] = true;
  }
  return args;
}

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

async function listFolder(kbId, folderId, prefix, out, withUrl, depth) {
  if (depth > 20) return;
  let cursor = '';
  let page = 0;
  do {
    const body = { knowledge_base_id: kbId, cursor, limit: 50 };
    if (folderId) body.folder_id = folderId;
    const resp = await call('openapi/wiki/v1/get_knowledge_list', body);
    const items = (resp.data && resp.data.knowledge_list) || [];
    for (const it of items) {
      const p = prefix ? prefix + '/' + it.title : it.title;
      if (it.media_type === 99) {
        out.push({ type: 'folder', title: it.title, media_id: it.media_id, media_type: 99, path: p });
        await listFolder(kbId, it.media_id, p, out, withUrl, depth + 1);
      } else {
        const entry = { type: 'file', title: it.title, media_id: it.media_id, media_type: it.media_type, path: p };
        if (withUrl) {
          try {
            const mi = await call('openapi/wiki/v1/get_media_info', { media_id: it.media_id });
            const ui = (mi.data && mi.data.url_info) || {};
            entry.url = ui.url || '';
            if (!ui.url) entry.url_error = mi.msg || 'no url';
          } catch (e) { entry.url_error = e.message; }
        }
        out.push(entry);
      }
    }
    cursor = (resp.data && resp.data.next_cursor) || '';
    if (resp.data && resp.data.is_end) break;
    if (++page > 50) break; // 单目录上限 2500 条
  } while (cursor);
}

function printTree(out) {
  for (const it of out) {
    const tag = it.type === 'folder' ? '📁' : '📄';
    const mt = MEDIA_TYPE_NAME[it.media_type] || ('type' + it.media_type);
    console.log(`${tag} [${mt}] ${it.path}  (${it.media_id})`);
  }
}

async function main() {
  const args = parseArgs(process.argv);
  await __withRetry(args, async () => {
    const kbId = await resolveKbId(args);
    const out = [];
    await listFolder(kbId, null, '', out, !!args['with-url'], 0);
    const files = out.filter(x => x.type === 'file');
    const folders = out.filter(x => x.type === 'folder');
    if (args.json) {
      console.log(JSON.stringify(out, null, 2));
    } else {
      printTree(out);
      console.log(`\n=== 统计：文件夹 ${folders.length} 个，文件 ${files.length} 个 ===`);
    }
  });
}

main().catch((err) => { console.error(`[error] ${err.message}`); process.exit(1); });
