#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const DEFAULT_BASE_URL = 'https://ima.qq.com';
// V1.0.7+：凭证单一来源 = 环境变量（IMA_OPENAPI_CLIENTID / IMA_OPENAPI_APIKEY）。
// 强制设置：未设置即明确报错，不做任何文件/多层级自动降级查找。
// ima.copilot 环境已由平台自动注入；自建环境需主动 export（见 SKILL.md「Credential Check」）。

// Only one category of errors:
//   -100: programmatic error (bad args, missing credentials, network, etc.)
const ERR_PROGRAMMATIC = -100;

function loadCredentials(options = {}) {
  // 单一来源：环境变量（options 显式入参仅限程序内部主动传入，不属于自动降级）
  const clientId =
    options.clientId ||
    process.env.IMA_OPENAPI_CLIENTID ||
    process.env.IMA_CLIENT_ID;
  const apiKey =
    options.apiKey ||
    process.env.IMA_OPENAPI_APIKEY ||
    process.env.IMA_API_KEY;

  if (!clientId || !apiKey) {
    const err = new Error(
      '未设置凭证环境变量 IMA_OPENAPI_CLIENTID / IMA_OPENAPI_APIKEY，技能无法使用。' +
      'ima.copilot 环境已自动注入，无需配置；自建环境请主动 export' +
      '（可写入 ~/.bashrc 或 ~/.zshrc；Windows 用系统环境变量）。凭证获取见 SKILL.md「Credential Check」。'
    );
    err.code = ERR_PROGRAMMATIC;
    err.msg = err.message;
    throw err;
  }

  return { clientId, apiKey };
}

function loadSkillVersion(options = {}) {
  if (options.skillVersion) return options.skillVersion;
  if (process.env.IMA_SKILL_VERSION) return process.env.IMA_SKILL_VERSION;

  const metaPath = path.join(__dirname, 'meta.json');
  try {
    const meta = JSON.parse(fs.readFileSync(metaPath, 'utf8'));
    return meta.version || 'unknown';
  } catch {
    return 'unknown';
  }
}

async function postJson(apiPath, body, requestOptions) {
  const { clientId, apiKey, skillVersion, baseUrl } = requestOptions;

  const res = await fetch(`${baseUrl}/${apiPath}`, {
    method: 'POST',
    headers: {
      'ima-openapi-clientid': clientId,
      'ima-openapi-apikey': apiKey,
      'ima-openapi-ctx': `skill_version=${skillVersion}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
  });

  return await res.text();
}

async function imaApi(apiPath, body, options = {}) {
  const baseUrl = options.baseUrl || process.env.IMA_BASE_URL || DEFAULT_BASE_URL;
  const { clientId, apiKey } = loadCredentials(options);
  const skillVersion = loadSkillVersion(options);

  const requestOptions = {
    clientId,
    apiKey,
    skillVersion,
    baseUrl,
  };

  return postJson(apiPath, body, requestOptions);
}

function parseBody(raw) {
  if (!raw || !raw.trim()) return {};

  try {
    return JSON.parse(raw);
  } catch {
    const err = new Error('invalid JSON body');
    err.code = ERR_PROGRAMMATIC;
    err.msg = '请求 body 不是合法的 JSON，请检查输入。';
    throw err;
  }
}

function parseOptions(raw, restArgs) {
  let options = {};

  if (raw && raw.trim()) {
    try {
      options = JSON.parse(raw);
    } catch {
      const err = new Error('invalid options JSON');
      err.code = ERR_PROGRAMMATIC;
      err.msg = 'options 参数不是合法的 JSON，请检查输入。';
      throw err;
    }
  }

  return options;
}

async function main() {
  const [, , apiPath, rawBody = '{}', rawOptions = '{}', ...rest] = process.argv;

  if (!apiPath) {
    process.stderr.write(JSON.stringify({ code: ERR_PROGRAMMATIC, msg: '缺少必需参数：apiPath。' }));
    // Unix exit codes are 0-255; use 1 as generic failure. Callers should parse stderr JSON for the real code.
    process.exit(1);
  }

  try {
    const body = parseBody(rawBody);
    const options = parseOptions(rawOptions, rest);
    const resp = await imaApi(apiPath, body, options);
    process.stdout.write(resp);
  } catch (err) {
    const code = err && typeof err.code === 'number' ? err.code : ERR_PROGRAMMATIC;
    const msg = (err && err.msg) || (err && err.message) || '未知错误';
    process.stderr.write(JSON.stringify({ code, msg }));
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

module.exports = {
  imaApi,
  ERR_PROGRAMMATIC,
};
