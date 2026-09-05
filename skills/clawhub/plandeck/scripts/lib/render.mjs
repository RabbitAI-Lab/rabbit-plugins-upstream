// render.mjs — the Plandeck board app (index.html + styles.css + app.js).
//
// A static app hydrated by /api/board and kept live over /events (SSE). The
// Kanban layout, the six-lane flow, the gold critical path, the progress ring,
// and the "next action" banner are all Plandeck's own.

import { copyFileSync, existsSync, mkdirSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { describeEntry } from "./journal.mjs";

const __dirname = dirname(fileURLToPath(import.meta.url));
const markPath = join(__dirname, "..", "..", "media", "plandeck-mark.svg");

/**
 * The LLM-legible hand-off. A tiny, stable file an agent re-reads after /clear
 * to know the ONE next move without parsing the whole plan. Kept in its own
 * file on purpose: rewriting a block at the front of a large plan would
 * invalidate the model's prompt cache on every update — this does not.
 */
export function nextMarkdown(payload, boardUrl = "", recentEntries = []) {
  const n = payload.nextAction || {};
  const r = payload.rollup || { pct: 0, donePoints: 0, totalPoints: 0, counts: {} };
  const cards = payload.cards || [];
  const archivedCount = r.archived?.count || 0;
  const ready = cards.filter((c) => c.column === "ready").map((c) => c.id);
  const blocked = cards.filter((c) => c.column === "blocked").map((c) => c.id);
  const card = cards.find((c) => c.id === n.cardId);
  const tags = [];
  if (card) {
    if (card.priority) tags.push(card.priority);
    if (card.onCriticalPath) tags.push("critical path");
    if (Number.isFinite(card.estimate)) tags.push(`${card.estimate} pts`);
    if (card.unblocks) tags.push(`unblocks ${card.unblocks}`);
  }
  const head = n.cardId ? `**${n.cardId} · ${n.title || card?.title || ""}**` : "**No card ready**";
  const badge = tags.length ? `  \`${tags.join("` `")}\`` : "";

  const lines = [
    "# ▸ NEXT",
    "",
    `${head}${badge}`,
    n.detail || "",
    "",
    `- Progress: ${r.pct}% (${r.donePoints}/${r.totalPoints} pts, ${(r.counts.done || 0) + archivedCount}/${cards.length + archivedCount} cards)`,
  ];
  if (ready.length) lines.push(`- Ready now: ${ready.join(", ")}`);
  if (blocked.length) lines.push(`- Blocked: ${blocked.join(", ")}`);
  if (payload.criticalPath && payload.criticalPath.chain && payload.criticalPath.chain.length) {
    lines.push(`- Critical path: ${payload.criticalPath.chain.join(" → ")} (${payload.criticalPath.length} pts)`);
  }
  if (payload.warnings && payload.warnings.length) lines.push(`- ⚠ ${payload.warnings.map((w) => w.detail).join("; ")}`);
  if (recentEntries.length) {
    lines.push("", "## Since you left");
    for (const entry of recentEntries) lines.push(`- ${describeEntry(entry)}`);
    lines.push("");
  }
  if (boardUrl) lines.push(`- Live board: ${boardUrl}`);
  lines.push("", "_Regenerate with `plandeck next --write`. This file is the plan's re-entry breadcrumb; the plan itself lives in plan.yaml._");
  return lines.join("\n") + "\n";
}

/** Write the self-contained static board application for a plan directory. */
export function writeBoardApp(planDir) {
  const appDir = join(planDir, ".plandeck-board");
  mkdirSync(appDir, { recursive: true });
  writeFileSync(join(appDir, "index.html"), `${boardHtml()}\n`);
  writeFileSync(join(appDir, "styles.css"), `${boardCss()}\n`);
  writeFileSync(join(appDir, "app.js"), `${boardJs()}\n`);
  if (existsSync(markPath)) copyFileSync(markPath, join(appDir, "plandeck-mark.svg"));
  return appDir;
}

function boardHtml() {
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Plandeck</title>
  <link rel="stylesheet" href="./styles.css">
  <link rel="icon" href="./plandeck-mark.svg" type="image/svg+xml">
</head>
<body>
  <header class="topbar">
    <div class="brand">
      <img class="brand-mark" src="./plandeck-mark.svg" alt="" width="30" height="30">
      <span class="brand-name">Plandeck</span>
      <span class="live-dot" id="live-dot" title="Live"></span>
    </div>
    <div class="topbar-tools">
      <div class="seg" id="theme-seg" role="group" aria-label="Theme">
        <button data-theme="system" class="on">Auto</button>
        <button data-theme="light">Light</button>
        <button data-theme="dark">Dark</button>
      </div>
    </div>
  </header>

  <main class="shell">
    <section class="plan-head">
      <div class="plan-head-left">
        <div class="plan-meta">
          <p class="eyebrow" id="plan-kind">Plan</p>
          <span class="archive-chip" id="archive-chip" hidden></span>
        </div>
        <h1 id="plan-title">Loading…</h1>
        <p class="north-star" id="plan-northstar"></p>
      </div>
      <div class="plan-head-right">
        <div class="ring" id="ring" style="--pct:0">
          <div class="ring-label"><b id="ring-pct">0%</b><span>done</span></div>
        </div>
        <dl class="stat-grid">
          <div><dt>Points</dt><dd id="stat-points">0 / 0</dd></div>
          <div><dt>Velocity</dt><dd id="stat-velocity">—</dd></div>
          <div><dt>ETA</dt><dd id="stat-eta">—</dd></div>
        </dl>
      </div>
    </section>

    <section class="next-banner" id="next-banner" hidden>
      <span class="next-kicker">Do this next</span>
      <span class="next-body" id="next-body"></span>
    </section>

    <section class="critpath" id="critpath" hidden>
      <span class="critpath-kicker">Critical path</span>
      <span class="critpath-chain" id="critpath-chain"></span>
    </section>

    <section class="warnings" id="warnings" hidden></section>

    <section class="error-banner" id="error-banner" hidden></section>

    <section class="board" id="board" aria-label="Plandeck board"></section>
  </main>

  <div class="modal" id="modal" hidden>
    <button class="modal-scrim" type="button" data-close aria-label="Close"></button>
    <article class="modal-panel" role="dialog" aria-modal="true" aria-labelledby="modal-title">
      <header class="modal-header">
        <div>
          <p class="eyebrow" id="modal-id">Card</p>
          <h2 id="modal-title">Card</h2>
        </div>
        <button class="icon-btn" type="button" data-close aria-label="Close">✕</button>
      </header>
      <div class="modal-body" id="modal-body"></div>
    </article>
  </div>

  <script src="./app.js" type="module"></script>
</body>
</html>`;
}

function boardCss() {
  return `:root{
  color-scheme:light;
  --canvas:#f7f6f3; --surface:#fff; --surface-2:#fbfbfa; --ink:#1a1a1a; --muted:#7a7a76;
  --line:#e9e8e4; --line-strong:#d8d7d2;
  --violet:#5b53e8; --violet-soft:#efedff;
  --gold:#e0a100; --gold-soft:#fbf1d6; --gold-line:#eccf7a;
  --emerald:#2f8f5b; --emerald-soft:#e6f4ec;
  --red:#c23b3b; --red-soft:#fbe9e9;
  --blue:#2f6ca0; --blue-soft:#e6f1fa;
  --radius:12px;
  font-family:"SF Pro Text","Geist Sans","Inter","Helvetica Neue",Arial,sans-serif;
}
:root[data-theme="dark"]{
  color-scheme:dark;
  --canvas:#0b1020; --surface:#141b2e; --surface-2:#101728; --ink:#f2f5fb; --muted:#98a3bd;
  --line:#242c42; --line-strong:#33405e; --violet:#8b84ff; --violet-soft:#221f45;
  --gold:#f0c66a; --gold-soft:#33290f; --gold-line:#5a4a20;
  --emerald:#5fce93; --emerald-soft:#123324; --red:#f0888a; --red-soft:#331a1c;
  --blue:#8fc4ef; --blue-soft:#132635;
}
@media (prefers-color-scheme:dark){:root[data-theme="system"]{
  color-scheme:dark;
  --canvas:#0b1020; --surface:#141b2e; --surface-2:#101728; --ink:#f2f5fb; --muted:#98a3bd;
  --line:#242c42; --line-strong:#33405e; --violet:#8b84ff; --violet-soft:#221f45;
  --gold:#f0c66a; --gold-soft:#33290f; --gold-line:#5a4a20;
  --emerald:#5fce93; --emerald-soft:#123324; --red:#f0888a; --red-soft:#331a1c;
  --blue:#8fc4ef; --blue-soft:#132635;
}}
*{box-sizing:border-box}
body{margin:0;min-height:100vh;background:var(--canvas);color:var(--ink);-webkit-font-smoothing:antialiased}
a{color:inherit}
h1,h2,h3,p,dl,dd{margin:0}

.topbar{position:sticky;top:14px;z-index:20;display:flex;align-items:center;justify-content:space-between;
  width:min(1360px,calc(100% - 40px));margin:14px auto 0;padding:9px 12px 9px 16px;
  border:1px solid var(--line);border-radius:999px;background:color-mix(in srgb,var(--surface) 82%,transparent);
  box-shadow:0 14px 40px rgba(24,28,50,.10);backdrop-filter:blur(18px)}
.brand{display:inline-flex;align-items:center;gap:9px;font-weight:800;font-size:17px;letter-spacing:-.01em}
.brand-mark{display:block}
.live-dot{width:8px;height:8px;border-radius:999px;background:var(--emerald);box-shadow:0 0 0 4px color-mix(in srgb,var(--emerald) 18%,transparent);margin-left:2px}
.live-dot.off{background:var(--gold);box-shadow:0 0 0 4px color-mix(in srgb,var(--gold) 18%,transparent)}
.seg{display:inline-flex;gap:2px;padding:3px;border:1px solid var(--line);border-radius:999px;background:var(--surface-2)}
.seg button{border:0;border-radius:999px;padding:6px 12px;background:transparent;color:var(--muted);font-weight:700;font-size:13px;cursor:pointer}
.seg button.on{background:var(--surface);color:var(--ink);box-shadow:0 1px 2px rgba(0,0,0,.08)}

.shell{width:min(1440px,100%);margin:0 auto;padding:24px clamp(16px,3vw,28px) 56px}

.plan-head{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:28px;align-items:end;padding:18px 0 22px;border-bottom:1px solid var(--line)}
.plan-meta{display:flex;align-items:center;gap:9px}
.eyebrow{color:var(--muted);font-size:11px;font-weight:800;letter-spacing:.09em;text-transform:uppercase}
.archive-chip{display:inline-flex;padding:3px 7px;border:1px solid var(--line);border-radius:999px;background:var(--surface-2);color:var(--muted);font-size:10.5px;font-weight:700}
.archive-chip[hidden]{display:none}
#plan-title{margin:8px 0 10px;font-size:clamp(30px,4.4vw,54px);line-height:1;letter-spacing:-.02em}
.north-star{max-width:60ch;color:var(--muted);line-height:1.5;font-size:15px}
.plan-head-right{display:flex;align-items:center;gap:22px}
.ring{--pct:0;width:96px;height:96px;border-radius:999px;display:grid;place-items:center;flex:none;
  background:conic-gradient(var(--emerald) calc(var(--pct)*1%),var(--line) 0)}
.ring{position:relative}
.ring::before{content:"";position:absolute;inset:0;margin:auto;width:74px;height:74px;border-radius:999px;background:var(--surface)}
.ring-label{position:relative;text-align:center;line-height:1.05}
.ring-label b{font-size:22px}.ring-label span{display:block;color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.06em}
.stat-grid{display:grid;grid-template-columns:repeat(3,auto);gap:1px;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:var(--line)}
.stat-grid div{padding:11px 15px;background:var(--surface);min-width:78px}
.stat-grid dt{color:var(--muted);font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin-bottom:5px}
.stat-grid dd{font-size:15px;font-weight:700;font-variant-numeric:tabular-nums}

.next-banner{display:flex;align-items:center;gap:12px;margin-top:18px;padding:13px 16px;border:1px solid var(--gold-line);
  border-radius:var(--radius);background:linear-gradient(90deg,var(--gold-soft),transparent 70%)}
.next-kicker{flex:none;font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--gold);
  padding:4px 9px;border:1px solid var(--gold-line);border-radius:999px;background:var(--surface)}
.next-body{font-size:15px;font-weight:600;line-height:1.4}
.next-body b{color:var(--gold)}

.critpath{display:flex;align-items:center;gap:10px;margin-top:12px;flex-wrap:wrap}
.critpath-kicker{color:var(--muted);font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase}
.critpath-chain{display:inline-flex;gap:6px;flex-wrap:wrap;align-items:center}
.chip-node{display:inline-flex;align-items:center;gap:6px;padding:4px 9px;border:1px solid var(--gold-line);border-radius:999px;
  background:var(--gold-soft);font-size:12px;font-weight:700;font-variant-numeric:tabular-nums}
.chip-node .arrow{color:var(--muted)}
.critpath-chain .sep{color:var(--muted);font-weight:700}

.warnings{display:grid;gap:6px;margin-top:14px}
.warn{display:flex;gap:8px;align-items:center;padding:8px 12px;border:1px solid var(--red-soft);border-radius:9px;background:var(--red-soft);color:var(--red);font-size:13px;font-weight:600}
.warn.soft{border-color:var(--gold-line);background:var(--gold-soft);color:var(--gold)}
.error-banner{margin-top:14px;padding:10px 13px;border:1px solid var(--red);border-radius:9px;background:var(--red-soft);color:var(--red);font-size:13px;font-weight:700}
.error-banner[hidden]{display:none}

.board{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(248px,1fr);gap:14px;margin-top:22px;overflow-x:auto;padding-bottom:8px;scroll-snap-type:x proximity}
.column{min-width:0;border:1px solid var(--line);border-radius:var(--radius);background:var(--surface-2);display:flex;flex-direction:column;scroll-snap-align:start}
.column-head{display:flex;align-items:baseline;justify-content:space-between;gap:8px;padding:13px 14px 10px}
.column-head h2{font-size:13.5px;font-weight:800;letter-spacing:.02em;text-transform:uppercase;color:var(--ink)}
.column-head .blurb{display:block;margin-top:3px;color:var(--muted);font-size:11.5px;font-weight:500;letter-spacing:0;text-transform:none}
.column-count{flex:none;color:var(--muted);font-size:12px;font-weight:700;font-variant-numeric:tabular-nums}
.column[data-col="ready"] .column-count{color:var(--emerald)}
.card-list{display:grid;gap:9px;padding:4px 10px 12px;align-content:start;min-height:24px}

.card{position:relative;display:flex;flex-direction:column;gap:9px;padding:12px;border:1px solid var(--line);border-radius:10px;
  background:var(--surface);cursor:pointer;text-align:left;transition:transform .14s ease,border-color .14s ease,box-shadow .14s ease}
.card:hover{transform:translateY(-1px);border-color:var(--line-strong);box-shadow:0 6px 18px rgba(24,28,50,.08)}
.card.crit{border-left:3px solid var(--gold)}
.card.active{border-color:transparent;background:
  linear-gradient(var(--surface),var(--surface)) padding-box,
  linear-gradient(115deg,var(--violet),var(--gold),var(--emerald),var(--violet)) border-box;
  box-shadow:0 12px 30px rgba(91,83,232,.14)}
.card.active::before{content:"";position:absolute;inset:-1px;z-index:0;border-radius:10px;
  background:conic-gradient(from 0deg,transparent 0 60%,color-mix(in srgb,var(--violet) 40%,transparent),color-mix(in srgb,var(--gold) 50%,transparent),transparent 82%);
  animation:spin 3s linear infinite;opacity:.7}
.card.active::after{content:"";position:absolute;inset:1px;z-index:0;border-radius:9px;background:var(--surface)}
.card>*{position:relative;z-index:1}
@keyframes spin{to{transform:rotate(360deg)}}
.card-top{display:flex;align-items:center;justify-content:space-between;gap:8px}
.card-id{color:var(--muted);font-family:"Geist Mono","SF Mono",ui-monospace,monospace;font-size:11.5px;font-weight:600}
.card-id .star{color:var(--gold)}
.est{display:inline-flex;align-items:center;gap:3px;padding:2px 7px;border-radius:999px;background:var(--violet-soft);color:var(--violet);font-size:11px;font-weight:800;font-variant-numeric:tabular-nums}
.card-title{font-size:14px;line-height:1.35;font-weight:600;overflow-wrap:anywhere}
.card-foot{display:flex;flex-wrap:wrap;gap:5px;align-items:center;margin-top:auto}
.badge{display:inline-flex;align-items:center;gap:4px;padding:3px 7px;border-radius:6px;font-size:10.5px;font-weight:800;letter-spacing:.02em;text-transform:uppercase}
.b-role{background:var(--blue-soft);color:var(--blue)}
.b-p0,.b-p1{background:var(--red-soft);color:var(--red)}
.b-p2{background:var(--gold-soft);color:var(--gold)}
.b-p3,.b-p4{background:var(--surface-2);color:var(--muted);border:1px solid var(--line)}
.b-risk-high{background:var(--red-soft);color:var(--red)}
.b-risk-med{background:var(--gold-soft);color:var(--gold)}
.b-ready{background:var(--emerald-soft);color:var(--emerald)}
.b-aging{background:var(--gold-soft);color:var(--gold)}
.dep{display:inline-flex;align-items:center;gap:5px;color:var(--muted);font-size:11px;font-weight:600}
.dep.unmet{color:var(--red)}
.dep.unlocks{color:var(--emerald)}
.card.done .card-title{color:var(--muted)}
.column[data-col="done"] .card{background:var(--surface-2)}
.empty{padding:14px;color:var(--muted);font-size:13px;text-align:center}

.modal[hidden]{display:none}
.modal{position:fixed;inset:0;z-index:40;display:grid;place-items:center;padding:22px}
.modal-scrim{position:absolute;inset:0;border:0;background:rgba(12,14,26,.44);backdrop-filter:blur(2px)}
.modal-panel{position:relative;width:min(720px,100%);max-height:min(84vh,860px);overflow:auto;border:1px solid var(--line);border-radius:16px;background:var(--surface);box-shadow:0 40px 90px rgba(0,0,0,.34)}
.modal-header{position:sticky;top:0;display:flex;align-items:start;justify-content:space-between;gap:16px;padding:18px 20px;border-bottom:1px solid var(--line);background:var(--surface)}
.modal-header h2{font-size:21px;line-height:1.2;letter-spacing:-.01em}
.icon-btn{width:32px;height:32px;flex:none;border:1px solid var(--line);border-radius:8px;background:var(--surface);color:var(--muted);cursor:pointer;font-size:14px}
.modal-body{display:grid;gap:16px;padding:20px}
.kv{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:1px;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:var(--line)}
.kv div{background:var(--surface-2);padding:10px 12px}
.kv dt{color:var(--muted);font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.05em;margin-bottom:4px}
.kv dd{font-size:14px;font-weight:600}
.block h3{font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin-bottom:7px}
.block ul{margin:0;padding-left:18px;display:grid;gap:4px}
.block code,.mono{font-family:"Geist Mono","SF Mono",ui-monospace,monospace;font-size:12.5px}
.cmd{display:flex;gap:8px;align-items:center;padding:6px 9px;border:1px solid var(--line);border-radius:7px;background:var(--surface-2);font-family:"Geist Mono",ui-monospace,monospace;font-size:12.5px}
.cmd .ok{color:var(--emerald);font-weight:800}.cmd .fail{color:var(--red);font-weight:800}
.note{white-space:pre-wrap;line-height:1.5;font-size:13.5px;border:1px solid var(--line);border-radius:10px;padding:12px 14px;background:var(--surface-2)}

@media (max-width:720px){.plan-head{grid-template-columns:1fr}.plan-head-right{justify-content:flex-start}}
@media (prefers-reduced-motion:reduce){.card.active::before{animation:none;opacity:.24}.card{transition:none}}`;
}

function boardJs() {
  // Runtime interpolation and template backticks are escaped (\` and \${) so
  // they survive being embedded in this outer template literal.
  return `const $ = (s, r=document)=>r.querySelector(s);
const board = $("#board");
let liveDot = $("#live-dot");

const THEME_KEY = "plandeck-theme";
function applyTheme(t){document.documentElement.dataset.theme=t;
  for(const b of document.querySelectorAll("#theme-seg button")) b.classList.toggle("on", b.dataset.theme===t);
  try{localStorage.setItem(THEME_KEY,t)}catch{}}
applyTheme((()=>{try{return localStorage.getItem(THEME_KEY)}catch{return null}})()||"system");
$("#theme-seg").addEventListener("click",e=>{const b=e.target.closest("button");if(b)applyTheme(b.dataset.theme)});

const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const pri=p=>p?\`<span class="badge b-\${p.toLowerCase()}">\${esc(p)}</span>\`:"";

function render(p){
  const error=$("#error-banner");
  if(p.error&&p.columns&&p.columns.length){
    error.hidden=false;error.textContent="plan.yaml broken: "+p.error+" — showing last good state"}
  else{error.hidden=true;if(p.error){board.innerHTML=\`<div class="empty">\${esc(p.error)}</div>\`;return}}
  $("#plan-kind").textContent=(p.plan.kind||"plan").replace(/_/g," ");
  $("#plan-title").textContent=p.plan.title;
  const ns=$("#plan-northstar");ns.textContent=p.plan.northStar||"";ns.hidden=!p.plan.northStar;
  const archive=$("#archive-chip");const archived=p.rollup.archived?.count||0;
  archive.textContent=archived+" archived";archive.hidden=!archived;

  const pct=p.rollup.pct||0;
  const ring=$("#ring");ring.style.setProperty("--pct",pct);$("#ring-pct").textContent=pct+"%";
  $("#stat-points").textContent=\`\${p.rollup.donePoints} / \${p.rollup.totalPoints}\`;
  $("#stat-velocity").textContent=p.eta.velocity?\`\${p.eta.velocity}/day\${p.eta.basis?" ("+p.eta.basis+")":""}\`:"—";
  $("#stat-eta").textContent=p.eta.date?\`\${p.eta.date} (\${p.eta.days}d)\`:"—";

  const nb=$("#next-banner");
  if(p.nextAction&&p.nextAction.detail){nb.hidden=false;
    $("#next-body").innerHTML=(p.nextAction.cardId?\`<b>\${esc(p.nextAction.cardId)}</b> · \`:"")+esc(p.nextAction.detail)}
  else nb.hidden=true;

  const cp=$("#critpath");
  if(p.criticalPath&&p.criticalPath.chain&&p.criticalPath.chain.length){cp.hidden=false;
    $("#critpath-chain").innerHTML=p.criticalPath.chain.map((id,i)=>
      \`\${i?'<span class="sep">›</span>':''}<span class="chip-node">\${esc(id)}</span>\`).join("")+
      \` <span class="sep">= \${p.criticalPath.length} pts</span>\`}
  else cp.hidden=true;

  const w=$("#warnings");
  if(p.warnings&&p.warnings.length){w.hidden=false;
    w.innerHTML=p.warnings.map(x=>\`<div class="warn \${x.kind==='aging'||x.kind==='multi-active'?'soft':''}">⚠ \${esc(x.detail)}</div>\`).join("")}
  else w.hidden=true;

  board.innerHTML="";
  for(const col of p.columns){
    const el=document.createElement("section");el.className="column";el.dataset.col=col.id;
    el.innerHTML=\`<div class="column-head"><div><h2>\${esc(col.title)}</h2><span class="blurb">\${esc(col.blurb)}</span></div>
      <span class="column-count">\${col.count}\${col.points?' · '+col.points+'p':''}</span></div>
      <div class="card-list"></div>\`;
    const listEl=el.querySelector(".card-list");
    if(!col.cards.length)listEl.innerHTML='<div class="empty">—</div>';
    for(const c of col.cards)listEl.appendChild(cardEl(c));
    board.appendChild(el);
  }
}

function cardEl(c){
  const b=document.createElement("button");
  b.className="card"+(c.status==="active"||c.column==="doing"?" active":"")+(c.onCriticalPath?" crit":"")+(c.column==="done"?" done":"");
  b.addEventListener("click",()=>openModal(c));
  const est=Number.isFinite(c.estimate)?\`<span class="est">\${c.estimate}p</span>\`:"";
  const badges=[
    c.role?\`<span class="badge b-role">\${esc(c.role)}</span>\`:"",
    pri(c.priority),
    c.risk&&c.risk!=="low"?\`<span class="badge b-risk-\${esc(c.risk)}">\${esc(c.risk)} risk</span>\`:"",
    c.ready&&c.column==="ready"?'<span class="badge b-ready">ready</span>':"",
    c.aging?\`<span class="badge b-aging">\${c.ageDays}d idle</span>\`:"",
  ].join("");
  let dep="";
  if(c.unmetDeps&&c.unmetDeps.length)dep=\`<span class="dep unmet">⛓ waiting on \${c.unmetDeps.map(esc).join(", ")}</span>\`;
  else if(c.dependsOn&&c.dependsOn.length)dep=\`<span class="dep">⛓ after \${c.dependsOn.map(esc).join(", ")}</span>\`;
  if(c.unblocks>0)dep+=\`<span class="dep unlocks">🔓 unlocks \${c.unblocks}</span>\`;
  b.innerHTML=\`<div class="card-top"><span class="card-id">\${esc(c.id)}\${c.onCriticalPath?' <span class="star" title="critical path">★</span>':''}</span>\${est}</div>
    <div class="card-title">\${esc(c.title)}</div>
    <div class="card-foot">\${badges}\${dep?'<span style="flex-basis:100%"></span>'+dep:''}</div>\`;
  return b;
}

const modal=$("#modal");
function openModal(c){
  $("#modal-id").textContent=c.id+(c.onCriticalPath?" · critical path":"");
  $("#modal-title").textContent=c.title;
  const kv=[
    ["Column",c.column],["Role",c.role||"—"],["Estimate",Number.isFinite(c.estimate)?c.estimate+" pts":"—"],
    ["Priority",c.priority||"—"],["Confidence",Number.isFinite(c.confidence)?Math.round(c.confidence*100)+"%":"—"],
    ["Risk",c.risk||"—"],["Unblocks",c.unblocks],["Age",c.ageDays!=null?c.ageDays+"d":"—"],
  ].map(([k,v])=>\`<div><dt>\${esc(k)}</dt><dd>\${esc(v)}</dd></div>\`).join("");
  let html=\`<dl class="kv">\${kv}</dl>\`;
  if(c.nextAction)html+=\`<div class="block"><h3>Next action</h3><div class="note">\${esc(c.nextAction)}</div></div>\`;
  if(c.objective&&c.objective!==c.title)html+=\`<div class="block"><h3>Objective</h3><p>\${esc(c.objective)}</p></div>\`;
  if(c.dependsOn&&c.dependsOn.length)html+=\`<div class="block"><h3>Depends on</h3><ul>\${c.dependsOn.map(d=>\`<li class="mono">\${esc(d)}\${c.unmetDeps.includes(d)?' — <span style="color:var(--red)">not done</span>':' — <span style="color:var(--emerald)">done</span>'}</li>\`).join("")}</ul></div>\`;
  if(c.verify&&c.verify.length)html+=\`<div class="block"><h3>Verify</h3>\${c.verify.map(v=>\`<div class="cmd">\${esc(v)}</div>\`).join("")}</div>\`;
  if(c.receipt){const r=c.receipt;
    let rc="";if(r.summary)rc+=\`<p>\${esc(r.summary)}</p>\`;
    if(r.changed_files&&r.changed_files.length)rc+=\`<h3 style="margin-top:10px">Changed</h3><ul>\${r.changed_files.map(f=>\`<li class="mono">\${esc(f)}</li>\`).join("")}</ul>\`;
    if(r.commands&&r.commands.length)rc+=r.commands.map(cm=>\`<div class="cmd">\${esc(cm.cmd)} \${cm.status?\`<span class="\${cm.status==='pass'?'ok':cm.status==='fail'?'fail':''}">\${esc(cm.status)}</span>\`:''}</div>\`).join("");
    if(rc)html+=\`<div class="block"><h3>Receipt\${r.result?' · '+esc(r.result):''}</h3>\${rc}</div>\`}
  if(c.noteContent)html+=\`<div class="block"><h3>Note</h3><div class="note">\${esc(c.noteContent)}</div></div>\`;
  $("#modal-body").innerHTML=html;
  modal.hidden=false;
}
modal.addEventListener("click",e=>{if(e.target.matches("[data-close],.modal-scrim"))modal.hidden=true});
document.addEventListener("keydown",e=>{if(e.key==="Escape")modal.hidden=true});

function setLive(on){liveDot.classList.toggle("off",!on);liveDot.title=on?"Live":"Reconnecting…"}

async function boot(){
  if(window.__PLANDECK_STATIC__){render(window.__PLANDECK_STATIC__);setLive(true);return;}
  try{const r=await fetch("./api/board",{cache:"no-store"});render(await r.json())}catch(e){}
  connect();
}
function connect(){
  const es=new EventSource("./events");
  es.addEventListener("board",e=>{setLive(true);try{render(JSON.parse(e.data))}catch{}});
  es.onopen=()=>setLive(true);
  es.onerror=()=>{setLive(false)};
}
boot();`;
}
