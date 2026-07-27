// 极简 HTTP 工具：超时、重试（429/5xx 与网络错误指数退避）、并发池。零第三方依赖。

const DEFAULT_TIMEOUT_MS = 60_000;
const MAX_ATTEMPTS = 6;

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

export async function fetchWithRetry(url, opts = {}) {
  const { headers = {}, timeoutMs = DEFAULT_TIMEOUT_MS, attempts = MAX_ATTEMPTS, method, body } = opts;
  let lastErr;
  for (let attempt = 1; attempt <= attempts; attempt++) {
    const ctrl = new AbortController();
    const timer = setTimeout(() => ctrl.abort(), timeoutMs);
    try {
      const res = await fetch(url, {
        method: method || (body ? "POST" : "GET"),
        body,
        headers: { "user-agent": "rabbit-plugins-upstream-sync", ...headers },
        signal: ctrl.signal,
      });
      if (res.ok) return res;
      // 限流/服务端错误 → 退避重试；其余 4xx 直接抛出
      if (res.status === 429 || res.status >= 500) {
        const retryAfter = Number(res.headers.get("retry-after")) || 0;
        const wait = Math.max(retryAfter * 1000, 2 ** attempt * 1000) + Math.random() * 1000;
        await res.arrayBuffer().catch(() => {}); // 释放连接
        if (attempt < attempts) {
          console.warn(`  [http] ${res.status} ${url} → ${Math.round(wait)}ms 后重试 (${attempt}/${attempts})`);
          await sleep(wait);
          continue;
        }
      }
      const errText = await res.text().catch(() => "");
      const err = new Error(`HTTP ${res.status} ${url}: ${errText.slice(0, 300)}`);
      err.status = res.status;
      err.body = errText;
      throw err;
    } catch (e) {
      lastErr = e;
      if (e.status && e.status < 500 && e.status !== 429) throw e; // 4xx 不重试
      if (attempt < attempts) {
        const wait = 2 ** attempt * 1000 + Math.random() * 1000;
        console.warn(`  [http] ${e.message} → ${Math.round(wait)}ms 后重试 (${attempt}/${attempts})`);
        await sleep(wait);
      }
    } finally {
      clearTimeout(timer);
    }
  }
  throw lastErr;
}

export async function fetchJson(url, opts = {}) {
  const res = await fetchWithRetry(url, opts);
  return res.json();
}

export async function fetchText(url, opts = {}) {
  const res = await fetchWithRetry(url, opts);
  return res.text();
}

export async function fetchBuffer(url, opts = {}) {
  const res = await fetchWithRetry(url, opts);
  return Buffer.from(await res.arrayBuffer());
}

// 并发池：limit 并发执行 async task
export function createLimiter(concurrency) {
  let active = 0;
  const queue = [];
  const next = () => {
    if (active >= concurrency || queue.length === 0) return;
    active++;
    const { fn, resolve, reject } = queue.shift();
    fn()
      .then(resolve, reject)
      .finally(() => {
        active--;
        next();
      });
  };
  return (fn) =>
    new Promise((resolve, reject) => {
      queue.push({ fn, resolve, reject });
      next();
    });
}
