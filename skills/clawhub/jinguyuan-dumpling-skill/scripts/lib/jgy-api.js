'use strict';

/**
 * Controlled REST client for the JGY identity + business endpoints.
 *
 * Hardening (skill plan §5):
 * - Endpoints are compiled from a controlled base; only an HTTPS host allowlist is accepted, so
 *   conversation content can never redirect the client to an arbitrary token/API host.
 * - Explicit timeout on every request.
 * - No secrets are logged; callers own redaction of any surfaced fields.
 *
 * Dev/test may override the base via JGY_BASE_URL and add hosts via JGY_ALLOWED_HOSTS. Production
 * defaults to https://mcp.jinguyuan.cloud.
 */

const DEFAULT_BASE = (process.env.JGY_BASE_URL || 'https://mcp.jinguyuan.cloud').replace(/\/$/, '');
const REQUEST_TIMEOUT_MS = Number.parseInt(process.env.JGY_TIMEOUT_MS || '', 10) || 15_000;

function allowedHosts() {
  const hosts = new Set(['mcp.jinguyuan.cloud']);
  // Dev override: JGY_ALLOWED_HOSTS="127.0.0.1:9000,localhost:9000"
  for (const h of String(process.env.JGY_ALLOWED_HOSTS || '').split(/[\s,]+/).filter(Boolean)) {
    hosts.add(h.toLowerCase());
  }
  try { hosts.add(new URL(DEFAULT_BASE).host.toLowerCase()); } catch { /* ignore */ }
  return hosts;
}

function assertAllowed(url) {
  const parsed = new URL(url);
  const isLoopback = ['127.0.0.1', 'localhost', '[::1]'].some((h) => parsed.host.toLowerCase().startsWith(h));
  if (parsed.protocol !== 'https:' && !isLoopback) {
    throw new ApiError('UNSAFE_ENDPOINT', 'Only HTTPS endpoints are allowed.');
  }
  if (!allowedHosts().has(parsed.host.toLowerCase())) {
    throw new ApiError('UNSAFE_ENDPOINT', 'Endpoint host is not in the allowlist.');
  }
  return parsed.toString();
}

class ApiError extends Error {
  constructor(code, message, { status = 0, body = null } = {}) {
    super(message || code);
    this.code = code;
    this.status = status;
    this.body = body;
  }
}

function createApiClient({ baseUrl = DEFAULT_BASE, fetchImpl = globalThis.fetch, timeoutMs = REQUEST_TIMEOUT_MS } = {}) {
  const base = String(baseUrl).replace(/\/$/, '');
  const issuer = `${base}/auth`;
  const businessApi = `${base}/api/v1`;

  async function request(url, { method = 'GET', headers = {}, json = null, form = null, bearer = null } = {}) {
    const safeUrl = assertAllowed(url);
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeoutMs);
    const reqHeaders = { accept: 'application/json', ...headers };
    let body;
    if (json) { reqHeaders['content-type'] = 'application/json'; body = JSON.stringify(json); }
    else if (form) { reqHeaders['content-type'] = 'application/x-www-form-urlencoded'; body = new URLSearchParams(form).toString(); }
    if (bearer) reqHeaders.authorization = `Bearer ${bearer}`;

    let res;
    try {
      res = await fetchImpl(safeUrl, { method, headers: reqHeaders, body, signal: controller.signal });
    } catch (e) {
      throw new ApiError(e && e.name === 'AbortError' ? 'REQUEST_TIMEOUT' : 'NETWORK_ERROR', 'Request failed.');
    } finally {
      clearTimeout(timer);
    }
    const text = await res.text();
    let parsed = null;
    try { parsed = text ? JSON.parse(text) : {}; } catch { parsed = { raw: text }; }
    if (!res.ok) throw new ApiError('HTTP_ERROR', `HTTP ${res.status}`, { status: res.status, body: parsed });
    return parsed;
  }

  return {
    baseUrl: base,
    issuer,
    businessApi,
    // --- identity endpoints ---
    phoneStart: (json) => request(`${issuer}/api/phone/start`, { method: 'POST', json }),
    phoneVerify: (json) => request(`${issuer}/api/phone/verify`, { method: 'POST', json }),
    refresh: (form) => request(`${issuer}/oauth/token`, { method: 'POST', form }),
    revoke: (form) => request(`${issuer}/oauth/revoke`, { method: 'POST', form }),
    // --- business endpoints ---
    authenticatedTest: (bearer) => request(`${businessApi}/authenticated-test`, { method: 'GET', bearer }),
    // Public capability access (Phase 5 migration surface): GET without args, POST with JSON args.
    getCapability: (capabilityPath, bearer = null) => request(`${businessApi}/${String(capabilityPath).replace(/^\//, '')}`, { method: 'GET', bearer }),
    postCapability: (capabilityPath, json, bearer = null) => request(`${businessApi}/${String(capabilityPath).replace(/^\//, '')}`, { method: 'POST', json, bearer }),
    request,
  };
}

module.exports = { createApiClient, ApiError, assertAllowed, DEFAULT_BASE };
