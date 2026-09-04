// board.mjs — Plandeck's local multi-board hub and live board server.
//
// One process owns every registered plan, its generated app, file watcher, SSE
// clients, and last-good payload. A second CLI process can hand a board to the
// existing hub instead of consuming another port.

import { createServer } from "node:http";
import { existsSync, readFileSync, renameSync, unlinkSync, watch, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { basename, join, resolve } from "node:path";
import { atomicWriteFile, buildPayload } from "./lib/deck.mjs";
import { observe } from "./lib/continuity.mjs";
import { readJournal, recentForNext, resolveActor } from "./lib/journal.mjs";
import { nextMarkdown, writeBoardApp } from "./lib/render.mjs";

const MIME = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".svg": "image/svg+xml; charset=utf-8",
};
const BIND_HOST = "127.0.0.1";
const PUBLIC_HOST = "plandeck.localhost";
const BODY_LIMIT = 64 * 1024;
let breadcrumbWriteCounter = 0;

// Read at call time so tests and parallel CI runs can isolate discovery with
// PLANDECK_HUB_BREADCRUMB instead of sharing one global temp file.
function hubBreadcrumbPath() {
  return process.env.PLANDECK_HUB_BREADCRUMB || join(tmpdir(), "plandeck-hub.json");
}
export const PORT = 41747;
// Windows reserves scattered high-port ranges (Hyper-V / WSL); a fixed port can
// hit EACCES. Fall back down a small ladder, then to an ephemeral port.
const PORT_LADDER = [PORT, 42747, 43747, 44747, 45747, 0];

/** Start a board hub, or register the plan with a compatible hub already on the requested port. */
export async function runBoard(options = {}) {
  const planDir = resolve(options.planDir || "");
  const actor = resolveActor(options.actor);
  if (!options.planDir) throw new Error("Missing plan directory. Usage: plandeck board <dir>");
  if (!existsSync(join(planDir, "plan.yaml"))) throw new Error(`No plan.yaml in ${planDir}`);

  const appDir = writeBoardApp(planDir);
  if (options.once) {
    const payload = buildPayload(planDir);
    if (options.json) console.log(JSON.stringify({ planDir, appDir, payload }, null, 2));
    else console.log(`Generated Plandeck board app at ${appDir}`);
    return { planDir, appDir, payload };
  }

  const host = options.host || BIND_HOST;
  const publicHost = options.host || PUBLIC_HOST;
  const requested = Number.isInteger(options.port) ? options.port : PORT;
  const outcome = await listen({ planDir, host, publicHost, requested, actor, explicitPort: Number.isInteger(options.port) });

  if (outcome.registration) {
    const summary = outcome.registration;
    const port = Number(new URL(summary.url).port);
    const result = {
      ...summary,
      port,
      hub: true,
      registered: true,
      // Same shape as the hub branch: close() unregisters this board so every
      // caller can tear down without caring which branch served it.
      close: () => unregisterFromHub(summary),
    };
    if (options.json) {
      console.log(JSON.stringify(result, null, 2));
    } else {
      console.log(`Plandeck board:  ${summary.url}`);
      console.log(`Served by the existing Plandeck hub at ${new URL(summary.url).origin}/`);
    }
    return result;
  }

  const { hub, server, port } = outcome;
  let record;
  try {
    record = addBoard(hub, planDir, appDir, actor);
  } catch (error) {
    await closeHub(hub, server);
    throw error;
  }
  const summary = boardSummary(hub, record);

  if (options.json) {
    console.log(JSON.stringify({ planDir, url: summary.url, port }, null, 2));
  } else {
    console.log(`Plandeck board:  ${summary.url}`);
    console.log(`Hub index:       ${hubOrigin(hub)}/`);
    console.log(`Watching ${join(planDir, "plan.yaml")}\nPress Ctrl-C to stop.`);
  }

  return {
    planDir,
    url: summary.url,
    boardPath: summary.boardPath,
    port,
    hub: true,
    close: () => closeHub(hub, server),
  };
}

async function listen({ planDir, host, publicHost, requested, actor, explicitPort }) {
  // An explicit --port pins the caller to that port; breadcrumb discovery is
  // only for default invocations hunting the hub wherever it landed.
  const breadcrumb = explicitPort ? null : readHubBreadcrumb();
  if (breadcrumb) {
    const registration = await registerWithHub({ planDir, host: breadcrumb.host, port: breadcrumb.port, actor });
    if (registration) return { registration };
    removeStaleBreadcrumb(breadcrumb);
  }

  const hub = {
    boards: new Map(),
    clients: new Set(),
    host,
    publicHost,
    port: null,
    closePromise: null,
    startedAt: new Date().toISOString(),
    breadcrumb: null,
  };
  const ladder = [requested, ...PORT_LADDER].filter((p, i, all) => all.indexOf(p) === i);
  let lastError = null;

  for (const candidate of ladder) {
    const server = createServer((req, res) => {
      handleRequest(hub, req, res).catch((error) => {
        if (res.headersSent) {
          res.end();
          return;
        }
        sendText(res, error.statusCode || 400, error.message || "Request failed", {
          closeConnection: error.closeConnection === true,
          socket: req.socket,
        });
      });
    });
    try {
      await new Promise((ok, fail) => {
        server.once("error", fail);
        server.listen(candidate, host, () => {
          server.off("error", fail);
          ok();
        });
      });
    } catch (error) {
      lastError = error;
      if (error.code === "EADDRINUSE") {
        const registration = await registerWithHub({ planDir, host, port: candidate, actor });
        if (registration) return { registration };
      }
      if (error.code === "EADDRINUSE" || error.code === "EACCES") continue;
      throw error;
    }

    hub.port = server.address().port;
    try {
      hub.breadcrumb = writeHubBreadcrumb(hub);
    } catch (error) {
      await closeServer(server);
      throw error;
    }
    return { hub, server, port: hub.port };
  }
  throw lastError || new Error("Could not start the Plandeck board server.");
}

async function registerWithHub({ planDir, host, port, actor }) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 1000);
  try {
    const target = `http://${urlHost(connectHost(host))}:${port}/api/boards`;
    const handshake = await fetch(target, { signal: controller.signal });
    if (handshake.status !== 200) return null;
    const state = await handshake.json();
    if (!state || state.hub !== true) return null;
    const response = await fetch(target, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ planDir, actor }),
      signal: controller.signal,
    });
    if (response.status !== 200) return null;
    const summary = await response.json();
    if (!summary || typeof summary.planDir !== "string" || typeof summary.url !== "string" || typeof summary.boardPath !== "string") return null;
    if (rootKey(summary.planDir) !== rootKey(planDir) || !/^\/[A-Za-z0-9-]+\/$/.test(summary.boardPath)) return null;
    const boardUrl = new URL(summary.url);
    if (boardUrl.protocol !== "http:" || boardUrl.pathname !== summary.boardPath) return null;
    return summary;
  } catch {
    return null;
  } finally {
    clearTimeout(timer);
  }
}

async function unregisterFromHub(summary) {
  try {
    const origin = new URL(summary.url).origin;
    await fetch(`${origin}/api/boards?path=${encodeURIComponent(summary.boardPath)}`, { method: "DELETE" });
  } catch {
    // The hub may already be gone; unregistering is best effort.
  }
}

function readHubBreadcrumb() {
  try {
    const value = JSON.parse(readFileSync(hubBreadcrumbPath(), "utf8"));
    if (!value || typeof value !== "object") return null;
    if (!Number.isInteger(value.port) || value.port < 1 || value.port > 65535) return null;
    if (typeof value.host !== "string" || !value.host) return null;
    if (!Number.isInteger(value.pid) || value.pid < 1 || typeof value.startedAt !== "string") return null;
    return { port: value.port, host: value.host, pid: value.pid, startedAt: value.startedAt };
  } catch {
    return null;
  }
}

function writeHubBreadcrumb(hub) {
  const breadcrumb = {
    port: hub.port,
    host: hub.host,
    pid: process.pid,
    startedAt: hub.startedAt,
  };
  breadcrumbWriteCounter += 1;
  const tempPath = `${hubBreadcrumbPath()}.${process.pid}.${Date.now()}.${breadcrumbWriteCounter}.tmp`;
  try {
    writeFileSync(tempPath, `${JSON.stringify(breadcrumb, null, 2)}\n`, { encoding: "utf8", flag: "wx" });
    renameSync(tempPath, hubBreadcrumbPath());
  } catch (error) {
    try {
      unlinkSync(tempPath);
    } catch {
      // The rename may have completed, or the temporary file was never created.
    }
    throw error;
  }
  return breadcrumb;
}

function removeStaleBreadcrumb(expected) {
  try {
    const current = readHubBreadcrumb();
    if (!current || !sameBreadcrumb(current, expected)) return;
    unlinkSync(hubBreadcrumbPath());
  } catch {
    // Discovery must fall through when a stale breadcrumb cannot be removed.
  }
}

function removeHubBreadcrumb(hub) {
  if (hub.breadcrumb) removeStaleBreadcrumb(hub.breadcrumb);
}

function sameBreadcrumb(a, b) {
  return a.port === b.port && a.host === b.host && a.pid === b.pid && a.startedAt === b.startedAt;
}

async function handleRequest(hub, req, res) {
  const requestUrl = new URL(req.url || "/", `http://${BIND_HOST}`);
  const { pathname } = requestUrl;

  if (pathname === "/api/boards") {
    if (req.method === "GET") {
      sendJson(res, hubPayload(hub));
      return;
    }
    if (req.method === "POST") {
      requireTrustedMutation(hub, req);
      const body = await readJson(req);
      if (!body || typeof body.planDir !== "string" || !body.planDir.trim()) throw requestError(400, "planDir is required.");
      const root = resolve(body.planDir);
      if (!existsSync(join(root, "plan.yaml"))) throw requestError(400, `No plan.yaml in ${root}`);
      const actor = resolveActor(typeof body.actor === "string" ? body.actor : undefined);
      const record = addBoard(hub, root, writeBoardApp(root), actor);
      sendJson(res, boardSummary(hub, record));
      return;
    }
    if (req.method === "DELETE") {
      requireTrustedMutation(hub, req);
      const boardPath = normalizeBoardPath(requestUrl.searchParams.get("path"));
      if (!boardPath) throw requestError(400, "DELETE /api/boards needs a board path.");
      if (!removeBoard(hub, boardPath)) {
        sendJson(res, { removed: false, boardPath }, 404);
        return;
      }
      sendJson(res, { removed: true, boardPath });
      return;
    }
    methodNotAllowed(res, "GET, POST, DELETE");
    return;
  }

  if (pathname === "/events") {
    if (req.method !== "GET") {
      methodNotAllowed(res, "GET");
      return;
    }
    openEvents(req, res, hub.clients, "boards", indexPayload(hub));
    return;
  }

  if (pathname === "/") {
    if (req.method !== "GET") {
      methodNotAllowed(res, "GET");
      return;
    }
    sendHtml(res, hubHtml(indexPayload(hub)));
    return;
  }

  const record = matchBoard(hub, pathname);
  if (!record) {
    sendUnknown(hub, res, pathname);
    return;
  }
  if (!existsSync(join(record.root, "plan.yaml"))) {
    removeBoard(hub, record.boardPath);
    sendUnknown(hub, res, pathname);
    return;
  }
  handleBoardRequest(record, req, res, pathname, requestUrl.searchParams);
}

function handleBoardRequest(record, req, res, pathname, searchParams) {
  const prefix = record.boardPath.slice(0, -1);
  if (pathname === prefix) {
    redirect(res, record.boardPath);
    return;
  }
  if (req.method !== "GET") {
    methodNotAllowed(res, "GET");
    return;
  }

  const rest = pathname === record.boardPath ? "/" : pathname.slice(prefix.length);
  if (rest === "/api/board") {
    sendJson(res, record.lastPayload);
    return;
  }
  if (rest === "/api/journal") {
    sendJson(res, {
      entries: readJournal(record.root, {
        since: searchParams.get("since"),
        limit: Number(searchParams.get("limit")) || 20,
      }),
    });
    return;
  }
  if (rest === "/events") {
    openEvents(req, res, record.clients, "board", record.lastPayload);
    return;
  }
  serveStatic(record.appDir, rest, res);
}

function addBoard(hub, planDir, appDir, actor) {
  const root = resolve(planDir);
  const existing = [...hub.boards.values()].find((record) => rootKey(record.root) === rootKey(root));
  if (existing) {
    existing.appDir = appDir;
    existing.actor = resolveActor(actor);
    refreshBoard(hub, existing);
    if (hub.boards.get(existing.boardPath) === existing) return existing;
    return addBoard(hub, root, appDir, actor);
  }

  const boardPath = uniqueBoardPath(hub, safeSlug(root));
  const record = {
    root,
    appDir,
    clients: new Set(),
    watcher: null,
    lastPayload: emptyErrorPayload("Board has not loaded yet."),
    lastGood: null,
    startedAt: new Date().toISOString(),
    boardPath,
    nextWarned: false,
    actor: resolveActor(actor),
  };
  hub.boards.set(boardPath, record);
  refreshBoard(hub, record, false);
  if (!hub.boards.has(boardPath)) throw new Error(`No plan.yaml in ${root}`);

  try {
    record.watcher = watchPlan(root, () => refreshBoard(hub, record));
    record.watcher.on("error", () => refreshBoard(hub, record));
  } catch (error) {
    hub.boards.delete(boardPath);
    throw error;
  }
  broadcastHub(hub);
  return record;
}

function refreshBoard(hub, record, notify = true) {
  if (hub.boards.get(record.boardPath) !== record) return null;
  if (!existsSync(join(record.root, "plan.yaml"))) {
    removeBoard(hub, record.boardPath, notify);
    return null;
  }

  let payload;
  try {
    payload = buildPayload(record.root);
    observe(record.root, payload.cards, { actor: record.actor });
    record.lastGood = payload;
    writeNext(record, payload, boardSummary(hub, record).url);
  } catch (error) {
    if (isMissingBoardError(record, error)) {
      removeBoard(hub, record.boardPath, notify);
      return null;
    }
    payload = stalePayload(record.lastGood, error);
  }

  record.lastPayload = payload;
  broadcast(record.clients, "board", payload);
  if (notify) broadcastHub(hub);
  return payload;
}

function writeNext(record, payload, url) {
  try {
    const path = join(record.root, "NEXT.md");
    const content = nextMarkdown(payload, url, recentForNext(record.root, 5));
    if (existsSync(path) && readFileSync(path, "utf8") === content) return;
    atomicWriteFile(path, content);
  } catch (error) {
    if (record.nextWarned) return;
    record.nextWarned = true;
    console.warn(`Could not refresh ${join(record.root, "NEXT.md")}: ${error.message || error}`);
  }
}

function removeBoard(hub, boardPath, notify = true) {
  const record = hub.boards.get(boardPath);
  if (!record) return false;
  hub.boards.delete(boardPath);
  try {
    record.watcher?.close();
  } catch {
    // A watcher may already be closed after its directory disappears.
  }
  for (const client of record.clients) {
    try {
      client.end();
    } catch {
      // The peer may already have closed its connection.
    }
  }
  record.clients.clear();
  if (notify) broadcastHub(hub);
  return true;
}

function boardSummary(hub, record) {
  const payload = record.lastPayload || record.lastGood || emptyErrorPayload("Board unavailable.");
  return {
    planDir: record.root,
    url: `${hubOrigin(hub)}${record.boardPath}`,
    boardPath: record.boardPath,
    title: payload.plan?.title || "Plandeck",
    slug: record.boardPath.slice(1, -1),
    startedAt: record.startedAt,
  };
}

function hubPayload(hub) {
  return {
    hub: true,
    boards: sortedBoards(hub).map((record) => {
      return {
        ...boardSummary(hub, record),
        rollup: indexRollup(record.lastPayload?.rollup),
      };
    }),
  };
}

function indexRollup(rollup = {}) {
  const counts = rollup?.counts || {};
  const archived = Math.max(0, Number(rollup?.archived?.count) || 0);
  return {
    pct: Number(rollup?.pct) || 0,
    counts: {
      ...counts,
      total: (Number(counts.total) || 0) + archived,
      done: (Number(counts.done) || 0) + archived,
    },
  };
}

function indexPayload(hub) {
  return {
    hub: true,
    boards: sortedBoards(hub).map((record) => {
      const payload = record.lastPayload || {};
      return {
        ...boardSummary(hub, record),
        rollup: indexRollup(payload.rollup),
        nextAction: payload.nextAction || null,
      };
    }),
  };
}

function broadcastHub(hub) {
  broadcast(hub.clients, "boards", indexPayload(hub));
}

function openEvents(req, res, clients, event, payload) {
  res.writeHead(200, {
    "Content-Type": "text/event-stream; charset=utf-8",
    "Cache-Control": "no-cache, no-transform",
    Connection: "keep-alive",
    "X-Accel-Buffering": "no",
  });
  res.write("retry: 1000\n\n");
  clients.add(res);
  sendEvent(res, event, payload);
  req.on("close", () => clients.delete(res));
}

function broadcast(clients, event, payload) {
  for (const client of clients) {
    try {
      sendEvent(client, event, payload);
    } catch {
      clients.delete(client);
    }
  }
}

function matchBoard(hub, pathname) {
  return sortedBoards(hub)
    .sort((a, b) => b.boardPath.length - a.boardPath.length)
    .find((record) => pathname === record.boardPath.slice(0, -1) || pathname.startsWith(record.boardPath)) || null;
}

function uniqueBoardPath(hub, desiredSlug) {
  const base = slug(desiredSlug);
  let candidate = `/${base}/`;
  let suffix = 2;
  while (hub.boards.has(candidate)) {
    candidate = `/${base}-${suffix}/`;
    suffix += 1;
  }
  return candidate;
}

function safeSlug(planDir) {
  try {
    return buildPayload(planDir).plan.slug;
  } catch {
    return basename(planDir);
  }
}

function stalePayload(lastGood, error) {
  if (lastGood) return { ...lastGood, error: error.message || String(error), stale: true };
  return emptyErrorPayload(error.message || String(error));
}

function emptyErrorPayload(message) {
  return {
    error: message,
    stale: false,
    plan: { title: "Plandeck", slug: "", kind: "error" },
    rollup: { pct: 0, counts: {}, donePoints: 0, totalPoints: 0, archived: { count: 0, points: 0 } },
    eta: {},
    criticalPath: { chain: [] },
    nextAction: {},
    warnings: [],
    columns: [],
    cards: [],
  };
}

function isMissingBoardError(record) {
  return !existsSync(record.root) || !existsSync(join(record.root, "plan.yaml"));
}

function watchPlan(dir, onChange) {
  const debounced = debounce(onChange, 80);
  // Generated files are ignored, so refreshing NEXT.md cannot feed the loop.
  const relevant = (name) => !name || name === "plan.yaml" || name === "archive.yaml" || name === "cards" || /^cards[\\/]/.test(name);
  try {
    return watch(dir, { persistent: true, recursive: true }, (_event, name) => {
      if (relevant(name)) debounced();
    });
  } catch {
    // Recursive watch is unsupported here (Linux before Node 20), so a watcher
    // on the plan dir alone never hears edits inside cards/. Watch both, and
    // attach the cards/ watcher late when the directory appears after startup.
    let cardsWatcher = null;
    const watchCards = () => {
      if (cardsWatcher) return;
      try {
        cardsWatcher = watch(join(dir, "cards"), { persistent: true }, () => debounced());
      } catch { /* cards/ does not exist yet */ }
    };
    const topWatcher = watch(dir, { persistent: true }, (_event, name) => {
      if (!name || name === "cards") watchCards();
      if (relevant(name)) debounced();
    });
    watchCards();
    return {
      close: () => {
        topWatcher.close();
        if (cardsWatcher) cardsWatcher.close();
      },
    };
  }
}

function hubHtml(state) {
  const cards = state.boards.map(hubCardHtml).join("");
  const initial = JSON.stringify(state).replace(/</g, "\\u003c");
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Plandeck Hub</title>
  <style>
  :root{color-scheme:light;--canvas:#f7f6f3;--surface:#fff;--surface-2:#fbfbfa;--ink:#1a1a1a;--muted:#7a7a76;
    --line:#e9e8e4;--violet:#5b53e8;--violet-soft:#efedff;--emerald:#2f8f5b;--emerald-soft:#e6f4ec;--gold:#b7791f;--radius:14px;
    font-family:"SF Pro Text","Geist Sans","Inter","Helvetica Neue",Arial,sans-serif}
  @media(prefers-color-scheme:dark){:root{color-scheme:dark;--canvas:#0b1020;--surface:#141b2e;--surface-2:#101728;
    --ink:#f2f5fb;--muted:#98a3bd;--line:#242c42;--violet:#8b84ff;--violet-soft:#221f45;--emerald:#5fce93;--emerald-soft:#123324;--gold:#e0ad55}}
  *{box-sizing:border-box}body{margin:0;min-height:100vh;background:var(--canvas);color:var(--ink);-webkit-font-smoothing:antialiased}
  header,main{width:min(1040px,calc(100% - 32px));margin-inline:auto}header{display:flex;justify-content:space-between;align-items:center;padding:24px 0 16px}
  .brand{font-size:17px;font-weight:800}.live{display:inline-flex;align-items:center;gap:7px;color:var(--muted);font-size:12px;font-weight:700}
  .dot{width:8px;height:8px;border-radius:50%;background:var(--emerald);box-shadow:0 0 0 4px color-mix(in srgb,var(--emerald) 18%,transparent)}
  .dot.off{background:var(--gold);box-shadow:0 0 0 4px color-mix(in srgb,var(--gold) 18%,transparent)}
  .hero{padding:42px 0 28px;border-bottom:1px solid var(--line)}h1,p{margin:0}.eyebrow{color:var(--violet);font-size:11px;font-weight:800;letter-spacing:.1em;text-transform:uppercase}
  h1{margin-top:10px;font-size:clamp(36px,7vw,68px);letter-spacing:-.04em;line-height:.96}.lede{max-width:58ch;margin-top:16px;color:var(--muted);line-height:1.55}
  .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;padding:24px 0 56px}.card{display:grid;gap:16px;padding:18px;border:1px solid var(--line);
    border-radius:var(--radius);background:var(--surface);color:inherit;text-decoration:none;box-shadow:0 10px 30px rgba(24,28,50,.06)}
  .card:hover{border-color:var(--violet)}.card-top{display:flex;justify-content:space-between;gap:12px;align-items:start}.card h2{margin:0;font-size:19px;line-height:1.25}
  .pct{flex:none;padding:5px 9px;border-radius:999px;background:var(--emerald-soft);color:var(--emerald);font-size:12px;font-weight:800}.lanes{color:var(--muted);font-size:12px}
  .next{padding:11px 12px;border-radius:9px;background:var(--violet-soft);font-size:13px;line-height:1.45}.next b{color:var(--violet)}.path{color:var(--muted);font:11px "SF Mono",ui-monospace,monospace}
  .empty{grid-column:1/-1;padding:32px;border:1px dashed var(--line);border-radius:var(--radius);color:var(--muted);text-align:center}
  </style>
</head>
<body>
  <header><div class="brand">Plandeck</div><div class="live"><span class="dot" id="live-dot" title="Live"></span><span id="live-count">${state.boards.length} live</span></div></header>
  <main>
    <section class="hero"><p class="eyebrow">Multi-board hub</p><h1>Every live plan,<br>one port.</h1><p class="lede">Open a board, follow its next move, or keep this index visible while agents work.</p></section>
    <section class="grid" id="boards">${cards || '<div class="empty">No live boards registered.</div>'}</section>
  </main>
  <script>
  const initial=${initial};
  const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
  const card=b=>{const c=b.rollup?.counts||{};const n=b.nextAction||{};return '<a class="card" href="'+esc(b.url)+'"><div class="card-top"><h2>'+esc(b.title)+'</h2><span class="pct">'+(b.rollup?.pct||0)+'%</span></div><div class="lanes">Ready '+(c.ready||0)+' · Active '+(c.active||0)+' · Blocked '+(c.blocked||0)+' · Done '+(c.done||0)+'/'+(c.total||0)+'</div><div class="next"><b>Next</b> '+esc(n.detail||"No next action.")+'</div><div class="path">'+esc(b.boardPath)+'</div></a>'};
  const render=s=>{document.querySelector("#live-count").textContent=s.boards.length+" live";document.querySelector("#boards").innerHTML=s.boards.length?s.boards.map(card).join(""):'<div class="empty">No live boards registered.</div>'};
  render(initial);
  const events=new EventSource("/events");
  const setLive=on=>{const dot=document.querySelector("#live-dot");dot.classList.toggle("off",!on);dot.title=on?"Live":"Reconnecting…"};
  events.onopen=()=>setLive(true);
  events.onerror=()=>setLive(false);
  events.addEventListener("boards",event=>{try{render(JSON.parse(event.data))}catch{}});
  </script>
</body>
</html>`;
}

function hubCardHtml(board) {
  const counts = board.rollup?.counts || {};
  const next = board.nextAction?.detail || "No next action.";
  return `<a class="card" href="${escapeHtml(board.url)}"><div class="card-top"><h2>${escapeHtml(board.title)}</h2><span class="pct">${board.rollup?.pct || 0}%</span></div><div class="lanes">Ready ${counts.ready || 0} · Active ${counts.active || 0} · Blocked ${counts.blocked || 0} · Done ${counts.done || 0}/${counts.total || 0}</div><div class="next"><b>Next</b> ${escapeHtml(next)}</div><div class="path">${escapeHtml(board.boardPath)}</div></a>`;
}

function serveStatic(appDir, rest, res) {
  const clean = rest === "/" ? "/index.html" : rest;
  if (!/^\/[A-Za-z0-9_.-]+$/.test(clean)) {
    sendText(res, 404, "Not found");
    return;
  }
  const file = join(appDir, clean.slice(1));
  if (!existsSync(file)) {
    sendText(res, 404, "Not found");
    return;
  }
  const ext = clean.match(/\.[^.]+$/)?.[0] || "";
  res.writeHead(200, {
    "Content-Type": MIME[ext] || "application/octet-stream",
    "Cache-Control": "no-store",
  });
  res.end(readFileSync(file));
}

async function readJson(req) {
  const chunks = [];
  let length = 0;
  for await (const chunk of req) {
    length += chunk.length;
    if (length > BODY_LIMIT) throw requestError(413, "Request body is too large.", { closeConnection: true });
    chunks.push(chunk);
  }
  try {
    return JSON.parse(Buffer.concat(chunks).toString("utf8"));
  } catch {
    throw requestError(400, "Request body must be JSON.");
  }
}

function requireTrustedMutation(hub, req) {
  const host = String(req.headers.host || "").trim().toLowerCase();
  const allowedHosts = new Set([
    `127.0.0.1:${hub.port}`,
    `localhost:${hub.port}`,
    `${PUBLIC_HOST}:${hub.port}`,
  ]);
  if (!allowedHosts.has(host)) throw requestError(403, "Untrusted Host header.");

  const contentType = String(req.headers["content-type"] || "").split(";", 1)[0].trim().toLowerCase();
  if (contentType !== "application/json") throw requestError(415, "Content-Type must be application/json.");
}

function sendUnknown(hub, res, pathname) {
  const boards = sortedBoards(hub);
  const listed = boards.length
    ? boards.map((record) => `- ${record.boardPath}  ${record.lastPayload?.plan?.title || "Plandeck"}`).join("\n")
    : "- (none)";
  sendText(res, 404, `Unknown Plandeck hub path: ${pathname}\n\nRegistered boards:\n${listed}\n\nDo not kill the hub to restart one board. Unregister that board with DELETE /api/boards?path=/<slug>/.`);
}

function sortedBoards(hub) {
  return [...hub.boards.values()].sort((a, b) => a.boardPath.localeCompare(b.boardPath));
}

function normalizeBoardPath(value) {
  if (!value || typeof value !== "string") return null;
  const clean = `/${value.replace(/^\/+|\/+$/g, "")}/`;
  return clean === "//" ? null : clean;
}

function rootKey(value) {
  const normalized = resolve(value);
  return process.platform === "win32" ? normalized.toLowerCase() : normalized;
}

function connectHost(host) {
  if (host === "0.0.0.0") return BIND_HOST;
  if (host === "::") return "::1";
  return host;
}

function hubOrigin(hub) {
  return `http://${urlHost(hub.publicHost)}:${hub.port}`;
}

function urlHost(host) {
  return host.includes(":") && !host.startsWith("[") ? `[${host}]` : host;
}

function requestError(statusCode, message, options = {}) {
  const error = new Error(message);
  error.statusCode = statusCode;
  Object.assign(error, options);
  return error;
}

async function closeHub(hub, server) {
  if (hub.closePromise) return hub.closePromise;
  for (const boardPath of [...hub.boards.keys()]) removeBoard(hub, boardPath, false);
  for (const client of hub.clients) {
    try {
      client.end();
    } catch {
      // The peer may already have closed its connection.
    }
  }
  hub.clients.clear();
  hub.closePromise = new Promise((ok, fail) => {
    server.close((error) => {
      if (!error || error.code === "ERR_SERVER_NOT_RUNNING") ok();
      else fail(error);
    });
  }).finally(() => removeHubBreadcrumb(hub));
  return hub.closePromise;
}

function closeServer(server) {
  return new Promise((ok) => server.close(() => ok()));
}

function sendJson(res, obj, status = 200) {
  res.writeHead(status, {
    "Content-Type": "application/json; charset=utf-8",
    "Cache-Control": "no-store",
  });
  res.end(JSON.stringify(obj, null, 2));
}

function sendHtml(res, html) {
  res.writeHead(200, {
    "Content-Type": "text/html; charset=utf-8",
    "Cache-Control": "no-store",
  });
  res.end(html);
}

function sendText(res, status, body, { closeConnection = false, socket = null } = {}) {
  const headers = { "Content-Type": "text/plain; charset=utf-8" };
  if (closeConnection) {
    headers.Connection = "close";
    res.shouldKeepAlive = false;
  }
  res.writeHead(status, headers);
  res.end(body, () => {
    if (closeConnection && socket && !socket.destroyed) socket.destroy();
  });
}

function sendEvent(res, event, payload) {
  res.write(`event: ${event}\ndata: ${JSON.stringify(payload)}\n\n`);
}

function methodNotAllowed(res, allow) {
  res.writeHead(405, {
    Allow: allow,
    "Content-Type": "text/plain; charset=utf-8",
  });
  res.end("Method not allowed");
}

function redirect(res, location) {
  res.writeHead(302, { Location: location, "Cache-Control": "no-store" });
  res.end();
}

function debounce(fn, ms) {
  let timer = null;
  return () => {
    clearTimeout(timer);
    timer = setTimeout(fn, ms);
  };
}

function escapeHtml(value) {
  return String(value ?? "").replace(/[&<>"']/g, (char) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;",
  })[char]);
}

function slug(value) {
  return String(value || "").trim().toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "") || "plan";
}
