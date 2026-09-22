"""
visual_session.py — 合成大图生成器（蓝图 + 结构 + 评分同屏 HTML）

调用三件套的数据收集函数，合成一张「施工蓝图」HTML 报告：
  - 综合评分（64px 大字，三秒法则）
  - BR-5 五维就绪度
  - 10 格完成度
  - 文件结构图（按 archetype 重点段高亮）
  - 改进项（P0/P1/P2 分级）
  - 行动按钮（通过 / 回退 / 导出 brief）

数据源单一（visualize_blueprint / render_structure / b09_summary 三件套共用），
HTML 模板仅做"视觉合成"，不引入新的数据源——保证三件套升级时此处自动跟随。

用法：
    python scripts/visual_session.py <蓝图目录> --output <session.html>
    python scripts/visual_session.py <蓝图目录> --output <session.html> --focus 6   # 高亮 B07
    python scripts/visual_session.py <蓝图目录> --json                                 # 结构化摘要
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Optional

from retry import read_text_robust

# 三件套数据收集（复用，不重复解析）
from visualize_blueprint import collect_blueprint, BLOCK_SHORT
from b09_summary import parse_b09
from render_structure import (
    load_archetypes, get_archetype, parse_b07, parse_index_meta,
    merge_tree, build_rows, SKELETON_SEGMENTS,
)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from errors import enable_utf8  # noqa: E402

enable_utf8()  # Windows GBK 控制台下保证中文（含 stderr 报错）不乱码

# ───────────────────────── 设计语言（与方案 HTML 一致） ─────────────────────────

COLORS = {
    "light": {
        "bg": "#faf6f0",
        "panel": "#ffffff",
        "border": "#e3d8c2",
        "text": "#2b2418",
        "sub": "#6b5e48",
        "faint": "#a39476",
        "wood": "#d4a574",
        "wood_deep": "#b8854f",
        "wood_bg": "#fbeed4",
        "blue": "#5b7bf0",
        "blue_deep": "#3d5ac9",
        "blue_bg": "#eef2fe",
        "coral": "#e07b5c",
        "coral_deep": "#c75a3c",
        "coral_bg": "#fce8de",
        "green": "#6fa86f",
        "green_bg": "#e8f2e8",
        "red": "#d94c4c",
        "red_bg": "#fbe3e3",
        "panel_alt": "#fffaf2",
    },
    "dark": {
        "bg": "#1f1a14",
        "panel": "#2a2418",
        "border": "#4a3f2e",
        "text": "#f5ecdb",
        "sub": "#a39476",
        "faint": "#6b5e48",
        "wood": "#e0b884",
        "wood_deep": "#e0b884",
        "wood_bg": "#3a3220",
        "blue": "#7b93f7",
        "blue_deep": "#7b93f7",
        "blue_bg": "#2a3252",
        "coral": "#e07b5c",
        "coral_deep": "#e07b5c",
        "coral_bg": "#3a2820",
        "green": "#8fc88f",
        "green_bg": "#243a31",
        "red": "#f87171",
        "red_bg": "#3a2820",
        "panel_alt": "#2a2418",
    },
}


# ───────────────────────── 工具函数 ─────────────────────────

def escape_html(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;").replace("'", "&#39;"))


def escape_xml(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ───────────────────────── 数据收集 ─────────────────────────

def collect_session(bp_dir: Path) -> dict:
    """一次收集所有需要的数据——三件套数据源不重复解析。"""
    bp_data = collect_blueprint(bp_dir)
    b09_data = parse_b09(bp_dir)
    arch_data = load_archetypes()

    # 07-计划.md 解析
    b07_text = read_text_robust(bp_dir / "07-计划.md") or ""
    parsed = parse_b07(b07_text)
    meta = parse_index_meta(bp_dir)

    # archetype 选型
    arch_id = parsed.get("archetype") or "minimal"
    arch = get_archetype(arch_data, arch_id)
    rows = build_rows(merge_tree(arch.get("tree", []), parsed), parsed)

    # visual_skin 字段（若存在）
    visual_skin = arch.get("visual_skin", {})

    return {
        "bp": bp_data,
        "b09": b09_data,
        "arch": arch,
        "arch_data": arch_data,
        "rows": rows,
        "parsed": parsed,
        "meta": meta,
        "visual_skin": visual_skin,
    }


# ───────────────────────── 合成 HTML 渲染 ─────────────────────────

def render_combined_svg(data: dict, theme: str = "light", focus_idx: int = 2) -> str:
    """合成大图 SVG：综合分 + BR-5 + 进度 + 改进项 + 行动按钮（不含文件结构——文件结构单独走 render_structure，组合起来 SVG 太大）。

    双 SVG 组合策略：本函数输出主面板 SVG；文件结构由调用方追加 render_structure 的 SVG，
    HTML 容器里两者并排显示。
    """
    c = COLORS[theme]
    bp = data["bp"]
    b09 = data["b09"]
    visual_skin = data.get("visual_skin") or {}
    arch = data["arch"]

    width, height = 1080, 540
    iqs = b09.get("iqs") or 0
    evs = b09.get("evs") or 0
    overall = b09.get("overall") or 0
    br5 = b09.get("br5") or {}
    lowest = b09.get("lowest")
    improvements = b09.get("improvements") or []
    archetype_id = arch.get("id", "minimal")
    archetype_name = arch.get("name", "—")

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" font-family="-apple-system, \'Segoe UI\', \'Microsoft YaHei\', sans-serif">',
        f'  <rect width="{width}" height="{height}" fill="{c["bg"]}" rx="14"/>',
        f'  <rect x="12" y="12" width="{width - 24}" height="{height - 24}" fill="{c["panel"]}" stroke="{c["border"]}" stroke-width="1.5" rx="12"/>',
        # 顶部标题 + 综合分
        f'  <text x="40" y="48" font-size="22" font-weight="800" fill="{c["text"]}" font-family="\'Source Han Serif SC\', \'Songti SC\', serif">{escape_xml(bp["title"])} — 施工蓝图</text>',
        f'  <text x="40" y="70" font-size="12" fill="{c["sub"]}">archetype: {escape_xml(archetype_id)} ({escape_xml(archetype_name)}) · 通道 {escape_xml(bp["channel"])} · 状态 {escape_xml(bp["status"])} · 综合 </text>',
        f'  <text x="280" y="70" font-size="14" font-weight="700" fill="{c["wood"]}">{overall:.0f}</text>',
        f'  <text x="306" y="70" font-size="12" fill="{c["sub"]}"> / 100</text>',
    ]

    # 左上：综合评分大数字 + 状态
    lines.append(f'  <rect x="40" y="92" width="320" height="170" fill="{c["panel_alt"]}" stroke="{c["wood"]}" rx="10"/>')
    lines.append(f'  <text x="60" y="124" font-size="13" font-weight="700" fill="{c["wood_deep"]}">综合评分</text>')
    lines.append(f'  <text x="60" y="206" font-size="64" font-weight="800" fill="{c["wood"]}" font-family="\'Source Han Serif SC\', serif">{overall:.0f}</text>')
    lines.append(f'  <text x="200" y="180" font-size="11" fill="{c["sub"]}">↑ 机器算：IQS={iqs:.0f} × EVS={evs:.0f}</text>')
    lines.append(f'  <line x1="60" y1="222" x2="340" y2="222" stroke="{c["border"]}"/>')
    if b09.get("lowest_br5"):
        lowest_dim, lowest_score = b09["lowest_br5"]
        lines.append(f'  <text x="60" y="244" font-size="11" fill="{c["red"]}">⚠ 最低 {lowest_dim} = {lowest_score:.1f}（优先补强）</text>')
    else:
        lines.append(f'  <text x="60" y="244" font-size="11" fill="{c["green"]}">✓ BR-5 五维均 ≥ 4</text>')

    # 中上：BR-5 五维
    lines.append(f'  <rect x="380" y="92" width="340" height="170" fill="{c["panel_alt"]}" stroke="{c["blue"]}" rx="10"/>')
    lines.append(f'  <text x="400" y="124" font-size="13" font-weight="700" fill="{c["blue_deep"]}">BR-5 五维就绪度</text>')
    if br5:
        names = {"T": "边界可信", "R": "失败可控", "A": "触发可辨", "C": "结构可解", "E": "验证可证"}
        low = lowest[0] if lowest else None
        for i, dim in enumerate(("T", "R", "A", "C", "E")):
            score = br5.get(dim, 0)
            y = 144 + i * 22
            color = c["red"] if low and dim == low else c["wood"]
            lines.append(f'  <text x="400" y="{y}" font-size="11" fill="{c["sub"]}">{dim} {names[dim]}</text>')
            lines.append(f'  <rect x="488" y="{y - 8}" width="180" height="10" fill="{c["border"]}" rx="5"/>')
            lines.append(f'  <rect x="488" y="{y - 8}" width="{int(180 * score / 5)}" height="10" fill="{color}" rx="5"/>')
            lines.append(f'  <text x="678" y="{y}" font-size="11" fill="{c["text"]}" font-weight="{700 if dim == low else 400}">{score:.1f}{" ⚠" if dim == low else ""}</text>')
    else:
        lines.append(f'  <text x="400" y="160" font-size="11" fill="{c["sub"]}">BR-5 未填，需在 B09 评分。</text>')

    # 右上：10 格进度
    lines.append(f'  <rect x="740" y="92" width="300" height="170" fill="{c["panel_alt"]}" stroke="{c["wood"]}" rx="10"/>')
    lines.append(f'  <text x="760" y="124" font-size="13" font-weight="700" fill="{c["wood_deep"]}">10 格完成度</text>')
    grid_w = (300 - 40) / 5  # 5 列
    for i, b in enumerate(bp["blocks"]):
        col = i % 5
        row = i // 5
        x = 760 + col * grid_w + 4
        y = 136 + row * 50
        comp = b["completion"]
        is_focus = (i == focus_idx)
        if comp >= 0.95:
            fill = c["green"]
        elif comp >= 0.35:
            fill = c["wood"]
        else:
            fill = c["border"]
        lines.append(f'  <rect x="{x}" y="{y}" width="{grid_w - 8}" height="32" fill="{fill}" rx="4"/>')
        if is_focus:
            lines.append(f'  <rect x="{x - 2}" y="{y - 2}" width="{grid_w - 4}" height="36" fill="none" stroke="{c["accent"] if "accent" in c else c["wood_deep"]}" stroke-width="2" rx="6"/>')
        short = b["short"].split("\n")[0]  # B01
        lines.append(f'  <text x="{x + (grid_w - 8) / 2}" y="{y + 14}" font-size="10" font-weight="700" fill="#ffffff" text-anchor="middle">{escape_xml(short)}</text>')
        lines.append(f'  <text x="{x + (grid_w - 8) / 2}" y="{y + 26}" font-size="9" fill="#ffffff" text-anchor="middle">{int(comp * 100)}%</text>')
    lines.append(f'  <text x="760" y="248" font-size="10" fill="{c["sub"]}">100% ✓ · 35%+ ▲ · &lt;35% ▢ · 高亮 B{bp["blocks"][focus_idx]["id"][-2:]}</text>')

    # 下半部：左 = 改进项 / 中 = 文件结构 + 重点段 / 右 = 行动按钮

    # 下左：改进项
    lines.append(f'  <rect x="40" y="280" width="500" height="240" fill="{c["panel"]}" stroke="{c["border"]}" rx="10"/>')
    lines.append(f'  <text x="60" y="308" font-size="13" font-weight="700" fill="{c["wood_deep"]}">📋 改进项（评分指向）</text>')
    lines.append(f'  <line x1="60" y1="316" x2="520" y2="316" stroke="{c["border"]}"/>')
    if improvements:
        for i, item in enumerate(improvements[:4]):
            y = 336 + i * 42
            # 分级标识
            first_char = item[:2]
            if "P0" in item[:4]:
                badge, badge_bg = "P0", c["coral_bg"]
                badge_text = c["coral_deep"]
            elif "P1" in item[:4]:
                badge, badge_bg = "P1", c["wood_bg"]
                badge_text = c["wood_deep"]
            else:
                badge, badge_bg = "P2", c["blue_bg"]
                badge_text = c["blue_deep"]
            lines.append(f'  <rect x="60" y="{y}" width="500" height="36" fill="{badge_bg}" rx="6"/>')
            lines.append(f'  <rect x="68" y="{y + 6}" width="32" height="24" fill="{badge_text}" rx="4"/>')
            lines.append(f'  <text x="84" y="{y + 22}" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">{badge}</text>')
            text = item[:80] + ("…" if len(item) > 80 else "")
            lines.append(f'  <text x="108" y="{y + 22}" font-size="11" fill="{c["text"]}">{escape_xml(text)}</text>')
    else:
        lines.append(f'  <text x="60" y="346" font-size="11" fill="{c["sub"]}">未检测到改进项，请先完成 B09 评分。</text>')

    # 下右：archetype 重点段 + 行动按钮
    lines.append(f'  <rect x="560" y="280" width="480" height="240" fill="{c["panel"]}" stroke="{c["border"]}" rx="10"/>')
    # 重点段（来自 visual_skin.emphasis_segment）
    emphasis = visual_skin.get("emphasis_segment", "")
    if emphasis:
        lines.append(f'  <rect x="580" y="300" width="440" height="50" fill="{c["coral_bg"]}" stroke="{c["coral"]}" stroke-width="1.5" rx="8"/>')
        lines.append(f'  <text x="600" y="320" font-size="11" font-weight="700" fill="{c["coral_deep"]}">🎯 框架重点段（archetype={escape_xml(archetype_id)}）</text>')
        lines.append(f'  <text x="600" y="340" font-size="11" fill="{c["text"]}">▍ {escape_xml(emphasis)}</text>')
    else:
        lines.append(f'  <rect x="580" y="300" width="440" height="50" fill="{c["wood_bg"]}" stroke="{c["wood"]}" rx="8"/>')
        lines.append(f'  <text x="600" y="320" font-size="11" font-weight="700" fill="{c["wood_deep"]}">archetype={escape_xml(archetype_id)}</text>')
        lines.append(f'  <text x="600" y="340" font-size="11" fill="{c["sub"]}">未配置 visual_skin.emphasis_segment</text>')

    # 关键决策
    decisions = bp.get("decisions", [])
    if decisions:
        lines.append(f'  <text x="580" y="376" font-size="11" font-weight="700" fill="{c["wood_deep"]}">▍ 关键决策（B06）</text>')
        for i, d in enumerate(decisions[:2]):
            y = 394 + i * 18
            lines.append(f'  <text x="600" y="{y}" font-size="10" fill="{c["text"]}">• {escape_xml(d[:90])}</text>')

    # 行动按钮
    btn_y = 450
    lines.append(f'  <rect x="580" y="{btn_y}" width="440" height="48" fill="{c["wood"]}" rx="24"/>')
    lines.append(f'  <text x="800" y="{btn_y + 30}" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle">✓ 通过验收，移交 skill-creator</text>')

    lines.append(f'  <rect x="580" y="{btn_y + 56}" width="212" height="36" fill="{c["panel"]}" stroke="{c["sub"]}" rx="18"/>')
    lines.append(f'  <text x="686" y="{btn_y + 78}" font-size="11" fill="{c["sub"]}" text-anchor="middle">→ 回 ③ 深化</text>')

    lines.append(f'  <rect x="808" y="{btn_y + 56}" width="212" height="36" fill="{c["panel"]}" stroke="{c["sub"]}" rx="18"/>')
    lines.append(f'  <text x="914" y="{btn_y + 78}" font-size="11" fill="{c["sub"]}" text-anchor="middle">📥 导出 brief</text>')

    lines.append("</svg>")
    return "\n".join(lines)


def render_html(data: dict, theme: str = "light", focus_idx: int = 2) -> str:
    """合成大图 HTML：主面板 SVG + 文件结构 SVG + 三件套说明 + 时间戳。"""
    bp = data["bp"]
    arch = data["arch"]
    main_svg = render_combined_svg(data, theme=theme, focus_idx=focus_idx)

    # 文件结构图（直接调用 render_structure.render_svg）
    from render_structure import render_svg as render_struct_svg
    struct_svg = render_struct_svg(arch, data["rows"], data["meta"], data["parsed"], theme, mode="已按蓝图填充")

    # 引入主 SVG 进 HTML（去掉 <?xml ?> 与 <svg> 的 xmlns 双写）
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape_html(bp["title"])} — 施工蓝图（合成大图）</title>
<style>
  :root {{
    --bg: {COLORS[theme]["bg"]};
    --panel: {COLORS[theme]["panel"]};
    --border: {COLORS[theme]["border"]};
    --text: {COLORS[theme]["text"]};
    --sub: {COLORS[theme]["sub"]};
    --wood: {COLORS[theme]["wood"]};
    --wood-deep: {COLORS[theme]["wood_deep"]};
  }}
  body {{
    margin: 0; padding: 32px;
    background: var(--bg);
    color: var(--text);
    font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif;
    line-height: 1.6;
  }}
  .meta {{
    max-width: 1100px;
    margin: 0 auto 24px;
    padding: 16px 24px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
  }}
  .meta-title {{
    font-size: 14px;
    color: var(--sub);
  }}
  .meta-title strong {{
    font-family: "Source Han Serif SC", "Songti SC", serif;
    font-size: 18px;
    color: var(--text);
    margin-right: 12px;
  }}
  .meta-actions a {{
    display: inline-block;
    padding: 6px 14px;
    margin-left: 8px;
    background: var(--wood);
    color: white;
    text-decoration: none;
    border-radius: 18px;
    font-size: 12px;
    font-weight: 600;
  }}
  .panel {{
    max-width: 1100px;
    margin: 0 auto 24px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
  }}
  .panel-header {{
    padding: 14px 24px;
    background: var(--bg);
    border-bottom: 1px solid var(--border);
    font-size: 13px;
    font-weight: 700;
    color: var(--wood-deep);
    letter-spacing: 0.5px;
  }}
  .panel-body {{ padding: 24px; overflow-x: auto; }}
  .panel-body svg {{ display: block; max-width: 100%; height: auto; }}
  footer {{
    max-width: 1100px;
    margin: 24px auto;
    padding: 16px 24px;
    color: var(--sub);
    font-size: 11px;
    text-align: center;
    border-top: 1px solid var(--border);
  }}
</style>
</head>
<body>

<div class="meta">
  <div class="meta-title">
    <strong>{escape_html(bp["title"])}</strong>
    施工蓝图 · 合成大图
  </div>
  <div class="meta-actions">
    <a href="#main">主面板</a>
    <a href="#struct">文件结构</a>
    <a href="#footer">数据源</a>
  </div>
</div>

<div class="panel" id="main">
  <div class="panel-header">▍ 主面板（综合分 + BR-5 + 10 格进度 + 改进项 + 行动）</div>
  <div class="panel-body">
    {main_svg}
  </div>
</div>

<div class="panel" id="struct">
  <div class="panel-header">▍ 文件结构图（archetype: {escape_html(arch.get("id", "—"))} · {escape_html(arch.get("name", "—"))}）</div>
  <div class="panel-body">
    {struct_svg}
  </div>
</div>

<footer id="footer">
  📐 数据源：visualize_blueprint.py · render_structure.py · b09_summary.py（三件套共用 blocks.py / archetypes.json） · 模式：{theme}
  <br>由 scripts/visual_session.py 生成 · 三秒法则：综合分大字 + 最低分项红色 ⚠ + archetype 重点段高亮
</footer>

</body>
</html>"""


# ───────────────────────── 主流程 ─────────────────────────

def main() -> int:
    ap = argparse.ArgumentParser(
        description="合成大图：蓝图 + 结构 + 评分同屏 HTML",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("blueprint_dir", help="蓝图目录（含 index.md + 01-10.md）")
    ap.add_argument("--output", "-o", help="输出 HTML 文件路径（默认 stdout，仅非 --json 时）")
    ap.add_argument("--theme", choices=("light", "dark"), default="light", help="主题")
    ap.add_argument("--focus", type=int, default=2, help="10 格进度高亮索引（0-based，默认 2=B03）")
    ap.add_argument("--json", action="store_true", help="输出结构化 JSON 摘要，不生成 HTML")
    args = ap.parse_args()

    bp_dir = Path(args.blueprint_dir).resolve()
    try:
        data = collect_session(bp_dir)
    except FileNotFoundError as e:
        print(f"[visual_session] {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"[visual_session] 数据收集失败: {e}", file=sys.stderr)
        return 1

    if args.json:
        # 输出简要摘要
        out_data = {
            "title": data["bp"]["title"],
            "overall": data["bp"]["overall"],
            "archetype": data["arch"]["id"],
            "archetype_name": data["arch"]["name"],
            "br5": data["b09"].get("br5", {}),
            "lowest": data["b09"].get("lowest"),
            "improvements_count": len(data["b09"].get("improvements", [])),
            "visual_skin": data.get("visual_skin"),
        }
        print(json.dumps(out_data, ensure_ascii=False, indent=2))
        return 0

    focus_idx = max(0, min(args.focus, len(data["bp"]["blocks"]) - 1))
    html = render_html(data, theme=args.theme, focus_idx=focus_idx)
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        print(f"已生成合成大图: {out}")
    else:
        print(html)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())