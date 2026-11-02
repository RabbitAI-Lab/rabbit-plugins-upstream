#!/usr/bin/env node
/**
 * 小爱音箱消息监听 / TTS 播报桥接（CLI 入口）。
 *
 * 命令：
 *   node xiaoai-listen.js                监听并把语音指令以 JSON 行写到 stdout
 *   node xiaoai-listen.js speak "文本"   通过小爱音箱 TTS 播报
 *   node xiaoai-listen.js test           测试登录与设备连接
 *   node xiaoai-listen.js check          检查会话缓存目录/文件权限（不联网）
 *   node xiaoai-listen.js clean          清理本地会话缓存（含 passToken）
 */

import path from "node:path";
import { fileURLToPath } from "node:url";

import {
  ConfigError,
  MAX_TTS_TEXT_LENGTH,
  VERSION,
  pollOnce,
} from "./lib/core.js";
import { loadEnvironment } from "./lib/env.js";
import { connectMiNA } from "./lib/mi-client.js";
import { installRedactedConsole, redactSecrets } from "./lib/redact.js";
import { checkRuntimeSecurity, loadConfig, resolveRuntimeStateDir } from "./lib/runtime.js";
import {
  CACHE_FILE_NAME,
  cleanStateDir,
  findLegacyCachePaths,
  prepareSessionState,
  verifyCacheFile,
} from "./lib/state.js";

// 上游库失败时会把带 Cookie 的 axios 错误对象打到 console；
// 在加载凭据之前先安装脱敏，避免 passToken/serviceToken 进入 stderr。
installRedactedConsole();

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SKILL_ROOT = path.resolve(__dirname, "..");

const USAGE = `用法：
  node scripts/xiaoai-listen.js                 监听语音指令（stdout 仅输出 JSON 行）
  node scripts/xiaoai-listen.js speak "文本"    TTS 播报
  node scripts/xiaoai-listen.js test            测试登录与设备
  node scripts/xiaoai-listen.js check           检查缓存目录/文件权限（不联网）
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
  XIAOAI_STATE_DIR        会话缓存目录，默认当前用户的私有状态目录
  XIAOAI_ALLOW_INSECURE_STATE_DIR
                          仅在权限无法强制/ACL 无法验证时显式放行（有风险）
  XIAOAI_ENV_FILE         指定 .env 路径，默认 scripts/.env 或技能根目录 .env
  DEBUG                   设为 true 输出调试信息（stderr）`;

const ACTION_TEXT = {
  created: "新建",
  kept: "复用",
  replaced: "替换为安全文件",
  reset: "重置损坏内容",
  sanitized: "清理未知字段",
};

function log(line) {
  process.stderr.write(`${redactSecrets(line)}\n`);
}

/**
 * 提示旧版本可能遗留的凭据文件。只告警，不自动读取或删除。
 */
function warnLegacyCache(config) {
  const legacy = findLegacyCachePaths({
    scriptDir: __dirname,
    skillRoot: SKILL_ROOT,
    excludeDirs: config?.stateDir ? [config.stateDir] : [],
  });

  for (const file of legacy) {
    log(`⚠️  发现遗留会话文件：${file}`);
    log("    该文件可能包含小米账号凭据，请运行 clean 清理，并且不要提交到版本库。");
  }
}

/**
 * 校验私有状态目录，切换工作目录，并预创建 0600 的会话缓存。
 */
function prepareState(config) {
  warnLegacyCache(config);
  const session = prepareSessionState(config);

  for (const line of session.warnings) {
    log(line);
  }
  log(
    `📁 会话缓存目录：${session.dir}（来源：${
      config.stateDirSource === "env" ? "XIAOAI_STATE_DIR" : "默认"
    }）`,
  );
  if (process.platform === "win32") {
    log("🔒 目录校验通过：位于当前用户目录内，未跟随符号链接");
  } else {
    log(`🔒 目录校验通过：${session.dirMode}，属主为当前用户`);
  }
  log(
    `📝 会话缓存文件：${session.cacheFile}（${session.mode}，${
      ACTION_TEXT[session.action] ?? session.action
    }）`,
  );
  return session;
}

async function connect(config, { redirectLogs = true } = {}) {
  log("🔌 正在连接小爱音箱...");

  const client = await connectMiNA(config, { redirectLogs });

  if (!client) {
    throw new Error(
      "登录失败：请检查 MI_USER_ID、passToken/密码与 MI_DEVICE_ID（DEBUG=true 可打印设备列表）",
    );
  }

  log("✅ 连接成功");
  return client;
}

async function initSession(config, options = {}) {
  const session = prepareState(config);
  const client = await connect(config, options);

  const verified = verifyCacheFile(session.dir, {
    allowInsecure: config.allowInsecureStateDir,
    expected: session.identity ?? undefined,
  });
  for (const line of verified.warnings) {
    log(line);
  }
  log(`🔐 缓存文件校验通过：${verified.mode}`);
  return client;
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
  const resolved = resolveRuntimeStateDir();
  const primaryDir = resolved.dir;
  const legacyDirs = new Set();

  for (const file of findLegacyCachePaths({ scriptDir: __dirname, skillRoot: SKILL_ROOT })) {
    const dir = path.dirname(file);
    if (dir !== primaryDir) {
      legacyDirs.add(dir);
    }
  }

  let firstFailure = null;

  const reportResult = (dir, result, { isPrimary }) => {
    if (result.removedFile) {
      process.stdout.write(`✅ 已删除会话缓存：${path.join(dir, CACHE_FILE_NAME)}\n`);
    } else if (isPrimary) {
      process.stdout.write(`ℹ️  未找到会话缓存：${path.join(dir, CACHE_FILE_NAME)}\n`);
    }
    if (result.dirRemoved) {
      process.stdout.write(`✅ 已删除空缓存目录：${dir}\n`);
    }
    for (const note of result.notes) {
      process.stdout.write(`${note}\n`);
    }
  };

  try {
    const result = cleanStateDir(primaryDir, { removeEmptyDir: true });
    reportResult(primaryDir, result, { isPrimary: true });
  } catch (error) {
    firstFailure = error;
    log(`❌ 清理状态目录失败：${error.message}`);
  }

  for (const dir of legacyDirs) {
    try {
      // legacy 位置只删“像小米会话缓存”的文件，且绝不删除目录本身。
      const result = cleanStateDir(dir, { requireCacheSignature: true });
      reportResult(dir, result, { isPrimary: false });
    } catch (error) {
      firstFailure = firstFailure ?? error;
      log(`⚠️  跳过 ${dir}：${error.message}`);
    }
  }

  if (firstFailure) {
    throw firstFailure instanceof ConfigError
      ? firstFailure
      : new ConfigError(`清理未完成：${firstFailure.message}`);
  }
  process.stdout.write(
    "提示：删除本地缓存不等于撤销凭据；如 passToken 可能已泄露，请在小米账号中退出登录并更换 passToken。\n",
  );
}

function runCheck() {
  const report = checkRuntimeSecurity({
    scriptDir: __dirname,
    skillRoot: SKILL_ROOT,
    cwd: process.cwd(),
  });

  process.stdout.write("🔎 状态检查\n");
  for (const line of report.lines) {
    process.stdout.write(`   ${line}\n`);
  }
  process.stdout.write(`   结论：${report.ok ? "通过" : "失败"}\n`);
  process.exitCode = report.exitCode;
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

  loadEnvironment({ scriptDir: __dirname, skillRoot: SKILL_ROOT, warn: log });

  if (command === "clean") {
    runClean();
    return;
  }
  if (command === "check" || command === "doctor") {
    runCheck();
    return;
  }

  const config = loadConfig();

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
