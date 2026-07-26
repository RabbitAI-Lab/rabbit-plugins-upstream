"""Interactive line-chart component shared by the dashboards: renders
directly in the browser via a small inline JS runtime (one <script> emitted
once per page) instead of precomputing static SVG paths in Python. Gives
hover tooltips and keeps every chart visually identical since they all go
through the same renderer.
"""
import json

ICHART_STYLE = """
  .ichart-wrap { position:relative; }
  .ichart-legend { display:flex; gap:14px; margin-bottom:8px; font-size:11px; color:#8e8e93; }
  .ichart-legend .sw { display:inline-flex; align-items:center; gap:5px; }
  .ichart-legend .sw i { width:9px; height:9px; border-radius:50%; display:inline-block; }
  .ichart-tip { position:absolute; pointer-events:none; background:rgba(30,30,32,.96);
    border:1px solid #38383a; border-radius:8px; padding:6px 9px; font-size:11px;
    color:#fff; white-space:nowrap; opacity:0; transform:translate(-50%,-100%);
    transition:opacity .08s; z-index:5; }
  .ichart-tip .d { color:#8e8e93; margin-bottom:2px; }
  .ichart-tip .row { display:flex; align-items:center; gap:5px; }
  .ichart-tip .row i { width:7px; height:7px; border-radius:50%; display:inline-block; }
"""

ICHART_SCRIPT = """
function renderIChart(id) {
  const cfg = window.__ICHART_DATA[id];
  const root = document.getElementById(id);
  const width = 640, height = cfg.height || 190;
  const padL = 40, padR = 12, padT = 12, padB = 22;
  const plotW = width - padL - padR, plotH = height - padT - padB;
  const n = cfg.labels.length;
  let vals = [];
  cfg.series.forEach(s => s.values.forEach(v => { if (v !== null && v !== undefined) vals.push(v); }));
  if (cfg.goal != null) vals.push(cfg.goal);
  let lo = Math.min(0, ...vals), hi = Math.max(1, ...vals);
  if (lo === hi) { hi = lo + 1; }
  hi = hi * 1.08;
  const x = i => padL + (n > 1 ? plotW * i / (n - 1) : plotW / 2);
  const y = v => padT + plotH - plotH * (v - lo) / (hi - lo);
  const fmt = cfg.yFmt || (v => Math.round(v));

  let svg = `<svg viewBox="0 0 ${width} ${height}" xmlns="http://www.w3.org/2000/svg" font-family="ui-monospace,monospace" font-size="10">`;
  for (const frac of [0, 0.5, 1]) {
    const gy = padT + plotH * (1 - frac);
    const gv = lo + (hi - lo) * frac;
    svg += `<line x1="${padL}" y1="${gy.toFixed(1)}" x2="${width - padR}" y2="${gy.toFixed(1)}" stroke="#2a2f3a" stroke-width="1"/>`;
    svg += `<text x="2" y="${(gy + 3).toFixed(1)}" fill="#8e8e93">${fmt(gv)}</text>`;
  }
  if (cfg.goal != null) {
    const gy = y(cfg.goal).toFixed(1);
    svg += `<line x1="${padL}" y1="${gy}" x2="${width - padR}" y2="${gy}" stroke="#8e8e93" stroke-width="1" stroke-dasharray="3,3" opacity="0.7"/>`;
  }
  cfg.series.forEach(s => {
    const pts = s.values.map((v, i) => v == null ? null : [x(i), y(v)]).filter(p => p);
    if (pts.length >= 2) {
      const path = 'M ' + pts.map(p => `${p[0].toFixed(1)} ${p[1].toFixed(1)}`).join(' L ');
      svg += `<path d="${path}" fill="none" stroke="${s.color}" stroke-width="2" ${s.dashed ? 'stroke-dasharray="5,4"' : ''}/>`;
    }
  });
  const step = Math.max(1, Math.round(n / 7));
  const lastRegular = Math.floor((n - 1) / step) * step;
  for (let i = 0; i < n; i++) {
    if (i % step === 0 || (i === n - 1 && i - lastRegular >= step / 2)) {
      const anchor = i === n - 1 ? 'end' : (i === 0 ? 'start' : 'middle');
      const tx = i === n - 1 ? width - padR : (i === 0 ? padL : x(i));
      svg += `<text x="${tx.toFixed(1)}" y="${height - 4}" fill="#8e8e93" text-anchor="${anchor}">${cfg.labels[i]}</text>`;
    }
  }
  svg += `<g id="${id}-cursor" style="display:none"><line x1="0" y1="${padT}" x2="0" y2="${padT + plotH}" stroke="#8e8e93" stroke-width="1" stroke-dasharray="2,2"/></g>`;
  cfg.series.forEach((s, si) => {
    svg += `<g id="${id}-dots-${si}"></g>`;
  });
  svg += `<rect id="${id}-overlay" x="${padL}" y="${padT}" width="${plotW}" height="${plotH}" fill="transparent"/>`;
  svg += `</svg>`;

  root.innerHTML = svg;
  const svgEl = root.querySelector('svg');
  const overlay = root.querySelector(`#${id}-overlay`);
  const cursor = root.querySelector(`#${id}-cursor`);
  const dotGroups = cfg.series.map((_, si) => root.querySelector(`#${id}-dots-${si}`));
  let tip = root.querySelector('.ichart-tip');
  if (!tip) {
    tip = document.createElement('div');
    tip.className = 'ichart-tip';
    root.appendChild(tip);
  }

  function nearestIndex(clientX) {
    const rect = svgEl.getBoundingClientRect();
    const px = (clientX - rect.left) / rect.width * width;
    let best = 0, bestDist = Infinity;
    for (let i = 0; i < n; i++) {
      const d = Math.abs(x(i) - px);
      if (d < bestDist) { bestDist = d; best = i; }
    }
    return best;
  }

  function show(i) {
    cursor.style.display = '';
    cursor.setAttribute('transform', `translate(${x(i).toFixed(1)}, 0)`);
    let rows = '';
    cfg.series.forEach((s, si) => {
      const v = s.values[i];
      dotGroups[si].innerHTML = v == null ? '' :
        `<circle cx="${x(i).toFixed(1)}" cy="${y(v).toFixed(1)}" r="3" fill="${s.color}"/>`;
      if (v != null) rows += `<div class="row"><i style="background:${s.color}"></i>${s.name}: ${fmt(v)}</div>`;
    });
    tip.innerHTML = `<div class="d">${cfg.labels[i]}${cfg.fullLabels ? ' (' + cfg.fullLabels[i] + ')' : ''}</div>${rows}`;
    tip.style.opacity = '1';
    const rect = svgEl.getBoundingClientRect();
    tip.style.left = `${(x(i) / width) * rect.width}px`;
    tip.style.top = `${(y(Math.max(...cfg.series.map(s => s.values[i] ?? lo))) / height) * rect.height - 8}px`;
  }
  function hide() {
    cursor.style.display = 'none';
    dotGroups.forEach(g => g.innerHTML = '');
    tip.style.opacity = '0';
  }
  overlay.addEventListener('mousemove', e => show(nearestIndex(e.clientX)));
  overlay.addEventListener('mouseleave', hide);
  overlay.addEventListener('touchmove', e => { show(nearestIndex(e.touches[0].clientX)); e.preventDefault(); }, { passive: false });
}
window.__ICHART_DATA = window.__ICHART_DATA || {};
document.addEventListener('DOMContentLoaded', () => {
  Object.keys(window.__ICHART_DATA).forEach(renderIChart);
});
"""


def chart(chart_id, labels, series, goal=None, height=190, y_fmt_js="v => v.toFixed(0)", legend=True):
    """series: list of {name, color, values, dashed(optional)}. Registers the
    chart's data on window.__ICHART_DATA and emits its container div (+ a
    legend row if requested). Include ICHART_SCRIPT once per page."""
    cfg = {
        "labels": labels,
        "series": [{"name": s["name"], "color": s["color"], "values": s["values"],
                    "dashed": s.get("dashed", False)} for s in series],
        "goal": goal,
        "height": height,
    }
    parts = []
    if legend:
        sw = "".join(f'<span class="sw"><i style="background:{s["color"]}"></i>{s["name"]}</span>' for s in series)
        parts.append(f'<div class="ichart-legend">{sw}</div>')
    parts.append(f'<div class="ichart-wrap" id="{chart_id}"></div>')
    parts.append(f'<script>window.__ICHART_DATA["{chart_id}"] = {json.dumps(cfg)}; '
                 f'window.__ICHART_DATA["{chart_id}"].yFmt = {y_fmt_js};</script>')
    return "".join(parts)
