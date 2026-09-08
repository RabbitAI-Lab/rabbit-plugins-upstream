// fetch.mjs — Amazon HTTP client with browser-realistic headers + cookie jar +
// jittered cadence + warmup. Plain Node fetch (no got-scraping unless we hit
// a hard TLS-fingerprint block — then upgrade per the spec).

import { classifyResponse } from "./detect.mjs";

const CHROME_VERSION = "131"; // refresh annually.

function defaultHeaders({ isWarmup = false } = {}) {
  return {
    "user-agent": `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/${CHROME_VERSION}.0.0.0 Safari/537.36`,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "accept-language": "es-ES,es;q=0.9,en;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "sec-ch-ua": `"Chromium";v="${CHROME_VERSION}", "Not?A_Brand";v="24"`,
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-site": isWarmup ? "none" : "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "upgrade-insecure-requests": "1",
    "dnt": "1",
  };
}

function parseSetCookie(headers) {
  const sc = [];
  if (typeof headers.getSetCookie === "function") {
    for (const v of headers.getSetCookie()) sc.push(v);
  } else if (headers.get) {
    const v = headers.get("set-cookie");
    if (v) sc.push(v);
  }
  const jar = {};
  for (const line of sc) {
    const [pair] = line.split(";");
    const eq = pair.indexOf("=");
    if (eq > 0) jar[pair.slice(0, eq).trim()] = pair.slice(eq + 1).trim();
  }
  return jar;
}

function cookieHeader(jar) {
  return Object.entries(jar).map(([k, v]) => `${k}=${v}`).join("; ");
}

async function sleepJitter(baseMs, jitterMs) {
  if (baseMs <= 0 && jitterMs <= 0) return;
  const delay = baseMs + Math.floor(Math.random() * jitterMs * 2 - jitterMs);
  await new Promise(r => setTimeout(r, Math.max(0, delay)));
}

export function createFetcher({ fetch = globalThis.fetch, baseDelayMs = 2000, jitterMs = 1000 } = {}) {
  let jar = {};
  let warmedUp = false;
  let warmupTried = false;

  async function rawGet(url, { isWarmup = false } = {}) {
    const headers = defaultHeaders({ isWarmup });
    const cookie = cookieHeader(jar);
    if (cookie) headers.cookie = cookie;
    const res = await fetch(url, { headers, redirect: "follow" });
    Object.assign(jar, parseSetCookie(res.headers));
    const body = await res.text();
    return { status: res.status, headers: res.headers, body };
  }

  // Best-effort cookie seeding. The amazon.es HOMEPAGE often serves a harsher
  // AWS WAF JS challenge (HTTP 202) even when the /s search endpoint returns a
  // clean 200 — so a blocked warmup must NOT gate the real fetch. We attempt it
  // once for the cookies, record whether it worked, and proceed regardless.
  // Only the real target response (classified in get()) decides OK vs BLOCKED.
  async function warmup() {
    if (warmupTried) return;
    warmupTried = true;
    try {
      const r = await rawGet("https://www.amazon.es/", { isWarmup: true });
      const cls = classifyResponse({ status: r.status, body: r.body });
      if (cls.outcome === "OK") warmedUp = true;
    } catch {
      /* best-effort: a failed warmup never blocks the real fetch */
    }
  }

  async function get(url) {
    await warmup();
    await sleepJitter(baseDelayMs, jitterMs);
    let r = await rawGet(url);
    let cls = classifyResponse({ status: r.status, body: r.body });
    if (cls.outcome === "BLOCKED" && cls.reason === "rate-limit") {
      await sleepJitter(baseDelayMs * 2, jitterMs);
      r = await rawGet(url);
      cls = classifyResponse({ status: r.status, body: r.body });
    }
    if (cls.outcome === "OK") return { outcome: "OK", body: r.body, finalUrl: url };
    return { outcome: "BLOCKED", reason: cls.reason, body: r.body, finalUrl: url };
  }

  return {
    get,
    get cookies() { return { ...jar }; },
  };
}
