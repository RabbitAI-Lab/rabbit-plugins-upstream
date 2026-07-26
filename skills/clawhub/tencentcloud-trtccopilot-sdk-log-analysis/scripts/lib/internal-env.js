import dns from 'node:dns';

const URL_RE = /https?:\/\/[^\s'"<>`]+/gi;
const TOKEN_RE = /\b(token|password|passwd|secret|authorization)\s*[:=]\s*([^\s,;]+)/gi;
const BASIC_RE = /Authorization:\s*Basic\s+[A-Za-z0-9+/=]+/gi;

const INTERNAL_HOST = 'copilot.trtc.woa.com';

export function redactSensitiveText(input) {
  return String(input || '')
    .replace(BASIC_RE, 'Authorization: <redacted>')
    .replace(URL_RE, '<redacted-url>')
    .replace(TOKEN_RE, '$1=<redacted>');
}

export function redactObject(value) {
  if (Array.isArray(value)) return value.map(redactObject);
  if (!value || typeof value !== 'object') {
    return typeof value === 'string' ? redactSensitiveText(value) : value;
  }
  const out = {};
  for (const [key, item] of Object.entries(value)) {
    if (/url|token|secret|password|authorization/i.test(key)) out[key] = '<redacted-url>';
    else out[key] = redactObject(item);
  }
  return out;
}

function internalHost() {
  return INTERNAL_HOST;
}

// Trusted internal network is detected purely by DNS resolution of the copilot host.
// The host only resolves inside Tencent's network; external networks get ENOTFOUND.
// `lookup` is injectable for tests.
export async function detectInternalNetwork({ lookup = dns.promises.lookup } = {}) {
  const host = internalHost();
  try {
    const { address } = await lookup(host);
    return { allowed: true, reason: `resolved:${host}`, address };
  } catch (err) {
    return { allowed: false, reason: `unresolved:${host}`, code: err?.code || 'ENOTFOUND' };
  }
}

export async function assertInternalNetwork(toolName, { lookup } = {}) {
  const result = await detectInternalNetwork({ lookup });
  if (result.allowed) return result;
  throw new Error(
    `${toolName} 仅在可信内网环境可用：无法解析 ${internalHost()}，请确认当前处于内网且已 trtccopilot login。`,
  );
}
