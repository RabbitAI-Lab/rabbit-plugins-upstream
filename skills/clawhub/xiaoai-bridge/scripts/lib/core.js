/**
 * xiaoai-bridge 核心逻辑。
 *
 * 这里放可离线测试的纯函数与少量配置解析，CLI/网络逻辑在 xiaoai-listen.js。
 *
 * 安全背景：
 * @mi-gpt/miot 会把包含 passToken / serviceToken 的会话缓存写到
 * `process.cwd()` 下的 `.mi.json`，因此 CLI 必须在登录前把 cwd 切到一个
 * 经过校验的私有目录（目录/文件校验逻辑见 lib/state.js）。
 */

import { ConfigError } from "./errors.js";
import { resolveStateDir } from "./state.js";

export { ConfigError };

export const VERSION = "1.2.4";

export const DEFAULT_POLL_INTERVAL_MS = 1000;
export const MIN_POLL_INTERVAL_MS = 500;
export const MAX_POLL_INTERVAL_MS = 60000;
export const DEFAULT_TRIGGER_PREFIX = "请";
export const MAX_TTS_TEXT_LENGTH = 1000;

const TRUE_VALUES = new Set(["1", "true", "yes", "on"]);

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
 * 注意：这里不创建目录、不切工作目录，副作用留给 prepareSessionState。
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

  const stateDirInfo = resolveStateDir(env);

  return {
    userId,
    did,
    passToken,
    password,
    debug: isTrue(env.DEBUG),
    triggerPrefix,
    allowUnfiltered,
    pollIntervalMs: parsePollInterval(env.POLL_INTERVAL),
    stateDir: stateDirInfo.dir,
    stateDirSource: stateDirInfo.source,
    allowInsecureStateDir: isTrue(env.XIAOAI_ALLOW_INSECURE_STATE_DIR),
  };
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
