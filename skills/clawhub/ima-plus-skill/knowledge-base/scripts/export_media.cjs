#!/usr/bin/env node
'use strict';

/**
 * 导出知识库中某个媒体的内容，获取下载链接（封装 openapi/wiki/v1/export_media_for_ima_sandbox）
 * 可选 --download 将内容下载到本地 --out 指定的路径。
 *
 * Usage:
 *   node export_media.cjs --media-id <media_id>
 *   node export_media.cjs --media-id <media_id> --download --out /path/to/save.pdf
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

async function main() {
  const args = parseArgs(process.argv);
  if (!args['media-id']) {
    console.error('[error] 缺少必需参数 --media-id <media_id>');
    process.exit(1);
  }

  log('⏳', `导出 media_id=${args['media-id']}…`);
  const resp = await call('openapi/wiki/v1/export_media_for_ima_sandbox', {
    media_id: args['media-id'],
  });
  const data = resp.data || {};
  const mediaType = data.media_type;
  const info = data.media_content_url_info || {};
  const url = info.url;
  const headers = info.headers || {};

  log('✅', `media_type=${mediaType}`);
  log('🔗', `下载链接：${url}`);
  if (Object.keys(headers).length) log('📋', `需带 header：${JSON.stringify(headers)}`);

  if (args.download) {
    if (!args.out) {
      console.error('[error] --download 需配合 --out <本地保存路径>');
      process.exit(1);
    }
    log('⏳', `下载到 ${args.out}…`);
    const hdr = {};
    for (const [k, v] of Object.entries(headers)) hdr[k] = v;
    const r = await fetch(url, { headers: hdr });
    if (!r.ok) throw new Error(`下载失败 HTTP ${r.status}`);
    const buf = Buffer.from(await r.arrayBuffer());
    fs.writeFileSync(args.out, buf);
    log('✅', `已保存 ${buf.length} 字节到 ${args.out}`);
  }
}

main().catch((err) => {
  console.error(`[error] ${err.message}`);
  process.exit(1);
});
