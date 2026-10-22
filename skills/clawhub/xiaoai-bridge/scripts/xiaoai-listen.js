#!/usr/bin/env node
/**
 * 小爱音箱消息监听 / TTS 播报桥接（CLI 入口）。
 *
 * 命令：
 *   node xiaoai-listen.js                监听并把语音指令以 JSON 行写到 stdout
 *   node xiaoai-listen.js speak "文本"   通过小爱音箱 TTS 播报
 *   node xiaoai-listen.js test           测试登录与设备连接
 *   node xiaoai-listen.js clean          清理本地会话缓存（含 passToken）
 */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import dotenv from "dotenv";
import { getMiNA } from "@mi-gpt/miot";

import {
  ConfigError,
  DEFAULT_STATE_DIR,
  MAX_TTS_TEXT_LENGTH,
  VERSION,
  ensureStateDir,
  parseConfig,
  pollOnce,
  restrictFilePermissions,
  withLogsToStderr,
} from "./lib/core.js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SKILL_ROOT = path.resolve(__dirname, "..");

const USAGE = `用法：
  node scripts/xiaoai-listen.js                 监听语音指令（stdout 仅输出 JSON 行）
  node scripts/xiaoai-listen.js speak "文本"    TTS 播报
  node scripts/xiaoai-listen.js test            测试登录与设备
  node scripts/xiaoai-listen.js clean           清理本地会话缓存
  node scripts/xiaoai-listen.js --help          显示帮助
  node scripts/xiaoai-listen.js --version       显示版本

环境变量：
  MI_USER_ID              必填，纯数字小米 ID
  MI_DEVICE_ID            必填，设备名称 / miotDID / MAC
  MI_PASS_TOKEN           推荐，与 MI_PASSWORD 二选一
  MI_PASSWORD             备选，可能触发安全验证
  TRIGGER_PREFIX          触发词前缀，默认“请”
  XIAOAI_ALLOW_UNFILTERED 设为 true 才允许空触发词（处理所有消息）
  POLL_INTERVAL           轮询间隔毫秒，默认 1000（范围 500-60000）
  XIAOAI_STATE_DIR        会话缓存目录，默认系统临时目录下的 xiaoai-bridge
  XIAOAI_ENV_FILE         指定 .env 路径，默认 scripts/.env 或技能根目录 .env
  DEBUG                   设为 true 输出调试信息（stderr）`;

function log(line) {
  process.stderr.write(`${line}\n`);
}

/**
 * 加载 .env：优先 scripts/.env，其次技能根目录 .env。
 * 使用绝对路径，避免依赖当前工作目录。
 */
function loadEnvironment() {
  const explicit = String(process.env.XIAOAI_ENV_FILE ?? "").trim();
  const candidates = explicit
    ? [path.resolve(explicit)]
    : [path.join(__dirname, ".env"), path.join(SKILL_ROOT, ".env")];

  for (const file of candidates) {
    // quiet: true 避免 dotenv v17 向 stdout 打印注入提示，破坏 JSON 契约。
    dotenv.config({ path: file, quiet: true });
  }
}

/**
 * 提示历史版本遗留的凭据文件。只告警，不自动读取或删除。
 */
function warnLegacyCache() {
  const candidates = new Set([
    path.join(__dirname, ".mi.json"),
    path.join(SKILL_ROOT, ".mi.json"),
    path.join(process.cwd(), ".mi.json"),
  ]);

  for (const file of candidates) {
    if (fs.existsSync(file)) {
      log(`⚠️  发现遗留会话文件：${file}`);
      log("    该文件可能包含小米账号凭据，请立即删除，并且不要提交到版本库。");
    }
  }
}

/**
 * 切换到私有状态目录，确保 @mi-gpt/miot 的 .mi.json 缓存不会落进技能目录。
 */
function prepareState(config) {
  warnLegacyCache();
  const stateDir = ensureStateDir(config.stateDir);
  process.chdir(stateDir);
  log(`📁 会话缓存目录：${stateDir}`);
  return stateDir;
}

async function connect(config, { redirectLogs = true } = {}) {
  log("🔌 正在连接小爱音箱...");

  const createClient = () =>
    getMiNA({
      userId: config.userId,
      passToken: config.passToken || undefined,
      password: config.password || undefined,
      did: config.did,
      debug: config.debug,
    });

  const client = redirectLogs
    ? await withLogsToStderr(createClient)
    : await createClient();

  if (!client) {
    throw new Error(
      "登录失败：请检查 MI_USER_ID、passToken/密码与 MI_DEVICE_ID（DEBUG=true 可打印设备列表）",
    );
  }

  const cacheFile = path.join(process.cwd(), ".mi.json");
  if (fs.existsSync(cacheFile)) {
    restrictFilePermissions(cacheFile);
  }

  log("✅ 连接成功");
  return client;
}

async function initSession(config, options = {}) {
  prepareState(config);
  return connect(config, options);
}

async function runListen(client, config) {
  const state = {
    lastTimestamp: Date.now(),
    triggerPrefix: config.triggerPrefix,
    allowUnfiltered: config.allowUnfiltered,
  };

  let running = true;
  let wakeFromSleep = null;
  const wait = (ms) =>
    new Promise((resolve) => {
      const timer = setTimeout(() => {
        wakeFromSleep = null;
        resolve();
      }, ms);
      wakeFromSleep = () => {
        clearTimeout(timer);
        wakeFromSleep = null;
        resolve();
      };
    });

  const stop = (signal) => {
    if (!running) {
      return;
    }
    running = false;
    log(`\n👋 收到 ${signal}，停止监听`);
    wakeFromSleep?.();
  };
  process.once("SIGINT", () => stop("SIGINT"));
  process.once("SIGTERM", () => stop("SIGTERM"));

  log("🎤 开始监听消息...");

  let failures = 0;
  let backoffMs = 1000;

  while (running) {
    try {
      const messages = await pollOnce(client, state);
      failures = 0;
      backoffMs = 1000;

      for (const message of messages) {
        process.stdout.write(`${JSON.stringify(message)}\n`);
      }
    } catch (error) {
      failures += 1;
      log(`❌ 获取消息失败（连续 ${failures} 次）：${error.message}`);
      await wait(backoffMs);
      backoffMs = Math.min(30000, backoffMs * 2);
      continue;
    }

    if (!running) {
      break;
    }
    await wait(config.pollIntervalMs);
  }
}

async function runSpeak(config, text) {
  const content = String(text ?? "").trim();
  if (!content) {
    throw new ConfigError('用法：node scripts/xiaoai-listen.js speak "要说的话"');
  }
  if (content.length > MAX_TTS_TEXT_LENGTH) {
    throw new ConfigError(`TTS 文本超过 ${MAX_TTS_TEXT_LENGTH} 字符，请先拆分后再播报`);
  }

  const client = await initSession(config);
  const ok = await client.play({ text: content });
  if (!ok) {
    throw new Error("TTS 播报失败");
  }
  log("✅ 播报已发送");
}

async function runTest(config) {
  // 测试模式保留库自身的调试输出（DEBUG=true 时可查看设备列表）。
  await initSession(config, { redirectLogs: false });
  log("✅ 连接测试通过");
}

function runClean() {
  const raw = String(process.env.XIAOAI_STATE_DIR ?? "").trim();
  const stateDir = path.resolve(raw || DEFAULT_STATE_DIR);
  const cacheFile = path.join(stateDir, ".mi.json");

  if (fs.existsSync(cacheFile)) {
    fs.rmSync(cacheFile, { force: true });
    process.stdout.write(`✅ 已删除会话缓存：${cacheFile}\n`);
  } else {
    process.stdout.write(`ℹ️  未找到会话缓存：${cacheFile}\n`);
  }

  try {
    if (fs.existsSync(stateDir) && fs.readdirSync(stateDir).length === 0) {
      fs.rmdirSync(stateDir);
      process.stdout.write(`✅ 已删除空缓存目录：${stateDir}\n`);
    }
  } catch {
    // 目录被占用时忽略即可。
  }
}

function printHelp() {
  process.stdout.write(`${USAGE}\n`);
}

async function main(argv) {
  const [command, ...rest] = argv;

  if (command === "--help" || command === "-h" || command === "help") {
    printHelp();
    return;
  }
  if (command === "--version" || command === "-V") {
    process.stdout.write(`${VERSION}\n`);
    return;
  }

  loadEnvironment();

  if (command === "clean") {
    runClean();
    return;
  }

  const config = parseConfig(process.env);

  if (command === "speak") {
    await runSpeak(config, rest.join(" "));
    return;
  }
  if (command === "test") {
    await runTest(config);
    return;
  }
  if (command === undefined) {
    const client = await initSession(config);
    await runListen(client, config);
    return;
  }

  throw new ConfigError(`未知命令：${command}\n\n${USAGE}`);
}

try {
  await main(process.argv.slice(2));
} catch (error) {
  if (error instanceof ConfigError) {
    log(`❌ 配置错误：${error.message}`);
    process.exitCode = 2;
  } else {
    log(`❌ ${error.message}`);
    process.exitCode = 1;
  }
}
