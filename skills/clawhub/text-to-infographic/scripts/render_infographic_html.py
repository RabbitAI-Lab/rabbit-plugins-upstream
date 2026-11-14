#!/usr/bin/env python3
"""render_infographic_html.py — plan JSON → 自包含静态 HTML 信息图。

约束（即「安全渲染」叙事的技术承诺）：
- 仅 HTML + 内联 CSS + 内联 SVG（几何布局用），零 JavaScript；
- 零外部请求：无 CDN、无字体外链、无图片外链；
- 零依赖：仅 Python 标准库，无 pip 安装；
- 中文优先字体栈，print-safe。

用法:
    python3 render_infographic_html.py plan.json [out.html]
    cat plan.json | python3 render_infographic_html.py - out.html
"""
import json
import math
import re
import sys
from html import escape

# ---------------------------------------------------------------- palettes
PALETTES = {
    "terracotta": {"accent": "#C96F4A", "accent2": "#E8A87C", "bg": "#FBF7F2",
                    "ink": "#2B2622", "muted": "#8A7F76", "line": "#E5D9CD"},
    "ocean":      {"accent": "#2C6E8F", "accent2": "#7FB6CF", "bg": "#F4F8FA",
                    "ink": "#1F2A30", "muted": "#71848E", "line": "#D6E4EC"},
    "forest":     {"accent": "#3E6B4F", "accent2": "#8FB996", "bg": "#F5F8F4",
                    "ink": "#22301F", "muted": "#74836F", "line": "#D8E4D4"},
    "ink":        {"accent": "#4A4A72", "accent2": "#9A9AC2", "bg": "#F6F6F9",
                    "ink": "#242432", "muted": "#75758A", "line": "#DFDFEA"},
    "mono":       {"accent": "#333333", "accent2": "#8C8C8C", "bg": "#F7F7F7",
                    "ink": "#1A1A1A", "muted": "#777777", "line": "#DDDDDD"},
}

FONT_STACK = ('-apple-system,"PingFang SC","Hiragino Sans GB",'
              '"Microsoft YaHei","Noto Sans CJK SC",sans-serif')

# 唯一允许的颜色格式：#RGB 或 #RRGGBB（纯十六进制，天然不含任何可注入字符）。
# 与 schemas/infographic-plan.schema.json 及 validate_infographic_plan.py 保持一致。
_HEX_COLOR_RE = re.compile(r'^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$')


def _validate_color(value, field="accent"):
    """渲染器边界校验：拒绝一切非十六进制颜色，防止 CSS/SVG 注入。"""
    if not isinstance(value, str) or not _HEX_COLOR_RE.match(value):
        raise ValueError(
            f"visual_system.{field} 必须是十六进制颜色（#RGB 或 #RRGGBB），收到: {value!r}")
    return value


def esc(s):
    return escape(str(s), quote=True)


def palette_of(plan):
    vs = plan.get("visual_system") or {}
    p = dict(PALETTES.get(vs.get("palette", "terracotta"), PALETTES["terracotta"]))
    if vs.get("accent"):
        # 严格校验：accent 会插进 CSS 与 SVG 属性，只放行十六进制颜色，非法直接拒绝渲染。
        p["accent"] = _validate_color(vs["accent"], "accent")
    return p


def blocks_of(plan):
    return plan.get("blocks", [])


def rel_of(plan):
    return plan.get("relations", [])


# ---------------------------------------------------------------- flywheel
def render_flywheel(plan, p):
    blocks = blocks_of(plan)
    n = len(blocks)
    cx = cy = 260.0
    r_out, r_in = 190.0, 120.0
    arcs, labels, arrows = [], [], []

    for i, b in enumerate(blocks):
        a0 = -math.pi / 2 + 2 * math.pi * i / n
        a1 = -math.pi / 2 + 2 * math.pi * (i + 1) / n
        fill = p["accent"] if i % 2 == 0 else p["accent2"]

        def pt(r, a):
            return cx + r * math.cos(a), cy + r * math.sin(a)

        x0, y0 = pt(r_out, a0)
        x1, y1 = pt(r_out, a1)
        x2, y2 = pt(r_in, a1)
        x3, y3 = pt(r_in, a0)
        large = 1 if (a1 - a0) > math.pi else 0
        arcs.append(
            f'<path d="M{x0:.1f},{y0:.1f} A{r_out},{r_out} 0 {large} 1 {x1:.1f},{y1:.1f} '
            f'L{x2:.1f},{y2:.1f} A{r_in},{r_in} 0 {large} 0 {x3:.1f},{y3:.1f} Z" '
            f'fill="{fill}" stroke="#fff" stroke-width="3"/>')

        # arrow at segment end (clockwise)
        am = a1 - (a1 - a0) * 0.08
        xa, ya = pt((r_out + r_in) / 2, am)
        tang = am + math.pi / 2
        ah = 14
        p1 = (xa + ah * math.cos(tang), ya + ah * math.sin(tang))
        p2 = (xa + 8 * math.cos(tang - math.pi / 2), ya + 8 * math.sin(tang - math.pi / 2))
        p3 = (xa + 8 * math.cos(tang + math.pi / 2), ya + 8 * math.sin(tang + math.pi / 2))
        arrows.append(
            f'<polygon points="{p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f} '
            f'{p3[0]:.1f},{p3[1]:.1f}" fill="#fff" opacity="0.95"/>')

        am2 = (a0 + a1) / 2
        lx, ly = pt(r_out + 34, am2)
        anchor = "middle"
        if lx > cx + 40:
            anchor = "start"
            lx += 6
        elif lx < cx - 40:
            anchor = "end"
            lx -= 6
        num = f'<tspan fill="{p["muted"]}" font-size="12">{i + 1}. </tspan>'
        labels.append(
            f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" '
            f'font-size="15" font-weight="600" fill="{p["ink"]}">{num}{esc(b["title"])}</text>')

    center = (f'<text x="{cx}" y="{cy - 6}" text-anchor="middle" font-size="20" '
              f'font-weight="700" fill="{p["ink"]}">{esc(plan["meta"]["title"])}</text>')
    if plan["meta"].get("subtitle"):
        center += (f'<text x="{cx}" y="{cy + 18}" text-anchor="middle" font-size="12" '
                   f'fill="{p["muted"]}">{esc(plan["meta"]["subtitle"])}</text>')

    svg = (f'<svg viewBox="0 0 620 520" role="img" style="max-width:620px;width:100%;height:auto">'
           f'{"".join(arcs)}{"".join(arrows)}{center}{"".join(labels)}</svg>')
    return f'<div class="ig-canvas">{svg}</div>'


# ---------------------------------------------------------------- fishbone
def render_fishbone(plan, p):
    blocks = blocks_of(plan)
    heads = [b for b in blocks if b.get("role") == "head"]
    causes = [b for b in blocks if b.get("role") != "head"]
    head = heads[0] if heads else blocks[0]
    if not heads:
        causes = blocks[1:]

    W, H = 720, max(360, 120 * ((len(causes) + 1) // 2) + 120)
    sx0, sx1, sy = 40, W - 170, H / 2
    spine = (f'<line x1="{sx0}" y1="{sy}" x2="{sx1}" y2="{sy}" '
             f'stroke="{p["ink"]}" stroke-width="4"/>')
    head_box = (
        f'<rect x="{sx1 + 10}" y="{sy - 44}" width="150" height="88" rx="10" '
        f'fill="{p["accent"]}"/>'
        f'<text x="{sx1 + 85}" y="{sy - 8}" text-anchor="middle" font-size="15" '
        f'font-weight="700" fill="#fff">{esc(head["title"])}</text>')
    if head.get("text"):
        t = head["text"][:22]
        head_box += (f'<text x="{sx1 + 85}" y="{sy + 16}" text-anchor="middle" '
                     f'font-size="11" fill="#fff" opacity="0.9">{esc(t)}</text>')

    parts, up, down = [], [], []
    for b in causes:
        (up if len(up) <= len(down) else down).append(b)

    def branch(bs, sign):
        out = []
        k = len(bs)
        for j, b in enumerate(bs):
            bx = sx0 + (sx1 - sx0 - 90) * (j + 1) / (k + 1)
            tipy = sy + sign * 110
            out.append(f'<line x1="{bx - 70}" y1="{tipy}" x2="{bx}" y2="{sy}" '
                       f'stroke="{p["accent2"]}" stroke-width="3"/>')
            ly = tipy + (18 if sign > 0 else -10)
            out.append(f'<text x="{bx - 70}" y="{ly}" font-size="14" font-weight="600" '
                       f'fill="{p["ink"]}">{esc(b["title"])}</text>')
            if b.get("text"):
                out.append(f'<text x="{bx - 70}" y="{ly + 18}" font-size="11" '
                           f'fill="{p["muted"]}">{esc(b["text"][:30])}</text>')
        return out

    parts += branch(up, -1)
    parts += branch(down, +1)
    svg = (f'<svg viewBox="0 0 {W} {H}" role="img" style="max-width:{W}px;width:100%;height:auto">'
           f'{spine}{"".join(parts)}{head_box}</svg>')
    return f'<div class="ig-canvas">{svg}</div>'


# ---------------------------------------------------------------- sankey
def render_sankey(plan, p):
    blocks = {b["id"]: b for b in blocks_of(plan)}
    rels = [r for r in rel_of(plan) if r.get("weight") is not None]
    # column assignment: longest-path level
    level = {bid: 0 for bid in blocks}
    for _ in range(len(blocks)):
        for r in rels:
            level[r["to"]] = max(level[r["to"]], level[r["from"]] + 1)
    cols = {}
    for bid, lv in level.items():
        cols.setdefault(lv, []).append(bid)

    W, H = 760, 420
    pad, colw, x0 = 46, 26, 60
    total_w = x0 + len(cols) * (colw + 110)
    max_flow = max([sum(r["weight"] for r in rels if r["from"] == bid) or
                    sum(r["weight"] for r in rels if r["to"] == bid)
                    for bid in blocks] + [1])
    scale = (H - 2 * pad) / max_flow * 0.8

    def node_height(bid):
        f = max(sum(r["weight"] for r in rels if r["from"] == bid),
                sum(r["weight"] for r in rels if r["to"] == bid), 0.0001)
        return f * scale

    node_pos = {}
    for lv, ids in sorted(cols.items()):
        ids = sorted(ids, key=lambda b: -(node_height(b)))
        th = sum(node_height(b) for b in ids) + 14 * (len(ids) - 1)
        y = (H - th) / 2
        for bid in ids:
            h = node_height(bid)
            node_pos[bid] = (x0 + lv * (colw + 110), y, h)
            y += h + 14

    ribbons = []
    for r in rels:
        x0n, y0n, h0n = node_pos[r["from"]]
        x1n, y1n, h1n = node_pos[r["to"]]
        t = r["weight"] * scale
        ya = y0n + h0n / 2 - t / 2
        yb = y1n + h1n / 2 - t / 2
        xm = (x0n + colw + x1n) / 2
        ribbons.append(
            f'<path d="M{x0n + colw},{ya:.1f} C{xm},{ya:.1f} {xm},{yb:.1f} {x1n},{yb:.1f} '
            f'L{x1n},{yb + t:.1f} C{xm},{yb + t:.1f} {xm},{ya + t:.1f} {x0n + colw},{ya + t:.1f} Z" '
            f'fill="{p["accent2"]}" opacity="0.55" stroke="none"/>')

    nodes = []
    for bid, (nx, ny, nh) in node_pos.items():
        b = blocks[bid]
        nodes.append(f'<rect x="{nx}" y="{ny:.1f}" width="{colw}" height="{nh:.1f}" '
                     f'rx="3" fill="{p["accent"]}"/>')
        lbl = f'{esc(b["title"])}'
        if b.get("value"):
            lbl += f'（{esc(b["value"])}）'
        nodes.append(f'<text x="{nx + colw + 6}" y="{ny + nh / 2 + 4:.1f}" font-size="12" '
                     f'font-weight="600" fill="{p["ink"]}">{lbl}</text>')

    svg = (f'<svg viewBox="0 0 {max(total_w, W)} {H}" role="img" '
           f'style="max-width:{max(total_w, W)}px;width:100%;height:auto">'
           f'{"".join(ribbons)}{"".join(nodes)}</svg>')
    return f'<div class="ig-canvas">{svg}</div>'


# ---------------------------------------------------------------- pyramid
def render_pyramid(plan, p):
    """SVG 金字塔：blocks 顺序即层级，第一个 block 为基座（最宽、最深色）。"""
    blocks = blocks_of(plan)
    n = len(blocks)
    LH, GAP = 64, 6                     # 层高 / 层间距
    shape_w, cx = 560, 290              # 形状区最大宽 / 中轴
    side_x = cx + shape_w / 2 + 18      # 右侧文字栏起点
    W, H = 780, n * (LH + GAP) + 60
    top_y = 30

    def width_at(level_bottom_idx):
        """第 i 层（0=基座）的底边宽：线性收缩，顶层收为尖。"""
        return shape_w * (n - level_bottom_idx) / n

    parts = []
    for i, b in enumerate(blocks):          # i=0 基座
        y_top = top_y + (n - 1 - i) * (LH + GAP)   # 基座画在最下
        wb = width_at(i)
        wt = width_at(i + 1) if i + 1 < n else 0.0
        yb, yt = y_top + LH, y_top
        xlb, xrb = cx - wb / 2, cx + wb / 2
        xlt, xrt = cx - wt / 2, cx + wt / 2
        op = 1.0 - 0.55 * (i / max(n - 1, 1))      # 基座最深
        parts.append(
            f'<polygon points="{xlt:.1f},{yt} {xrt:.1f},{yt} {xrb:.1f},{yb} {xlb:.1f},{yb}" '
            f'fill="{p["accent"]}" opacity="{op:.2f}"/>')
        mid_y = yt + LH / 2 + 5
        label = f'{i + 1}. {esc(b["title"])}'
        inner_ok = wb > len(b["title"]) * 17 + 60   # 粗略判断能否放进形状内
        if inner_ok:
            parts.append(f'<text x="{cx}" y="{mid_y}" text-anchor="middle" font-size="15" '
                         f'font-weight="700" fill="#fff">{label}</text>')
            tx = xrb + 14
        else:
            tx = xrt + 14
        if b.get("text") and tx + 170 < W:
            parts.append(f'<text x="{tx}" y="{mid_y - 4}" font-size="14" font-weight="600" '
                         f'fill="{p["ink"]}">{esc(b["title"])}</text>')
            parts.append(f'<text x="{tx}" y="{mid_y + 15}" font-size="12" '
                         f'fill="{p["muted"]}">{esc(b["text"][:26])}</text>')
        elif not inner_ok:
            parts.append(f'<text x="{tx}" y="{mid_y}" font-size="14" font-weight="600" '
                         f'fill="{p["ink"]}">{label}</text>')

    svg = (f'<svg viewBox="0 0 {W} {H}" role="img" style="max-width:{W}px;width:100%;height:auto">'
           f'{"".join(parts)}</svg>')
    return f'<div class="ig-canvas">{svg}</div>'


# ---------------------------------------------------------------- timeline
def render_timeline(plan, p):
    items = []
    for b in blocks_of(plan):
        t = f'<span class="tl-time">{esc(b["time"])}</span>' if b.get("time") else ""
        txt = f'<p class="tl-text">{esc(b["text"])}</p>' if b.get("text") else ""
        items.append(f'''
  <li class="tl-item">
    <span class="tl-dot"></span>
    <div class="tl-body">{t}<b class="tl-title">{esc(b["title"])}</b>{txt}</div>
  </li>''')
    return f'<ol class="timeline">{"".join(items)}</ol>'


# ---------------------------------------------------------------- dashboard
def render_dashboard(plan, p):
    cards = []
    for b in blocks_of(plan):
        val = f'<div class="db-value">{esc(b["value"])}<small>{esc(b.get("unit", ""))}</small></div>' \
            if b.get("value") else ""
        metric = f'<div class="db-metric">{esc(b["metric"])}</div>' if b.get("metric") else ""
        time = f'<span class="db-time">{esc(b["time"])}</span>' if b.get("time") else ""
        txt = f'<p class="db-text">{esc(b["text"])}</p>' if b.get("text") else ""
        cards.append(f'''
  <div class="db-card">
    {metric}{val}
    <b class="db-title">{esc(b["title"])}</b>{txt}{time}
  </div>''')
    return f'<div class="dashboard">{"".join(cards)}</div>'


RENDERERS = {
    "flywheel": render_flywheel,
    "fishbone": render_fishbone,
    "sankey": render_sankey,
    "pyramid": render_pyramid,
    "timeline": render_timeline,
    "dashboard": render_dashboard,
}


# ---------------------------------------------------------------- shell
def render_html(plan):
    p = palette_of(plan)
    layout = plan["layout"]
    if layout not in RENDERERS:
        raise ValueError(f"unknown layout: {layout}")
    body = RENDERERS[layout](plan, p)
    meta = plan["meta"]
    footer = meta.get("footer") or meta.get("source_note") or ""
    title_line = f'<h1 class="ig-title">{esc(meta["title"])}</h1>'
    subtitle = f'<p class="ig-subtitle">{esc(meta["subtitle"])}</p>' if meta.get("subtitle") else ""
    footer_html = f'<div class="ig-footer">{esc(footer)}</div>' if footer else ""
    return f'''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; img-src data:; base-uri 'none'; form-action 'none'">
<title>{esc(meta["title"])}</title>
<style>
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{background:{p["bg"]};color:{p["ink"]};font-family:{FONT_STACK};
       display:flex;justify-content:center;padding:32px 16px}}
  .ig{{background:#fff;border:1px solid {p["line"]};border-radius:16px;
      max-width:820px;width:100%;padding:36px 32px}}
  .ig-title{{font-size:26px;font-weight:800;letter-spacing:.5px}}
  .ig-subtitle{{color:{p["muted"]};font-size:14px;margin-top:6px}}
  .ig-canvas{{margin-top:22px;text-align:center}}
  .ig-footer{{margin-top:24px;padding-top:14px;border-top:1px dashed {p["line"]};
      color:{p["muted"]};font-size:12px}}
  /* timeline */
  .timeline{{list-style:none;margin-top:22px;padding-left:6px}}
  .tl-item{{position:relative;padding:0 0 22px 26px;border-left:2px solid {p["line"]}}}
  .tl-item:last-child{{border-left-color:transparent}}
  .tl-dot{{position:absolute;left:-7px;top:2px;width:12px;height:12px;border-radius:50%;
      background:{p["accent"]};box-shadow:0 0 0 3px {p["bg"]}}}
  .tl-time{{display:inline-block;font-size:12px;font-weight:700;color:{p["accent"]};
      background:{p["bg"]};border-radius:4px;padding:2px 8px;margin-bottom:4px}}
  .tl-title{{display:block;font-size:15px;margin-top:2px}}
  .tl-text{{font-size:13px;color:{p["muted"]};margin-top:3px}}
  /* dashboard */
  .dashboard{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
      gap:14px;margin-top:22px}}
  .db-card{{border:1px solid {p["line"]};border-radius:12px;padding:16px;
      background:linear-gradient(180deg,#fff, {p["bg"]})}}
  .db-metric{{font-size:12px;color:{p["muted"]};font-weight:600}}
  .db-value{{font-size:30px;font-weight:800;color:{p["accent"]};margin:4px 0 2px}}
  .db-value small{{font-size:13px;font-weight:600;color:{p["muted"]};margin-left:3px}}
  .db-title{{display:block;font-size:14px;margin-top:6px}}
  .db-text{{font-size:12px;color:{p["muted"]};margin-top:4px}}
  .db-time{{display:inline-block;margin-top:8px;font-size:11px;color:{p["muted"]}}}
  @media print{{body{{padding:0}}.ig{{border:none}}}}
</style>
</head>
<body>
<main class="ig">
  {title_line}
  {subtitle}
  {body}
  {footer_html}
</main>
</body>
</html>
'''


def main():
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    src = sys.argv[1]
    data = sys.stdin.read() if src == "-" else open(src, encoding="utf-8").read()
    plan = json.loads(data)
    html_out = render_html(plan)
    if len(sys.argv) > 2 and sys.argv[2] != "-":
        with open(sys.argv[2], "w", encoding="utf-8") as f:
            f.write(html_out)
        print(f"OK -> {sys.argv[2]}")
    else:
        sys.stdout.write(html_out)


if __name__ == "__main__":
    main()
