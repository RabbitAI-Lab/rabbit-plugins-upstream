// Minimal CDP screenshot driver (no deps; uses Node's global WebSocket).
// Usage: node shot.mjs <url> <out.png> <width> <height> [mobile] [action]
// action: none | dialog | menu | nav

const [, , url, out, wArg, hArg, mobileArg = 'false', action = 'none'] = process.argv;
const width = Number(wArg);
const height = Number(hArg);
const mobile = mobileArg === 'true';

const ENDPOINT = 'http://127.0.0.1:9222';

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function newTarget() {
  const res = await fetch(`${ENDPOINT}/json/new?about:blank`, { method: 'PUT' });
  if (!res.ok) throw new Error(`target create failed: ${res.status}`);
  return res.json();
}

class Cdp {
  constructor(ws) {
    this.ws = ws;
    this.id = 0;
    this.pending = new Map();
    ws.addEventListener('message', (ev) => {
      const msg = JSON.parse(ev.data);
      if (msg.id && this.pending.has(msg.id)) {
        const { resolve, reject } = this.pending.get(msg.id);
        this.pending.delete(msg.id);
        if (msg.error) reject(new Error(JSON.stringify(msg.error)));
        else resolve(msg.result);
      }
    });
  }

  send(method, params = {}) {
    const id = ++this.id;
    this.ws.send(JSON.stringify({ id, method, params }));
    return new Promise((resolve, reject) => {
      this.pending.set(id, { resolve, reject });
      setTimeout(() => {
        if (this.pending.has(id)) {
          this.pending.delete(id);
          reject(new Error(`timeout: ${method}`));
        }
      }, 60000);
    });
  }

  async evaluate(expression) {
    const r = await this.send('Runtime.evaluate', {
      expression,
      awaitPromise: true,
      returnByValue: true,
    });
    if (r.exceptionDetails) throw new Error(`eval failed: ${JSON.stringify(r.exceptionDetails)}`);
    return r.result.value;
  }
}

// Click an element by CSS selector, via real mouse events at its centre.
// `text` narrows a selector match to the first element containing that string.
async function click(cdp, selector, text = null) {
  const box = await cdp.evaluate(`(() => {
    const els = [...document.querySelectorAll(${JSON.stringify(selector)})];
    const el = ${text === null ? 'els[0]' : `els.find((e) => e.textContent.includes(${JSON.stringify(text)}))`};
    if (!el) return null;
    const r = el.getBoundingClientRect();
    return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
  })()`);
  if (!box) throw new Error(`selector not found: ${selector}${text ? ` (text: ${text})` : ''}`);
  for (const type of ['mousePressed', 'mouseReleased']) {
    await cdp.send('Input.dispatchMouseEvent', {
      type,
      x: box.x,
      y: box.y,
      button: 'left',
      clickCount: 1,
    });
  }
}

async function typeInto(cdp, selector, text) {
  await click(cdp, selector);
  for (const ch of text) {
    await cdp.send('Input.dispatchKeyEvent', { type: 'keyDown', text: ch });
    await cdp.send('Input.dispatchKeyEvent', { type: 'keyUp', text: ch });
  }
}

const target = await newTarget();
const ws = new WebSocket(target.webSocketDebuggerUrl);
await new Promise((resolve, reject) => {
  ws.addEventListener('open', resolve, { once: true });
  ws.addEventListener('error', reject, { once: true });
});

const cdp = new Cdp(ws);
await cdp.send('Page.enable');
await cdp.send('Runtime.enable');
await cdp.send('Log.enable');
await cdp.send('Console.enable');

// Collect console errors so we can report them honestly.
const consoleErrors = [];
ws.addEventListener('message', (ev) => {
  const msg = JSON.parse(ev.data);
  if (msg.method === 'Log.entryAdded' && msg.params.entry.level === 'error') {
    consoleErrors.push(msg.params.entry.text);
  }
  if (msg.method === 'Runtime.exceptionThrown') {
    consoleErrors.push(msg.params.exceptionDetails.text || 'exception');
  }
});

await cdp.send('Emulation.setDeviceMetricsOverride', {
  width,
  height,
  deviceScaleFactor: 2,
  mobile,
  screenWidth: width,
  screenHeight: height,
});
if (mobile) {
  await cdp.send('Emulation.setTouchEmulationEnabled', { enabled: true, maxTouchPoints: 5 });
}

await cdp.send('Page.navigate', { url });
// Wait for network to settle and MUI to hydrate.
await sleep(6000);
await cdp.evaluate(`document.fonts.ready`);
await sleep(1500);

if (action === 'dialog') {
  await click(cdp, 'button', 'New ticket');
  await sleep(1200);
  // Fill the first two text inputs so the dialog shows real content, not placeholders.
  const inputs = ['.MuiDialog-root input[type="text"], .MuiDialog-root input:not([type])'];
  await typeInto(cdp, inputs[0], 'Refund not received after cancellation');
  await sleep(400);
}

if (action === 'menu') {
  await click(cdp, 'button[aria-label="Ticket actions"]');
  await sleep(800);
}

const { data } = await cdp.send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
const fs = await import('node:fs/promises');
await fs.writeFile(out, Buffer.from(data, 'base64'));

const title = await cdp.evaluate('document.title');
const finalUrl = await cdp.evaluate('location.href');
const dims = await cdp.evaluate('({ w: innerWidth, h: innerHeight, scrollW: document.documentElement.scrollWidth })');

console.log(
  JSON.stringify(
    { out, title, finalUrl, viewport: dims, horizontalOverflow: dims.scrollW > dims.w, consoleErrors },
    null,
    2
  )
);

await fetch(`${ENDPOINT}/json/close/${target.id}`);
ws.close();
