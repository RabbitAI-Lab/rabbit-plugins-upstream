const SECRET_KEYS = ['apikey', 'authorization', 'secret', 'password', 'token', 'credential', 'privatekey', 'mnemonic'];

function isSecretKey(key: string): boolean {
  const normalized = key.toLowerCase().replace(/[^a-z]/g, '');
  if (['maxtokens','maxcompletiontokens','prompttokens','completiontokens','totaltokens','inputtokens','outputtokens'].includes(normalized)) return false;
  return SECRET_KEYS.some((needle) => normalized.includes(needle));
}

export function redact(value?: string): string {
  if (!value) return '';
  return '[redacted]';
}

function redactAny(value: unknown, parentKey?: string, seen: WeakSet<object> = new WeakSet()): unknown {
  if (value === null || value === undefined) return value;

  if (typeof value === 'string') {
    return parentKey && isSecretKey(parentKey) ? redact(value) : value;
  }

  if (typeof value !== 'object') return value;

  if (seen.has(value)) return '[circular]';
  seen.add(value);

  if (Array.isArray(value)) {
    return value.map((entry) => redactAny(entry, parentKey, seen));
  }

  const out: Record<string, unknown> = {};
  const namedSecret = Object.entries(value).some(([k,v]) => ['name','key'].includes(k) && typeof v === 'string' && isSecretKey(v));
  for (const [k, v] of Object.entries(value)) {
    if (['__proto__','constructor','prototype'].includes(k)) continue;
    if (isSecretKey(k) || (namedSecret && k === 'value')) {
      out[k] = typeof v === 'string' ? redact(v) : '[redacted]';
      continue;
    }
    out[k] = redactAny(v, k, seen);
  }
  return out;
}

export function redactObject<T extends Record<string, unknown>>(obj: T): T {
  return redactAny(obj) as T;
}
