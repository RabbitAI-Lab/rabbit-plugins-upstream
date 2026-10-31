/**
 * 共享错误类型。
 *
 * 单独成文件是为了让 core.js 与 state.js 共用同一个 ConfigError，
 * 又不会形成 ESM 循环依赖（state.js 不依赖 core.js）。
 */

export class ConfigError extends Error {
  constructor(message) {
    super(message);
    this.name = "ConfigError";
    this.code = "CONFIG_ERROR";
  }
}
