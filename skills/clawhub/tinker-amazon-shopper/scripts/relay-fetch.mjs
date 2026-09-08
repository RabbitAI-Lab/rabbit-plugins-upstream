#!/usr/bin/env node
// relay-fetch.mjs — fetch an amazon.es search page THROUGH the shared,
// logged-in browser tab instead of over anonymous HTTP.
//
// Why (2026-08-06, the microSD run): anonymous HTTP is fine for price and title
// but STRUCTURALLY cannot answer "does it arrive tomorrow". Without an account
// and a postcode Amazon returns a pessimistic generic estimate — the same query
// showed "sáb, 8 de ago" over HTTP and "FREE delivery Tomorrow, 7 Aug" in the
// logged-in tab. Any delivery-sensitive question must come through the relay.
//
// It also unlocks the refinement tokens that only appear once you interact with
// the UI, e.g. rh=p_90:6820340031 is amazon.es's "Get It Tomorrow" filter.
//
// Same-site only: it refuses any URL that is not amazon.es, per the standing
// relay rule that the agent may navigate within a site but never across sites.
//
// Usage:
//   node relay-fetch.mjs --url "https://www.amazon.es/-/en/s?k=micro+sd+1tb&rh=p_90%3A6820340031" \
//                        --out /tmp/page.html [--settle 4000]
//   node relay-fetch.mjs --list

import { spawnSync } from "node:child_process";
import fs from "node:fs";

const CDP_TARGET = `${process.env.HOME}/src/tinkerclaw/scripts/cdp-target.mjs`;
const RELAY_HTTP = "http://127.0.0.1:18792";
const WS = "ws://127.0.0.1:18792/cdp";

const argv = process.argv.slice(2);
const flag = (n, d) => {
  const i = argv.indexOf(`--${n}`);
  return i < 0 ? d : argv[i + 1];
};

async function tabs() {
  const res = await fetch(`${RELAY_HTTP}/json/list`, { signal: AbortSignal.timeout(8000) });
  return res.json();
}

/**
 * ONE CDP socket for the whole page capture.
 *
 * The first version spawned the cdp-target helper once per evaluate — and a
 * chunked capture is a dozen evaluates, so a dozen fresh CDP connects per page.
 * That is the documented way to wedge this relay: it started refusing
 * connections after the second page every time. Hold a single connection and
 * issue every call over it.
 */
class CdpSession {
  #ws = null;
  #id = 0;
  #pending = new Map();
  #sessionId = null;

  async open(targetId) {
    this.#ws = new WebSocket(WS);
    await new Promise((resolve, reject) => {
      this.#ws.addEventListener("open", resolve, { once: true });
      this.#ws.addEventListener("error", () => reject(new Error("cdp connect failed")), { once: true });
    });
    this.#ws.addEventListener("message", (ev) => {
      let msg;
      try {
        msg = JSON.parse(typeof ev.data === "string" ? ev.data : "");
      } catch {
        return;
      }
      const p = this.#pending.get(msg.id);
      if (!p) return;
      this.#pending.delete(msg.id);
      msg.error ? p.reject(new Error(JSON.stringify(msg.error))) : p.resolve(msg.result);
    });
    const att = await this.#send("Target.attachToTarget", { targetId, flatten: true });
    this.#sessionId = att.sessionId;
  }

  #send(method, params, sessionId) {
    const id = ++this.#id;
    const payload = { id, method, params };
    if (sessionId) payload.sessionId = sessionId;
    return new Promise((resolve, reject) => {
      this.#pending.set(id, { resolve, reject });
      this.#ws.send(JSON.stringify(payload));
      setTimeout(() => {
        if (this.#pending.delete(id)) reject(new Error(`cdp timeout: ${method}`));
      }, 60000);
    });
  }

  async evaluate(expr) {
    const r = await this.#send(
      "Runtime.evaluate",
      { expression: expr, returnByValue: true, awaitPromise: true },
      this.#sessionId,
    );
    if (r.exceptionDetails) throw new Error(r.exceptionDetails.text || "evaluate threw");
    return r.result?.value;
  }

  close() {
    try {
      this.#ws?.close();
    } catch {
      /* already gone */
    }
  }
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function main() {
  const list = await tabs();
  const amazon = list.find((t) => /amazon\./i.test(t.url || ""));

  if (argv.includes("--list") || !flag("url")) {
    console.log(JSON.stringify(list.map((t) => ({ id: t.id, title: t.title, url: t.url })), null, 2));
    if (!flag("url")) process.exit(argv.includes("--list") ? 0 : 3);
    return;
  }
  if (!amazon) {
    console.error("relay-fetch: no shared amazon.es tab. Share one in the extension, then re-run.");
    process.exit(4);
  }

  const url = flag("url");
  if (!/^https:\/\/(www\.)?amazon\.es\//i.test(url)) {
    console.error(`relay-fetch: refusing cross-site navigation to ${url}`);
    process.exit(5);
  }

  const settle = Number(flag("settle", "4500"));
  const cdp = new CdpSession();
  await cdp.open(amazon.id);
  const evaluate = (expr) => cdp.evaluate(expr);
  // location.href keeps it a same-document-origin navigation the relay allows.
  await evaluate(`location.href=${JSON.stringify(url)}; "nav"`);

  // Poll for a settled results page rather than sleeping a fixed time.
  let html = "";
  for (let i = 0; i < 20; i++) {
    await sleep(i === 0 ? settle : 1000);
    const probe = await evaluate(
      `JSON.stringify({ready:document.readyState,n:document.querySelectorAll('[data-component-type="s-search-result"]').length,href:location.href})`,
    );
    const p = typeof probe === "string" ? JSON.parse(probe) : probe;
    if (p.ready === "complete" && p.n > 0) {
      // A whole amazon.es document is ~1.8 MB and a single evaluate() round-trip
      // truncates it around 146 KB — silently, mid-attribute, so the parser just
      // sees zero cards. Stash the RESULTS CONTAINER (the only part the parser
      // needs) in a page variable and pull it back in slices.
      const lenRaw = await evaluate(
        `window.__ljcap=(document.getElementById('search')||document.documentElement).outerHTML; String(window.__ljcap.length)`,
      );
      const total = Number(typeof lenRaw === "string" ? lenRaw : String(lenRaw));
      const CHUNK = 100000;
      const parts = [];
      for (let off = 0; off < total; off += CHUNK) {
        const piece = await evaluate(`window.__ljcap.slice(${off}, ${off + CHUNK})`);
        parts.push(typeof piece === "string" ? piece : String(piece));
      }
      html = parts.join("");
      if (html.length !== total) {
        console.error(`relay-fetch: WARNING reassembled ${html.length} of ${total} bytes`);
      }
      console.error(`relay-fetch: ${p.n} cards · ${total} bytes · ${p.href}`);
      break;
    }
  }
  if (!html) {
    cdp.close();
    console.error("relay-fetch: page never produced search results");
    process.exit(1);
  }

  cdp.close();

  const out = flag("out");
  if (out) {
    fs.writeFileSync(out, html);
    console.log(JSON.stringify({ ok: true, out, bytes: html.length }));
  } else {
    process.stdout.write(html);
  }
}

await main();
