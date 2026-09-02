#!/usr/bin/env python3
"""Render a validated infographic plan into a single-file, self-contained HTML visual.

The output is a standalone HTML document with inline CSS (no external assets,
no JavaScript, no CDN fonts). It is designed to be:

- opened directly in a browser (works offline)
- printed or exported to PDF cleanly
- embedded into Lark / Feishu docs or sheets as a visual block
- re-edited by downstream tools because content stays in the DOM

Differentiation: clarity and information hierarchy come before decoration.
No animations, no hero graphics, no font CDN dependencies.
"""

from __future__ import annotations

import argparse
import html
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_infographic_plan import (  # type: ignore
    DEFAULT_SCHEMA_PATH,
    _validate_schema_subset,
    apply_defaults,
    load_json,
    validate_business_rules,
)

# ---------------------------------------------------------------------------
# Visual system -> CSS variables
# ---------------------------------------------------------------------------

DEFAULT_COLORS = {
    "brand": ["#2457F5", "#13B98A", "#EF4444"],
    "mono": ["#334155", "#64748B", "#94A3B8"],
    "duo": ["#0F172A", "#38BDF8", "#F59E0B"],
    "triad": ["#2457F5", "#13B98A", "#FFB020"],
    "custom": ["#2457F5", "#13B98A", "#EF4444"],
}

EMPHASIS_STYLES = {
    "clean": {"radius": "10px", "heading_font": "inherit", "shadow": "0 1px 3px rgba(15,23,42,.08)"},
    "editorial": {"radius": "4px", "heading_font": "Georgia, \"Noto Serif SC\", \"Songti SC\", serif", "shadow": "0 1px 2px rgba(15,23,42,.06)"},
    "playful": {"radius": "18px", "heading_font": "inherit", "shadow": "0 2px 8px rgba(15,23,42,.10)"},
    "technical": {"radius": "4px", "heading_font": "\"SF Mono\", \"JetBrains Mono\", \"Courier New\", monospace", "shadow": "none"},
    "luxury": {"radius": "6px", "heading_font": "Georgia, \"Noto Serif SC\", \"Songti SC\", serif", "shadow": "0 1px 3px rgba(15,23,42,.10)"},
}


def resolve_palette(visual_system: Optional[Dict[str, Any]]) -> Dict[str, str]:
    vs = visual_system or {}
    colors = vs.get("brand_colors") or []
    mode = vs.get("palette_mode") or "brand"
    fallback = DEFAULT_COLORS.get(mode, DEFAULT_COLORS["brand"])
    return {
        "primary": colors[0] if len(colors) > 0 else fallback[0],
        "accent": colors[1] if len(colors) > 1 else fallback[1],
        "warn": colors[2] if len(colors) > 2 else fallback[2],
    }


def esc(value: Any) -> str:
    return html.escape(str(value if value is not None else ""))


def truncate(text: str, limit: int) -> str:
    text = str(text or "")
    return text if len(text) <= limit else text[: limit - 1] + "…"


# ---------------------------------------------------------------------------
# Block helpers
# ---------------------------------------------------------------------------


def layout_blocks(plan: Dict[str, Any], *block_types: str) -> List[Dict[str, Any]]:
    types = set(block_types)
    return [b for b in plan.get("blocks", []) if isinstance(b, dict) and b.get("block_type") in types]


def is_primary(block: Dict[str, Any]) -> bool:
    return block.get("visual_role") == "primary"


def build_header(plan: Dict[str, Any]) -> str:
    message = plan.get("message", {}) or {}
    title = message.get("title", "")
    subtitle = message.get("subtitle", "")
    takeaway = message.get("core_takeaway", "")

    parts = ['<header class="ig-header">']
    if title:
        parts.append(f"<h1 class=\"ig-h1\">{esc(title)}</h1>")
    if subtitle:
        parts.append(f"<p class=\"ig-sub\">{esc(subtitle)}</p>")
    if takeaway:
        parts.append(f'<div class="ig-takeaway">{esc(takeaway)}</div>')
    parts.append("</header>")
    return "\n".join(parts)


def build_footer_simple(plan: Dict[str, Any]) -> str:
    message = plan.get("message", {}) or {}
    cta = message.get("cta", "")
    notes = layout_blocks(plan, "note")
    legend = layout_blocks(plan, "legend")
    parts: List[str] = ['<footer class="ig-footer">']
    if legend:
        legend_items = "".join(
            f"<span class=\"ig-legend-item\"><b>{esc(b.get('title'))}</b> {esc(b.get('content'))}</span>"
            for b in legend
        )
        parts.append(f'<div class="ig-legend">{legend_items}</div>')
    if notes:
        note_text = notes[0].get("content") or notes[0].get("title") or ""
        parts.append(f'<div class="ig-note">📌 {esc(note_text)}</div>')
    if cta:
        parts.append(f'<div class="ig-cta">{esc(cta)}</div>')
    infographic_id = plan.get("infographic_id", "")
    parts.append(
        f'<div class="ig-meta">text-to-infographic · {esc(infographic_id)} · '
        f"overview 图，细节见 companion doc</div>"
    )
    parts.append("</footer>")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Layout builders
# ---------------------------------------------------------------------------


def _node_card(block: Dict[str, Any], css_class: str = "ig-node") -> str:
    title = block.get("title", "")
    content = block.get("content", "")
    role = block.get("visual_role", "secondary")
    return (
        f'<div class="{css_class} role-{esc(role)}">'
        f"<div class=\"ig-node-title\">{esc(title)}</div>"
        f"<div class=\"ig-node-body\">{esc(content)}</div>"
        f"</div>"
    )


def build_radial(plan: Dict[str, Any]) -> str:
    """flywheel: SVG ring with clockwise loop arrows and a center summary."""
    nodes = layout_blocks(plan, "stage", "node", "metric", "callout")
    relations = plan.get("relations", []) or []

    size = 760
    cx = cy = size / 2
    ring_r = 250
    node_w, node_h = 210, 92

    ordered = _order_nodes_by_relations(nodes, relations)
    n = len(ordered)
    angle_start = -90.0
    slots = []

    def place(i: int) -> Tuple[float, float]:
        angle = math.radians(angle_start + (360.0 / max(n, 1)) * i)
        x = cx + ring_r * math.cos(angle)
        y = cy + ring_r * math.sin(angle)
        return x, y

    node_centers: Dict[str, Tuple[float, float]] = {}
    for i, node in enumerate(ordered):
        x, y = place(i)
        node_centers[node.get("block_id", "")] = (x, y)
        slots.append((node, x, y))

    def arrow_marker() -> str:
        return (
            '<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" '
            'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            '<path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker>'
        )

    def node_svg(slot: Tuple[Dict[str, Any], float, float]) -> str:
        block, x, y = slot
        role = block.get("visual_role", "secondary")
        fill = "#FFFFFF" if role != "primary" else "var(--primary)"
        stroke = "var(--primary)" if role != "primary" else "var(--primary)"
        text_fill = "#0F172A" if role != "primary" else "#FFFFFF"
        title = truncate(block.get("title", ""), 18)
        content = truncate(block.get("content", ""), 26)
        label_y = y - 4
        body_y = y + 20
        return (
            f'<g transform="translate({x - node_w/2:.0f},{y - node_h/2:.0f})">'
            f'<rect width="{node_w}" height="{node_h}" rx="12" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{1.5 if role != "primary" else 2}"/>'
            f'<text x="{node_w/2}" y="38" text-anchor="middle" '
            f'font-size="15" font-weight="700" fill="{text_fill}">{esc(title)}</text>'
            f'<text x="{node_w/2}" y="62" text-anchor="middle" font-size="12" '
            f'fill="{text_fill}" opacity="0.85">{esc(content)}</text>'
            f"</g>"
        )

    def loop_paths() -> str:
        parts: List[str] = []
        seen: set = set()
        for rel in relations:
            frm, to = rel.get("from"), rel.get("to")
            if frm not in node_centers or to not in node_centers:
                continue
            key = (frm, to)
            if key in seen:
                continue
            seen.add(key)
            (x1, y1), (x2, y2) = node_centers[frm], node_centers[to]
            # arc along the ring between the two node centers
            mid_angle = math.atan2(y1 - cy, x1 - cx) + math.atan2(y2 - cy, x2 - cx) / 2
            mx = cx + ring_r * math.cos(mid_angle)
            my = cy + ring_r * math.sin(mid_angle)
            d = f"M {x1:.0f} {y1:.0f} Q {mx:.0f} {my:.0f} {x2:.0f} {y2:.0f}"
            label = truncate(rel.get("label", ""), 16)
            parts.append(
                f'<path d="{d}" fill="none" stroke="var(--accent)" stroke-width="2.5" '
                f'stroke-dasharray="6 4" marker-end="url(#arrow)" opacity="0.9"/>'
            )
            if label:
                lx = (x1 + 2 * mx + x2) / 4
                ly = (y1 + 2 * my + y2) / 4
                parts.append(
                    f'<text x="{lx:.0f}" y="{ly:.0f}" text-anchor="middle" font-size="11" '
                    f'fill="var(--muted-text)">{esc(label)}</text>'
                )
        return "\n".join(parts)

    def center_svg() -> str:
        summary_blocks = layout_blocks(plan, "summary", "title")
        center_lines: List[str] = []
        if summary_blocks:
            for sb in summary_blocks[:2]:
                t = sb.get("title", "")
                c = sb.get("content", "")
                if c:
                    center_lines.extend([t, c] if t and t != c else [c])
        if not center_lines:
            message = plan.get("message", {}) or {}
            center_lines.append(message.get("title", "Overview"))
            if message.get("core_takeaway"):
                center_lines.append(message["core_takeaway"])
        lines = [truncate(line, 20) for line in center_lines][:4]
        out = [
            f'<circle cx="{cx}" cy="{cy}" r="128" fill="var(--primary)" opacity="0.06" '
            f'stroke="var(--primary)" stroke-width="1.5"/>'
        ]
        y = cy - (len(lines) - 1) * 16 / 2 + 16
        for line in lines:
            weight = 800 if line == lines[0] else 500
            out.append(
                f'<text x="{cx}" y="{y:.0f}" text-anchor="middle" font-size="{16 if weight==800 else 13}" '
                f'font-weight="{weight}" fill="var(--text)">{esc(line)}</text>'
            )
            y += 24
        return "\n".join(out)

    svg = (
        f'<svg class="ig-svg" viewBox="0 0 {size} {size}" role="img" '
        f'aria-label="{esc(plan.get("message", {}).get("title", "Infographic"))}">'
        f"{arrow_marker()}{center_svg()}{loop_paths()}"
        + "".join(node_svg(s) for s in slots)
        + "</svg>"
    )
    return f'<div class="ig-layout layout-radial">{svg}</div>'


def _order_nodes_by_relations(
    nodes: List[Dict[str, Any]], relations: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """Prefer the chain order implied by relations, falling back to plan order."""
    by_id = {n.get("block_id"): n for n in nodes if n.get("block_id")}
    chain: List[str] = []
    used: set = set()
    for rel in relations:
        frm, to = rel.get("from"), rel.get("to")
        if frm in by_id and frm not in used:
            used.add(frm)
            chain.append(frm)
        if to in by_id and to not in used:
            used.add(to)
            chain.append(to)
    ordered = [by_id[c] for c in chain if c in by_id]
    for n in nodes:
        if n.get("block_id") not in used:
            ordered.append(n)
    return ordered or nodes


def build_spine_branch(plan: Dict[str, Any]) -> str:
    """fishbone: SVG spine with alternating cause branches feeding an effect head."""
    effects = layout_blocks(plan, "effect")
    causes = layout_blocks(plan, "cause")
    relations = plan.get("relations", []) or []

    width, height = 1480, 620
    spine_y = 330
    head_x, head_w, head_h = 1240, 200, 150
    cause_w, cause_h = 260, 86

    effect = effects[0] if effects else None
    effect_label = effect.get("title", "问题") if effect else plan.get("message", {}).get("title", "")
    effect_content = effect.get("content", "") if effect else ""

    def head_svg() -> str:
        out = [
            f'<rect x="{head_x}" y="{spine_y - head_h/2}" width="{head_w}" height="{head_h}" rx="12" '
            f'fill="var(--primary)" stroke="var(--primary)" stroke-width="2"/>',
            f'<text x="{head_x + head_w/2}" y="{spine_y - 8}" text-anchor="middle" font-size="19" '
            f'font-weight="800" fill="#FFFFFF">{esc(truncate(effect_label, 14))}</text>',
            f'<text x="{head_x + head_w/2}" y="{spine_y + 22}" text-anchor="middle" font-size="12.5" '
            f'fill="#FFFFFF" opacity="0.9">{esc(truncate(effect_content, 26))}</text>',
        ]
        return "\n".join(out)

    def cause_svg(cause: Dict[str, Any], index: int, total: int) -> str:
        up = index % 2 == 0
        x_start = 140
        x_end = head_x - 80
        span = x_end - x_start
        x = x_start + (span * (index + 1) / (total + 1)) - cause_w / 2
        cy = spine_y - (index // 2 + 1) * 108 if up else spine_y + (index // 2 + 1) * 108
        cx = x + cause_w / 2
        line_y = spine_y if up else spine_y
        out = [
            f'<line x1="{cx}" y1="{cy + (cause_h/2 if up else -cause_h/2)}" x2="{cx}" y2="{line_y}" '
            f'stroke="var(--muted-text)" stroke-width="1.5" stroke-dasharray="4 3"/>',
            f'<rect x="{x:.0f}" y="{cy - cause_h/2}" width="{cause_w}" height="{cause_h}" rx="10" '
            f'fill="#FFFFFF" stroke="var(--accent)" stroke-width="1.5"/>',
            f'<text x="{cx:.0f}" y="{cy - 6}" text-anchor="middle" font-size="14.5" font-weight="700" '
            f'fill="var(--text)">{esc(truncate(cause.get("title", ""), 16))}</text>',
            f'<text x="{cx:.0f}" y="{cy + 18}" text-anchor="middle" font-size="11.5" '
            f'fill="var(--muted-text)">{esc(truncate(cause.get("content", ""), 24))}</text>',
        ]
        return "\n".join(out)

    spine = (
        f'<line x1="80" y1="{spine_y}" x2="{head_x + head_w}" y2="{spine_y}" '
        f'stroke="var(--primary)" stroke-width="3"/>'
    )
    labels = "".join(
        f'<text x="{(140 + (head_x - 80) * (i + 1) / (len(causes) + 1)):.0f}" y="{spine_y - 14}" '
        f'text-anchor="middle" font-size="11" fill="var(--muted-text)">{esc(truncate(r.get("label",""), 18))}</text>'
        for i, r in enumerate(relations[: len(causes)])
    )
    svg = (
        f'<svg class="ig-svg" viewBox="0 0 {width} {height}" role="img">'
        f"{spine}{labels}{head_svg()}"
        + "".join(cause_svg(c, i, len(causes)) for i, c in enumerate(causes))
        + "</svg>"
    )
    return f'<div class="ig-layout layout-spine">{svg}</div>'


def build_pyramid(plan: Dict[str, Any]) -> str:
    layers = sorted(
        layout_blocks(plan, "node", "stage"),
        key=lambda b: (b.get("payload", {}) or {}).get("layer", 999),
    )
    max_layer = max([(b.get("payload", {}) or {}).get("layer", 1) for b in layers] or [1])
    parts: List[str] = []
    for idx, layer in enumerate(layers):
        payload = layer.get("payload", {}) or {}
        width_pct = max(30, 100 - (max_layer - idx) * 16) if max_layer > 1 else 100
        label = payload.get("customer_value") or layer.get("content") or ""
        role = layer.get("visual_role", "secondary")
        parts.append(
            f'<div class="ig-pyramid-layer" style="width:{width_pct}%">'
            f'<div class="ig-pyramid-inner role-{esc(role)}">'
            f'<div class="ig-node-title">{esc(layer.get("title",""))}</div>'
            f'<div class="ig-node-body">{esc(label)}</div>'
            f"</div></div>"
        )
    if len(parts) > 1:
        join = '<div class="ig-pyramid-up" aria-hidden="true">▲</div>'
        parts = [p for pair in zip(parts, [join] * len(parts)) for p in pair][:-1]
    return f'<div class="ig-layout layout-pyramid">{"".join(parts)}</div>'


def build_timeline(plan: Dict[str, Any]) -> str:
    stages = layout_blocks(plan, "stage", "node", "milestone")
    relations = plan.get("relations", []) or []
    ordered = _order_nodes_by_relations(stages, relations)
    parts: List[str] = []
    for i, stage in enumerate(ordered):
        payload = stage.get("payload", {}) or {}
        badge = payload.get("quarter") or payload.get("phase") or f"{i + 1}"
        parts.append(
            f'<div class="ig-tl-item">'
            f'<div class="ig-tl-badge">{esc(badge)}</div>'
            f"<div class=\"ig-tl-card role-{esc(stage.get('visual_role','secondary'))}\">"
            f"<div class=\"ig-node-title\">{esc(stage.get('title',''))}</div>"
            f"<div class=\"ig-node-body\">{esc(stage.get('content',''))}</div>"
            f"</div></div>"
        )
    body = "".join(
        f'<div class="ig-tl-step">{card}<div class="ig-tl-arrow">→</div></div>'
        if i < len(parts) - 1
        else f'<div class="ig-tl-step">{card}</div>'
        for i, card in enumerate(parts)
    )
    return f'<div class="ig-layout layout-timeline">{body}</div>'


def build_dashboard(plan: Dict[str, Any]) -> str:
    metrics = layout_blocks(plan, "metric")
    note_blocks = layout_blocks(plan, "note")
    relations = plan.get("relations", []) or []

    groups: List[Tuple[str, List[Dict[str, Any]]]] = []
    seen: set = set()
    for m in metrics:
        g = m.get("group_id") or "其他"
        if g not in seen:
            seen.add(g)
            groups.append((g, []))
        groups[-1][1].append(m)

    def trend_html(block: Dict[str, Any]) -> str:
        payload = block.get("payload", {}) or {}
        trend = payload.get("trend")
        if trend == "up":
            return '<span class="ig-trend up">▲</span>'
        if trend == "down":
            return '<span class="ig-trend down">▼</span>'
        return '<span class="ig-trend flat">→</span>'

    metric_html = "".join(
        f'<div class="ig-metric-card role-{esc(m.get("visual_role","secondary"))}">'
        f'<div class="ig-metric-label">{esc(m.get("title",""))}{trend_html(m)}</div>'
        f'<div class="ig-metric-value">{esc(m.get("content",""))}</div>'
        f'<div class="ig-metric-target">{esc((m.get("payload",{}) or {}).get("target",""))}</div>'
        f"</div>"
        for m in metrics
    )

    group_html = ""
    for gname, members in groups:
        group_html += (
            f'<div class="ig-dash-group"><div class="ig-dash-group-title">{esc(gname)}</div>'
            f'<div class="ig-dash-grid">'
            + "".join(
                f'<div class="ig-metric-card role-{esc(m.get("visual_role","secondary"))}">'
                f'<div class="ig-metric-label">{esc(m.get("title",""))}{trend_html(m)}</div>'
                f'<div class="ig-metric-value">{esc(m.get("content",""))}</div>'
                f'<div class="ig-metric-target">{esc((m.get("payload",{}) or {}).get("target",""))}</div>'
                f"</div>"
                for m in members
            )
            + "</div></div>"
        )

    highlight_html = ""
    if relations:
        by_id = {b.get("block_id"): b for b in plan.get("blocks", [])}
        items = []
        for r in relations:
            frm, to = r.get("from"), r.get("to")
            target = by_id.get(to, {}).get("title", to)
            label = r.get("label") or frm
            items.append(f"<li><b>{esc(label)}</b> → {esc(target)}</li>")
        if items:
            highlight_html = f'<div class="ig-dash-highlights"><h3>重点关联</h3><ul>{"".join(items)}</ul></div>'

    note_html = ""
    if note_blocks:
        n = note_blocks[0]
        note_html = (
            f'<div class="ig-note ig-note-card">📌 {esc(n.get("content") or n.get("title") or "")}</div>'
        )
    return (
        f'<div class="ig-layout layout-dashboard">'
        f"{highlight_html}{group_html}{note_html}</div>"
    )


def build_flow(plan: Dict[str, Any]) -> str:
    chart_family = plan.get("chart_family")
    if chart_family == "sankey":
        return _build_sankey(plan)
    return _build_process_flow(plan)


def _build_process_flow(plan: Dict[str, Any]) -> str:
    stages = layout_blocks(plan, "stage", "node")
    relations = plan.get("relations", []) or []
    ordered = _order_nodes_by_relations(stages, relations)
    parts: List[str] = []
    for i, stage in enumerate(ordered):
        payload = stage.get("payload", {}) or {}
        badge = payload.get("phase") or payload.get("quarter") or f"{i + 1}"
        parts.append(
            f'<div class="ig-pf-card role-{esc(stage.get("visual_role","secondary"))}">'
            f'<div class="ig-pf-badge">{esc(badge)}</div>'
            f"<div class=\"ig-node-title\">{esc(stage.get('title',''))}</div>"
            f"<div class=\"ig-node-body\">{esc(stage.get('content',''))}</div>"
            f"</div>"
        )
    body = "".join(
        f'<div class="ig-pf-step">{card}<div class="ig-tl-arrow">→</div></div>'
        if i < len(parts) - 1
        else f'<div class="ig-pf-step">{card}</div>'
        for i, card in enumerate(parts)
    )
    return f'<div class="ig-layout layout-flow">{body}</div>'


def _build_sankey(plan: Dict[str, Any]) -> str:
    nodes = layout_blocks(plan, "node", "stage")
    relations = plan.get("relations", []) or []
    by_id = {n.get("block_id"): n for n in nodes}

    stage_order = ["source", "signup", "activation", "paid", "churn", "outcomes"]
    columns: Dict[str, List[Dict[str, Any]]] = {}
    for n in nodes:
        stage = (n.get("payload", {}) or {}).get("stage", "other")
        key = stage if stage in stage_order else "other"
        columns.setdefault(key, []).append(n)
    col_keys = [k for k in stage_order if k in columns] + [k for k in columns if k not in stage_order]

    width, height = 1320, 640
    col_x = 120
    gap = (width - 2 * col_x - 260) / max(len(col_keys) - 1, 1)
    node_w = 240
    top_pad = 70
    node_gap = 34

    weights = [r.get("weight") or 0 for r in relations]
    max_w = max(weights) if weights else 1

    # compute column geometry (x, y positions)
    col_geo: Dict[str, Tuple[float, List[Tuple[float, float]]]] = {}
    for i, key in enumerate(col_keys):
        members = columns[key]
        total_h = sum(max(46, (sum(r.get("weight", 0) for r in relations if r.get("to") == m.get("block_id") or r.get("from") == m.get("block_id"))) / max_w * 64) for m in members)
        y = top_pad
        positions: List[Tuple[float, float]] = []
        for m in members:
            mh = max(46, (sum(r.get("weight", 0) for r in relations if (r.get("from") == m.get("block_id")) or (r.get("to") == m.get("block_id"))) / max_w * 64))
            positions.append((y, mh))
            y += mh + node_gap
        col_geo[key] = (col_x + i * gap, positions)

    def node_svg(block: Dict[str, Any], x: float, y: float, h: float) -> str:
        fill = "#FFFFFF"
        stroke = "var(--accent)"
        if block.get("visual_role") == "primary":
            fill = "var(--primary)"
            stroke = "var(--primary)"
        text_fill = "#FFFFFF" if fill == "var(--primary)" else "var(--text)"
        title = truncate(block.get("title", ""), 12)
        content = truncate(block.get("content", ""), 20)
        return (
            f'<g transform="translate({x:.0f},{y:.0f})">'
            f'<rect width="{node_w}" height="{h:.0f}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
            f'<text x="12" y="22" font-size="14.5" font-weight="700" fill="{text_fill}">{esc(title)}</text>'
            f'<text x="12" y="42" font-size="11.5" fill="{text_fill}" opacity="0.85">{esc(content)}</text>'
            f"</g>"
        )

    def flow_svg() -> str:
        parts: List[str] = []
        for r in relations:
            frm, to = r.get("from"), r.get("to")
            if frm not in by_id or to not in by_id:
                continue
            f_col = (by_id[frm].get("payload", {}) or {}).get("stage")
            t_col = (by_id[to].get("payload", {}) or {}).get("stage")
            if f_col not in col_geo or t_col not in col_geo:
                continue
            fx, fpos = col_geo[f_col]
            tx, tpos = col_geo[t_col]
            idx_f = columns[f_col].index(by_id[frm])
            idx_t = columns[t_col].index(by_id[to])
            fy, fh = fpos[idx_f]
            ty, th = tpos[idx_t]
            y1 = fy + fh / 2
            y2 = ty + th / 2
            w = 2 + (r.get("weight", 0) / max_w) * 30
            label = f"{truncate(r.get('label',''), 12)} {r.get('weight','')}"
            parts.append(
                f'<path d="M {fx + node_w} {y1:.0f} C {fx + node_w + 60} {y1:.0f}, {tx - 60} {y2:.0f}, '
                f'{tx} {y2:.0f}" fill="none" stroke="var(--accent)" stroke-opacity="0.55" '
                f'stroke-width="{w:.1f}"/>'
            )
            mx = (fx + node_w + tx) / 2
            my = (y1 + y2) / 2
            parts.append(
                f'<text x="{mx:.0f}" y="{my:.0f}" text-anchor="middle" font-size="11" '
                f'fill="var(--muted-text)">{esc(label)}</text>'
            )
        return "\n".join(parts)

    svg = (
        f'<svg class="ig-svg" viewBox="0 0 {width} {height}" role="img">'
        f"{flow_svg()}"
        + "".join(
            node_svg(m, col_geo[key][0], pos[0], pos[1])
            for key in col_keys
            for m, pos in zip(columns[key], col_geo[key][1])
        )
        + "</svg>"
    )
    return f'<div class="ig-layout layout-sankey">{svg}</div>'


def build_grid(plan: Dict[str, Any]) -> str:
    blocks = [
        b
        for b in plan.get("blocks", [])
        if isinstance(b, dict) and b.get("block_type") not in ("title", "summary", "cta", "legend", "note")
    ]
    cards = "".join(_node_card(b) for b in blocks)
    return f'<div class="ig-layout layout-grid">{cards}</div>'


# ---------------------------------------------------------------------------
# HTML assembly
# ---------------------------------------------------------------------------

BASE_CSS = """
:root {{
  --primary: {primary};
  --accent: {accent};
  --warn: {warn};
  --bg: #F8FAFC;
  --panel: #FFFFFF;
  --text: #0F172A;
  --muted-text: #64748B;
  --border: #E2E8F0;
  --radius: {radius};
  --shadow: {shadow};
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ -webkit-text-size-adjust: 100%; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei",
    "Noto Sans SC", "Helvetica Neue", Arial, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.5;
  padding: 28px;
  max-width: 1180px;
  margin: 0 auto;
}}
h1, h2, h3 {{
  font-family: {heading_font};
}}
.ig-header {{ margin-bottom: 20px; }}
.ig-h1 {{ font-size: 30px; font-weight: 800; letter-spacing: -0.01em; }}
.ig-sub {{ color: var(--muted-text); font-size: 15px; margin-top: 4px; }}
.ig-takeaway {{
  margin-top: 14px; padding: 12px 16px; background: color-mix(in srgb, var(--primary) 8%, white);
  border-left: 4px solid var(--primary); border-radius: var(--radius);
  font-size: 15px; font-weight: 600; color: var(--text);
}}
.ig-layout {{ margin: 8px 0 20px; }}
.ig-svg {{ width: 100%; height: auto; background: var(--panel); border: 1px solid var(--border); border-radius: var(--radius); }}
/* generic node cards */
.ig-node, .ig-metric-card, .ig-tl-card, .ig-pf-card, .ig-pyramid-inner {{
  background: var(--panel); border: 1px solid var(--border); border-radius: var(--radius);
  padding: 12px 14px; box-shadow: var(--shadow);
}}
.role-primary {{ border-width: 2px; border-color: var(--primary); }}
.role-supporting {{ opacity: 0.72; }}
.ig-node-title {{ font-size: 14.5px; font-weight: 700; }}
.ig-node-body {{ font-size: 12.5px; color: var(--muted-text); margin-top: 2px; }}
/* pyramid */
.layout-pyramid {{ display: flex; flex-direction: column; align-items: center; gap: 2px; }}
.ig-pyramid-layer {{ }}
.ig-pyramid-inner {{ text-align: center; padding: 14px 10px; border: 1.5px solid var(--accent); clip-path: polygon(4% 0, 96% 0, 100% 100%, 0 100%); }}
.ig-pyramid-inner.role-primary {{ border-color: var(--primary); background: color-mix(in srgb, var(--primary) 6%, white); }}
.ig-pyramid-up {{ color: var(--accent); text-align: center; font-size: 13px; line-height: 1.6; }}
/* timeline / process flow */
.layout-timeline, .layout-flow {{ display: flex; align-items: stretch; justify-content: center; gap: 0; flex-wrap: wrap; }}
.ig-tl-step, .ig-pf-step {{ display: flex; align-items: center; gap: 0; }}
.ig-tl-card, .ig-pf-card {{ width: 210px; position: relative; }}
.ig-tl-badge, .ig-pf-badge {{
  display: inline-block; background: var(--primary); color: #fff; font-size: 11.5px; font-weight: 700;
  border-radius: 999px; padding: 2px 10px; margin-bottom: 8px;
}}
.ig-tl-arrow {{ padding: 0 10px; color: var(--accent); font-weight: 700; font-size: 18px; }}
/* dashboard */
.layout-dashboard {{ display: flex; flex-direction: column; gap: 16px; }}
.ig-dash-group-title {{ font-size: 13px; font-weight: 800; color: var(--muted-text); text-transform: uppercase; letter-spacing: .04em; margin-bottom: 8px; }}
.ig-dash-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; }}
.ig-metric-card {{ }}
.ig-metric-label {{ font-size: 12.5px; color: var(--muted-text); font-weight: 600; }}
.ig-metric-value {{ font-size: 24px; font-weight: 800; margin-top: 4px; }}
.ig-metric-target {{ font-size: 12px; color: var(--muted-text); margin-top: 4px; }}
.ig-trend {{ font-size: 12px; margin-left: 6px; }}
.ig-trend.up {{ color: #16A34A; }}
.ig-trend.down {{ color: var(--warn); }}
.ig-trend.flat {{ color: var(--muted-text); }}
.ig-dash-highlights {{ background: color-mix(in srgb, var(--warn) 7%, white); border: 1px solid color-mix(in srgb, var(--warn) 30%, white); border-radius: var(--radius); padding: 12px 16px; }}
.ig-dash-highlights h3 {{ font-size: 13px; margin-bottom: 6px; }}
.ig-dash-highlights ul {{ padding-left: 18px; font-size: 13px; }}
/* generic grid fallback */
.layout-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; }}
/* footer */
.ig-footer {{ margin-top: 22px; border-top: 1px solid var(--border); padding-top: 14px; }}
.ig-note, .ig-cta, .ig-legend, .ig-meta {{ font-size: 12.5px; margin-top: 8px; }}
.ig-cta {{ font-weight: 700; color: var(--primary); }}
.ig-legend {{ color: var(--muted-text); }}
.ig-meta {{ color: var(--muted-text); opacity: .8; font-size: 11.5px; }}
.ig-note-card {{ background: #FEF9C3; border: 1px solid #EAB308; border-radius: var(--radius); padding: 10px 14px; }}
@media print {{
  body {{ background: #fff; padding: 12px; max-width: none; }}
  .ig-takeaway, .ig-node, .ig-metric-card, .ig-tl-card, .ig-pf-card, .ig-pyramid-inner {{
    box-shadow: none !important; break-inside: avoid;
  }}
  .ig-svg {{ break-inside: avoid; }}
}}
"""


def build_html(plan: Dict[str, Any]) -> str:
    palette = resolve_palette(plan.get("visual_system"))
    emphasis = (plan.get("visual_system", {}) or {}).get("emphasis_style") or "clean"
    style_attrs = EMPHASIS_STYLES.get(emphasis, EMPHASIS_STYLES["clean"])
    css = BASE_CSS.format(
        primary=palette["primary"],
        accent=palette["accent"],
        warn=palette["warn"],
        radius=style_attrs["radius"],
        shadow=style_attrs["shadow"],
        heading_font=style_attrs["heading_font"],
    )

    layout_mode = (plan.get("layout", {}) or {}).get("layout_mode", "grid")
    if layout_mode == "radial":
        body_layout = build_radial(plan)
    elif layout_mode == "spine-branch":
        body_layout = build_spine_branch(plan)
    elif layout_mode == "pyramid":
        body_layout = build_pyramid(plan)
    elif layout_mode == "timeline":
        body_layout = build_timeline(plan)
    elif layout_mode == "dashboard":
        body_layout = build_dashboard(plan)
    elif layout_mode == "flow":
        body_layout = build_flow(plan)
    else:
        body_layout = build_grid(plan)

    lang = plan.get("language") or "zh-CN"
    title = (plan.get("message", {}) or {}).get("title", "Infographic")
    html_doc = f"""<!DOCTYPE html>
<html lang="{esc(lang)}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<style>
{css}
</style>
</head>
<body>
{build_header(plan)}
{body_layout}
{build_footer_simple(plan)}
</body>
</html>
"""
    return html_doc


def render_plan(plan_path: Path, schema_path: Path) -> Dict[str, Any]:
    raw = load_json(plan_path)
    schema = load_json(schema_path)
    normalized = apply_defaults(raw)
    errors: List[str] = []
    _validate_schema_subset(normalized, schema, "$", errors)
    business_errors, warnings = validate_business_rules(raw, normalized)
    errors.extend(business_errors)
    if errors:
        raise SystemExit(
            json.dumps(
                {
                    "ok": False,
                    "file": str(plan_path),
                    "errors": errors,
                    "warnings": warnings,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    return normalized


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render a validated infographic plan into a self-contained HTML visual."
    )
    parser.add_argument("infographic_plans", nargs="+", help="Path(s) to infographic plan JSON")
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA_PATH), help="Path to infographic-plan schema")
    parser.add_argument("--out", default="/tmp/text-to-infographic-render", help="Output directory for HTML files")
    parser.add_argument("--stdout", action="store_true", help="Print the first rendered HTML to stdout instead of writing files")
    args = parser.parse_args()

    schema_path = Path(args.schema)
    out_dir = Path(args.out)

    if not args.stdout:
        out_dir.mkdir(parents=True, exist_ok=True)

    rendered: List[Path] = []
    for plan_path in args.infographic_plans:
        plan = render_plan(Path(plan_path), schema_path)
        html_doc = build_html(plan)
        if args.stdout:
            print(html_doc)
            return 0
        out_file = out_dir / f"{plan.get('infographic_id', Path(plan_path).stem)}.html"
        out_file.write_text(html_doc, encoding="utf-8")
        rendered.append(out_file)

    summary = {
        "ok": True,
        "out_dir": str(out_dir),
        "files": [str(p) for p in rendered],
        "count": len(rendered),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
