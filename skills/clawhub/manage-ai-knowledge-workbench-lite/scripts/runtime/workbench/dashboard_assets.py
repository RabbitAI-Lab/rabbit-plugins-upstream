"""Dependency-free dashboard templates bundled with the deterministic core."""

from __future__ import annotations


STYLES_CSS = r"""
:root {
  color-scheme: light;
  --bg: #f4f7fb;
  --panel: rgba(255, 255, 255, 0.94);
  --ink: #152033;
  --muted: #667085;
  --line: #dce3ec;
  --brand: #3157d5;
  --brand-soft: #e9eeff;
  --good: #157f5b;
  --warn: #a15c00;
  --danger: #a53a4b;
  --shadow: 0 18px 45px rgba(32, 48, 78, 0.09);
}
* { box-sizing: border-box; }
body {
  margin: 0;
  min-height: 100vh;
  color: var(--ink);
  background:
    radial-gradient(circle at 8% 0%, #dfe8ff 0, transparent 30%),
    radial-gradient(circle at 100% 8%, #dff6ed 0, transparent 25%),
    var(--bg);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
}
a { color: inherit; }
.shell { width: min(1480px, calc(100% - 32px)); margin: 0 auto; padding: 28px 0 48px; }
.hero {
  display: grid;
  grid-template-columns: 1.5fr 1fr;
  gap: 24px;
  padding: 32px;
  border: 1px solid rgba(255,255,255,.8);
  border-radius: 24px;
  background: linear-gradient(135deg, rgba(255,255,255,.96), rgba(240,244,255,.9));
  box-shadow: var(--shadow);
}
.eyebrow { margin: 0 0 8px; color: var(--brand); font-size: 13px; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; }
h1 { margin: 0; font-size: clamp(32px, 4vw, 58px); line-height: 1.05; letter-spacing: -.04em; }
.hero p { color: var(--muted); line-height: 1.7; max-width: 760px; }
.hero-meta { display: grid; gap: 10px; align-content: center; }
.meta-row { display: flex; justify-content: space-between; gap: 18px; padding: 12px 14px; border-radius: 13px; background: rgba(255,255,255,.75); }
.meta-row span { color: var(--muted); }
.toolbar { display: flex; gap: 12px; margin: 22px 0; }
.toolbar input {
  width: 100%; padding: 14px 16px; border: 1px solid var(--line); border-radius: 14px;
  background: rgba(255,255,255,.95); color: var(--ink); font-size: 15px; outline: none;
}
.toolbar input:focus { border-color: var(--brand); box-shadow: 0 0 0 4px var(--brand-soft); }
.kpis { display: grid; grid-template-columns: repeat(5, 1fr); gap: 14px; }
.kpi, .panel { border: 1px solid var(--line); background: var(--panel); box-shadow: var(--shadow); }
.kpi { padding: 18px; border-radius: 18px; }
.kpi span { color: var(--muted); font-size: 13px; }
.kpi strong { display: block; margin-top: 8px; font-size: 30px; letter-spacing: -.03em; }
.grid { display: grid; grid-template-columns: repeat(12, 1fr); gap: 18px; margin-top: 18px; }
.panel { grid-column: span 6; border-radius: 20px; padding: 22px; min-width: 0; }
.panel.wide { grid-column: span 12; }
.panel h2 { margin: 0 0 6px; font-size: 20px; }
.panel-sub { margin: 0 0 18px; color: var(--muted); font-size: 14px; }
.chips { display: flex; flex-wrap: wrap; gap: 8px; }
.chip { padding: 7px 10px; border-radius: 999px; background: var(--brand-soft); color: #2949ae; font-size: 13px; }
.list { display: grid; gap: 10px; }
.row { display: grid; gap: 4px; padding: 13px; border: 1px solid var(--line); border-radius: 13px; background: #fff; }
.row strong { overflow-wrap: anywhere; }
.row small { color: var(--muted); overflow-wrap: anywhere; }
.project { padding: 15px; border-radius: 15px; background: #fff; border: 1px solid var(--line); }
.project-head { display: flex; justify-content: space-between; gap: 12px; align-items: baseline; }
.progress { height: 8px; margin-top: 12px; border-radius: 999px; background: #edf0f5; overflow: hidden; }
.progress i { display: block; height: 100%; background: linear-gradient(90deg, var(--brand), #6e8cff); }
.muted { color: var(--muted); }
.good { color: var(--good); }
.warn { color: var(--warn); }
.danger { color: var(--danger); }
.graph { min-height: 300px; border: 1px solid var(--line); border-radius: 14px; background: #fbfcff; overflow: hidden; }
.graph svg { display: block; width: 100%; height: 300px; }
.node { fill: #fff; stroke: var(--brand); stroke-width: 2; }
.edge { stroke: #b9c5dc; stroke-width: 1.5; }
.node-label { fill: var(--ink); font-size: 11px; }
.boundary { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
.boundary div { padding: 13px; border-radius: 13px; background: #f8f9fc; border: 1px solid var(--line); }
.empty { color: var(--muted); padding: 16px; text-align: center; }
footer { margin-top: 20px; color: var(--muted); text-align: center; font-size: 13px; }
@media (max-width: 980px) {
  .hero { grid-template-columns: 1fr; }
  .kpis { grid-template-columns: repeat(2, 1fr); }
  .panel { grid-column: span 12; }
  .boundary { grid-template-columns: 1fr; }
}
@media (max-width: 560px) {
  .shell { width: min(100% - 20px, 1480px); padding-top: 10px; }
  .hero { padding: 22px; border-radius: 18px; }
  .kpis { grid-template-columns: 1fr; }
}
""".strip() + "\n"


APP_JS = r"""
(() => {
  "use strict";
  const embedded = document.getElementById("workbench-data");
  const data = JSON.parse(embedded.textContent);
  const byId = (id) => document.getElementById(id);
  const escapeText = (value) => String(value ?? "");
  const shortPath = (record) => `${record.source_id}/${record.path}`;

  const setText = (id, value) => { byId(id).textContent = escapeText(value); };
  setText("generated", data.generated_at);
  setText("privacy", data.privacy.mode);
  setText("update-mode", data.update.mode);
  setText("source-count", data.summary.files_total);
  setText("visible-count", data.summary.visible_records);
  setText("relation-count", data.summary.relations_total);
  setText("issue-count", data.summary.issues_total);
  setText("excluded-count", data.summary.excluded_sensitive);

  const renderRecords = (records) => {
    const root = byId("records");
    root.replaceChildren();
    if (!records.length) {
      const empty = document.createElement("div");
      empty.className = "empty";
      empty.textContent = "没有匹配的可见记录";
      root.appendChild(empty);
      return;
    }
    records.slice(0, 80).forEach((record) => {
      const row = document.createElement("div");
      row.className = "row";
      const title = document.createElement("strong");
      title.textContent = record.title;
      const meta = document.createElement("small");
      meta.textContent = `${shortPath(record)} · ${record.type || record.kind} · ${record.sensitivity}`;
      row.append(title, meta);
      root.appendChild(row);
    });
  };

  const renderTopics = () => {
    const root = byId("topics");
    data.topics.forEach((topic) => {
      const chip = document.createElement("span");
      chip.className = "chip";
      chip.textContent = `${topic.label} · ${topic.count}`;
      root.appendChild(chip);
    });
    if (!data.topics.length) root.textContent = "暂无标签";
  };

  const renderProjects = () => {
    const root = byId("projects");
    data.projects.forEach((project) => {
      const card = document.createElement("div");
      card.className = "project";
      const head = document.createElement("div");
      head.className = "project-head";
      const title = document.createElement("strong");
      title.textContent = project.title;
      const value = document.createElement("span");
      value.className = project.progress.status === "known" ? "good" : "muted";
      value.textContent = project.progress.status === "known" ? `${project.progress.value}%` : "unknown";
      head.append(title, value);
      const basis = document.createElement("small");
      basis.className = "muted";
      basis.textContent = project.progress.basis || "没有可审计分母";
      card.append(head, basis);
      if (project.progress.status === "known") {
        const bar = document.createElement("div");
        bar.className = "progress";
        const fill = document.createElement("i");
        fill.style.width = `${Math.max(0, Math.min(100, project.progress.value))}%`;
        bar.appendChild(fill);
        card.appendChild(bar);
      }
      root.appendChild(card);
    });
    if (!data.projects.length) root.textContent = "暂无带证据的项目状态";
  };

  const renderRecent = () => {
    const root = byId("recent");
    data.recent_changes.forEach((record) => {
      const row = document.createElement("div");
      row.className = "row";
      const title = document.createElement("strong");
      title.textContent = record.title;
      const meta = document.createElement("small");
      meta.textContent = `${shortPath(record)} · ${record.updated_at}`;
      row.append(title, meta);
      root.appendChild(row);
    });
    if (!data.recent_changes.length) root.textContent = "暂无变化";
  };

  const renderGraph = () => {
    const root = byId("graph");
    const relations = data.relations.slice(0, 60);
    const nodeNames = [...new Set(relations.flatMap((edge) => [edge.from, edge.to]))].slice(0, 30);
    if (!nodeNames.length) {
      root.textContent = "暂无可见关系";
      root.classList.add("empty");
      return;
    }
    const svgNS = "http://www.w3.org/2000/svg";
    const svg = document.createElementNS(svgNS, "svg");
    svg.setAttribute("viewBox", "0 0 900 300");
    const positions = new Map();
    nodeNames.forEach((name, index) => {
      const angle = (Math.PI * 2 * index) / nodeNames.length;
      positions.set(name, {x: 450 + Math.cos(angle) * 310, y: 150 + Math.sin(angle) * 105});
    });
    relations.forEach((edge) => {
      if (!positions.has(edge.from) || !positions.has(edge.to)) return;
      const line = document.createElementNS(svgNS, "line");
      line.classList.add("edge");
      line.setAttribute("x1", positions.get(edge.from).x);
      line.setAttribute("y1", positions.get(edge.from).y);
      line.setAttribute("x2", positions.get(edge.to).x);
      line.setAttribute("y2", positions.get(edge.to).y);
      svg.appendChild(line);
    });
    nodeNames.forEach((name) => {
      const position = positions.get(name);
      const circle = document.createElementNS(svgNS, "circle");
      circle.classList.add("node");
      circle.setAttribute("cx", position.x);
      circle.setAttribute("cy", position.y);
      circle.setAttribute("r", 8);
      const label = document.createElementNS(svgNS, "text");
      label.classList.add("node-label");
      label.setAttribute("x", position.x + 11);
      label.setAttribute("y", position.y + 4);
      label.textContent = name.split("/").pop().slice(0, 28);
      svg.append(circle, label);
    });
    root.appendChild(svg);
  };

  renderRecords(data.records);
  renderTopics();
  renderProjects();
  renderRecent();
  renderGraph();

  byId("search").addEventListener("input", (event) => {
    const query = event.target.value.trim().toLocaleLowerCase();
    const filtered = !query ? data.records : data.records.filter((record) => {
      const haystack = [record.title, record.path, record.type, ...(record.tags || [])].join(" ").toLocaleLowerCase();
      return haystack.includes(query);
    });
    renderRecords(filtered);
  });
})();
""".strip() + "\n"


INDEX_TEMPLATE = r"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; form-action 'none'">
  <title>AI 自动知识工作台</title>
  <link rel="icon" href="data:,">
  <link rel="stylesheet" href="assets/styles.css">
</head>
<body>
  <main class="shell">
    <section class="hero">
      <div>
        <p class="eyebrow">Local-first · Derived · Read-only sources</p>
        <h1>AI 自动知识工作台</h1>
        <p>AI 负责规划和推进，确定性引擎负责扫描、校验与渲染。原始资料保持只读，页面只展示允许的派生元数据。</p>
      </div>
      <div class="hero-meta">
        <div class="meta-row"><span>生成时间</span><strong id="generated">-</strong></div>
        <div class="meta-row"><span>隐私模式</span><strong id="privacy">-</strong></div>
        <div class="meta-row"><span>更新模式</span><strong id="update-mode">-</strong></div>
      </div>
    </section>

    <div class="toolbar"><input id="search" type="search" placeholder="搜索标题、相对路径、类型或标签" aria-label="搜索可见记录"></div>
    <section class="kpis">
      <article class="kpi"><span>源记录</span><strong id="source-count">0</strong></article>
      <article class="kpi"><span>可见记录</span><strong id="visible-count">0</strong></article>
      <article class="kpi"><span>可见关系</span><strong id="relation-count">0</strong></article>
      <article class="kpi"><span>检查问题</span><strong id="issue-count">0</strong></article>
      <article class="kpi"><span>敏感排除</span><strong id="excluded-count">0</strong></article>
    </section>

    <section class="grid">
      <article class="panel"><h2>项目状态</h2><p class="panel-sub">没有证据分母时保持 unknown</p><div id="projects" class="list"></div></article>
      <article class="panel"><h2>知识主题</h2><p class="panel-sub">按可见记录标签聚合</p><div id="topics" class="chips"></div></article>
      <article class="panel"><h2>最近变化</h2><p class="panel-sub">mtime 只表示文件活动，不代表进度提升</p><div id="recent" class="list"></div></article>
      <article class="panel"><h2>可见记录</h2><p class="panel-sub">最多显示前 80 条，可用上方搜索过滤</p><div id="records" class="list"></div></article>
      <article class="panel wide"><h2>知识关系</h2><p class="panel-sub">只包含可见 Markdown 记录之间已解析的显式链接</p><div id="graph" class="graph"></div></article>
      <article class="panel wide">
        <h2>数据与权限边界</h2>
        <p class="panel-sub">页面不是事实源，也不是远程数据库</p>
        <div class="boundary">
          <div><strong>原始资料</strong><br><span class="muted">保持在用户指定目录，默认只读</span></div>
          <div><strong>知识与 HTML</strong><br><span class="muted">均为可重建派生产物</span></div>
          <div><strong>正文与敏感数据</strong><br><span class="muted">正文不嵌入；敏感记录不进入可见视图</span></div>
        </div>
      </article>
    </section>
    <footer>AI Knowledge Workbench · loopback or offline static view</footer>
  </main>
  <script id="workbench-data" type="application/json">__EMBEDDED_DATA__</script>
  <script src="assets/app.js" defer></script>
</body>
</html>
"""
