'use strict';
/**
 * src/client.js — 后端 /api/v1 API 客户端。
 *
 * - 内置全局 fetch，单次请求 15s 超时（AbortController）
 * - 统一信封 {"code","message","data"}：code !== 0 抛 BizError
 * - HTTP 层失败（连接拒绝/超时/非信封响应）抛 NetworkError
 */
const REQUEST_TIMEOUT_MS = 15000;

let _insecureNoted = false;

/** 忽略 HTTPS 证书校验（服务端自签/域名不匹配证书时由 insecure 配置开启）。进程级，仅提示一次。 */
function allowInsecureTls() {
  process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';
  if (!_insecureNoted) {
    _insecureNoted = true;
    process.stderr.write('[warn] 已按配置忽略 HTTPS 证书校验（insecure=true）\n');
  }
}

/** 业务错误：code 为后端错误码（1001/1002/3001/...） */
class BizError extends Error {
  constructor(code, message) {
    super(message);
    this.name = 'BizError';
    this.code = code;
  }
}

/** 网络/服务不可达错误 */
class NetworkError extends Error {
  constructor(message) {
    super(message);
    this.name = 'NetworkError';
    this.code = 'NETWORK_ERROR';
  }
}

class ApiClient {
  /** @param {{baseUrl: string, token?: string}} opts */
  constructor({ baseUrl, token }) {
    this.baseUrl = String(baseUrl).replace(/\/+$/, '');
    this.token = token || '';
  }

  /**
   * 发起 API 请求，成功返回信封 data。
   * 超时覆盖整个请求（含响应体读取）：超时计时器在 body 解析完成后才清除。
   * @param {'GET'|'POST'} method
   * @param {string} apiPath 以 / 开头，相对 /api/v1
   * @param {{body?: object, headers?: object}} [opts]
   */
  async request(method, apiPath, opts = {}) {
    const { body, headers = {} } = opts;
    const ctrl = new AbortController();
    const timer = setTimeout(() => ctrl.abort(), REQUEST_TIMEOUT_MS);
    let res;
    let payload = null;
    try {
      res = await fetch(this.baseUrl + '/api/v1' + apiPath, {
        method,
        headers: {
          ...(body ? { 'Content-Type': 'application/json' } : {}),
          ...(this.token ? { Authorization: `Bearer ${this.token}` } : {}),
          ...headers,
        },
        body: body ? JSON.stringify(body) : undefined,
        signal: ctrl.signal,
      });
      try {
        payload = await res.json();
      } catch (err) {
        // 读取响应体期间超时也要按超时处理, 不能当成"非 JSON"吞掉
        if (err.name === 'AbortError') throw err;
        /* 非 JSON 响应，按 HTTP 层错误处理 */
      }
    } catch (err) {
      if (err.name === 'AbortError') {
        throw new NetworkError(`请求超时（${REQUEST_TIMEOUT_MS / 1000}s）: ${this.baseUrl}`);
      }
      throw new NetworkError(`无法连接后端服务 ${this.baseUrl}: ${err.message}`);
    } finally {
      clearTimeout(timer);
    }

    if (payload && typeof payload.code === 'number') {
      if (payload.code === 0) return payload.data;
      throw new BizError(payload.code, payload.message || `业务错误 code=${payload.code}`);
    }
    if (res.status === 429) throw new BizError(4290, '触发限流，请稍后重试');
    throw new NetworkError(`后端返回异常响应 HTTP ${res.status}（期望统一信封 JSON）`);
  }

  // ---- auth ----
  sendSmsCode(phone, scene = 'register') {
    return this.request('POST', '/auth/sms-code', { body: { phone, scene } });
  }
  register(phone, code, password) {
    return this.request('POST', '/auth/register', { body: { phone, code, password } });
  }
  login(phone, password) {
    return this.request('POST', '/auth/login', { body: { phone, password } });
  }
  logout() {
    return this.request('POST', '/auth/logout');
  }

  // ---- CLI 登录会话 (扫码/链接登录) ----
  createCliSession() {
    return this.request('POST', '/auth/cli-session');
  }
  checkCliSession(accessToken) {
    return this.request('POST', '/auth/cli-session/check', { body: { access_token: accessToken } });
  }

  // ---- user ----
  profile() {
    return this.request('GET', '/user/profile');
  }

  // ---- tasks ----
  submitTask(items, idempotencyKey) {
    return this.request('POST', '/tasks', {
      body: { items },
      headers: { 'X-Idempotency-Key': idempotencyKey },
    });
  }
  getTask(taskId) {
    return this.request('GET', `/tasks/${encodeURIComponent(taskId)}`);
  }
}

module.exports = { ApiClient, BizError, NetworkError, REQUEST_TIMEOUT_MS, allowInsecureTls };
