#!/usr/bin/env node
'use strict';

/**
 * 知识库打包导出为 zip（IMA.plus 知识库模块附属功能）
 *
 * 支持三种范围：
 *   1. 整个知识库：            --kb <kb_id>  |  --kb-name <知识库名称>
 *   2. 指定文件夹（递归子内容）： 在上述基础上 + --folder-id <folder_id>
 *   3. 指定多个文件：           + --media-ids <id1,id2,id3>
 *
 * 行为：
 *   - 递归收集文件清单，按知识库原始目录结构落盘（保留文件夹层级）
 *   - 同名文件自动加序号（_1 / _2 …）避免互相覆盖
 *   - 逐个调用 export_media_for_ima_sandbox 导出并带 headers 下载
 *   - 全部下载完成后整体打包成 zip（UTF-8 文件名）
 *   - 导出失败的文件如实报告，不影响其余文件；全部失败则不生成 zip
 *
 * 凭证优先级（与 ima_api.cjs 保持一致）：
 *   config.json（clientId/apiKey）  >  env IMA_OPENAPI_CLIENTID/APIKEY / IMA_CLIENT_ID/API_KEY  >  ~/.config/ima
 *   凭证获取：在 ima app 的 copilot 对话索要环境变量 IMA_OPENAPI_CLIENTID/APIKEY 的凭证，
 *        写入 ~/.config/ima/ 或技能目录 config.json 即可开箱即用（完整 SOP 见 SKILL.md「Credential Check」）。
 *   注意：个人在 agent-interface 申请的 key 未开通导出权限（导出报 220030），
 *        ima.copilot 环境可能重置技能目录 config.json（凭证被清），建议凭证放 ~/.config/ima/。
 *
 * Usage:
 *   node export_kb_zip.cjs --kb-name "我的知识库"
 *   node export_kb_zip.cjs --kb <kb_id> --folder-id folder_xxx
 *   node export_kb_zip.cjs --kb <kb_id> --media-ids id1,id2
 *   node export_kb_zip.cjs --kb-name "我的知识库" --dry-run        # 只列清单不下载
 *   node export_kb_zip.cjs --kb-name "我的知识库" --out /path/x.zip --keep
 */

const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const zlib = require('node:zlib');

const BASE = 'https://ima.qq.com';
const CONFIG_FILE = path.join(__dirname, '..', '..', 'config.json');

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

function readFileSafe(p) {
  try { return fs.readFileSync(p, 'utf8').trim(); } catch { return ''; }
}

// ─── 纯 Node zip 打包（跨平台，不依赖系统 zip 命令）───────────────
// Windows 没有 zip 命令；PowerShell Compress-Archive 对中文/UTF-8 文件名支持差。
// 此处用 zlib deflate + 手写 zip 结构（Local File Header + Central Directory + EOCD），
// 文件名 UTF-8 编码 + UTF-8 flag，Windows / Linux / macOS 行为完全一致。
const CRC_TABLE = (() => {
  const t = new Uint32Array(256);
  for (let n = 0; n < 256; n++) {
    let c = n;
    for (let k = 0; k < 8; k++) c = (c & 1) ? (0xedb88320 ^ (c >>> 1)) : (c >>> 1);
    t[n] = c >>> 0;
  }
  return t;
})();

function crc32(buf) {
  let c = 0xffffffff;
  for (let i = 0; i < buf.length; i++) c = CRC_TABLE[(c ^ buf[i]) & 0xff] ^ (c >>> 8);
  return (c ^ 0xffffffff) >>> 0;
}

// 递归打包 dirPath 下全部文件到 outPath（保留相对目录结构，UTF-8 文件名）
function zipDirectory(dirPath, outPath) {
  const files = [];
  (function walk(dir, prefix) {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, entry.name);
      const rel = prefix ? `${prefix}/${entry.name}` : entry.name;
      if (entry.isDirectory()) walk(full, rel);
      else if (entry.isFile()) files.push({ full, rel });
    }
  })(dirPath, '');

  const central = [];
  const fd = fs.openSync(outPath, 'w');
  let offset = 0;
  try {
    for (const f of files) {
      const data = fs.readFileSync(f.full);
      const nameBuf = Buffer.from(f.rel, 'utf8');
      const crc = crc32(data);
      const comp = zlib.deflateRawSync(data, { level: 6 });

      // Local File Header
      const lfh = Buffer.alloc(30);
      lfh.writeUInt32LE(0x04034b50, 0);  // signature
      lfh.writeUInt16LE(20, 4);          // version needed
      lfh.writeUInt16LE(0x0800, 6);      // general purpose flag: UTF-8
      lfh.writeUInt16LE(8, 8);           // compression: deflate
      lfh.writeUInt32LE(crc, 14);
      lfh.writeUInt32LE(comp.length, 18);
      lfh.writeUInt32LE(data.length, 22);
      lfh.writeUInt16LE(nameBuf.length, 26);
      lfh.writeUInt16LE(0, 28);          // extra len
      fs.writeSync(fd, lfh);
      fs.writeSync(fd, nameBuf);
      fs.writeSync(fd, comp);

      // Central Directory entry
      const cd = Buffer.alloc(46);
      cd.writeUInt32LE(0x02014b50, 0);   // signature
      cd.writeUInt16LE(20, 4);           // version made by
      cd.writeUInt16LE(20, 6);           // version needed
      cd.writeUInt16LE(0x0800, 8);       // flag: UTF-8
      cd.writeUInt16LE(8, 10);           // method: deflate
      cd.writeUInt32LE(crc, 16);
      cd.writeUInt32LE(comp.length, 20);
      cd.writeUInt32LE(data.length, 24);
      cd.writeUInt16LE(nameBuf.length, 28);
      cd.writeUInt32LE(offset, 42);      // local header offset
      central.push(cd, nameBuf);
      offset += lfh.length + nameBuf.length + comp.length;
    }

    const cdBuf = Buffer.concat(central);
    const eocd = Buffer.alloc(22);
    eocd.writeUInt32LE(0x06054b50, 0);   // signature
    eocd.writeUInt16LE(files.length, 8);
    eocd.writeUInt16LE(files.length, 10);
    eocd.writeUInt32LE(cdBuf.length, 12);
    eocd.writeUInt32LE(offset, 16);
    fs.writeSync(fd, cdBuf);
    fs.writeSync(fd, eocd);
  } finally {
    fs.closeSync(fd);
  }
  return files.length;
}

function loadCreds() {
  let skillCfg = {};
  try { if (fs.existsSync(CONFIG_FILE)) skillCfg = JSON.parse(fs.readFileSync(CONFIG_FILE, 'utf8')); } catch {}
  const clientId =
    skillCfg.clientId ||
    process.env.IMA_OPENAPI_CLIENTID || process.env.IMA_CLIENT_ID ||
    readFileSafe(path.join(os.homedir(), '.config/ima/client_id'));
  const apiKey =
    skillCfg.apiKey ||
    process.env.IMA_OPENAPI_APIKEY || process.env.IMA_API_KEY ||
    readFileSafe(path.join(os.homedir(), '.config/ima/api_key'));
  if (!clientId || !apiKey) {
    throw new Error('未找到 IMA 凭证：请在 skill 目录 config.json 配置 clientId/apiKey，或设置环境变量 IMA_OPENAPI_CLIENTID / IMA_OPENAPI_APIKEY。');
  }
  return { clientId, apiKey };
}

async function imaPost(apiPath, body, creds) {
  const res = await fetch(`${BASE}/${apiPath}`, {
    method: 'POST',
    headers: {
      'ima-openapi-clientid': creds.clientId,
      'ima-openapi-apikey': creds.apiKey,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
  });
  const text = await res.text();
  let json;
  try { json = JSON.parse(text); } catch { throw new Error(`接口 ${apiPath} 返回非 JSON：${text}`); }
  return json;
}

async function call(apiPath, body, creds) {
  const json = await imaPost(apiPath, body, creds);
  if (json.code !== 0) throw new Error(`接口 ${apiPath} 失败 (code=${json.code}): ${json.msg || ''}`);
  return json;
}

async function resolveKbId(args, creds) {
  if (args.kb) return args.kb;
  if (!args['kb-name']) throw new Error('缺少必需参数：--kb <kb_id> 或 --kb-name <知识库名称>');
  const resp = await call('openapi/wiki/v1/search_knowledge_base', { query: args['kb-name'], cursor: '', limit: 20 }, creds);
  const list = (resp.data && resp.data.info_list) || [];
  const hit = list.find(x => x.kb_name === args['kb-name']) || list.find(x => (x.kb_name || '').includes(args['kb-name']));
  if (!hit) throw new Error(`未找到知识库：${args['kb-name']}`);
  return hit.kb_id;
}

async function listFolder(kbId, folderId, prefix, out, creds, depth) {
  if (depth > 20) return;
  let cursor = '';
  let page = 0;
  do {
    const body = { knowledge_base_id: kbId, cursor, limit: 50 };
    if (folderId) body.folder_id = folderId;
    const resp = await call('openapi/wiki/v1/get_knowledge_list', body, creds);
    const items = (resp.data && resp.data.knowledge_list) || [];
    for (const it of items) {
      const p = prefix ? prefix + '/' + it.title : it.title;
      if (it.media_type === 99) {
        await listFolder(kbId, it.media_id, p, out, creds, depth + 1);
      } else {
        out.push({ title: it.title, media_id: it.media_id, media_type: it.media_type, path: p });
      }
    }
    cursor = (resp.data && resp.data.next_cursor) || '';
    if (resp.data && resp.data.is_end) break;
    if (++page > 50) break; // 单目录上限 2500 条
  } while (cursor);
}

async function main() {
  const args = parseArgs(process.argv);
  const creds = loadCreds();
  const kbId = await resolveKbId(args, creds);

  // 1. 收集文件清单（从根或指定文件夹递归）
  let files = [];
  await listFolder(kbId, args['folder-id'] || null, '', files, creds, 0);

  // 2. 若指定了文件清单，则按 media_id 筛选（保留其在目录树中的路径）
  if (args['media-ids']) {
    const ids = String(args['media-ids']).split(',').map(s => s.trim()).filter(Boolean);
    const byId = new Map(files.map(f => [f.media_id, f]));
    files = ids.map(id => byId.get(id) || { title: id, media_id: id, media_type: 0, path: id });
  }

  if (args['dry-run']) {
    console.log(`[dry-run] 将导出 ${files.length} 个文件：`);
    for (const f of files) console.log(`  ${f.path}  (${f.media_id})`);
    return;
  }
  if (!files.length) { console.log('没有可导出的文件。'); return; }

  // 3. 逐个导出下载到临时目录（保留目录结构，重名加序号）
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'kb-export-'));
  const used = {};
  let ok = 0;
  const fail = [];
  for (const f of files) {
    let rel = f.path;
    if (rel in used) {
      used[rel] += 1;
      const d = path.dirname(rel);
      const base = path.basename(rel);
      const dot = base.lastIndexOf('.');
      const stem = dot > 0 ? base.slice(0, dot) : base;
      const ext = dot > 0 ? base.slice(dot) : '';
      rel = path.join(d, `${stem}_${used[rel]}${ext}`);
    } else {
      used[rel] = 0;
    }
    try {
      const resp = await call('openapi/wiki/v1/export_media_for_ima_sandbox', { media_id: f.media_id }, creds);
      const info = (resp.data && resp.data.media_content_url_info) || {};
      const url = info.url;
      const headers = info.headers || {};
      if (!url) throw new Error('无下载链接（该类型可能不支持导出）');
      const target = path.join(tmp, rel);
      fs.mkdirSync(path.dirname(target), { recursive: true });
      const hdr = {};
      for (const [k, v] of Object.entries(headers)) hdr[k] = v;
      const r = await fetch(url, { headers: hdr });
      if (!r.ok) throw new Error(`下载 HTTP ${r.status}`);
      const buf = Buffer.from(await r.arrayBuffer());
      fs.writeFileSync(target, buf);
      ok++;
      console.log(`  OK   ${rel}  (${buf.length} bytes)`);
    } catch (e) {
      fail.push({ path: rel, media_id: f.media_id, err: e.message });
      console.log(`  FAIL ${rel}: ${e.message}`);
    }
  }

  if (ok === 0) {
    console.error(`\n[error] 全部 ${files.length} 个文件导出失败，未生成 zip。`);
    fs.rmSync(tmp, { recursive: true, force: true });
    process.exit(1);
  }

  // 4. 打包成 zip（纯 Node 实现，跨平台，不依赖系统 zip）
  const out = args.out || path.join('/sandbox/workspace/outputs', `知识库导出_${Date.now()}.zip`);
  fs.mkdirSync(path.dirname(out), { recursive: true });
  const packed = zipDirectory(tmp, out);
  const size = fs.statSync(out).size;
  if (packed !== files.length) throw new Error(`zip 内文件数(${packed})与清单(${files.length})不一致`);

  console.log(`\n=== 完成 ===`);
  console.log(`导出成功: ${ok}/${files.length}`);
  if (fail.length) console.log(`失败: ${fail.length}（见上方 FAIL 列表，常见为网页/公众号类不支持导出）`);
  console.log(`zip 路径: ${out}  (${size} bytes)`);
  if (!args.keep) fs.rmSync(tmp, { recursive: true, force: true });
}

main().catch((err) => { console.error(`[error] ${err.message}`); process.exit(1); });
