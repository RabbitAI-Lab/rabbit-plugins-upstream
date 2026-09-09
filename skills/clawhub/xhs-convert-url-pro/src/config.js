'use strict';
/**
 * src/config.js — 配置文件读写与配置解析。
 *
 * 优先级: --base-url/--token 命令行参数 > 环境变量(XHS_BASE_URL) > 配置文件 > 内置默认。
 *
 * 配置文件位置（v1.1.0 起，用户级外部路径，升级 skill 不丢配置）:
 *   1. 环境变量 XHS_CONFIG_PATH 指定的路径（测试隔离用）
 *   2. 默认 ~/.xhs-convert/config.json
 *   3. 旧版配置在 skill 目录下的 config.local.json 会一次性自动迁移（拷贝）到上述默认路径
 */

const fs = require('fs');
const path = require('path');
const os = require('os');

const DEFAULT_BASE_URL = 'http://st.aidata366.com';

/** 用户级配置目录: ~/.xhs-convert */
function userConfigDir() {
  return path.join(os.homedir(), '.xhs-convert');
}

/** 用户级配置文件路径: ~/.xhs-convert/config.json */
function userConfigPath() {
  return path.join(userConfigDir(), 'config.json');
}

/** 旧版配置路径: skill 安装目录下 config.local.json */
function legacyConfigPath() {
  return path.join(__dirname, '..', 'config.local.json');
}

/**
 * 确定生效的配置文件路径，并处理一次性迁移:
 * - XHS_CONFIG_PATH 显式指定时直接使用，不做迁移
 * - ~/.xhs-convert/config.json 已存在时直接使用
 * - 否则若旧版 config.local.json 存在，拷贝到新路径（迁移失败则继续用旧路径，不阻塞）
 */
function configPath() {
  if (process.env.XHS_CONFIG_PATH) return process.env.XHS_CONFIG_PATH;
  const newPath = userConfigPath();
  if (fs.existsSync(newPath)) return newPath;
  const legacy = legacyConfigPath();
  if (fs.existsSync(legacy)) {
    try {
      fs.mkdirSync(userConfigDir(), { recursive: true });
      fs.copyFileSync(legacy, newPath);
      process.stderr.write(`[config] 已将旧配置迁移到 ${newPath}（原文件保留，可手动删除）\n`);
      return newPath;
    } catch {
      process.stderr.write(`[config] 配置迁移失败，继续使用旧路径 ${legacy}\n`);
      return legacy;
    }
  }
  return newPath;
}

/** 读取配置文件；不存在或损坏时按空配置处理。 */
function loadConfig() {
  try {
    return JSON.parse(fs.readFileSync(configPath(), 'utf8'));
  } catch {
    return {};
  }
}

/** 合并写配置文件（保留未涉及的字段）；自动创建父目录。 */
function saveConfig(patch) {
  const target = configPath();
  let current = {};
  try {
    current = JSON.parse(fs.readFileSync(target, 'utf8'));
  } catch {
    // 目标不存在或损坏则整体覆盖
  }
  const next = { ...current, ...patch };
  fs.mkdirSync(path.dirname(target), { recursive: true });
  fs.writeFileSync(target, JSON.stringify(next, null, 2) + '\n', 'utf8');
  return next;
}

/**
 * 解析生效配置。
 * @param {{token?: string, baseUrl?: string}} overrides 命令行参数（--token / --base-url）
 * insecure: 忽略 HTTPS 证书校验（服务端使用自签/域名不匹配证书时开启），
 *           配置文件 insecure=true 或环境变量 XHS_INSECURE=1
 */
function resolveConfig(overrides = {}) {
  const file = loadConfig();
  return {
    baseUrl: overrides.baseUrl || process.env.XHS_BASE_URL || file.base_url || DEFAULT_BASE_URL,
    token: overrides.token !== undefined ? overrides.token : (file.token || ''),
    insecure: process.env.XHS_INSECURE === '1' || file.insecure === true,
  };
}

/** token 脱敏：仅显示前 12 位 + ... */
function maskToken(token) {
  if (!token) return null;
  return token.length > 12 ? token.slice(0, 12) + '...' : token.slice(0, 4) + '...';
}

module.exports = {
  DEFAULT_BASE_URL,
  configPath,
  userConfigDir,
  userConfigPath,
  legacyConfigPath,
  loadConfig,
  saveConfig,
  resolveConfig,
  maskToken,
};
