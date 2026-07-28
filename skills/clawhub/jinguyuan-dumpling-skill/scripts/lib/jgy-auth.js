'use strict';

const fs = require('node:fs');
const path = require('node:path');
const store = require('./credential-store');
const { createApiClient, ApiError } = require('./jgy-api');

/**
 * Phone-login auth state machine for the Skill runtime.
 *
 * Responsibilities (master design §8 / skill plan §7):
 * - auth-start / auth-complete drive CloudBase phone OTP via the identity service.
 * - Access token auto-refreshes 120s before expiry; a single 401 triggers one refresh + retry.
 * - invalid_grant / reuse clears local creds and asks for re-login (no infinite retry).
 * - 403 insufficient_scope is NOT treated as expiry.
 * - Tokens/codes never returned to the caller; only sanitized status.
 *
 * All I/O is injectable (api client, now) for tests; creds live under JGY_HOME.
 */

const CLIENT_ID = process.env.JGY_CLIENT_ID || 'jinguyuan-dumpling-skill';
const RESOURCE = process.env.JGY_RESOURCE || 'https://mcp.jinguyuan.cloud';
const REFRESH_SKEW_MS = 120_000;

class AuthError extends Error {
  constructor(code, message, extra = {}) {
    super(message || code);
    this.code = code;
    this.extra = extra;
  }
}

function createAuth({ api = createApiClient(), now = () => Date.now() } = {}) {
  const deviceId = store.getOrCreateDeviceId();

  async function authStart(phone) {
    if (!phone) throw new AuthError('invalid_phone', '请提供手机号。');
    let res;
    try {
      res = await api.phoneStart({ phone, device_id: deviceId });
    } catch (e) {
      throw mapApiError(e, 'start');
    }
    return {
      state: 'verification_sent',
      login_id: res.login_id,
      phone_mask: res.phone_mask,
      expires_in: res.expires_in,
      retry_after: res.retry_after,
      next_action: 'ask_user_for_verification_code',
    };
  }

  async function authComplete({ loginId, code }) {
    if (!loginId) throw new AuthError('login_not_found', '缺少 login_id，请重新开始登录。');
    if (!code) throw new AuthError('verification_invalid', '请提供验证码。');
    let res;
    try {
      res = await api.phoneVerify({ login_id: loginId, code, device_id: deviceId, client_id: CLIENT_ID });
    } catch (e) {
      throw mapApiError(e, 'verify');
    }
    persistTokens(res);
    return {
      state: 'authenticated',
      principal_id: res.user?.principal_id,
      identity_level: res.user?.identity_level,
      expires_in: res.expires_in,
    };
  }

  function authStatus() {
    const creds = store.read();
    if (!creds || !creds.refresh_token) return { authenticated: false };
    return {
      authenticated: true,
      principal_id: creds.principal_id,
      identity_level: creds.identity_level,
    };
  }

  async function logout() {
    const creds = store.read();
    if (creds && creds.refresh_token) {
      try { await api.revoke({ token: creds.refresh_token }); } catch { /* revoke is best effort */ }
    }
    store.clear();
    return { state: 'logged_out' };
  }

  /** Return a currently-valid access token, refreshing ahead of expiry. Throws AuthError otherwise. */
  async function getAccessToken() {
    let creds = store.read();
    if (!creds || !creds.refresh_token) throw new AuthError('authentication_required', '需要先完成手机号登录。', { next_action: 'start_phone_login' });
    const expiresAt = Date.parse(creds.access_expires_at || 0);
    if (creds.access_token && Number.isFinite(expiresAt) && expiresAt - now() > REFRESH_SKEW_MS) {
      return creds.access_token;
    }
    creds = await withLock(() => doRefresh());
    return creds.access_token;
  }

  async function doRefresh() {
    // Re-read inside the lock: another process may have already rotated the token.
    const creds = store.read();
    if (!creds || !creds.refresh_token) throw new AuthError('authentication_required', '需要先完成手机号登录。', { next_action: 'start_phone_login' });
    const expiresAt = Date.parse(creds.access_expires_at || 0);
    if (creds.access_token && Number.isFinite(expiresAt) && expiresAt - now() > REFRESH_SKEW_MS) {
      return creds; // someone else refreshed while we waited for the lock
    }
    let res;
    try {
      res = await api.refresh({ grant_type: 'refresh_token', refresh_token: creds.refresh_token, client_id: CLIENT_ID, resource: RESOURCE });
    } catch (e) {
      if (isInvalidGrant(e)) {
        store.clear();
        throw new AuthError('reauthentication_required', '登录已失效，请重新手机号登录。', { next_action: 'start_phone_login' });
      }
      throw new AuthError('token_refresh_failed', '刷新登录态失败，请稍后重试。');
    }
    return persistRotated(res, creds);
  }

  /** Call the protected authenticated-test capability, refreshing + retrying once on a 401. */
  async function callAuthenticatedTest() {
    return callProtected((bearer) => api.authenticatedTest(bearer));
  }

  async function callProtected(fn) {
    let token = await getAccessToken();
    try {
      return await fn(token);
    } catch (e) {
      if (e instanceof ApiError && e.status === 401) {
        // Exactly one refresh + retry. A second failure is terminal and must map to a stable
        // error code — never bubble up as a raw throw (which becomes an opaque unexpected_error).
        const creds = await withLock(() => forceRefresh());
        token = creds.access_token;
        try {
          return await fn(token);
        } catch (retryErr) {
          if (retryErr instanceof ApiError && retryErr.status === 403) {
            throw new AuthError('insufficient_scope', '当前登录缺少所需权限。');
          }
          throw mapApiError(retryErr, 'call');
        }
      }
      if (e instanceof ApiError && e.status === 403) {
        throw new AuthError('insufficient_scope', '当前登录缺少所需权限。');
      }
      throw mapApiError(e, 'call');
    }
  }

  async function forceRefresh() {
    const creds = store.read();
    if (!creds || !creds.refresh_token) throw new AuthError('authentication_required', '需要先完成手机号登录。', { next_action: 'start_phone_login' });
    let res;
    try {
      res = await api.refresh({ grant_type: 'refresh_token', refresh_token: creds.refresh_token, client_id: CLIENT_ID, resource: RESOURCE });
    } catch (e) {
      if (isInvalidGrant(e)) {
        store.clear();
        throw new AuthError('reauthentication_required', '登录已失效，请重新手机号登录。', { next_action: 'start_phone_login' });
      }
      throw new AuthError('token_refresh_failed', '刷新登录态失败，请稍后重试。');
    }
    return persistRotated(res, creds);
  }

  // Save a freshly rotated token pair. The server has ALREADY rotated the refresh token by the
  // time we get here, so a failed local save would desync us: disk keeps the old (now-dead) token
  // and the next refresh would replay it and trip refresh-reuse family revocation. If persistence
  // fails we therefore clear local creds and ask for a clean re-login instead of leaking a raw
  // error (which the CLI would surface as an opaque `unexpected_error`).
  function persistRotated(res, prev) {
    try {
      return persistTokens(res, prev);
    } catch (persistErr) {
      store.clear();
      throw new AuthError('reauthentication_required', '登录状态保存失败，请重新手机号登录。', { next_action: 'start_phone_login' });
    }
  }

  function persistTokens(res, prev = {}) {
    const expiresInMs = (Number(res.expires_in) || 3600) * 1000;
    return store.write({
      client_id: CLIENT_ID,
      device_id: deviceId,
      access_token: res.access_token,
      access_expires_at: new Date(now() + expiresInMs).toISOString(),
      refresh_token: res.refresh_token || prev.refresh_token,
      principal_id: res.user?.principal_id || prev.principal_id,
      identity_level: res.user?.identity_level || prev.identity_level,
      phone_mask: res.user?.phone_mask || prev.phone_mask,
    });
  }

  // --- cross-process refresh lock (mkdir is atomic on POSIX) ---
  async function withLock(fn) {
    const lockDir = path.join(store.baseDir(), '.refresh.lock');
    store.baseDir(); // ensure base exists via store side effects on write; create dir defensively
    fs.mkdirSync(store.baseDir(), { recursive: true, mode: 0o700 });
    let held = false;
    for (let attempt = 0; attempt < 50 && !held; attempt += 1) {
      try { fs.mkdirSync(lockDir); held = true; } catch { await sleep(20); }
    }
    try {
      return await fn();
    } finally {
      if (held) { try { fs.rmdirSync(lockDir); } catch { /* ignore */ } }
    }
  }

  function sleep(ms) { return new Promise((r) => setTimeout(r, ms)); }

  return { authStart, authComplete, authStatus, logout, getAccessToken, callAuthenticatedTest, callProtected, deviceId };
}

function isInvalidGrant(e) {
  if (!(e instanceof ApiError)) return false;
  const errCode = e.body && (e.body.error || e.body.error_code);
  return e.status === 400 && /invalid_grant|revoked|reuse/i.test(String(errCode || ''));
}

function mapApiError(e, phase) {
  if (e instanceof AuthError) return e;
  if (e instanceof ApiError) {
    const upstream = e.body && (e.body.error || e.body.code);
    const map = {
      INVALID_PHONE: 'invalid_phone',
      RATE_LIMITED: 'verification_rate_limited',
      CODE_EXPIRED: 'verification_expired',
      CODE_INVALID: 'verification_invalid',
      TOO_MANY_ATTEMPTS: 'verification_rate_limited',
      LOGIN_NOT_FOUND: 'login_not_found',
      LOGIN_ALREADY_USED: 'login_not_found',
      DEVICE_MISMATCH: 'login_not_found',
      CAPTCHA_REQUIRED: 'captcha_required',
    };
    const code = map[upstream] || (e.code === 'REQUEST_TIMEOUT' || e.code === 'NETWORK_ERROR' ? 'api_unavailable' : 'api_unavailable');
    return new AuthError(code, humanMessage(code));
  }
  return new AuthError('api_unavailable', '服务暂不可用，请稍后重试。');
}

function humanMessage(code) {
  return {
    invalid_phone: '手机号格式不正确。',
    verification_rate_limited: '验证码发送过于频繁，请稍后再试。',
    verification_expired: '验证码已过期，请重新获取。',
    verification_invalid: '验证码不正确。',
    login_not_found: '登录会话无效，请重新开始登录。',
    captcha_required: '需要在浏览器授权页完成人机验证。',
    api_unavailable: '服务暂不可用，请稍后重试。',
  }[code] || '操作失败，请稍后重试。';
}

module.exports = { createAuth, AuthError, CLIENT_ID, RESOURCE };
