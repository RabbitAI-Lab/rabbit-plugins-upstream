import test from "node:test";
import assert from "node:assert/strict";
import { createFetcher } from "../scripts/fetch.mjs";

test("warmup + search succeeds with browser-realistic headers", async () => {
  const calls = [];
  const fetchImpl = async (url, opts) => {
    calls.push({ url, headers: opts.headers });
    return {
      status: 200,
      headers: {
        getSetCookie: () => ["session-id=foo; Path=/", "ubid-acbes=bar; Path=/"],
        get: () => null,
      },
      text: async () => "<html><head><title>Amazon.es : test</title></head><body>" + "x".repeat(6000) + "</body></html>",
    };
  };
  const f = createFetcher({ fetch: fetchImpl, jitterMs: 0, baseDelayMs: 0 });
  const res = await f.get("https://www.amazon.es/s?k=ph+minus");
  assert.equal(res.outcome, "OK");
  assert.equal(calls.length, 2, "should warmup then fetch target");
  assert.equal(calls[0].url, "https://www.amazon.es/");
  assert.match(calls[1].headers["user-agent"], /Chrome\/131/);
  assert.equal(calls[1].headers["accept-language"], "es-ES,es;q=0.9,en;q=0.8");
  assert.equal(calls[1].headers.cookie, "session-id=foo; ubid-acbes=bar");
});

test("captcha on target → BLOCKED:captcha, no retry", async () => {
  let nTargetCalls = 0;
  const fetchImpl = async (url, _opts) => {
    if (url === "https://www.amazon.es/") {
      return {
        status: 200,
        headers: new Map([["set-cookie", "session-id=x"]]),
        text: async () => "<html><head><title>Amazon.es</title></head><body>" + "x".repeat(6000) + "</body></html>",
      };
    }
    nTargetCalls++;
    return {
      status: 200,
      headers: new Map(),
      text: async () => "<html><body>Enter the characters you see below</body></html>",
    };
  };
  const f = createFetcher({ fetch: fetchImpl, jitterMs: 0, baseDelayMs: 0 });
  const res = await f.get("https://www.amazon.es/s?k=foo");
  assert.equal(res.outcome, "BLOCKED");
  assert.equal(res.reason, "captcha");
  assert.equal(nTargetCalls, 1, "must not retry on captcha");
});

test("503 on target → BLOCKED:rate-limit with one retry", async () => {
  let n = 0;
  const fetchImpl = async (url, _opts) => {
    if (url === "https://www.amazon.es/") {
      return { status: 200, headers: new Map(), text: async () => "<html><title>Amazon.es</title>" + "x".repeat(6000) + "</html>" };
    }
    n++;
    return { status: 503, headers: new Map(), text: async () => "" };
  };
  const f = createFetcher({ fetch: fetchImpl, jitterMs: 0, baseDelayMs: 0 });
  const res = await f.get("https://www.amazon.es/s?k=x");
  assert.equal(res.outcome, "BLOCKED");
  assert.equal(res.reason, "rate-limit");
  assert.equal(n, 2, "503 retried once");
});
