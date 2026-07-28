'use strict';

/**
 * Structured stdout for the jgy CLI. Everything the Agent consumes is JSON on stdout; secrets must
 * never appear here. Deep-redacts token / code / phone-ish fields defensively before printing.
 */

const SENSITIVE_KEY = /token|authorization|cookie|password|secret|credential|api[-_]?key|access_token|refresh_token|verification|otp/i;
// `code` 类键单独处理：只有值形如 4-8 位数字（短信验证码）才脱敏；机器错误码（error.code）必须可见。
const CODE_KEY = /(^|_)code$/i;
const OTP_LIKE = /^\d{4,8}$/;

function redactString(value) {
  return String(value == null ? '' : value)
    // 11-digit CN mobile -> masked
    .replace(/(?<!\d)(1[3-9]\d)\d{4}(\d{4})(?!\d)/g, '$1****$2')
    // bearer-ish long tokens
    .replace(/(bearer\s+)[A-Za-z0-9._-]{12,}/gi, '$1[redacted]');
}

function deepRedact(value, key = '') {
  if (key && SENSITIVE_KEY.test(key)) return '[redacted]';
  if (key && CODE_KEY.test(key) && typeof value === 'string' && OTP_LIKE.test(value)) return '[redacted]';
  if (typeof value === 'string') return redactString(value);
  if (Array.isArray(value)) return value.map((v) => deepRedact(v));
  if (value && typeof value === 'object') {
    return Object.fromEntries(Object.entries(value).map(([k, v]) => [k, deepRedact(v, k)]));
  }
  return value;
}

function ok(data = {}) {
  return { ok: true, ...data };
}

function err(code, message, extra = {}) {
  return { ok: false, error: { code, message, ...extra } };
}

/** Print a result object to stdout as redacted JSON. */
function emit(result, { stream = process.stdout } = {}) {
  stream.write(`${JSON.stringify(deepRedact(result))}\n`);
}

module.exports = { ok, err, emit, deepRedact, redactString };
