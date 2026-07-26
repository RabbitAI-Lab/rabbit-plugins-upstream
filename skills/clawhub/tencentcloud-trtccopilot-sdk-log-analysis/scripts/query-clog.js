#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import { pipeline } from 'node:stream/promises';
import { Readable } from 'node:stream';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

import { parseArgs, fail, makeSessionId, isPreviewEnabled } from './lib/args.js';
import { decodeFile } from './lib/decoder.js';
import { assertInternalNetwork, redactObject } from './lib/internal-env.js';
import { callApi } from './lib/copilot-cli.js';
import { parseLogLine } from './lib/timeline.js';
import { upsertViewerIndex, buildLogIndexRecord } from './lib/viewer-index.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SKILL_DIR = path.resolve(__dirname, '..');
const DEFAULT_OUTPUT_DIR = path.join(SKILL_DIR, 'tmp', 'sessions');

function sanitizeFileName(name) {
  return String(name).replace(/[/\\:*?"<>|]/g, '_').replace(/\s+/g, '_');
}

function filenameFromUrl(url) {
  try {
    const u = new URL(url);
    return path.basename(u.pathname) || 'unknown.log';
  } catch {
    return path.basename(String(url).split('?')[0]) || 'unknown.log';
  }
}

// NOTE: `/clog/query` is registered in the trtccopilot CLI discovery but, as of CLI 0.2.0,
// the backend route returns an HTML 404 for every parameter shape. This query path is
// implemented per the documented contract (sdkappid/userid/daterange[]) but is NOT yet
// end-to-end verified — it will start working once the backend route is fixed.
function unwrapClogList(json) {
  // Tolerate a few wrapper shapes: {data:{data,total}}, {data:[...]}, [...]
  if (Array.isArray(json)) return { list: json, count: json.length };
  const data = json?.data ?? json;
  if (Array.isArray(data)) return { list: data, count: json?.total ?? data.length };
  return { list: data?.data || [], count: data?.total || 0 };
}

function queryPage({ sdkappid, userid, date, page, size, logkey, fuzzy, business }) {
  const qs = new URLSearchParams();
  qs.append('sdkappid', String(sdkappid));
  qs.append('userid', String(userid));
  qs.append('daterange[]', `${date} 00:00:00`);
  qs.append('daterange[]', `${date} 23:59:59`);
  qs.append('page', String(page));
  qs.append('size', String(size));
  if (logkey) qs.append('logkey', String(logkey));
  if (fuzzy != null) qs.append('fuzzy', String(fuzzy));
  if (business != null) qs.append('business', String(business));

  const json = callApi('GET', `/clog/query?${qs.toString()}`);
  return unwrapClogList(json);
}

async function queryAllRecords(opts) {
  const size = 100;
  let page = 1;
  let all = [];
  while (page <= 10) {
    const result = queryPage({ ...opts, page, size });
    all = all.concat(result.list);
    if (result.list.length < size || all.length >= result.count) break;
    page++;
  }
  return all;
}

function deduplicateRecords(records) {
  const map = new Map();
  for (const record of records) {
    const name = filenameFromUrl(record.source_url || '');
    const key = `${record.sdkappid}|${record.user_id}|${name}`;
    const old = map.get(key);
    if (!old || new Date(record.update_time).getTime() > new Date(old.update_time).getTime()) map.set(key, record);
  }
  return [...map.values()];
}

async function downloadFile(url, filePath) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`下载失败 HTTP ${res.status}`);
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  await pipeline(Readable.fromWeb(res.body), fs.createWriteStream(filePath));
}

async function extractGzip(filePath) {
  const target = filePath.replace(/\.gz$/i, '');
  await pipeline(fs.createReadStream(filePath), zlib.createGunzip(), fs.createWriteStream(target));
  fs.rmSync(filePath, { force: true });
  return [target];
}

function listFilesRecursive(dir) {
  const out = [];
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, item.name);
    if (item.isDirectory()) out.push(...listFilesRecursive(p));
    else out.push(p);
  }
  return out;
}

async function extractZip(filePath) {
  const targetDir = path.dirname(filePath);
  const before = new Set(listFilesRecursive(targetDir));
  const r = spawnSync('unzip', ['-o', '-q', filePath, '-d', targetDir], { encoding: 'utf8' });
  if (r.status !== 0) throw new Error(`unzip 失败: ${r.stderr || r.stdout}`);
  fs.rmSync(filePath, { force: true });
  return listFilesRecursive(targetDir).filter(p => !before.has(p));
}

async function extractIfNeeded(filePath) {
  const lower = filePath.toLowerCase();
  if (lower.endsWith('.gz')) return extractGzip(filePath);
  if (lower.endsWith('.zip')) return extractZip(filePath);
  return [filePath];
}

function isBinaryLog(filePath) {
  return /\.(clog|xlog)$/i.test(filePath);
}

function decodeIfNeeded(filePath, { noDecode }) {
  if (noDecode || !isBinaryLog(filePath)) return filePath;
  const output = `${filePath}.log`;
  decodeFile(filePath, output, { skillDir: SKILL_DIR });
  fs.rmSync(filePath, { force: true });
  return output;
}

function readHeadTail(filePath) {
  const stat = fs.statSync(filePath);
  if (stat.size === 0) return [];
  const fd = fs.openSync(filePath, 'r');
  try {
    const headSize = Math.min(4096, stat.size);
    const head = Buffer.alloc(headSize);
    fs.readSync(fd, head, 0, headSize, 0);
    const tailSize = Math.min(4096, stat.size);
    const tail = Buffer.alloc(tailSize);
    fs.readSync(fd, tail, 0, tailSize, Math.max(0, stat.size - tailSize));
    const first = head.toString('utf8').split(/\r?\n/).find(line => line.trim());
    const last = tail.toString('utf8').split(/\r?\n/).reverse().find(line => line.trim());
    return [first, last].filter(Boolean);
  } finally {
    fs.closeSync(fd);
  }
}

function fileTimeRange(filePath) {
  const parsed = readHeadTail(filePath).map(line => parseLogLine(line));
  return {
    start: parsed[0]?.timeText || '',
    end: parsed.at(-1)?.timeText || '',
  };
}

async function processRecord(record, targetRoot, { noDecode }) {
  const uploadDir = sanitizeFileName(record.update_time || 'unknown-upload-time');
  const dir = path.join(targetRoot, String(record.sdkappid), sanitizeFileName(record.user_id || 'unknown-user'), uploadDir);
  const originalName = filenameFromUrl(record.source_url || 'unknown.log');
  const rawPath = path.join(dir, originalName);
  await downloadFile(record.source_url, rawPath);
  const extracted = await extractIfNeeded(rawPath);
  const decoded = extracted.map(file => decodeIfNeeded(file, { noDecode }));
  return decoded.map(file => ({
    file,
    originalName,
    size: fs.statSync(file).size,
    uploadTime: record.update_time,
    sdkAppId: record.sdkappid,
    userId: record.user_id,
    timeRange: fileTimeRange(file),
  }));
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help || args.h) {
    process.stdout.write(`Usage:\n  node scripts/query-clog.js --sdkappid <id> --userid <id> --date YYYY-MM-DD [--output-dir <dir>] [--no-decode]\n`);
    return;
  }
  const sdkappid = args.sdkappid || args['sdk-app-id'];
  const userid = args.userid || args['user-id'];
  const date = args.date;
  if (!sdkappid || !userid || !date) fail('必须提供 --sdkappid --userid --date');
  if (!/^\d{4}-\d{2}-\d{2}$/.test(String(date))) fail('--date 必须是 YYYY-MM-DD（上报日期，不是日志内容日期）');
  await assertInternalNetwork('TRTC Clog 拉取工具');

  const outBase = path.resolve(args['output-dir'] || DEFAULT_OUTPUT_DIR);
  const runDir = path.join(outBase, makeSessionId('clog'));
  const targetRoot = path.join(runDir, 'clog');
  fs.mkdirSync(targetRoot, { recursive: true });

  const records = await queryAllRecords({
    sdkappid,
    userid,
    date,
    logkey: args.logkey,
    fuzzy: args.fuzzy,
    business: args.business || 0,
  });
  const deduped = deduplicateRecords(records);
  const files = [];
  const errors = [];
  for (const record of deduped) {
    try {
      files.push(...await processRecord(record, targetRoot, { noDecode: args['no-decode'] === 'true' }));
    } catch (error) {
      errors.push({ record, error: error.message });
    }
  }

  fs.writeFileSync(path.join(runDir, 'records.json'), JSON.stringify(redactObject(records), null, 2), 'utf8');
  fs.writeFileSync(path.join(runDir, 'manifest.json'), JSON.stringify({
    source: 'clog',
    sdkappid,
    userid,
    date,
    totalRecords: records.length,
    deduplicatedRecords: deduped.length,
    successCount: files.length,
    failedCount: errors.length,
    files,
    errors: redactObject(errors),
    generated_at: new Date().toISOString(),
  }, null, 2), 'utf8');

  if (isPreviewEnabled()) {
    const indexRecords = files.map(f => buildLogIndexRecord(f.file, {
      source: 'clog', sdkAppId: f.sdkAppId, userId: f.userId,
    }));
    if (indexRecords.length) upsertViewerIndex(path.join(runDir, 'viewer-index.json'), indexRecords);
  }

  process.stdout.write(`[run-dir] ${runDir}\n`);
  process.stdout.write(`[manifest] ${path.join(runDir, 'manifest.json')}\n`);
  process.stdout.write(`[files]   ${files.map(f => f.file).join(',')}\n`);
  process.stdout.write(`[success] ${files.length}\n`);
  process.stdout.write(`[failed]  ${errors.length}\n`);
}

main().catch(error => fail(error.message, 2));
