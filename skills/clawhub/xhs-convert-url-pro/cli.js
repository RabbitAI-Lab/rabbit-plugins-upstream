#!/usr/bin/env node
'use strict';
/**
 * cli.js — 小红书转链 CLI 入口（命令分发、参数解析、输出格式控制）。
 *
 * 输出规约：stdout 只输出 JSON（{"ok":true,"data":...} / {"ok":false,"code","message"}），
 * 交互与进度一律走 stderr。
 * 退出码：0 成功 / 1 参数错误 / 2 认证失败(1002|1003) / 3 配额不足(3001) / 4 网络错误 / 5 其它。
 */
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { ApiClient, BizError, NetworkError, allowInsecureTls } = require('./src/client');
const { loadConfig, saveConfig, resolveConfig, maskToken, configPath, DEFAULT_BASE_URL } = require('./src/config');
const { runRegister, createRl, askHidden, PHONE_RE } = require('./src/register');

// package.json 同目录读取版本号（打包/安装后 cli.js 与 package.json 始终同级）
const SKILL_NAME = 'xhs-convert-url-pro';
const SKILL_VERSION = (() => {
  try {
    return JSON.parse(fs.readFileSync(path.join(__dirname, 'package.json'), 'utf8')).version || 'unknown';
  } catch {
    return 'unknown';
  }
})();

const TERMINAL_STATUS = new Set(['done', 'partial_failed', 'failed']);
const MIN_BATCH = 1;
const MAX_BATCH = 50;

class UsageError extends Error {
  constructor(message) {
    super(message);
    this.name = 'UsageError';
  }
}

// ---------------------------------------------------------------- 参数解析

const VALUE_FLAGS = new Set(['phone', 'password', 'file', 'interval', 'timeout', 'token', 'base-url', 'access-token']);
const MULTI_FLAGS = new Set(['url']);
const BOOL_FLAGS = new Set(['wait', 'help', 'link', 'check']);

function camel(s) {
  return s.replace(/-([a-z])/g, (_, c) => c.toUpperCase());
}

function parseArgs(argv) {
  const opts = {};
  const positional = [];
  for (let i = 0; i < argv.length; i++) {
    let arg = argv[i];
    if (!arg.startsWith('-')) {
      positional.push(arg);
      continue;
    }
    if (!arg.startsWith('--')) throw new UsageError(`未知参数: ${arg}`);
    let inline;
    const eq = arg.indexOf('=');
    if (eq > 2) {
      inline = arg.slice(eq + 1);
      arg = arg.slice(0, eq);
    }
    const name = arg.slice(2);
    if (VALUE_FLAGS.has(name)) {
      const value = inline !== undefined ? inline : argv[++i];
      if (value === undefined) throw new UsageError(`缺少参数值: ${arg}`);
      opts[camel(name)] = value;
    } else if (MULTI_FLAGS.has(name)) {
      const value = inline !== undefined ? inline : argv[++i];
      if (value === undefined) throw new UsageError(`缺少参数值: ${arg}`);
      (opts[camel(name)] = opts[camel(name)] || []).push(value);
    } else if (BOOL_FLAGS.has(name)) {
      if (inline !== undefined) throw new UsageError(`参数 ${arg} 不接受值`);
      opts[camel(name)] = true;
    } else {
      throw new UsageError(`未知参数: ${arg}`);
    }
  }
  const cmd = positional.shift() || '';
  return { cmd, args: positional, opts };
}

const USAGE = `小红书转链 CLI

用法: node cli.js <命令> [参数]

命令:
  version                           查看版本与安装信息（skill 名、版本、node 版本、配置文件路径）
  register --link                   生成注册二维码/链接（推荐；用户手机扫码注册，注册即送 50 条配额）
  register --check --access-token <串> 用户完成注册后确认并保存 token
  register                          终端交互式注册（安全策略要求图形验证码，终端不可用，请用 --link）
  login --link                      生成登录二维码/链接（推荐；用户浏览器登录授权，免输密码）
  login --check --access-token <串> 用户完成授权后确认并保存 token
  login --phone <手机号> [--password <密码>]   密码登录（服务端强制图形验证码，终端不可用，请用 --link）
  submit --url <url> [--url ...] [--file <路径>] [--wait] [--interval 秒] [--timeout 秒]
                                    提交转链任务（1~50 条，--file 按行读取，忽略空行与 # 注释）
  query <task_id> [--wait] [--interval 秒] [--timeout 秒]
                                    查询任务状态与结果
  quota                             查询配额与个人信息
  logout                            登出当前账号（服务端吊销 token + 清除本地保存的 token，用于切换账号）
  config set base-url <url>         设置后端服务地址
  config set insecure true|false    是否忽略 HTTPS 证书校验（自签/域名不匹配证书时开）
  config show                       查看当前配置（token 脱敏）

全局参数: --token <token>（临时覆盖配置）  --base-url <url>（默认 ${DEFAULT_BASE_URL}）`;

// ---------------------------------------------------------------- 输出

function printOk(data) {
  process.stdout.write(JSON.stringify({ ok: true, data }) + '\n');
}

function printFail(code, message) {
  process.stdout.write(JSON.stringify({ ok: false, code, message }) + '\n');
}

/** 错误 → 退出码映射 + 可操作提示。 */
function exitWithError(err) {
  if (err instanceof UsageError) {
    printFail(1001, `参数错误: ${err.message}`);
    process.stderr.write(USAGE + '\n');
    process.exit(1);
  }
  if (err instanceof BizError) {
    let message = err.message;
    let exitCode = 5;
    if (err.code === 1001) {
      exitCode = 1;  // 服务端参数错误与本地参数错误同一退出码
    } else if (err.code === 1002 || err.code === 1003) {
      exitCode = 2;
      message = `${err.message}（token 已失效或未登录，请执行 login 重新登录）`;
    } else if (err.code === 3001) {
      exitCode = 3;
      message = '配额不足，请联系管理员充值';
    } else if (err.code === 3003) {
      message = `${err.message}（请检查 task_id 是否正确、是否属于当前账号）`;
    } else if (err.code === 2003) {
      message = `${err.message}（终端无法完成图形验证码，请改用 --link 扫码/链接方式：node cli.js register --link 或 node cli.js login --link）`;
    } else if (err.code === 4290) {
      message = `${err.message}（请稍后重试）`;
    }
    printFail(err.code, message);
    process.exit(exitCode);
  }
  if (err instanceof NetworkError) {
    printFail(err.code, `${err.message}（请检查后端服务是否已启动、base-url 是否正确）`);
    process.exit(4);
  }
  printFail('INTERNAL_ERROR', err && err.message ? err.message : String(err));
  process.exit(5);
}

// ---------------------------------------------------------------- 轮询

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

/** 轮询任务直到终态；进度走 stderr，超时抛 TIMEOUT 业务错误（携带最后一次状态）。 */
async function pollTask(client, taskId, { intervalSec = 2, timeoutSec = 120 } = {}) {
  const deadline = Date.now() + timeoutSec * 1000;
  for (;;) {
    const task = await client.getTask(taskId);
    if (TERMINAL_STATUS.has(task.status)) return task;
    process.stderr.write(
      `[wait] task_id=${taskId} status=${task.status} success=${task.success_count} fail=${task.fail_count}\n`);
    if (Date.now() + intervalSec * 1000 > deadline) {
      const err = new BizError('TIMEOUT', `轮询超时（${timeoutSec}s），任务仍为 ${task.status} 状态，可稍后执行 query ${taskId} 查询`);
      err.data = task;
      throw err;
    }
    await sleep(intervalSec * 1000);
  }
}

function parsePositiveNumber(value, name, fallback) {
  if (value === undefined) return fallback;
  const n = Number(value);
  if (!Number.isFinite(n) || n <= 0) throw new UsageError(`--${name} 需为正数，收到: ${value}`);
  return n;
}

// ---------------------------------------------------------------- 各命令

async function cmdRegister(opts) {
  const cfg = resolveConfig(opts);
  if (opts.link) return cmdSessionLink(cfg, 'register');
  if (opts.check) return cmdSessionCheck(cfg, opts, 'register');
  const client = new ApiClient({ baseUrl: cfg.baseUrl });
  const data = await runRegister(client);
  printOk(data);
}

async function cmdLogin(opts) {
  const cfg = resolveConfig(opts);
  if (opts.link) return cmdSessionLink(cfg, 'login');
  if (opts.check) return cmdSessionCheck(cfg, opts, 'login');

  const phone = opts.phone;
  if (!phone || !PHONE_RE.test(phone)) throw new UsageError('login 需要 --phone（1 开头 11 位手机号），或使用 --link 扫码/链接登录');
  let password = opts.password;
  if (password === undefined) {
    const rl = createRl();
    try {
      password = await askHidden(rl, '密码: ');
    } finally {
      rl.close();
    }
  }
  if (!password) throw new UsageError('密码不能为空');
  const client = new ApiClient({ baseUrl: cfg.baseUrl });
  const data = await client.login(phone, password);
  saveConfig({ base_url: cfg.baseUrl, token: data.token });
  process.stderr.write('登录成功，token 已保存到配置文件\n');
  printOk({ phone, quota_balance: data.quota_balance });
}

/** login/register --link: 创建会话，输出二维码/链接，由用户在浏览器（手机）完成操作。 */
async function cmdSessionLink(cfg, scene) {
  const client = new ApiClient({ baseUrl: cfg.baseUrl });
  const data = await client.createCliSession();
  const isRegister = scene === 'register';
  const pageUrl = cfg.baseUrl + (isRegister ? data.register_path : data.login_path);
  const qrUrl = cfg.baseUrl + (isRegister ? data.register_qr_path : data.qr_path);
  const action = isRegister ? '注册' : '登录';
  // 给 AI agent 的用户引导话术走 stderr (stdout 只输出 JSON)
  process.stderr.write(
    `请把下面这段${action}引导原样发给用户：\n` +
    '----\n' +
    (isRegister
      ? '需要先注册账号（注册即送 10 条免费配额；不注册不登录没有配额，无法使用转链）。请用手机扫码或打开链接注册：\n\n'
      : '需要先登录。请用手机扫码或打开链接登录账号：\n\n') +
    `${action}方式（二选一）\n` +
    `二维码图片：${qrUrl}\n` +
    `${action}链接：${pageUrl}\n` +
    `access_token（${action}后校验用）：${data.access_token}\n` +
    `扫码/${action}完成后告诉我一声，我会执行校验并保存凭证，然后继续之前的操作：\n\n` +
    `node cli.js ${scene} --check --access-token "${data.access_token}"\n` +
    '（注册/使用中如遇问题，请拨打客服电话 18722121663）\n' +
    '----\n');
  printOk({
    qr_url: qrUrl,
    [isRegister ? 'register_url' : 'login_url']: pageUrl,
    access_token: data.access_token,
    expires_in: data.expires_in,
  });
}

/** login/register --check: 用户完成后确认；ready 时保存 token。 */
async function cmdSessionCheck(cfg, opts, scene) {
  const action = scene === 'register' ? '注册' : '登录';
  const accessToken = opts.accessToken;
  if (!accessToken || !/^[0-9a-f]{16,64}$/.test(accessToken)) {
    throw new UsageError(`${scene} --check 需要 --access-token（${scene} --link 下发的十六进制串）`);
  }
  const client = new ApiClient({ baseUrl: cfg.baseUrl });
  const data = await client.checkCliSession(accessToken);
  if (data.status === 'pending') {
    printFail('LOGIN_PENDING', `用户尚未完成${action}，请提醒用户完成扫码/链接${action}后再执行本命令`);
    process.exit(2);
  }
  if (data.status !== 'ready' || !data.token) {
    printFail('LOGIN_EXPIRED', `${action}会话已过期或已使用，请重新执行 ${scene} --link 发起${action}`);
    process.exit(2);
  }
  saveConfig({ base_url: cfg.baseUrl, token: data.token });
  process.stderr.write(`${action}成功，token 已保存到配置文件\n`);
  printOk({ phone: data.phone, quota_balance: data.quota_balance });
}

function collectUrls(opts) {
  const urls = [...(opts.url || [])];
  if (opts.file) {
    let content;
    try {
      content = fs.readFileSync(opts.file, 'utf8');
    } catch {
      throw new UsageError(`无法读取文件: ${opts.file}`);
    }
    for (const line of content.split(/\r?\n/)) {
      const s = line.trim();
      if (!s || s.startsWith('#')) continue;
      urls.push(s);
    }
  }
  if (urls.length < MIN_BATCH) throw new UsageError('请通过 --url 或 --file 提供至少 1 条 URL');
  if (urls.length > MAX_BATCH) throw new UsageError(`超出单次批量上限（${MAX_BATCH} 条），当前 ${urls.length} 条`);
  return urls;
}

function requireToken(cfg) {
  if (!cfg.token) throw new BizError(1002, '未登录：缺少 token');
}

async function cmdSubmit(opts) {
  const cfg = resolveConfig(opts);
  requireToken(cfg);
  const urls = collectUrls(opts);
  const client = new ApiClient({ baseUrl: cfg.baseUrl, token: cfg.token });
  const items = urls.map((url, i) => ({ id: i + 1, url }));
  // 幂等键按 URL 内容派生 (sha256 截断): 同一批 URL 重试/重复提交复用同一键,
  // 服务端幂等返回原任务, 不会重复扣费; 内容变化自动得到新键
  const idempotencyKey = crypto.createHash('sha256').update(urls.join('\n')).digest('hex').slice(0, 32);
  process.stderr.write(`提交 ${items.length} 条 URL（幂等键 ${idempotencyKey}）...\n`);
  const data = await client.submitTask(items, idempotencyKey);
  if (!opts.wait) {
    printOk(data);
    return;
  }
  process.stderr.write(`任务已创建 task_id=${data.task_id}，等待结果...\n`);
  const task = await pollTask(client, data.task_id, {
    intervalSec: parsePositiveNumber(opts.interval, 'interval', 2),
    timeoutSec: parsePositiveNumber(opts.timeout, 'timeout', 120),
  });
  printOk(task);
}

async function cmdQuery(args, opts) {
  const taskId = args[0];
  if (!taskId) throw new UsageError('query 需要 task_id 参数');
  const cfg = resolveConfig(opts);
  requireToken(cfg);
  const client = new ApiClient({ baseUrl: cfg.baseUrl, token: cfg.token });
  if (!opts.wait) {
    printOk(await client.getTask(taskId));
    return;
  }
  const task = await pollTask(client, taskId, {
    intervalSec: parsePositiveNumber(opts.interval, 'interval', 2),
    timeoutSec: parsePositiveNumber(opts.timeout, 'timeout', 120),
  });
  printOk(task);
}

async function cmdQuota(opts) {
  const cfg = resolveConfig(opts);
  requireToken(cfg);
  const client = new ApiClient({ baseUrl: cfg.baseUrl, token: cfg.token });
  printOk(await client.profile());
}

/** version: 输出 skill 名/版本/node 版本/配置路径，供排查"装的是哪一版"。 */
function cmdVersion() {
  printOk({
    name: SKILL_NAME,
    version: SKILL_VERSION,
    cli_path: __filename,
    node_version: process.version,
    config_path: configPath(),
  });
}

async function cmdLogout(opts) {
  const cfg = resolveConfig(opts);
  if (!cfg.token) throw new BizError(1002, '未登录：本地没有已保存的 token');
  const client = new ApiClient({ baseUrl: cfg.baseUrl, token: cfg.token });
  try {
    await client.logout();  // 服务端吊销 token (黑名单); 失败不阻塞本地清理
  } catch (err) {
    process.stderr.write(`服务端登出异常（已忽略，继续清除本地 token）: ${err.message}\n`);
  }
  saveConfig({ token: '' });
  process.stderr.write('已登出，本地 token 已清除；可执行 login --link 登录其他账号\n');
  printOk({ logged_out: true });
}

async function cmdConfig(args, opts) {
  const sub = args[0];
  if (sub === 'set' && args[1] === 'base-url') {
    const url = args[2];
    if (!url || !/^https?:\/\//.test(url)) throw new UsageError('config set base-url 需要 http(s):// 开头的地址');
    saveConfig({ base_url: url.replace(/\/+$/, '') });
    process.stderr.write(`base_url 已保存到 ${configPath()}\n`);
    printOk({ base_url: loadConfig().base_url });
    return;
  }
  if (sub === 'set' && args[1] === 'insecure') {
    const v = args[2];
    if (v !== 'true' && v !== 'false') throw new UsageError('config set insecure 需要 true 或 false');
    saveConfig({ insecure: v === 'true' });
    process.stderr.write(`insecure 已保存到 ${configPath()}\n`);
    printOk({ insecure: loadConfig().insecure === true });
    return;
  }
  if (sub === 'show') {
    const cfg = resolveConfig(opts);
    printOk({
      base_url: cfg.baseUrl,
      insecure: cfg.insecure,
      token: maskToken(cfg.token),
      config_path: configPath(),
    });
    return;
  }
  throw new UsageError('config 仅支持: config set base-url <url> / config set insecure true|false / config show');
}

// ---------------------------------------------------------------- 入口

async function main() {
  const { cmd, args, opts } = parseArgs(process.argv.slice(2));
  if (opts.help || !cmd) throw new UsageError('缺少命令');
  // insecure=true 时忽略 HTTPS 证书校验 (服务端自签/域名不匹配证书)
  if (resolveConfig(opts).insecure) allowInsecureTls();
  switch (cmd) {
    case 'version': return cmdVersion();
    case 'register': return cmdRegister(opts);
    case 'login': return cmdLogin(opts);
    case 'submit': return cmdSubmit(opts);
    case 'query': return cmdQuery(args, opts);
    case 'quota': return cmdQuota(opts);
    case 'logout': return cmdLogout(opts);
    case 'config': return cmdConfig(args, opts);
    default: throw new UsageError(`未知命令: ${cmd}`);
  }
}

main().catch(exitWithError);
