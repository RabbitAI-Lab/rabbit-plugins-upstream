#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

import { parseArgs, parseTimeArg, fail, makeSessionId, formatTs, isPreviewEnabled } from './lib/args.js';
import { assertInternalNetwork } from './lib/internal-env.js';
import { callApi } from './lib/copilot-cli.js';
import { makeFileId, upsertViewerIndex } from './lib/viewer-index.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SKILL_DIR = path.resolve(__dirname, '..');
const DEFAULT_OUTPUT_DIR = path.join(SKILL_DIR, 'tmp', 'sessions');
const MAX_TIME_WINDOW_MS = 7 * 24 * 3600 * 1000;

// The trtccopilot `/log-crawler/trtc` endpoint fetches AND parses Kibana logs server-side,
// returning flat rows. We only normalize field names for our output files.
function normalizeRow(row) {
  return {
    time: row.timestamp != null ? formatTs(row.timestamp) : (row.time || ''),
    sdkAppId: row.sdkAppId,
    userId: row.userId,
    roomId: row.roomId || '',
    uuid: row.uuid || '',
    log: row.log || '',
    version: row.version || '',
  };
}

// For Kibana, the log TYPE is AUTHORITATIVE from `--type`: web → kibana_web, native → kibana_native.
export function buildKibanaIndexRecord({ type, sdkAppId, userId, roomId, runDir, rows }) {
  const filePath = path.resolve(path.join(runDir, 'logs.txt'));
  return {
    id: makeFileId(filePath),
    filePath,
    fileName: 'logs.txt',
    source: 'kibana',
    logType: `kibana_${type}`,
    sdk: '实时音视频TRTC',
    sdkAppId: String(sdkAppId || ''),
    userId: String(userId || ''),
    roomId: String(roomId || ''),
    lines: Array.isArray(rows) ? rows.length : 0,
  };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help || args.h) {
    process.stdout.write(`Usage:\n  node scripts/query-kibana.js --sdk-app-id <id> --start <time|ms> --end <time|ms> --type web|native [--user-id <id>|--room-id <id>] [--output-dir <dir>]\n`);
    return;
  }
  const sdkAppId = Number(args['sdk-app-id'] || args.sdkAppId);
  const type = String(args.type || '').toLowerCase();
  if (!sdkAppId) fail('必须提供 --sdk-app-id');
  if (!['web', 'native'].includes(type)) fail('必须提供 --type web|native');
  if (type === 'web' && args['room-id'] && !args['user-id']) fail('Web Kibana 不支持按房间查询，请提供 --user-id');
  if (!args['user-id'] && !args['room-id']) fail('必须提供 --user-id 或 --room-id');

  const startTS = parseTimeArg(args.start);
  const endTS = parseTimeArg(args.end);
  if (!startTS || !endTS || endTS <= startTS) fail('--end 必须晚于 --start');
  if (endTS - startTS > MAX_TIME_WINDOW_MS) fail('Kibana 日志保留/查询窗口按 7 天处理，请缩小时间范围');
  await assertInternalNetwork('TRTC Kibana 查询工具');

  const body = {
    sdkAppId,
    type,
    startTS,
    endTS,
  };
  if (args['user-id']) body.userId = String(args['user-id']);
  if (args['room-id'] && type !== 'web') body.roomId = String(args['room-id']);

  const data = callApi('POST', '/log-crawler/trtc', { data: body });
  const rows = (data.logs || []).map(normalizeRow);

  const outBase = path.resolve(args['output-dir'] || DEFAULT_OUTPUT_DIR);
  const runDir = path.join(outBase, makeSessionId('kibana'));
  fs.mkdirSync(runDir, { recursive: true });
  fs.writeFileSync(path.join(runDir, 'raw-response.json'), JSON.stringify(data, null, 2), 'utf8');
  fs.writeFileSync(path.join(runDir, 'logs.ndjson'), rows.map(row => JSON.stringify(row)).join('\n') + (rows.length ? '\n' : ''), 'utf8');
  fs.writeFileSync(path.join(runDir, 'logs.txt'), rows.map(row => `[${row.time || ''}] ${row.userId || ''} ${row.roomId || ''} ${row.log || ''}`).join('\n'), 'utf8');
  fs.writeFileSync(path.join(runDir, 'manifest.json'), JSON.stringify({
    source: 'kibana',
    type,
    sdkAppId,
    userId: args['user-id'] || '',
    roomId: args['room-id'] || '',
    timeRange: { start: formatTs(startTS), end: formatTs(endTS), startTS, endTS },
    count: rows.length,
    total: data.total ?? rows.length,
    files: ['raw-response.json', 'logs.ndjson', 'logs.txt'],
    generated_at: new Date().toISOString(),
  }, null, 2), 'utf8');

  if (isPreviewEnabled()) {
    const indexRecord = buildKibanaIndexRecord({
      type, sdkAppId, userId: args['user-id'], roomId: args['room-id'], runDir, rows,
    });
    upsertViewerIndex(path.join(runDir, 'viewer-index.json'), [indexRecord]);
  }

  process.stdout.write(`[run-dir] ${runDir}\n`);
  process.stdout.write(`[logs]    ${path.join(runDir, 'logs.txt')}\n`);
  process.stdout.write(`[ndjson]  ${path.join(runDir, 'logs.ndjson')}\n`);
  process.stdout.write(`[count]   ${rows.length}\n`);
}

const isCliEntry = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isCliEntry) {
  main().catch(error => fail(error.message, 2));
}
