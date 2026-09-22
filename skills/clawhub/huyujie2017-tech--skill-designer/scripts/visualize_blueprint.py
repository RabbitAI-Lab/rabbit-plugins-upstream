"""
visualize_blueprint.py — 把 skill 蓝图目录渲染成一张 SVG 可视化图

读取 index.md 的 frontmatter + checkpoint，结合 01–10.md 的填充状态，
生成可视化图，帮助用户/评测者一眼看清蓝图全貌。两种模式：
    --mode completion（默认）  10 格积木链完成度进度图（每格填了多少）
    --mode essence             内容要点总览图（每格已填要点 2–4 行，四步流 Step② 初步方案用）

用法：
    python scripts/visualize_blueprint.py <蓝图目录> --output <xxx.svg> [--theme light|dark] [--mode completion|essence]
    python scripts/visualize_blueprint.py <蓝图目录> --json          # 输出结构化摘要
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Optional

from retry import read_text_robust
sys.path.insert(0, str(Path(__file__).resolve().parent))
from errors import enable_utf8  # noqa: E402

enable_utf8()  # Windows GBK 控制台下保证中文（含 stderr 报错）不乱码

BLOCK_FILES = [f"{i:02d}-条件.md" for i in range(1, 11)]
BLOCK_FILES[0] = "01-条件.md"
BLOCK_FILES[1] = "02-事实.md"
BLOCK_FILES[2] = "03-观点.md"
BLOCK_FILES[3] = "04-问题.md"
BLOCK_FILES[4] = "05-分析.md"
BLOCK_FILES[5] = "06-决策.md"
BLOCK_FILES[6] = "07-计划.md"
BLOCK_FILES[7] = "08-行动.md"
BLOCK_FILES[8] = "09-结果.md"
BLOCK_FILES[9] = "10-复盘.md"

BLOCK_SHORT = [
    "B01\n条件", "B02\n事实", "B03\n观点", "B04\n问题", "B05\n分析",
    "B06\n决策", "B07\n计划", "B08\n行动", "B09\n结果", "B10\n复盘",
]

COLORS = {
    "light": {
        # 积木原木色系——主 #d4a574 木 + 辅 #5b7bf0 蓝 + 点睛 #e07b5c 珊瑚
        "bg": "#faf6f0",
        "panel": "#ffffff",
        "border": "#e3d8c2",
        "text": "#2b2418",
        "sub": "#6b5e48",
        "done": "#6fa86f",     # 完成：积木绿
        "doing": "#d4a574",    # 进行中：原木色
        "todo": "#e3d8c2",     # 待办：米色
        "todo_text": "#a39476",
        "line": "#c8b48f",
        "accent": "#b8854f",   # 深木：标题重点
    },
    "dark": {
        # 深色主题对应：暖深底 + 米色文字
        "bg": "#1f1a14",
        "panel": "#2a2418",
        "border": "#4a3f2e",
        "text": "#f5ecdb",
        "sub": "#a39476",
        "done": "#8fc88f",
        "doing": "#e0b884",
        "todo": "#4a3f2e",
        "todo_text": "#6b5e48",
        "line": "#6b5e48",
        "accent": "#e0b884",
    },
}


def parse_frontmatter(text: str) -> dict:
    fm: dict[str, str] = {}
    if not text.startswith("---"):
        return fm
    end = text.find("---", 3)
    if end == -1:
        return fm
    block = text[3:end].strip()
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip().strip('"')
        fm[key] = val
    return fm


def parse_checkpoint(text: str) -> dict:
    """从 index.md 的 checkpoint 表提取字段。"""
    cp: dict[str, str] = {}
    m = re.search(r"## 进度快照.*?\n\| 字段 \| 值 \|\n\|[-\s|]+\n(.*?)\n##", text, re.S)
    if not m:
        return cp
    for line in m.group(1).strip().splitlines():
        cells = [c.strip() for c in line.split("|")]
        if len(cells) >= 3 and cells[1] and cells[2]:
            cp[cells[1]] = cells[2]
    return cp


def block_completion(block_path: Path) -> float:
    """返回 0.0–1.0 的完成度估计。"""
    text = read_text_robust(block_path) or ""
    if not text.strip():
        return 0.0

    # 占位符信号
    blanks = text.count("______")
    draft = text.count("【AI 建议】")
    pending = text.count("【需用户拍板】")

    # checklist 完成信号
    checked = text.count("☑")
    unchecked = text.count("☐")

    # 若 checklist 全勾，认为完成
    if unchecked == 0 and checked > 0 and blanks == 0 and pending == 0:
        return 1.0

    # 计算剩余工作量：每个占位符计 1 单位，每个 checklist 未完成计 0.5
    remaining = blanks + draft + pending + (unchecked * 0.5)

    # 估算总字段数：基于文本中列表项数量（粗略）
    list_items = len(re.findall(r"^\s*-\s+", text, re.M))
    total = max(list_items, 4)

    ratio = 1.0 - (remaining / total)
    return max(0.0, min(1.0, ratio))


def extract_decisions(block_path: Path) -> list[str]:
    """从 B06 提取关键决策摘要。"""
    text = read_text_robust(block_path) or ""
    decisions = []
    for line in text.splitlines():
        m = re.match(r"^\s*-\s*决策\s*\d+\s*[:：]\s*(.+?)\s*→\s*(.+?)$", line)
        if m:
            action, choice = m.group(1).strip(), m.group(2).strip()
            # 去掉草稿标记
            choice = re.sub(r"【[^】]+】", "", choice).strip()
            if choice and choice != "______":
                decisions.append(f"{action} → {choice}")
    return decisions[:3]


def extract_substance(block_path: Path, max_lines: int = 5) -> list[str]:
    """双轨进度图专用：提取每格的实质内容（要点更多行，不截断决策标签）。

    与 extract_essence 的区别：essence 用于 essence 模式单格 3 行；substance 用于
    dual-track 右轨 5 行 + 决策/待定项。规则：
      - 列表项优先（- 开头），跳过 checklist；
      - 跳过占位符 ______ 与空内容；
      - 去掉草稿标记再判断是否有实质；
      - 每行截断到 ~60 字符（双轨右轨宽度更大）；
      - 返回最多 max_lines 行。
    """
    text = read_text_robust(block_path) or ""
    candidates = []
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("-"):
            continue
        body = s.lstrip("- ").strip()
        if body.startswith("☐") or body.startswith("☑"):
            continue
        if "______" in body:
            continue
        cleaned = re.sub(r"【[^】]+】", "", body).strip(" ：:")
        if not cleaned or cleaned == "______":
            continue
        # 双轨右轨宽度更大，截到 60 字符
        if len(body) > 60:
            body = body[:59] + "…"
        candidates.append(body)
    return candidates[:max_lines] or ["（未填）"]


def extract_pending(block_path: Path, max_items: int = 2) -> list[str]:
    """从 B04/各格提取「待定项」摘要（双轨右轨的「待用户拍板」区块用）。"""
    text = read_text_robust(block_path) or ""
    items = []
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("-"):
            continue
        body = s.lstrip("- ").strip()
        # 待定项通常以「❶/❷」或「（问谁：用户/设计师）」等信号开头
        if any(sig in body for sig in ("❶", "❷", "❸", "待定", "问谁", "需用户")):
            cleaned = re.sub(r"【[^】]+】", "", body)
            # 双轨右轨稍宽，截到 50 字符
            if len(cleaned) > 50:
                cleaned = cleaned[:49] + "…"
            items.append(cleaned)
    return items[:max_items]


# 结论性信号词：命中则优先展示（essence 模式下每格挑"最像要点"的行）
ESSENCE_PRIORITY_KW = (
    "结论", "决策", "采用", "判断", "输入", "输出", "边界", "风险", "依据",
    "模式", "目标", "验证场景", "归纳", "结构框架", "archetype", "待定", "归属",
)


def extract_essence(block_path: Path, max_lines: int = 3) -> list[str]:
    """提取该格的关键内容要点（供 --mode essence 内容要点总览图展示）。

    规则：
      - 只取列表项（`- `）；
      - 跳过 checklist（☐/☑）与仍含占位符 `______` 的行（未填）；
      - 去掉【AI 建议】/【需用户拍板】标签后再判断是否有实质内容；
      - 结论性信号词命中的行优先，其余按出现顺序；
      - 每行截断到 ~40 字符；
      - 返回最多 max_lines 行；一格无内容返回 ["（未填）"]。
    """
    text = read_text_robust(block_path) or ""
    candidates: list[tuple[bool, str]] = []
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("-"):
            continue
        body = s.lstrip("- ").strip()
        if body.startswith("☐") or body.startswith("☑"):
            continue
        if "______" in body:
            continue
        cleaned = re.sub(r"【[^】]+】", "", body).strip(" ：:")
        if not cleaned or cleaned == "______":
            continue
        if len(body) > 40:
            body = body[:39] + "…"
        candidates.append((any(k in body for k in ESSENCE_PRIORITY_KW), body))
    # 结论性行优先；稳定排序保持同组内原顺序
    candidates.sort(key=lambda t: not t[0])
    picked = [b for _, b in candidates[:max_lines]]
    return picked or ["（未填）"]


def collect_blueprint(bp_dir: Path, mode: str = "completion") -> dict:
    index_path = bp_dir / "index.md"
    if not index_path.exists():
        raise FileNotFoundError(f"蓝图目录缺少 index.md: {bp_dir}")

    text = read_text_robust(index_path) or ""
    fm = parse_frontmatter(text)
    cp = parse_checkpoint(text)

    blocks = []
    for i, fname in enumerate(BLOCK_FILES, start=1):
        fpath = bp_dir / fname
        comp = block_completion(fpath) if fpath.exists() else 0.0
        essence = extract_essence(fpath) if (mode == "essence" and fpath.exists()) else []
        # dual-track 模式需要更详细的实质内容（5 行 + 决策 + 待定项）
        substance = extract_substance(fpath) if (mode == "dual-track" and fpath.exists()) else []
        decisions = extract_decisions(fpath) if (mode == "dual-track" and fpath.exists() and i == 6) else []
        pending = extract_pending(fpath) if (mode == "dual-track" and fpath.exists()) else []
        blocks.append({
            "id": f"B{i:02d}",
            "file": fname,
            "short": BLOCK_SHORT[i - 1],
            "completion": round(comp, 2),
            "essence": essence,
            "substance": substance,
            "decisions": decisions,
            "pending": pending,
        })

    decisions = extract_decisions(bp_dir / "06-决策.md")

    return {
        "title": fm.get("title", bp_dir.name),
        "platform": fm.get("platform", "—"),
        "entry": fm.get("entry", "—"),
        "channel": fm.get("channel", "—"),
        "status": fm.get("status", "草稿"),
        "checkpoint": cp,
        "blocks": blocks,
        "decisions": decisions,
        "overall": round(sum(b["completion"] for b in blocks) / len(blocks), 2),
    }


def escape_xml(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_svg(data: dict, theme: str = "light") -> str:
    c = COLORS[theme]
    width, height = 820, 520
    margin_x, margin_y = 40, 110
    cols, rows = 5, 2
    cell_w, cell_h = 136, 96
    gap_x, gap_y = 16, 28

    # 计算总体完成度色带
    overall = data["overall"]
    progress_w = 720
    filled_w = int(progress_w * overall)

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" font-family="-apple-system, \'Segoe UI\', \'Microsoft YaHei\', sans-serif">',
        f'  <rect width="{width}" height="{height}" fill="{c["bg"]}" rx="14"/>',
        f'  <rect x="12" y="12" width="{width - 24}" height="{height - 24}" fill="{c["panel"]}" stroke="{c["border"]}" stroke-width="1.5" rx="12"/>',
        # 标题
        f'  <text x="40" y="48" font-size="18" font-weight="700" fill="{c["text"]}">{escape_xml(data["title"])} — 技能蓝图</text>',
        f'  <text x="40" y="72" font-size="12" fill="{c["sub"]}">平台 {escape_xml(data["platform"])} · 入口 {escape_xml(data["entry"])} · 通道 {escape_xml(data["channel"])} · 状态 {escape_xml(data["status"])}</text>',
        # 总体进度条
        f'  <rect x="40" y="82" width="{progress_w}" height="10" fill="{c["todo"]}" rx="5"/>',
        f'  <rect x="40" y="82" width="{filled_w}" height="10" fill="{c["done"]}" rx="5"/>',
        f'  <text x="{40 + progress_w + 10}" y="91" font-size="11" fill="{c["sub"]}">{int(overall * 100)}%</text>',
    ]

    # 10 格积木
    for idx, b in enumerate(data["blocks"]):
        col = idx % cols
        row = idx // cols
        x = margin_x + col * (cell_w + gap_x)
        y = margin_y + row * (cell_h + gap_y)
        comp = b["completion"]
        if comp >= 0.95:
            fill, text_fill = c["done"], "#ffffff"
        elif comp >= 0.35:
            fill, text_fill = c["doing"], c["accent"]
        else:
            fill, text_fill = c["todo"], c["todo_text"]

        lines.append(f'  <rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" fill="{fill}" rx="10"/>')
        # 小标签
        for li, lt in enumerate(b["short"].split("\n")):
            weight = "700" if li == 0 else "500"
            size = "14" if li == 0 else "12"
            ly = y + 32 + li * 18
            lines.append(f'  <text x="{x + cell_w / 2}" y="{ly}" font-size="{size}" font-weight="{weight}" fill="{text_fill}" text-anchor="middle">{escape_xml(lt)}</text>')
        # 完成度小字
        lines.append(f'  <text x="{x + cell_w / 2}" y="{y + cell_h - 14}" font-size="10" fill="{text_fill}" text-anchor="middle" opacity="0.9">{int(comp * 100)}%</text>')

        # 连接线（除最后一个）
        if idx < len(data["blocks"]) - 1 and (col < cols - 1 or row == 0):
            nx = x + cell_w + 4
            ny = y + cell_h / 2
            if row == 0 and col == cols - 1:
                # 第一行末尾向下拐到第二行开头
                lines.append(f'  <path d="M{x + cell_w} {y + cell_h / 2} L{x + cell_w + gap_x / 2} {y + cell_h / 2} L{x + cell_w + gap_x / 2} {margin_y + cell_h + gap_y + cell_h / 2} L{margin_x - 4} {margin_y + cell_h + gap_y + cell_h / 2}" fill="none" stroke="{c["line"]}" stroke-width="1.5" stroke-dasharray="4 2"/>')
                lines.append(f'  <path d="M{margin_x - 8} {margin_y + cell_h + gap_y + cell_h / 2 - 4} L{margin_x - 4} {margin_y + cell_h + gap_y + cell_h / 2} L{margin_x - 8} {margin_y + cell_h + gap_y + cell_h / 2 + 4}" fill="none" stroke="{c["line"]}" stroke-width="1.5"/>')
            else:
                lines.append(f'  <line x1="{x + cell_w}" y1="{ny}" x2="{nx}" y2="{ny}" stroke="{c["line"]}" stroke-width="1.5" stroke-dasharray="4 2"/>')
                lines.append(f'  <path d="M{nx - 4} {ny - 4} L{nx} {ny} L{nx - 4} {ny + 4}" fill="none" stroke="{c["line"]}" stroke-width="1.5"/>')

    # 关键决策摘要
    y_dec = margin_y + rows * (cell_h + gap_y) + 6
    lines.append(f'  <text x="40" y="{y_dec}" font-size="12" font-weight="600" fill="{c["accent"]}">关键决策</text>')
    if data["decisions"]:
        for i, d in enumerate(data["decisions"][:2]):
            lines.append(f'  <text x="40" y="{y_dec + 18 + i * 16}" font-size="11" fill="{c["sub"]}">• {escape_xml(d[:75])}{"..." if len(d) > 75 else ""}</text>')
    else:
        lines.append(f'  <text x="40" y="{y_dec + 18}" font-size="11" fill="{c["sub"]}">B06 尚未填入关键决策。</text>')

    lines.append("</svg>")
    return "\n".join(lines)


def render_svg_essence(data: dict, theme: str = "light") -> str:
    """内容要点总览图：每格展示已填要点（最多 3 条），让初步方案可被一眼审。"""
    c = COLORS[theme]
    width, height = 880, 830
    margin_x, margin_y = 30, 108
    cols, rows = 2, 5
    gap_x, gap_y = 16, 14
    card_w = (width - margin_x * 2 - gap_x) / 2
    card_h = 126

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" font-family="-apple-system, \'Segoe UI\', \'Microsoft YaHei\', sans-serif">',
        f'  <rect width="{width}" height="{height}" fill="{c["bg"]}" rx="14"/>',
        f'  <rect x="12" y="12" width="{width - 24}" height="{height - 24}" fill="{c["panel"]}" stroke="{c["border"]}" stroke-width="1.5" rx="12"/>',
        # 标题
        f'  <text x="40" y="46" font-size="18" font-weight="700" fill="{c["text"]}">{escape_xml(data["title"])} — 初步方案（内容要点总览）</text>',
        f'  <text x="40" y="70" font-size="12" fill="{c["sub"]}">平台 {escape_xml(data["platform"])} · 入口 {escape_xml(data["entry"])} · 通道 {escape_xml(data["channel"])} · 状态 {escape_xml(data["status"])} · 总体 {int(data["overall"] * 100)}%</text>',
        f'  <text x="40" y="92" font-size="11" fill="{c["sub"]}">每格展示已填要点（最多 3 条）；带【AI 建议】的字段以“…”截断；空白格 = 待③深化设计。</text>',
    ]

    for idx, b in enumerate(data["blocks"]):
        col = idx % cols
        row = idx // cols
        x = margin_x + col * (card_w + gap_x)
        y = margin_y + row * (card_h + gap_y)
        comp = b["completion"]
        if comp >= 0.95:
            accent = c["done"]
        elif comp >= 0.35:
            accent = c["doing"]
        else:
            accent = c["todo_text"]

        # 卡片底
        lines.append(f'  <rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" fill="{c["panel"]}" stroke="{c["border"]}" stroke-width="1.2" rx="10"/>')
        # 标题
        title = b["short"].replace("\n", " ")  # "B01 条件"
        lines.append(f'  <text x="{x + 12}" y="{y + 22}" font-size="13" font-weight="700" fill="{c["text"]}">{escape_xml(title)}</text>')
        lines.append(f'  <text x="{x + card_w - 12}" y="{y + 22}" font-size="10" fill="{accent}" text-anchor="end">{int(comp * 100)}%</text>')
        # 分隔线
        lines.append(f'  <line x1="{x + 12}" y1="{y + 30}" x2="{x + card_w - 12}" y2="{y + 30}" stroke="{c["border"]}" stroke-width="1"/>')
        # 要点
        ess = b.get("essence") or ["（未填）"]
        for li, item in enumerate(ess[:3]):
            ly = y + 50 + li * 22
            lines.append(f'  <text x="{x + 14}" y="{ly}" font-size="11" fill="{c["sub"]}">• {escape_xml(item)}</text>')

    lines.append("</svg>")
    return "\n".join(lines)


def render_svg_dual_track(data: dict, theme: str = "light", focus_idx: int = 2) -> str:
    """双轨进度图：左轨 10 格完成度（小卡片网格）+ 右轨当前格实质内容卡片。

    设计目标：让"过程推演"可被一眼审——左轨扫一眼定位进度，右轨停留精读实质内容。
    focus_idx 是当前选中格的 0-based 索引（默认 2 = B03 观点，③深化设计阶段最常讨论）。
    """
    c = COLORS[theme]
    width, height = 1080, 600
    margin_x, margin_y = 32, 116
    left_w = 360        # 左轨宽度
    right_w = width - margin_x * 2 - left_w - 16
    right_x = margin_x + left_w + 16

    # 总体进度
    overall = data["overall"]
    progress_w = width - margin_x * 2

    # 找到当前格（默认 B03 = idx 2）
    focus_block = data["blocks"][focus_idx]
    focus_id = focus_block["id"]
    focus_substance = focus_block.get("substance", [])
    focus_decisions = focus_block.get("decisions", [])
    focus_pending = focus_block.get("pending", [])

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" font-family="-apple-system, \'Segoe UI\', \'Microsoft YaHei\', sans-serif">',
        f'  <rect width="{width}" height="{height}" fill="{c["bg"]}" rx="14"/>',
        f'  <rect x="12" y="12" width="{width - 24}" height="{height - 24}" fill="{c["panel"]}" stroke="{c["border"]}" stroke-width="1.5" rx="12"/>',
        # 标题
        f'  <text x="{margin_x}" y="46" font-size="18" font-weight="700" fill="{c["text"]}">🧩 双轨进度图 · 过程 vs 实质内容</text>',
        f'  <text x="{margin_x}" y="68" font-size="12" fill="{c["sub"]}">{escape_xml(data["title"])} · 平台 {escape_xml(data["platform"])} · 入口 {escape_xml(data["entry"])} · 通道 {escape_xml(data["channel"])}</text>',
        # 总体进度条
        f'  <rect x="{margin_x}" y="84" width="{progress_w}" height="10" fill="{c["todo"]}" rx="5"/>',
        f'  <rect x="{margin_x}" y="84" width="{int(progress_w * overall)}" height="10" fill="{c["doing"]}" rx="5"/>',
        f'  <text x="{width - margin_x}" y="103" font-size="11" fill="{c["sub"]}" text-anchor="end">总体 {int(overall * 100)}%</text>',
    ]

    # ── 左轨：10 格完成度 ──
    lines.append(f'  <text x="{margin_x}" y="128" font-size="13" font-weight="700" fill="{c["accent"]}">▌ 完成度（10 格）</text>')
    cell_w, cell_h = (left_w - 16) / 2, 56   # 2 列 5 行
    gap_x, gap_y = 16, 12
    for idx, b in enumerate(data["blocks"]):
        col = idx % 2
        row = idx // 2
        x = margin_x + col * (cell_w + gap_x)
        y = 138 + row * (cell_h + gap_y)
        comp = b["completion"]
        is_focus = (idx == focus_idx)

        if is_focus:
            # 当前选中：木色实心 + 白字
            fill, text_fill, sub_fill = c["doing"], "#ffffff", "#ffffff"
        elif comp >= 0.95:
            fill, text_fill, sub_fill = c["done"], "#ffffff", "#ffffff"
        elif comp >= 0.35:
            fill, text_fill, sub_fill = c["doing"], "#ffffff", "#ffffff"
        else:
            fill, text_fill, sub_fill = c["todo"], c["todo_text"], c["todo_text"]

        # 卡片
        lines.append(f'  <rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" fill="{fill}" rx="8"/>')
        if is_focus:
            # 当前选中描边强调
            lines.append(f'  <rect x="{x - 2}" y="{y - 2}" width="{cell_w + 4}" height="{cell_h + 4}" fill="none" stroke="{c["accent"]}" stroke-width="2" rx="10"/>')
        # 格名（B01 / 条件）
        short = b["short"].replace("\n", " ")
        lines.append(f'  <text x="{x + 12}" y="{y + 22}" font-size="12" font-weight="700" fill="{text_fill}">{escape_xml(short)}</text>')
        # 完成度
        lines.append(f'  <text x="{x + cell_w - 12}" y="{y + 22}" font-size="11" fill="{text_fill}" text-anchor="end">{int(comp * 100)}%</text>')
        # 进度条（小幅）
        bar_w = cell_w - 24
        bar_y = y + cell_h - 14
        lines.append(f'  <rect x="{x + 12}" y="{bar_y}" width="{bar_w}" height="6" fill="{text_fill}" fill-opacity="0.3" rx="3"/>')
        lines.append(f'  <rect x="{x + 12}" y="{bar_y}" width="{int(bar_w * comp)}" height="6" fill="{text_fill}" fill-opacity="0.95" rx="3"/>')

    # ── 右轨：当前格实质内容 ──
    lines.append(f'  <text x="{right_x}" y="128" font-size="13" font-weight="700" fill="{c["accent"]}">▌ 实质内容 · 高亮当前格 {focus_id}</text>')
    right_card_y = 138
    right_card_h = height - right_card_y - margin_y

    # 主卡片（底色木色淡）
    lines.append(f'  <rect x="{right_x}" y="{right_card_y}" width="{right_w}" height="{right_card_h}" fill="#fffaf2" stroke="{c["doing"]}" stroke-width="1.5" rx="10"/>')
    # 左侧木色竖条（强调当前选中）
    lines.append(f'  <rect x="{right_x}" y="{right_card_y}" width="6" height="{right_card_h}" fill="{c["doing"]}" rx="3 0 0 3"/>')
    # 标题
    title_text = f'{focus_id} · 当前格内容'
    lines.append(f'  <text x="{right_x + 20}" y="{right_card_y + 24}" font-size="13" font-weight="700" fill="{c["accent"]}">{escape_xml(title_text)}</text>')
    # 右侧统计
    stat_text = f'{len(focus_substance)} 行要点 · {len(focus_decisions)} 条决策 · {len(focus_pending)} 项待定'
    lines.append(f'  <text x="{right_x + right_w - 20}" y="{right_card_y + 24}" font-size="10" fill="{c["sub"]}" text-anchor="end">{escape_xml(stat_text)}</text>')
    lines.append(f'  <line x1="{right_x + 20}" y1="{right_card_y + 34}" x2="{right_x + right_w - 20}" y2="{right_card_y + 34}" stroke="{c["border"]}"/>')

    # 内容要点
    cy = right_card_y + 54
    for i, item in enumerate(focus_substance):
        lines.append(f'  <text x="{right_x + 24}" y="{cy}" font-size="11" fill="{c["text"]}">• {escape_xml(item)}</text>')
        cy += 22

    # 决策（如有）
    if focus_decisions:
        cy += 4
        lines.append(f'  <text x="{right_x + 20}" y="{cy}" font-size="11" font-weight="700" fill="{c["accent"]}">▍ 决策</text>')
        cy += 18
        for d in focus_decisions:
            # 决策用 badge 风格
            lines.append(f'  <rect x="{right_x + 24}" y="{cy - 12}" width="{right_w - 48}" height="20" fill="#e8f2e8" stroke="#6fa86f" rx="10"/>')
            lines.append(f'  <text x="{right_x + 36}" y="{cy + 3}" font-size="11" fill="#6fa86f">✓ {escape_xml(d[:90])}</text>')
            cy += 24

    # 待定项（如有）
    if focus_pending:
        cy += 4
        lines.append(f'  <text x="{right_x + 20}" y="{cy}" font-size="11" font-weight="700" fill="{c["accent"]}">▍ 待定项</text>')
        cy += 18
        for p in focus_pending:
            lines.append(f'  <text x="{right_x + 24}" y="{cy}" font-size="11" fill="#d94c4c">⚠ {escape_xml(p)}</text>')
            cy += 20

    # 页脚（提示双轨原理）
    lines.append(f'  <text x="{margin_x}" y="{height - 18}" font-size="10" fill="{c["sub"]}">左轨 = 完成度（机器算）｜·右轨 = 实质内容（每格已填要点 + 决策 + 待定项）｜·默认高亮 B03，--focus &lt;idx&gt; 切换</text>')

    lines.append("</svg>")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="把 skill 蓝图目录渲染成 SVG 可视化")
    ap.add_argument("blueprint_dir", help="蓝图目录（含 index.md + 01-10.md）")
    ap.add_argument("--output", "-o", help="输出 SVG 文件路径（默认 stdout）")
    ap.add_argument("--theme", choices=("light", "dark"), default="light", help="主题")
    ap.add_argument("--mode", choices=("completion", "essence", "dual-track"), default="completion",
                    help="渲染模式：completion（10 格完成度进度图，默认）｜essence（内容要点总览图，每格已填要点）｜dual-track（双轨进度图：左轨完成度 + 右轨当前格实质内容）")
    ap.add_argument("--focus", type=int, default=2,
                    help="dual-track 模式当前选中格索引（0-based，默认 2=B03 观点）")
    ap.add_argument("--json", action="store_true", help="输出结构化 JSON 摘要，不生成 SVG")
    args = ap.parse_args()

    bp_dir = Path(args.blueprint_dir).resolve()
    try:
        data = collect_blueprint(bp_dir, mode=args.mode)
    except FileNotFoundError as e:
        print(f"[visualize_blueprint] {e}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return 0

    if args.mode == "essence":
        svg = render_svg_essence(data, theme=args.theme)
    elif args.mode == "dual-track":
        # focus 索引越界保护
        focus_idx = max(0, min(args.focus, len(data["blocks"]) - 1))
        svg = render_svg_dual_track(data, theme=args.theme, focus_idx=focus_idx)
    else:
        svg = render_svg(data, theme=args.theme)

    if args.output:
        out = Path(args.output)
        out.write_text(svg, encoding="utf-8")
        print(f"已生成蓝图可视化: {out}")
    else:
        print(svg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
