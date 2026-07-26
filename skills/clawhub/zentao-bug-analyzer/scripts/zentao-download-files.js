#!/usr/bin/env node
/**
 * zentao-download-files.js — 下载禅道 Bug 的所有附件到本地
 *
 * 用法:
 *   node zentao-download-files.js --ws=<wsEndpoint> --bug-id=<id> --dir=<输出目录>
 *     [--zentao-url=http://zentao.gxatek.com:20080]
 *
 * 通过 page.exposeFunction 将 Node.js fs 暴露给浏览器端，
 * 在 page.evaluate 内直接 fetch → blob → 转 ArrayBuffer → 传回 Node.js 写入文件。
 * 对超大文件（>50MB）分批传输以避免 CDP 协议超时。
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

function parseArgs() {
  const args = process.argv.slice(2);
  const config = {
    wsEndpoint: '',
    bugId: 0,
    outputDir: '',
    zentaoUrl: 'http://zentao.gxatek.com:20080',
  };
  for (const arg of args) {
    if (arg.startsWith('--ws=')) config.wsEndpoint = arg.slice(5);
    if (arg.startsWith('--bug-id=')) config.bugId = parseInt(arg.slice(9), 10);
    if (arg.startsWith('--dir=')) config.outputDir = arg.slice(6);
    if (arg.startsWith('--zentao-url=')) config.zentaoUrl = arg.split('=')[1];
  }
  return config;
}

const CHUNK_SIZE = 10 * 1024 * 1024; // 10MB per chunk

async function downloadFileInBrowser(page, downloadUrl, filePath, fileSize) {
  return page.evaluate(async ({ downloadUrl, filePath, fileSize, CHUNK_SIZE }) => {
    const chunkSize = CHUNK_SIZE;
    const resp = await fetch(downloadUrl, { credentials: 'include' });
    if (!resp.ok) return { error: `HTTP ${resp.status}` };

    const contentLength = parseInt(resp.headers.get('Content-Length') || '0', 10);
    const total = contentLength || fileSize;
    const reader = resp.body.getReader();
    const chunks = [];
    let received = 0;

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      chunks.push(value);
      received += value.length;
    }

    // 合并所有 chunks
    let offset = 0;
    const allData = new Uint8Array(received);
    for (const chunk of chunks) {
      allData.set(chunk, offset);
      offset += chunk.length;
    }

    // 分批传回给 Node.js
    for (let i = 0; i < allData.length; i += chunkSize) {
      const end = Math.min(i + chunkSize, allData.length);
      const slice = allData.slice(i, end);
      // 转 base64
      let binary = '';
      for (let j = 0; j < slice.length; j++) {
        binary += String.fromCharCode(slice[j]);
      }
      const b64 = btoa(binary);
      // 通过 exposeFunction 传回
      window.__writeChunk(filePath, b64, i, end === allData.length);
    }

    return { ok: true, size: received };
  }, { downloadUrl, filePath, fileSize, CHUNK_SIZE });
}

async function main() {
  const config = parseArgs();

  if (!config.wsEndpoint) throw new Error('缺少 --ws 参数');
  if (!config.bugId) throw new Error('缺少 --bug-id 参数');
  if (!config.outputDir) throw new Error('缺少 --dir 参数');

  fs.mkdirSync(config.outputDir, { recursive: true });

  console.error(`[INFO] 连接到浏览器: ${config.wsEndpoint}`);
  const browser = await chromium.connectOverCDP(config.wsEndpoint, { timeout: 30000 });
  const page = browser.contexts()[0].pages()[0];

  // exposeFunction: 将文件写入能力暴露给浏览器端的 JS
  const fileBuffers = {};
  await page.exposeFunction('__writeChunk', (filePath, b64, offset, isLast) => {
    if (!fileBuffers[filePath]) {
      fileBuffers[filePath] = { chunks: [], totalSize: 0 };
    }
    const buf = Buffer.from(b64, 'base64');
    fileBuffers[filePath].chunks.push({ offset, data: buf });
    fileBuffers[filePath].totalSize += buf.length;

    if (isLast) {
      // 合并所有块并写入文件
      const fb = fileBuffers[filePath];
      const merged = Buffer.alloc(fb.totalSize);
      let pos = 0;
      fb.chunks.sort((a, b) => a.offset - b.offset);
      for (const chunk of fb.chunks) {
        chunk.data.copy(merged, pos);
        pos += chunk.data.length;
      }
      fs.writeFileSync(filePath, merged);
      delete fileBuffers[filePath];
    }
  });

  // 第一步：获取 Bug 详情
  console.error(`[INFO] 获取 Bug #${config.bugId} 附件列表...`);
  const bug = await page.evaluate(async ({ bugId, zentaoUrl }) => {
    const resp = await fetch(`${zentaoUrl}/api.php/v1/bugs/${bugId}`, { credentials: 'include' });
    if (!resp.ok) return { error: true, status: resp.status };
    const data = await resp.json();
    const files = {};
    if (data.files) {
      for (const [id, f] of Object.entries(data.files)) {
        files[id] = { id: f.id, title: f.title, size: f.size };
      }
    }
    return { error: false, files };
  }, { bugId: config.bugId, zentaoUrl: config.zentaoUrl });

  if (bug.error) throw new Error(`获取 Bug 详情失败 (HTTP ${bug.status})`);

  const fileEntries = Object.values(bug.files);
  if (fileEntries.length === 0) {
    console.error('[INFO] 该 Bug 没有附件');
    process.exit(0);
  }

  console.error(`[INFO] 共 ${fileEntries.length} 个附件`);

  // 第二步：逐文件下载
  for (const file of fileEntries) {
    const filePath = path.join(config.outputDir, file.title);
    const downloadUrl = `${config.zentaoUrl}/file-download-${file.id}.json`;
    console.error(`[INFO] 下载: ${file.title} (${(file.size / 1024 / 1024).toFixed(1)}MB)...`);

    const result = await downloadFileInBrowser(page, downloadUrl, filePath, file.size);

    if (result.error) {
      console.error(`[WARN] 下载失败: ${file.title} - ${result.error}`);
      continue;
    }

    if (fs.existsSync(filePath) && fs.statSync(filePath).size > 0) {
      const stat = fs.statSync(filePath);
      console.log(filePath);
      console.error(`[INFO] 完成: ${file.title} (${(stat.size / 1024 / 1024).toFixed(1)}MB)`);
    } else {
      console.error(`[WARN] 下载失败: ${file.title} - 文件未写入`);
    }
  }

  console.error('[INFO] 下载完成');
}

main().catch((err) => {
  console.error(`[ERROR] ${err.message}`);
  process.exit(1);
});
