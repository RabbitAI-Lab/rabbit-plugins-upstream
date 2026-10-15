#!/usr/bin/env node

const fs = require('fs');
const os = require('os');
const path = require('path');

const BASE_URL = (process.env.CLIP2MD_API_BASE || 'https://clip2.md/api/v1').replace(/\/+$/, '');
const CONFIG_DIR = path.join(os.homedir(), '.clip2md');
const CONFIG_FILE = path.join(CONFIG_DIR, 'config.json');
const DEFAULT_WAIT_TIMEOUT_SECONDS = 120;
const DEFAULT_WAIT_INTERVAL_SECONDS = 5;
const WAITING_STATUSES = new Set(['PENDING', 'PROCESSING', 'WAITING_SERVICE']);
const SUCCESS_STATUSES = new Set(['SUCCESS']);
const FAILURE_STATUSES = new Set([
  'FAILED',
  'FAILED_AUTH_EXPIRED',
  'FAILED_SERVICE_UNAVAILABLE',
  'MANUAL_REVIEW',
]);

class ApiError extends Error {
  constructor(status, detail, retryAfter = null) {
    super(detail);
    this.status = status;
    this.detail = detail;
    this.retryAfter = retryAfter;
  }
}

function loadConfig() {
  try {
    return JSON.parse(fs.readFileSync(CONFIG_FILE, 'utf-8'));
  } catch {
    return null;
  }
}

function saveConfig(config) {
  fs.mkdirSync(CONFIG_DIR, { recursive: true });
  fs.writeFileSync(CONFIG_FILE, JSON.stringify(config, null, 2));
}

function formatDetail(detail) {
  if (!detail) return '';
  if (typeof detail === 'string') return detail;
  if (Array.isArray(detail)) return detail.map(formatDetail).filter(Boolean).join('; ');
  if (typeof detail === 'object') {
    if (detail.msg) return detail.msg;
    if (detail.message) return detail.message;
    return JSON.stringify(detail);
  }
  return String(detail);
}

function formatApiError(error) {
  if (!(error instanceof ApiError)) return error.message || String(error);

  const retryHint = error.retryAfter ? ` 请在 ${error.retryAfter} 秒后重试。` : '';
  switch (error.status) {
    case 401:
      return 'Token 已过期或无效。请重新运行: node scripts/clip2md.js config <your_token>';
    case 403:
      return `额度不足或没有权限执行该操作。${error.detail || ''}`.trim();
    case 409:
      return `任务冲突，可能是重复链接或当前任务状态不允许该操作。${error.detail || ''}`.trim();
    case 429:
      return `请求过于频繁。${error.detail || ''}${retryHint}`.trim();
    case 503:
      return `clip2md 服务暂时不可用。${error.detail || ''}${retryHint}`.trim();
    default:
      return `请求失败 (${error.status}): ${error.detail || '未知错误'}`;
  }
}

function ensureToken() {
  const config = loadConfig();
  if (!config?.token) {
    throw new Error('未配置 token。请先运行: node scripts/clip2md.js config <your_token>');
  }
  return config.token;
}

async function request(method, path, body = null) {
  const token = ensureToken();

  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`,
  };

  const options = { method, headers };
  if (body) options.body = JSON.stringify(body);

  const res = await fetch(`${BASE_URL}${path}`, options);

  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: res.statusText }));
    throw new ApiError(
      res.status,
      formatDetail(err.detail || err.message || res.statusText),
      res.headers.get('retry-after')
    );
  }

  return res.json();
}

function parsePositiveInt(value, name) {
  const parsed = Number.parseInt(value, 10);
  if (!Number.isFinite(parsed) || parsed <= 0) {
    throw new Error(`${name} 必须是正整数`);
  }
  return parsed;
}

function parseWaitOptions(args) {
  const options = {
    timeout: DEFAULT_WAIT_TIMEOUT_SECONDS,
    interval: DEFAULT_WAIT_INTERVAL_SECONDS,
  };

  for (let i = 0; i < args.length; i += 1) {
    const arg = args[i];
    if (arg === '--timeout') {
      options.timeout = parsePositiveInt(args[++i], '--timeout');
    } else if (arg === '--interval') {
      options.interval = parsePositiveInt(args[++i], '--interval');
    } else {
      throw new Error(`未知参数: ${arg}`);
    }
  }

  return options;
}

function statusKind(status) {
  if (SUCCESS_STATUSES.has(status)) return 'success';
  if (WAITING_STATUSES.has(status)) return 'waiting';
  if (FAILURE_STATUSES.has(status)) return 'failure';
  return 'unknown';
}

function printTaskSummary(task) {
  console.log(`任务 ID: ${task.id}`);
  console.log(`状态: ${task.status}`);
  console.log(`链接: ${task.url}`);
  if (task.title || task.source_title) {
    console.log(`标题: ${task.title || task.source_title}`);
  }
  if (task.error_msg) {
    console.log(`错误: ${task.error_msg}`);
  }
  if (task.error_category) {
    console.log(`错误分类: ${task.error_category}`);
  }
  console.log(`Markdown: ${task.note_markdown_content ? '已生成' : '未生成'}`);

  const assetFields = ['asset_count', 'asset_ready_count', 'asset_pending_count', 'asset_failed_count'];
  if (assetFields.some((field) => typeof task[field] === 'number')) {
    console.log(
      `资源: 总数 ${task.asset_count ?? 0}, 已就绪 ${task.asset_ready_count ?? 0}, ` +
      `处理中 ${task.asset_pending_count ?? 0}, 失败 ${task.asset_failed_count ?? 0}`
    );
  }
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function cmdConfig(token) {
  if (!token) {
    throw new Error('用法: node scripts/clip2md.js config <token>');
  }
  saveConfig({ token });
  console.log('Token 已保存到 ~/.clip2md/config.json');
}

async function cmdClip(url) {
  if (!url) {
    throw new Error('用法: node scripts/clip2md.js clip <url>');
  }

  console.log(`正在剪藏: ${url}`);
  const task = await request('POST', '/tasks', { url });
  console.log(`任务已提交 (ID: ${task.id}, 状态: ${task.status})`);

  try {
    const user = await request('GET', '/auth/me');
    console.log(`剩余额度: 每日 ${user.daily_quota} 次, 永久 ${user.permanent_quota} 次`);
  } catch (error) {
    console.error(`额度查询失败: ${formatApiError(error)}`);
  }
}

async function cmdQuota() {
  const user = await request('GET', '/auth/me');
  console.log(`每日额度: ${user.daily_quota} 次`);
  console.log(`永久额度: ${user.permanent_quota} 次`);
}

async function cmdStatus(taskId) {
  if (!taskId) {
    throw new Error('用法: node scripts/clip2md.js status <task_id>');
  }
  const task = await request('GET', `/tasks/${encodeURIComponent(taskId)}`);
  printTaskSummary(task);
  if (statusKind(task.status) === 'failure') {
    process.exitCode = 2;
  }
}

async function cmdWait(taskId, optionArgs) {
  if (!taskId) {
    throw new Error('用法: node scripts/clip2md.js wait <task_id> [--timeout <seconds>] [--interval <seconds>]');
  }

  const options = parseWaitOptions(optionArgs);
  const deadline = Date.now() + options.timeout * 1000;
  let lastTask = null;

  while (Date.now() <= deadline) {
    lastTask = await request('GET', `/tasks/${encodeURIComponent(taskId)}`);
    const kind = statusKind(lastTask.status);

    if (kind === 'success') {
      console.log('任务已完成');
      printTaskSummary(lastTask);
      return;
    }

    if (kind === 'failure') {
      console.error('任务未能完成');
      printTaskSummary(lastTask);
      process.exitCode = 2;
      return;
    }

    console.log(`等待中: 任务 ${lastTask.id} 状态 ${lastTask.status}`);
    await sleep(options.interval * 1000);
  }

  console.error(`等待超时: ${options.timeout} 秒内任务未完成`);
  if (lastTask) {
    printTaskSummary(lastTask);
  }
  process.exitCode = 3;
}

function printHelp() {
  console.log(`clip2md - Agent 网页剪藏工具

用法:
  node scripts/clip2md.js config <token>                         配置认证 token
  node scripts/clip2md.js quota                                  查询剩余额度
  node scripts/clip2md.js clip <url>                             提交网页剪藏
  node scripts/clip2md.js status <task_id>                       查询任务状态
  node scripts/clip2md.js wait <task_id> [--timeout 120] [--interval 5]  等待任务完成`);
}

async function main() {
  const args = process.argv.slice(2);
  const cmd = args[0];

  switch (cmd) {
    case 'config':
      await cmdConfig(args[1]);
      break;
    case 'clip':
      await cmdClip(args[1]);
      break;
    case 'quota':
      await cmdQuota();
      break;
    case 'status':
      await cmdStatus(args[1]);
      break;
    case 'wait':
      await cmdWait(args[1], args.slice(2));
      break;
    default:
      printHelp();
      process.exitCode = 1;
  }
}

main().catch((error) => {
  console.error(formatApiError(error));
  process.exit(1);
});
