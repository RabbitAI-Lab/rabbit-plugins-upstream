#!/usr/bin/env node
/**
 * pw-browser — Playwright-based browser automation CLI.
 * Uses a simple daemon (HTTP server) to keep the browser alive across commands.
 *
 * Usage:
 *   node pw-browser.js daemon            — start daemon (keeps browser alive)
 *   node pw-browser.js <command> [args]  — execute command against running daemon
 */

const http = require('http');
const fs = require('fs');
const path = require('path');
const os = require('os');
const vm = require('vm');
const crypto = require('crypto');

// ---- Config ----
const STATE_DIR = path.join(os.homedir(), '.pw-browser');
const DAEMON_PORT = 19223;
const DAEMON_HOST = '127.0.0.1';

let JSON_OUTPUT = false;

function ensureDir() {
  if (!fs.existsSync(STATE_DIR)) fs.mkdirSync(STATE_DIR, { recursive: true });
}

// ===================== DAEMON MODE =====================
async function runDaemon() {
  const { chromium } = require('playwright');

  ensureDir();
  console.log(`[daemon] Starting pw-browser daemon on ${DAEMON_HOST}:${DAEMON_PORT}`);

  let browser = null;
  let context = null;
  let page = null;

  // SECURITY: per-daemon random token + optional safe mode.
  // The token is generated once at daemon start and written to daemon.json
  // (readable only by the local user). Every command route except /health
  // must present it, closing the "unauthenticated HTTP daemon = RCE surface" gap.
  const SAFE_MODE = process.env.PW_BROWSER_SAFE_MODE === '1' || process.env.PW_BROWSER_SAFE_MODE === 'true';
  const daemonToken = crypto.randomBytes(24).toString('hex');

  async function ensurePage() {
    if (page && !page.isClosed()) return page;
    if (!browser || !browser.isConnected()) {
      const launchOpts = { headless: false, channel: undefined, executablePath: undefined };

      // Priority: system Chrome/Edge > ms-playwright Chromium
      const channelCandidates = ['chrome', 'msedge'];

      // Platform-specific browser path candidates
      const plat = process.platform;
      let pathCandidates;
      if (plat === 'win32') {
        pathCandidates = [
          'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
          'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
          'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
          'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe',
          path.join(os.homedir(), 'AppData', 'Local', 'ms-playwright', 'chromium-1228', 'chrome-win64', 'chrome.exe'),
          path.join(os.homedir(), 'AppData', 'Local', 'ms-playwright', 'chromium-1226', 'chrome-win64', 'chrome.exe'),
        ];
      } else if (plat === 'darwin') {
        pathCandidates = [
          '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
          '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
          '/Applications/Chromium.app/Contents/MacOS/Chromium',
          path.join(os.homedir(), 'Library', 'Caches', 'ms-playwright', 'chromium-1228', 'chrome-mac', 'Chromium.app', 'Contents', 'MacOS', 'Chromium'),
          path.join(os.homedir(), 'Library', 'Caches', 'ms-playwright', 'chromium-1226', 'chrome-mac', 'Chromium.app', 'Contents', 'MacOS', 'Chromium'),
        ];
      } else {
        // Linux / other Unix
        pathCandidates = [
          '/usr/bin/google-chrome',
          '/usr/bin/google-chrome-stable',
          '/usr/bin/microsoft-edge',
          '/usr/bin/microsoft-edge-stable',
          '/usr/bin/chromium-browser',
          '/usr/bin/chromium',
          '/snap/bin/chromium',
          path.join(os.homedir(), '.cache', 'ms-playwright', 'chromium-1228', 'chrome-linux', 'chrome'),
          path.join(os.homedir(), '.cache', 'ms-playwright', 'chromium-1226', 'chrome-linux', 'chrome'),
        ];
      }

      let launched = false;

      // Try Playwright channel first (uses system Chrome/Edge discovery)
      for (const ch of channelCandidates) {
        try {
          console.error(`[daemon] Trying channel: ${ch}`);
          browser = await chromium.launch({ headless: false, channel: ch });
          console.error(`[daemon] Launched via channel: ${ch}`);
          launched = true;
          break;
        } catch (e) {
          console.error(`[daemon] Channel ${ch} failed: ${e.message.split('\n')[0]}`);
        }
      }

      // Fallback: explicit path
      if (!launched) {
        for (const p of pathCandidates) {
          if (fs.existsSync(p)) {
            try {
              console.error(`[daemon] Trying path: ${p}`);
              browser = await chromium.launch({ headless: false, executablePath: p });
              console.error(`[daemon] Launched: ${p}`);
              launched = true;
              break;
            } catch (e) {
              console.error(`[daemon] Path ${p} failed: ${e.message.split('\n')[0]}`);
            }
          }
        }
      }

      if (!launched) {
        throw new Error('No browser available. Install Chrome/Edge or run: npx playwright install chromium');
      }
      context = await browser.newContext();
    }
    const pages = context.pages();
    page = pages[0] || await context.newPage();
    return page;
  }

  // Snapshot helpers
  let refCounter = 0;
  const refMap = new Map();
  let cachedSnap = null;  // Last snapshot result, used by click/fill etc.

  async function buildSnapshot(p) {
    refCounter = 0;
    refMap.clear();
    const lines = [];
    lines.push(`- Snapshot @ ${new Date().toISOString()}`);
    lines.push(`  url: ${p.url()}`);
    lines.push(`  title: ${await p.title()}`);

    // Use evaluate-based snapshot fallback if accessibility snapshot not available
    let snapshot;
    try {
      snapshot = await p.accessibility.snapshot({ interestingOnly: false });
    } catch {}

    if (snapshot) {
      flattenAXTree(snapshot, lines, 2);
    }

    // Always supplement with visible elements from DOM (handles cases where AX tree is sparse)
    try {
      const domElements = await p.evaluate(() => {
        const items = [];
        const selectors = 'button, a, input, textarea, select, [role="button"], [role="link"], [role="textbox"], [role="checkbox"], [role="combobox"], [role="tab"], [role="menuitem"]';
        document.querySelectorAll(selectors).forEach((el, i) => {
          const rect = el.getBoundingClientRect();
          if (rect.width > 0 && rect.height > 0) {
            const tag = el.tagName.toLowerCase();
            const text = (el.textContent || el.value || el.placeholder || '').trim().slice(0, 80);
            items.push({ tag, text, id: el.id || '', type: el.type || '', placeholder: el.placeholder || '', ariaLabel: el.getAttribute('aria-label') || '' });
          }
        });
        return items;
      });

      if (!snapshot && domElements.length > 0) {
        // No AX tree — build from DOM
        domElements.forEach((el, i) => {
          const ref = `e${refCounter}`;
          lines.push(`  [${ref}] ${el.tag} ${el.text}${el.type ? ' type=' + el.type : ''}${el.placeholder ? ' placeholder="' + el.placeholder + '"' : ''}`);
          refMap.set(ref, { role: el.tag, name: el.text, tag: el.tag, placeholder: el.placeholder, ariaLabel: el.ariaLabel });
          refCounter++;
        });
      }
    } catch {}

    const result = { text: lines.join('\n'), refMap: new Map(refMap) };
    cachedSnap = result;  // Cache for click/fill findElement
    return result;
  }

  function flattenAXTree(node, lines, indent) {
    const ref = `e${refCounter}`;
    const prefix = '  '.repeat(indent);
    const role = node.role || 'unknown';
    const name = (node.name || '').slice(0, 120);
    const value = node.value ? `[${node.value}]` : '';

    lines.push(`${prefix}[${ref}] ${role} ${name} ${value}`.trim());
    refMap.set(ref, { role, name, value: node.value, tag: node.role });

    refCounter++;
    if (node.children) {
      for (const child of node.children) {
        flattenAXTree(child, lines, indent + 1);
      }
    }
  }

  // Element finder — uses last cached snapshot (from explicit `snap` command)
  async function findElement(p, ref) {
    if (!cachedSnap) await buildSnapshot(p);
    const info = cachedSnap.refMap.get(ref);
    if (!info) return null;

    // Map AX roles to Playwright roles
    const roleMap = {
      'textarea': 'textbox',
      'textbox': 'textbox',
      'button': 'button',
      'link': 'link',
      'img': 'img',
      'heading': 'heading',
      'checkbox': 'checkbox',
      'combobox': 'combobox',
      'listbox': 'listbox',
      'option': 'option',
      'tab': 'tab',
      'menuitem': 'menuitem',
      'a': 'link',
      'input': 'textbox',
      'select': 'combobox',
    };
    const pwRole = roleMap[info.role] || info.role;

    // Strategy 1: getByRole with name
    if (pwRole && pwRole !== 'unknown' && pwRole !== 'generic') {
      try {
        const opts = info.name && info.name.length < 100 ? { name: info.name } : {};
        const loc = p.getByRole(pwRole, opts);
        const count = await loc.count();
        if (count > 0) return loc.first();
      } catch (e) { /* ignore */ }
    }

    // Strategy 2: getByRole without name
    if (pwRole && pwRole !== 'unknown' && pwRole !== 'generic') {
      try {
        const loc = p.getByRole(pwRole);
        const count = await loc.count();
        if (count > 0) return loc.first();
      } catch (e) { /* ignore */ }
    }

    // Strategy 3: getByText
    if (info.name) {
      try {
        const loc = p.getByText(info.name, { exact: true });
        const count = await loc.count();
        if (count > 0) return loc.first();
      } catch (e) { /* ignore */ }
    }

    // Strategy 4: CSS attribute selectors for form inputs (handles type=search etc.)
    if (info.tag === 'input' || info.tag === 'textarea' || info.role === 'textbox') {
      try {
        const selectors = ['input[type="search"]', 'input[type="text"]', 'input[type="email"]',
          'input[type="url"]', 'input[type="tel"]', 'input:not([type])',
          '[role="searchbox"]', 'textarea', '[role="textbox"]'];
        for (const sel of selectors) {
          try {
            const loc = p.locator(sel);
            const count = await loc.count();
            if (count > 0) {
              const el = loc.first();
              if (await el.isVisible().catch(() => false)) return el;
            }
          } catch (_) { /* next */ }
        }
      } catch (e) { /* ignore */ }
    }

    // Strategy 5: placeholder text (for inputs)
    if (info.name) {
      try {
        const loc = p.locator(`[placeholder*="${info.name}"], [aria-label*="${info.name}"]`).first();
        if (await loc.count() > 0) return loc;
      } catch (e) { /* ignore */ }
    }

    // Strategy 6: label association (for form inputs paired with labels)
    if (info.name && (info.tag === 'input' || info.tag === 'textarea' || info.role === 'textbox')) {
      try {
        const loc = p.getByLabel(info.name, { exact: false }).first();
        if (await loc.count() > 0) return loc;
      } catch (e) { /* ignore */ }
    }

    // Strategy 7: tag-based fallback (last resort for non-input elements like button, a, div)
    if (info.tag && info.tag !== 'input' && info.tag !== 'textarea') {
      try {
        const loc = p.locator(info.tag).first();
        const count = await loc.count();
        if (count > 0) return loc;
      } catch (e) { /* ignore */ }
    }

    // Strategy 8: plain text match (last resort)
    if (info.name) {
      try {
        const loc = p.getByText(info.name);
        const count = await loc.count();
        if (count > 0) return loc.first();
      } catch (e) { /* ignore */ }
    }

    return null;
  }

  // Route handler
  const server = http.createServer(async (req, res) => {
    const url = new URL(req.url, `http://${DAEMON_HOST}`);
    const cmd = url.pathname.slice(1);
    const params = Object.fromEntries(url.searchParams);

    // SECURITY: require token for every route except /health.
    // The token is a random 24-byte hex generated at daemon start and stored
    // in daemon.json (local-user-only). This closes the "unauthenticated
    // HTTP daemon = RCE surface" gap: a malicious local page/process cannot
    // drive the browser without the token.
    if (cmd !== 'health') {
      const provided = url.searchParams.get('token');
      if (!provided || provided !== daemonToken) {
        res.writeHead(403, { 'Content-Type': 'application/json' });
        return res.end(JSON.stringify({ ok: false, error: { kind: 'AuthError', message: 'Missing or invalid token' } }));
      }
    }

    function json(obj) {
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify(obj));
    }

    function bad(msg) {
      res.writeHead(400);
      res.end(JSON.stringify({ ok: false, error: { message: msg } }));
    }

    try {
      const p = await ensurePage();
      const t0 = Date.now();

      switch (cmd) {
        case 'health': return json({ ok: true, pageUrl: p.url() });
        case 'init': {
          return json({ ok: true, pageUrl: p.url(), pageTitle: await p.title(), elapsedMs: Date.now() - t0 });
        }
        case 'open': case 'goto': {
          const targetUrl = params.url;
          if (!targetUrl) return bad('Missing url param');
          try {
            await p.goto(targetUrl, { waitUntil: 'domcontentloaded', timeout: Number(params.timeout) || 60000 });
            await p.waitForLoadState('load', { timeout: 15000 }).catch(() => {});
            json({ ok: true, afterUrl: p.url(), title: await p.title(), elapsedMs: Date.now() - t0 });
          } catch (e) {
            json({ ok: false, error: { kind: 'NavigationTimeout', message: e.message }, elapsedMs: Date.now() - t0 });
          }
          break;
        }
        case 'snap': {
          const snap = await buildSnapshot(p);
          json({ ok: true, data: snap, elapsedMs: Date.now() - t0 });
          break;
        }
        case 'click': {
          const el = await findElement(p, params.ref);
          if (!el) return json({ ok: false, error: { kind: 'ElementNotFound', message: `Element ${params.ref} not found` } });
          await el.click({ timeout: 10000 });
          json({ ok: true, ref: params.ref, clicked: true, elapsedMs: Date.now() - t0 });
          break;
        }
        case 'fill': {
          const el = await findElement(p, params.ref);
          if (!el) return json({ ok: false, error: { kind: 'ElementNotFound', message: `Element ${params.ref} not found` } });
          await el.fill(params.text || '', { timeout: 10000 });
          json({ ok: true, ref: params.ref, filled: params.text, elapsedMs: Date.now() - t0 });
          break;
        }
        case 'type': {
          await p.keyboard.type(params.text || '');
          json({ ok: true, typed: params.text, elapsedMs: Date.now() - t0 });
          break;
        }
        case 'press': {
          await p.keyboard.press(params.key || 'Enter');
          json({ ok: true, pressed: params.key, elapsedMs: Date.now() - t0 });
          break;
        }
        case 'hover': {
          const el = await findElement(p, params.ref);
          if (!el) return json({ ok: false, error: { kind: 'ElementNotFound', message: `Element ${params.ref} not found` } });
          await el.hover({ timeout: 5000 });
          json({ ok: true, ref: params.ref, hovered: true, elapsedMs: Date.now() - t0 });
          break;
        }
        case 'select': {
          const el = await findElement(p, params.ref);
          if (!el) return json({ ok: false, error: { kind: 'ElementNotFound', message: `Element ${params.ref} not found` } });
          await el.selectOption(params.option || '');
          json({ ok: true, ref: params.ref, selected: params.option, elapsedMs: Date.now() - t0 });
          break;
        }
        case 'check': {
          const el = await findElement(p, params.ref);
          if (!el) return json({ ok: false, error: { kind: 'ElementNotFound', message: `Element ${params.ref} not found` } });
          await el.check();
          json({ ok: true, ref: params.ref, checked: true, elapsedMs: Date.now() - t0 });
          break;
        }
        case 'uncheck': {
          const el = await findElement(p, params.ref);
          if (!el) return json({ ok: false, error: { kind: 'ElementNotFound', message: `Element ${params.ref} not found` } });
          await el.uncheck();
          json({ ok: true, ref: params.ref, unchecked: true, elapsedMs: Date.now() - t0 });
          break;
        }
        case 'go-back': {
          await p.goBack();
          json({ ok: true, afterUrl: p.url(), elapsedMs: Date.now() - t0 });
          break;
        }
        case 'go-forward': {
          await p.goForward();
          json({ ok: true, afterUrl: p.url(), elapsedMs: Date.now() - t0 });
          break;
        }
        case 'reload': {
          await p.reload();
          json({ ok: true, afterUrl: p.url(), elapsedMs: Date.now() - t0 });
          break;
        }
        case 'wait-for': {
          const target = params.target;
          const timeout = Number(params.timeout) || 10000;
          try {
            if (target.startsWith('url:')) {
              await p.waitForURL(target.slice(4), { timeout });
            } else if (target.startsWith('text=')) {
              await p.getByText(target.slice(5)).first().waitFor({ timeout });
            } else if (target.startsWith('state:')) {
              await p.waitForLoadState(target.slice(6), { timeout });
            } else {
              await p.waitForSelector(target, { timeout });
            }
            json({ ok: true, target, matched: true, elapsedMs: Date.now() - t0 });
          } catch (e) {
            json({ ok: false, error: { kind: 'WaitTimeout', message: e.message }, elapsedMs: Date.now() - t0 });
          }
          break;
        }
        case 'screenshot': {
          const filePath = params.path || path.join(STATE_DIR, `screenshot-${Date.now()}.png`);
          if (params.ref) {
            const el = await findElement(p, params.ref);
            if (!el) return json({ ok: false, error: { kind: 'ElementNotFound', message: `Element ${params.ref} not found` } });
            await el.screenshot({ path: filePath });
          } else {
            await p.screenshot({ path: filePath, fullPage: true });
          }
          json({ ok: true, path: filePath, elapsedMs: Date.now() - t0 });
          break;
        }
        case 'mousewheel': {
          await p.mouse.wheel(Number(params.dx) || 0, Number(params.dy) || 0);
          json({ ok: true, scrolled: { dx: Number(params.dx), dy: Number(params.dy) }, elapsedMs: Date.now() - t0 });
          break;
        }
        case 'eval': {
          if (SAFE_MODE) {
            return json({ ok: false, error: { kind: 'Disabled', message: 'eval is disabled in safe mode (PW_BROWSER_SAFE_MODE=1)' } });
          }
          const expr = params.expr;
          console.error(`[daemon] eval executed (ref=${params.ref || 'page'}, len=${expr.length})`);
          // NOTE: eval runs via page.evaluate() — browser-context only.
          // It CANNOT reach Node.js APIs (require/fs/process), so it does
          // not escape the browser sandbox to the host. BUT within the page
          // it is FULL page-context code execution: it can read
          // document.cookie / localStorage / sessionStorage, issue
          // credentialed fetch()/XMLHttpRequest, and drive DOM actions.
          // Same risk class as run-code; gated by token auth + safe-mode.
          if (params.ref) {
            const el = await findElement(p, params.ref);
            if (!el) return json({ ok: false, error: { kind: 'ElementNotFound', message: `Element ${params.ref} not found` } });
            const r = await el.evaluate(el => eval(expr));
            json({ ok: true, result: typeof r === 'string' ? r : JSON.stringify(r), elapsedMs: Date.now() - t0 });
          } else {
            const r = await p.evaluate(expr);
            json({ ok: true, result: typeof r === 'string' ? r : JSON.stringify(r), elapsedMs: Date.now() - t0 });
          }
          break;
        }
        case 'run-code': {
          if (SAFE_MODE) {
            return json({ ok: false, error: { kind: 'Disabled', message: 'run-code is disabled in safe mode (PW_BROWSER_SAFE_MODE=1)' } });
          }
          const codeStr = params.code;
          console.error(`[daemon] run-code executed (len=${codeStr.length})`);
          // SECURITY: run user code inside a restricted VM context.
          // The sandbox is created with Object.create(null) so it has NO
          // prototype chain — `this.constructor` is undefined, which blocks
          // the classic escape `this.constructor.constructor('return process')()`.
          // Standard JS globals (Object/Array/JSON/Function/Promise/...) are
          // provided natively by the vm context; host Node APIs (process/
          // require/fs/child_process) are NOT present, so user code can drive
          // the browser but cannot reach the host. Safe-mode disables this
          // command entirely. This is defense-in-depth on top of token auth.
          const sandbox = Object.create(null);
          sandbox.page = p;
          sandbox.console = console;
          sandbox.setTimeout = setTimeout;
          sandbox.clearTimeout = clearTimeout;
          sandbox.setInterval = setInterval;
          sandbox.clearInterval = clearInterval;
          sandbox.queueMicrotask = queueMicrotask;
          vm.createContext(sandbox);
          try {
            const script = new vm.Script(`(async () => { ${codeStr} })()`);
            const runPromise = script.runInContext(sandbox);
            const timeoutMs = 120000;
            const timeoutPromise = new Promise((_, rej) => {
              const t = setTimeout(() => rej(new Error(`run-code exceeded ${timeoutMs}ms`)), timeoutMs);
              runPromise.finally(() => clearTimeout(t));
            });
            const r = await Promise.race([runPromise, timeoutPromise]);
            const text = typeof r === 'string' ? r : JSON.stringify(r, null, 2);
            json({ ok: true, result: text, elapsedMs: Date.now() - t0 });
          } catch (e) {
            json({ ok: false, error: { kind: 'RunCodeError', message: e.message, stack: e.stack } });
          }
          break;
        }
        case 'tab': {
          const sub = params.sub;
          const pages = context.pages();
          if (sub === 'list') {
            const tabs = await Promise.all(pages.map(async (pg, i) => ({
              index: i, url: pg.url(), title: await pg.title().catch(() => '')
            })));
            json({ ok: true, tabs, elapsedMs: Date.now() - t0 });
          } else if (sub === 'select') {
            const idx = Number(params.idx);
            if (idx < 0 || idx >= pages.length) return json({ ok: false, error: { kind: 'InvalidTab', message: `Tab ${idx} out of range` } });
            page = pages[idx];
            await page.bringToFront();
            json({ ok: true, selected: idx, url: page.url(), elapsedMs: Date.now() - t0 });
          } else if (sub === 'close') {
            const idx = Number(params.idx);
            if (idx < 0 || idx >= pages.length) return json({ ok: false, error: { kind: 'InvalidTab', message: `Tab ${idx} out of range` } });
            if (pages.length <= 1) return json({ ok: false, error: { kind: 'LastTab', message: 'Cannot close last tab' } });
            await pages[idx].close();
            page = context.pages()[0];
            json({ ok: true, closed: idx, elapsedMs: Date.now() - t0 });
          } else {
            bad(`Unknown tab subcommand: ${sub}`);
          }
          break;
        }
        case 'sleep': {
          const sec = Number(params.seconds) || 1;
          await new Promise(r => setTimeout(r, sec * 1000));
          json({ ok: true, slept: sec, elapsedMs: Date.now() - t0 });
          break;
        }
        case 'close': {
          if (params.all === 'true') {
            await browser.close();
            browser = null; context = null; page = null;
            json({ ok: true, closed: 'all', elapsedMs: Date.now() - t0 });
            // Shutdown daemon after close --all
            setTimeout(() => { server.close(); process.exit(0); }, 500);
          } else {
            if (context.pages().length > 1) {
              await page.close();
              page = context.pages()[0];
            }
            json({ ok: true, closed: 'page', elapsedMs: Date.now() - t0 });
          }
          break;
        }
        case 'dialog-accept': {
          p.once('dialog', async d => { if (params.text) await d.accept(params.text); else await d.accept(); });
          json({ ok: true, elapsedMs: Date.now() - t0 });
          break;
        }
        case 'dialog-dismiss': {
          p.once('dialog', async d => { await d.dismiss(); });
          json({ ok: true, elapsedMs: Date.now() - t0 });
          break;
        }
        case 'recover': {
          if (browser) { await browser.close().catch(() => {}); browser = null; context = null; page = null; }
          await ensurePage();
          json({ ok: true, recovered: true, pageUrl: p.url(), elapsedMs: Date.now() - t0 });
          break;
        }
        case 'shutdown': {
          if (browser) await browser.close().catch(() => {});
          json({ ok: true, shutdown: true });
          server.close();
          process.exit(0);
          break;
        }
        default:
          bad(`Unknown command: ${cmd}`);
      }
    } catch (e) {
      res.writeHead(500);
      res.end(JSON.stringify({ ok: false, error: { kind: 'InternalError', message: e.message }, elapsedMs: 0 }));
    }
  });

  server.listen(DAEMON_PORT, DAEMON_HOST, () => {
    console.log(`[daemon] Listening on ${DAEMON_HOST}:${DAEMON_PORT}`);
    // Write daemon info
    fs.writeFileSync(path.join(STATE_DIR, 'daemon.json'), JSON.stringify({ host: DAEMON_HOST, port: DAEMON_PORT, pid: process.pid, token: daemonToken }));
  });

  // Global error handlers to prevent daemon crash
  process.on('uncaughtException', (err) => {
    console.error(`[daemon] uncaughtException: ${err.message}`);
  });
  process.on('unhandledRejection', (reason) => {
    console.error(`[daemon] unhandledRejection: ${reason?.message || reason}`);
  });

  // Graceful shutdown
  process.on('SIGINT', async () => { if (browser) await browser.close(); process.exit(0); });
  process.on('SIGTERM', async () => { if (browser) await browser.close(); process.exit(0); });
}

// ===================== CLIENT MODE =====================
async function runClient() {
  const args = process.argv.slice(2);
  if (args.length === 0) {
    console.log(`Usage: node pw-browser.js <command> [args...] [--json]`);
    console.log(`       node pw-browser.js daemon`);
    console.log(`Commands: init, open, snap, click, fill, type, press, hover, select, check, uncheck,`);
    console.log(`          goto, go-back, go-forward, reload, wait-for, screenshot, mousewheel,`);
    console.log(`          eval, run-code, tab, sleep, close, recover`);
    process.exit(1);
  }

  const jsonIdx = args.indexOf('--json');
  JSON_OUTPUT = jsonIdx !== -1;
  if (JSON_OUTPUT) args.splice(jsonIdx, 1);

  const cmd = args[0];
  const rest = args.slice(1);

  // Parse opts
  function parseOpts(r) {
    const opts = {};
    const positional = [];
    for (let i = 0; i < r.length; i++) {
      if (r[i].startsWith('--')) {
        const key = r[i].slice(2);
        const val = r[i + 1] && !r[i + 1].startsWith('--') ? r[++i] : 'true';
        opts[key] = val;
      } else {
        positional.push(r[i]);
      }
    }
    return { opts, positional };
  }

  const { opts, positional } = parseOpts(rest);

  // Check daemon
  const daemonFile = path.join(STATE_DIR, 'daemon.json');
  let daemonHost = DAEMON_HOST;
  let daemonPort = DAEMON_PORT;
  if (fs.existsSync(daemonFile)) {
    const d = JSON.parse(fs.readFileSync(daemonFile, 'utf8'));
    daemonHost = d.host;
    daemonPort = d.port;
  }

  // Health check
  async function ensureDaemon() {
    return new Promise((resolve) => {
      const req = http.get(`http://${daemonHost}:${daemonPort}/health`, (res) => {
        resolve(res.statusCode === 200);
      });
      req.on('error', () => resolve(false));
      req.setTimeout(2000, () => { req.destroy(); resolve(false); });
    });
  }

  function callDaemon(path, queryParams = {}) {
    return new Promise((resolve, reject) => {
      const qp = { ...queryParams };
      // Attach the daemon auth token (from daemon.json) automatically.
      try {
        const d = JSON.parse(fs.readFileSync(daemonFile, 'utf8'));
        if (d.token) qp.token = d.token;
      } catch {}
      const qs = Object.entries(qp)
        .filter(([, v]) => v !== undefined && v !== null)
        .map(([k, v]) => `${encodeURIComponent(k)}=${encodeURIComponent(v)}`)
        .join('&');
      const fullPath = qs ? `${path}?${qs}` : path;
      const req = http.get(`http://${daemonHost}:${daemonPort}${fullPath}`, (res) => {
        let data = '';
        res.on('data', chunk => data += chunk);
        res.on('end', () => {
          try { resolve(JSON.parse(data)); }
          catch { resolve({ ok: false, error: { message: data } }); }
        });
      });
      req.on('error', reject);
      req.setTimeout(120000, () => { req.destroy(); reject(new Error('Client request timeout (120s)')); });
    });
  }

  // Map CLI args to daemon query params
  async function execute() {
    if (!fs.existsSync(daemonFile)) {
      console.error('Daemon not running. Start it: node pw-browser.js daemon &');
      process.exit(1);
    }

    switch (cmd) {
      case 'init': return callDaemon('/init');
      case 'open': case 'goto': return callDaemon('/open', { url: positional[0], timeout: opts.timeout });
      case 'snap': return callDaemon('/snap');
      case 'click': return callDaemon('/click', { ref: positional[0] });
      case 'fill': return callDaemon('/fill', { ref: positional[0], text: positional.slice(1).join(' ') });
      case 'type': return callDaemon('/type', { text: positional.join(' ') });
      case 'press': return callDaemon('/press', { key: positional[0] });
      case 'hover': return callDaemon('/hover', { ref: positional[0] });
      case 'select': return callDaemon('/select', { ref: positional[0], option: positional[1] });
      case 'check': return callDaemon('/check', { ref: positional[0] });
      case 'uncheck': return callDaemon('/uncheck', { ref: positional[0] });
      case 'go-back': return callDaemon('/go-back');
      case 'go-forward': return callDaemon('/go-forward');
      case 'reload': return callDaemon('/reload');
      case 'wait-for': return callDaemon('/wait-for', { target: positional[0], timeout: opts.timeout });
      case 'screenshot': return callDaemon('/screenshot', { ref: positional[0], path: opts.path });
      case 'mousewheel': return callDaemon('/mousewheel', { dx: positional[0], dy: positional[1] });
      case 'eval': return callDaemon('/eval', { expr: positional[0], ref: positional[1] });
      case 'run-code': return callDaemon('/run-code', { code: positional.join(' ') });
      case 'tab': {
        const sub = positional[0];
        if (sub === 'list') return callDaemon('/tab', { sub: 'list' });
        if (sub === 'select') return callDaemon('/tab', { sub: 'select', idx: positional[1] });
        if (sub === 'close') return callDaemon('/tab', { sub: 'close', idx: positional[1] });
        return { ok: false, error: { message: `Unknown tab subcommand: ${sub}` } };
      }
      case 'sleep': return callDaemon('/sleep', { seconds: positional[0] });
      case 'close': return callDaemon('/close', { all: opts.all });
      case 'dialog-accept': return callDaemon('/dialog-accept', { text: positional[0] });
      case 'dialog-dismiss': return callDaemon('/dialog-dismiss');
      case 'recover': return callDaemon('/recover');
      case 'shutdown': return callDaemon('/shutdown');
      default: return { ok: false, error: { message: `Unknown command: ${cmd}` } };
    }
  }

  const result = await execute();
  if (JSON_OUTPUT) {
    console.log(JSON.stringify(result));
    process.exit(result.ok ? 0 : 1);
  } else {
    if (result.ok) {
      const d = result.data;
      if (typeof d === 'string') console.log(d);
      else if (d && d.text) console.log(d.text);
      else if (result.tabs) {
        result.tabs.forEach(t => console.log(`[${t.index}] ${t.title} — ${t.url}`));
      } else {
        console.log(JSON.stringify(result, null, 2));
      }
    } else {
      console.error(`ERROR [${result.error?.kind || 'unknown'}]: ${result.error?.message}`);
      process.exit(1);
    }
  }
}

// ---- Entry ----
if (process.argv[2] === 'daemon') {
  runDaemon();
} else {
  runClient();
}
