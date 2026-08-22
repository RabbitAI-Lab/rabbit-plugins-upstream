#!/usr/bin/env node
'use strict';

/**
 * notes_append.cjs — 追加内容到已有笔记（封装 openapi/note/v1/append_doc）
 *
 * ⚠️ 敏感操作：会不可撤销地修改用户已有笔记。调用前 AI 必须确认目标笔记明确。
 *
 *   --note-id <note_id>  必填，目标笔记 ID（用 search_note / list_note 获取）
 *   --content <markdown> 或 --file <path> 二选一（--file 优先）
 *   --format <0|1>       可选，默认 1（MARKDOWN），0=纯文本
 *
 * Usage:
 *   node notes_append.cjs --note-id <id> --content "追加的内容"
 *   node notes_append.cjs --note-id <id> --file /tmp/extra.md
 *
 * 自动处理：UTF-8 校验（非法字节直接中止）；过滤本地图片引用。
 */

const fs = require('node:fs');
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

function readContentFile(filePath) {
  const buf = fs.readFileSync(filePath);
  try {
    return new TextDecoder('utf-8', { fatal: true }).decode(buf);
  } catch {
    throw new Error(`文件 ${filePath} 不是合法 UTF-8，已中止写入（防止笔记永久乱码）`);
  }
}

function filterLocalImages(content) {
  const RE = /!\[[^\]]*\]\(([^)]+)\)/g;
  const removed = [];
  const out = content.replace(RE, (m, url) => {
    if (/^https?:\/\//i.test(url.trim())) return m;
    removed.push(url.trim());
    return '';
  });
  return { content: out, removed };
}

async function main() {
  const args = parseArgs(process.argv);
  if (!args['note-id']) { console.error('[error] 缺少必需参数 --note-id <note_id>'); process.exit(1); }
  const content = args.file ? readContentFile(args.file) : (args.content || '');
  if (!content.trim()) { console.error('[error] 缺少内容：--content <markdown> 或 --file <path>'); process.exit(1); }

  const format = args.format !== undefined ? Number(args.format) : 1;
  if (![0, 1].includes(format)) { console.error('[error] --format 只能是 0（纯文本）或 1（Markdown）'); process.exit(1); }

  const { content: clean, removed } = filterLocalImages(content);
  if (removed.length) log('⚠️', `已过滤本地图片引用（笔记接口不支持本地图片）：${removed.join('、')}`);

  const body = { note_id: args['note-id'], content_format: format, content: clean };

  if (args['dry-run']) {
    console.log('[dry-run] 请求体预览（未调用 API）：');
    console.log(JSON.stringify(body, null, 2));
    return;
  }

  log('⏳', `追加内容到笔记 ${args['note-id']}…`);
  await call('openapi/note/v1/append_doc', body);
  log('✅', `追加成功：note_id=${args['note-id']}`);
}

main().catch((err) => { console.error(`[error] ${err.message}`); process.exit(1); });
