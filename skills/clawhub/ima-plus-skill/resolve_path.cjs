#!/usr/bin/env node
'use strict';

/**
 * resolve_path.cjs — 自然语言路径解析器（ima.plus-skill 统一目录解析入口）
 *
 * 让 AI/用户用自然语言描述知识库与文件夹，脚本内部自动解析为 kb_id / folder_id，
 * 消除对长 kb_id 的记忆与幻觉依赖。
 *
 * 支持的路径格式（第一段=知识库名，后续段=文件夹逐级下钻）：
 *   --path "我的知识库"                      → 仅知识库（根目录）
 *   --path "我的知识库/项目"                  → 知识库 + 一级文件夹
 *   --path "我的知识库/项目/FAM"              → 知识库 + 多级文件夹
 *   --path "项目/FAM"（唯一库时省略库名）      → 自动匹配唯一知识库
 *   --path "FAM"（唯一库且文件夹唯一时）       → 自动匹配
 *
 * 也支持笔记笔记本：
 *   --notes --path "我的笔记本"              → 笔记本 folder_id
 *
 * Usage:
 *   node resolve_path.cjs --path "我的知识库/项目/FAM"
 *   node resolve_path.cjs --notes --path "默认笔记本"
 *   node resolve_path.cjs --kb-name "我的知识库" --folder-name "FAM"   （知识库名+单文件夹名）
 *
 * 输出：{ kb_id, folder_id, kb_name, folder_name, note_folder_id?, note_folder_name? }
 */

const path = require('node:path');
const { imaApi } = require(path.join(__dirname, 'ima_api.cjs'));

// ─── 工具函数 ───────────────────────────────────────────────────────────────
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

// ─── 知识库名 → kb_id ───────────────────────────────────────────────────────
async function resolveKbIdByName(kbName) {
  // 1) 关键词搜索（可能对新库/未索引库返回空）
  let list = [];
  try {
    const resp = await call('openapi/wiki/v1/search_knowledge_base', {
      query: kbName,
      cursor: '',
      limit: 20,
    });
    list = (resp.data && resp.data.info_list) || [];
  } catch (e) { /* 搜索失败则走全量回退 */ }
  let hit =
    list.find((k) => k.kb_name === kbName) ||
    list.find((k) => (k.kb_name || '').includes(kbName));
  // 2) 回退：空 query 拉全量再匹配（关键词搜索对新库不可靠，实测踩过）
  if (!hit) {
    const resp2 = await call('openapi/wiki/v1/search_knowledge_base', {
      query: '',
      cursor: '',
      limit: 20,
    });
    const all = (resp2.data && resp2.data.info_list) || [];
    hit =
      all.find((k) => k.kb_name === kbName) ||
      all.find((k) => (k.kb_name || '').includes(kbName));
    if (!hit) {
      const names = all.map((k) => k.kb_name).join('、');
      throw new Error(`未找到名称包含「${kbName}」的知识库。当前知识库：${names || '(无)'}`);
    }
  }
  return hit;
}

// 知识库 ID：优先 --path 第一段 / --kb / --kb-name
async function resolveKbId(args, { kbNameFromPath } = {}) {
  if (args.kb) return { kb_id: args.kb, kb_name: '(按ID指定)' };
  const name = kbNameFromPath || args['kb-name'];
  if (!name) {
    // 未指定名称：尝试唯一知识库（只有一个时自动采用）
    const resp = await call('openapi/wiki/v1/search_knowledge_base', { query: '', cursor: '', limit: 20 });
    const list = (resp.data && resp.data.info_list) || [];
    if (list.length === 1) {
      return { kb_id: list[0].kb_id, kb_name: list[0].kb_name, auto: true };
    }
    throw new Error(
      `无法确定目标知识库：请用 --path "知识库名/文件夹..." 或 --kb-name <名称> 指定。当前有 ${list.length} 个知识库。`
    );
  }
  const hit = await resolveKbIdByName(name);
  return { kb_id: hit.kb_id, kb_name: hit.kb_name };
}

// ─── 文件夹路径 → folder_id（逐级下钻） ─────────────────────────────────────
async function resolveFolderIdByPath(kbId, segments) {
  let folderId = '';
  let folderName = '';
  let parent = '';
  for (let i = 0; i < segments.length; i++) {
    const seg = String(segments[i]).trim();
    if (!seg) continue;
    const body = { knowledge_base_id: kbId, cursor: '', limit: 50 };
    if (parent) body.folder_id = parent;
    const resp = await call('openapi/wiki/v1/get_knowledge_list', body);
    const list = (resp.data && resp.data.knowledge_list) || [];
    const folders = list.filter((it) => it.media_type === 99); // 99 = 文件夹
    const hit =
      folders.find((f) => f.title === seg) ||
      folders.find((f) => (f.title || '').includes(seg));
    if (!hit) {
      const names = folders.map((f) => f.title).join('、');
      throw new Error(
        `在「${folderName || '根目录'}」下未找到文件夹「${seg}」。当前文件夹：${names || '(无)'}`
      );
    }
    folderId = hit.media_id;
    folderName = hit.title;
    parent = folderId;
  }
  return { folder_id: folderId, folder_name: folderName };
}

// ─── 完整路径解析（自然语言） ───────────────────────────────────────────────
async function resolvePathStr(pathStr, { notes = false } = {}) {
  if (notes) return resolveNotePathStr(pathStr);
  const segs = String(pathStr || '')
    .split(/[/\\]/)
    .map((s) => s.trim())
    .filter(Boolean);
  if (segs.length === 0) throw new Error('路径为空');
  // 第一段尝试当知识库名；若匹配失败，回退到唯一库自动识别（第一段视为文件夹路径）
  let kb, folderSegs;
  try {
    kb = await resolveKbId({ 'kb-name': segs[0] });
    folderSegs = segs.slice(1);
  } catch (e) {
    // 第一段不是知识库名 → 若账号唯一知识库则自动采用，全部段视为文件夹路径
    const kb2 = await resolveKbId({});
    kb = kb2;
    folderSegs = segs;
  }
  const folder = folderSegs.length
    ? await resolveFolderIdByPath(kb.kb_id, folderSegs)
    : { folder_id: '', folder_name: '' };
  return {
    kb_id: kb.kb_id,
    kb_name: kb.kb_name,
    folder_id: folder.folder_id,
    folder_name: folder.folder_name,
    auto_kb: !!kb.auto,
  };
}

// ─── 笔记本名 → 笔记本 folder_id（notes 模块） ───────────────────────────────
async function resolveNotePathStr(pathStr) {
  const name = String(pathStr || '').trim();
  if (!name) throw new Error('笔记本名称不能为空');
  const resp = await call('openapi/note/v1/list_notebook', { cursor: '0', limit: 20 });
  const list = (resp.data && resp.data.note_folder_infos) || [];
  const hit =
    list.find((n) => n.name === name || n.folder_name === name) ||
    list.find((n) => ((n.name || n.folder_name) || '').includes(name));
  if (!hit) {
    const names = list.map((n) => n.name || n.folder_name).join('、');
    throw new Error(`未找到笔记本「${name}」。当前笔记本：${names || '(无)'}`);
  }
  const hitName = hit.name || hit.folder_name;
  return { note_folder_id: hit.folder_id, note_folder_name: hitName };
}

// ─── CLI 入口 ───────────────────────────────────────────────────────────────
async function main() {
  const args = parseArgs(process.argv);
  if (!args.path && !args['kb-name']) {
    console.error('[error] 缺少参数：--path "知识库名/文件夹..." 或 --kb-name <知识库名> [--folder-name <文件夹名>]');
    process.exit(1);
  }
  let result;
  if (args.path) {
    result = await resolvePathStr(args.path, { notes: !!args.notes });
  } else {
    const { kb_id, kb_name } = await resolveKbId(args);
    let folder_id = '', folder_name = '';
    if (args['folder-name']) {
      const f = await resolveFolderIdByPath(kb_id, [args['folder-name']]);
      folder_id = f.folder_id;
      folder_name = f.folder_name;
    }
    result = { kb_id, kb_name, folder_id, folder_name };
  }
  console.log(JSON.stringify(result, null, 2));
}

// 模块导出（供其他脚本 require）
module.exports = {
  call,
  parseArgs,
  resolveKbId,
  resolveKbIdByName,
  resolveFolderIdByPath,
  resolvePathStr,
  resolveNotePathStr,
};

if (require.main === module) {
  main().catch((err) => {
    console.error(`[error] ${err.message}`);
    process.exit(1);
  });
}
