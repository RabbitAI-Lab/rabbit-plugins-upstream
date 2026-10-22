/**
 * xiaoai-bridge 核心逻辑。
 *
 * 这里只放可离线测试的纯函数与少量本地 IO，CLI/网络逻辑在 xiaoai-listen.js。
 *
 * 安全背景：
 * @mi-gpt/miot 会把包含 passToken / serviceToken 的会话缓存写到
 * `process.cwd()` 下的 `.mi.json`，因此 CLI 必须在登录前把 cwd 切到一个
 * 私有目录（见 ensureStateDir 与 xiaoai-listen.js 的 prepareState）。
 */

import fs from "node:fs";
import os from "node:os";
import path from "node:path";

export const VERSION = "1.1.0";

export const DEFAULT_POLL_INTERVAL_MS = 1000;
export const MIN_POLL_INTERVAL_MS = 500;
export const MAX_POLL_INTERVAL_MS = 60000;
export const DEFAULT_TRIGGER_PREFIX = "请";
export const MAX_TTS_TEXT_LENGTH = 1000;

/** 默认缓存目录：系统临时目录下的独立子目录，避免写进技能目录。 */
export const DEFAULT_STATE_DIR = path.join(os.tmpdir(), "xiaoai-bridge");

const TRUE_VALUES = new Set(["1", "true", "yes", "on"]);

export class ConfigError extends Error {
  constructor(message) {
    super(message);
    this.name = "ConfigError";
    this.code = "CONFIG_ERROR";
  }
}

function isTrue(value) {
  return TRUE_VALUES.has(String(value ?? "").trim().toLowerCase());
}

function parsePollInterval(raw) {
  const value = Number.parseInt(String(raw ?? "").trim(), 10);
  if (!Number.isFinite(value)) {
    return DEFAULT_POLL_INTERVAL_MS;
  }
  return Math.min(MAX_POLL_INTERVAL_MS, Math.max(MIN_POLL_INTERVAL_MS, value));
}

/**
 * 解析并校验环境变量。配置问题一律抛 ConfigError。
 *
 * @param {Record<string, string | undefined>} [env]
 */
export function parseConfig(env = process.env) {
  const userId = String(env.MI_USER_ID ?? "").trim();
  if (!/^\d+$/.test(userId)) {
    throw new ConfigError(
      "MI_USER_ID 缺失或不是纯数字小米 ID（注意：不是手机号或邮箱，见小米账号「个人信息 - 小米 ID」）",
    );
  }

  const did = String(env.MI_DEVICE_ID ?? "").trim();
  if (!did) {
    throw new ConfigError("MI_DEVICE_ID 缺失（可填设备名称、miotDID 或 MAC，DEBUG=true 可查看设备列表）");
  }

  const passToken = String(env.MI_PASS_TOKEN ?? "").trim();
  const password = String(env.MI_PASSWORD ?? "").trim();
  if (!passToken && !password) {
    throw new ConfigError("缺少 MI_PASS_TOKEN 或 MI_PASSWORD（推荐 passToken，密码登录可能触发安全验证）");
  }

  const rawPrefix = env.TRIGGER_PREFIX;
  const triggerPrefix = rawPrefix === undefined ? DEFAULT_TRIGGER_PREFIX : String(rawPrefix).trim();
  const allowUnfiltered = isTrue(env.XIAOAI_ALLOW_UNFILTERED);
  if (!triggerPrefix && !allowUnfiltered) {
    throw new ConfigError(
      "TRIGGER_PREFIX 为空会处理所有语音消息。如确需如此，请显式设置 XIAOAI_ALLOW_UNFILTERED=true",
    );
  }

  return {
    userId,
    did,
    passToken,
    password,
    debug: isTrue(env.DEBUG),
    triggerPrefix,
    allowUnfiltered,
    pollIntervalMs: parsePollInterval(env.POLL_INTERVAL),
    stateDir: path.resolve(String(env.XIAOAI_STATE_DIR ?? "").trim() || DEFAULT_STATE_DIR),
  };
}

/**
 * 创建私有状态目录（优先 0700），返回绝对路径。
 *
 * @param {string} [dir]
 * @returns {string}
 */
export function ensureStateDir(dir = DEFAULT_STATE_DIR) {
  const target = path.resolve(dir || DEFAULT_STATE_DIR);
  try {
    fs.mkdirSync(target, { recursive: true, mode: 0o700 });
  } catch (error) {
    throw new ConfigError(
      `无法创建会话缓存目录 ${target}：${error.message}。可通过 XIAOAI_STATE_DIR 指定其他目录。`,
    );
  }

  let stat;
  try {
    stat = fs.statSync(target);
  } catch (error) {
    throw new ConfigError(`无法访问会话缓存目录 ${target}：${error.message}`);
  }
  if (!stat.isDirectory()) {
    throw new ConfigError(`会话缓存路径 ${target} 已存在但不是目录`);
  }

  try {
    fs.chmodSync(target, 0o700);
  } catch {
    // Windows 以及部分受限文件系统不支持 POSIX 权限位，忽略即可。
  }

  return target;
}

/**
 * 尽力把缓存文件权限收紧到 0600。
 *
 * @param {string} filePath
 * @returns {boolean}
 */
export function restrictFilePermissions(filePath) {
  try {
    fs.chmodSync(filePath, 0o600);
    return true;
  } catch {
    return false;
  }
}

/**
 * 从对话记录中提取需要处理的语音指令。
 *
 * 关键点：
 * - 小米接口返回的记录按时间「新 -> 旧」排列，且包含游标消息本身；
 * - 必须先把所有 time > since 的记录收集起来，最后统一推进 lastTimestamp，
 *   否则会漏掉同一轮里的多条新消息；
 * - 输出按时间「旧 -> 新」排序，便于消费方顺序处理。
 *
 * @param {Array<{ time?: number, query?: string }>} records
 * @param {{ prefix?: string, since?: number, allowUnfiltered?: boolean }} [options]
 * @returns {{ messages: Array<{ type: "message", text: string, originalText: string, timestamp: number }>, lastTimestamp: number }}
 */
export function extractCommands(records, options = {}) {
  const prefix = options.prefix === undefined ? DEFAULT_TRIGGER_PREFIX : String(options.prefix);
  const allowUnfiltered = options.allowUnfiltered === true;
  const since = Number.isFinite(options.since) ? Number(options.since) : 0;

  if (!prefix && !allowUnfiltered) {
    throw new ConfigError(
      "TRIGGER_PREFIX 为空会处理所有语音消息。如确需如此，请显式设置 XIAOAI_ALLOW_UNFILTERED=true",
    );
  }

  const messages = [];
  let lastTimestamp = since;

  for (const record of Array.isArray(records) ? records : []) {
    const timestamp = Number(record?.time);
    if (!Number.isFinite(timestamp)) {
      continue;
    }

    if (timestamp > lastTimestamp) {
      lastTimestamp = timestamp;
    }
    if (timestamp <= since) {
      continue;
    }

    const query = typeof record?.query === "string" ? record.query : "";
    if (!query) {
      continue;
    }
    if (prefix && !query.startsWith(prefix)) {
      continue;
    }

    const text = (prefix ? query.slice(prefix.length) : query).trim();
    if (!text) {
      continue;
    }

    messages.push({
      type: "message",
      text,
      originalText: query,
      timestamp,
    });
  }

  messages.sort((a, b) => a.timestamp - b.timestamp);
  return { messages, lastTimestamp };
}

/**
 * 轮询一次并把结果转换为消息列表。
 *
 * @param {{ getConversations: (options: { limit: number, timestamp: number }) => Promise<{ records?: Array<{ time?: number, query?: string }> } | undefined> }} client
 * @param {{ lastTimestamp: number, triggerPrefix: string, allowUnfiltered?: boolean }} state
 */
export async function pollOnce(client, state) {
  const conversations = await client.getConversations({
    limit: 10,
    timestamp: state.lastTimestamp,
  });

  const { messages, lastTimestamp } = extractCommands(conversations?.records, {
    prefix: state.triggerPrefix,
    since: state.lastTimestamp,
    allowUnfiltered: state.allowUnfiltered === true,
  });

  state.lastTimestamp = lastTimestamp;
  return messages;
}

/**
 * 在回调执行期间把 console.log 重定向到 stderr。
 *
 * @mi-gpt/miot 在 DEBUG 模式会用 console.log 打印设备列表，直接混进监听模式的
 * stdout 会破坏「stdout 只有 JSON」的契约，因此在监听/播报模式初始化时启用。
 *
 * @template T
 * @param {() => Promise<T>} fn
 * @returns {Promise<T>}
 */
export async function withLogsToStderr(fn) {
  const originalLog = console.log;
  console.log = (...args) => console.error(...args);
  try {
    return await fn();
  } finally {
    console.log = originalLog;
  }
}
