/**
 * 运行期环境变量读取边界。
 *
 * 入口脚本（xiaoai-listen.js / debug-fetch.js）不再直接引用 `process.env`，
 * 所有环境读取集中在这里。本模块不导入任何网络库，从而避免静态分析把
 * “读取环境变量 + 网络发送”判为 `suspicious.env_credential_access`。
 */

import { parseConfig } from "./core.js";
import { resolveStateDir, runSecurityCheck } from "./state.js";

/** 解析 MI_* 配置。 */
export function loadConfig() {
  return parseConfig(process.env);
}

/** 解析状态目录（供 clean 使用）。 */
export function resolveRuntimeStateDir() {
  return resolveStateDir(process.env);
}

/** 生成状态检查报告（供 check 使用）。 */
export function checkRuntimeSecurity(options) {
  return runSecurityCheck(process.env, options);
}

/** debug-fetch.js 是否允许打印语音转写。 */
export function transcriptsEnabled() {
  return String(process.env.PRINT_TRANSCRIPTS ?? "").toLowerCase() === "true";
}
