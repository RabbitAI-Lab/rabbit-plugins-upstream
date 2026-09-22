"""
render_structure.py — 把 skill 的文件结构渲染成一张「积木式结构图」SVG

与 visualize_blueprint.py 的分工：
    visualize_blueprint.py → 画「10 格进度」（设计过程走到哪）
    render_structure.py    → 画「文件结构」（最终产物长什么样）

数据来源两层：
    1. 骨架：scripts/archetypes.json 的 7 套结构框架范例（按 skill 类型选型）
    2. 内容：蓝图 07-计划.md 的实际填写（目录骨架 / 五段章节骨架 / 资源分配）

用法：
    python scripts/render_structure.py <蓝图目录> --output structure.svg [--theme light|dark]
    python scripts/render_structure.py --archetype full --output structure.svg   # 只出空白范例
    python scripts/render_structure.py <蓝图目录> --format md --output structure.md
    python scripts/render_structure.py --list                                    # 列出所有框架
    python scripts/render_structure.py <蓝图目录> --json                         # 结构化摘要
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

HERE = Path(__file__).resolve().parent
ARCHETYPES_PATH = HERE / "archetypes.json"

PLACEHOLDER = "______"

# 五段章节骨架（B07 ②）——每段的默认提示，未填写时展示
SKELETON_SEGMENTS = [
    ("Workflow", "标准执行顺序 ≤7 步，每步一句话，含分支与收尾"),
    ("Clarification Protocol", "四类提问策略各自的适用条件（一次性/逐步/选项式/关键假设）"),
    ("Resource Routing", "强路由句式：命中【X】→ 加载【Y】→ 产出【Z】"),
    ("Failure Handling", "四状态 + 升级条件 + 回退方式"),
    ("Validation", "产物存在 / 退出码 / 格式校验 / 报告验证命令与结果"),
]

COLORS = {
    "light": {
        # 积木原木色系——主 #d4a574 木 + 辅 #5b7bf0 蓝 + 点睛 #e07b5c 珊瑚
        "bg": "#faf6f0", "panel": "#ffffff", "border": "#e3d8c2",
        "text": "#2b2418", "sub": "#6b5e48", "faint": "#a39476",
        "dir": "#5b7bf0", "dir_bg": "#eef2fe",      # 目录用蓝（决策色）
        "file": "#2b2418", "file_bg": "#f5ecdb",     # 文件用木色
        "filled": "#6fa86f", "filled_bg": "#e8f2e8", # 已填用积木绿
        "pending": "#d8cdb4",
        "skeleton_bg": "#fff8e8", "skeleton_border": "#f0d79a", "skeleton_text": "#7a5c1e",
        "line": "#c8b48f", "accent": "#b8854f", "legend": "#f5ecdb",
    },
    "dark": {
        "bg": "#1f1a14", "panel": "#2a2418", "border": "#4a3f2e",
        "text": "#f5ecdb", "sub": "#a39476", "faint": "#6b5e48",
        "dir": "#7b93f7", "dir_bg": "#2a3252",
        "file": "#e0b884", "file_bg": "#2a2418",
        "filled": "#8fc88f", "filled_bg": "#243a31",
        "pending": "#4a3f2e",
        "skeleton_bg": "#3a3220", "skeleton_border": "#6b5a2e", "skeleton_text": "#f0d79a",
        "line": "#6b5e48", "accent": "#e0b884", "legend": "#2a2418",
    },
}


# ───────────────────────── 数据加载与解析 ─────────────────────────

def load_archetypes() -> dict:
    if not ARCHETYPES_PATH.exists():
        raise FileNotFoundError(f"缺少结构框架库: {ARCHETYPES_PATH}")
    text = read_text_robust(ARCHETYPES_PATH) or ""
    return json.loads(text)


ARCHETYPE_IDS = ("minimal", "pipeline", "tool", "knowledge", "template", "full", "suite")


def get_archetype(data: dict, aid: Optional[str]) -> dict:
    """解析结构框架：**容错优先**——旧蓝图 / 手填蓝图可能写中文名或自定义描述，
    识别不出时降级为默认框架并告警，绝不阻塞出图。"""
    archs = data.get("archetypes", [])
    default = next((a for a in archs if a["id"] == "minimal"), archs[0])

    if not aid:
        return default

    key = aid.strip().lower()
    # 1) 精确 id
    for a in archs:
        if a["id"] == key:
            return a
    # 2) 中文名 / 英文名包含匹配（如「模板产出型」「template（模板产出型）」）
    for a in archs:
        if key in a["name"].lower() or key in a.get("name_zh", ""):
            return a
    # 3) 反向包含：字段值里嵌着 id
    for a in archs:
        if a["id"] in key:
            return a
    # 4) 降级：告警 + 默认框架（不阻塞）
    print(f"[render_structure] 警告：无法识别结构框架 '{aid}'，已降级为默认 "
          f"'{default['id']}'（可选：{', '.join(a['id'] for a in archs)}）", file=sys.stderr)
    return default


# v2.14.0 起标记体系换为三档；旧标记保留以兼容历史蓝图
DRAFT_MARKS = (
    "【AI 建议】", "【需用户拍板】", "【待回填】",
    "【草稿，待确认】", "【草稿,待确认】", "【待确认】",
)


def clean(s: str) -> str:
    """清理草稿标记与多余空白。

    注意：只删「草稿/待拍板」这类**特定**标记，不能无差别删所有【】——
    Resource Routing 的「命中【X】→ 加载【Y】→ 产出【Z】」里【】是正文。
    """
    for mark in DRAFT_MARKS:
        s = s.replace(mark, "")
    s = s.replace(PLACEHOLDER, "").strip().strip("／/,，、;；")
    s = re.sub(r"\s+", " ", s)
    return s


# 从「目录骨架」文本中识别出的文件名 / 子目录名（\w 含中文，支持「月报.xlsx」这类命名）
NAME_RE = re.compile(
    r"[\w.\-]+\.(?:py|md|json|sh|yaml|yml|js|ts|xlsx|docx|csv|txt|html|svg)"
    r"|[\w\-]+/"
)


def extract_names(text: str) -> list:
    """从 'render.py 渲染 + validate.py 校验' 这类描述中抽出文件名/子目录名。"""
    if not text:
        return []
    out = []
    for m in NAME_RE.finditer(text):
        n = m.group(0)
        if n not in out:
            out.append(n)
    return out


def is_blank(s: str) -> bool:
    return (not s) or (PLACEHOLDER in s) or s.strip() in {"", "—", "-", "（待填）"}


def parse_b07(text: str) -> dict:
    """从 07-计划.md 抽取结构信息。解析失败时返回空值，由调用方降级为范例。"""
    out: dict = {
        "archetype": "", "scripts": "", "references": "", "assets": "",
        "alloc_scripts": "", "alloc_references": "", "alloc_assets": "",
        "segments": {},
    }
    if not text:
        return out

    m = re.search(r"结构框架\s*archetype\s*[:：]\s*(.+)", text)
    if m:
        raw = clean(m.group(1))
        low = raw.lower()
        # 先在字段值里找已知 id（兼容「template（模板产出型）」这类写法）
        hit = next((k for k in ARCHETYPE_IDS if re.search(rf"(?<![a-z]){k}(?![a-z])", low)), "")
        v = hit or re.split(r"[（(,，\s]", raw)[0]
        if v:
            out["archetype"] = v

    # ① 目录骨架：SKILL.md + scripts/（X）+ references/（Y）+ assets/（Z）
    m = re.search(r"①\s*目录骨架.*?scripts/\s*[（(]([^）)]*)[）)]", text, re.S)
    if m:
        out["scripts"] = clean(m.group(1))
    m = re.search(r"references/\s*[（(]([^）)]*)[）)]", text, re.S)
    if m:
        out["references"] = clean(m.group(1))
    m = re.search(r"assets/\s*[（(]([^）)]*)[）)]", text, re.S)
    if m:
        out["assets"] = clean(m.group(1))

    # ② 五段章节骨架
    for seg, _ in SKELETON_SEGMENTS:
        m = re.search(rf"##\s*{re.escape(seg)}\s*[:：]\s*(.+)", text)
        if m:
            v = clean(m.group(1))
            if not is_blank(v):
                out["segments"][seg] = v

    # ③ 资源分配
    m = re.search(r"③\s*资源分配\s*[:：]\s*(.+)", text)
    if m:
        line = m.group(1)
        for key in ("scripts", "references", "assets"):
            mm = re.search(rf"{key}\s*=\s*([^/]+?)(?=\s*/\s*(?:scripts|references|assets)\s*=|$)", line)
            if mm:
                v = clean(mm.group(1))
                if not is_blank(v):
                    out[f"alloc_{key}"] = v

    # 目录骨架里声明的具体文件名 → 注入为目录的子节点
    out["children"] = {
        "scripts": extract_names(out["scripts"]),
        "references": extract_names(out["references"]),
        "assets": extract_names(out["assets"]),
    }
    return out


def parse_index_meta(bp_dir: Path) -> dict:
    idx = bp_dir / "index.md"
    meta = {"title": bp_dir.name, "platform": "—", "channel": "—"}
    if not idx.exists():
        return meta
    text = read_text_robust(idx) or ""
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            for line in text[3:end].splitlines():
                m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
                if m:
                    k, v = m.group(1), m.group(2).strip().strip('"')
                    if k == "title":
                        meta["title"] = v
                    elif k == "platform":
                        meta["platform"] = v
                    elif k == "channel":
                        meta["channel"] = v
    return meta


# ───────────────────────── 行布局计算 ─────────────────────────

def merge_tree(tree: list, parsed: dict) -> list:
    """把 B07 目录骨架里声明的具体文件名注入为对应目录的子节点（范例里没有的才追加）。"""
    import copy

    tree = copy.deepcopy(tree)
    spec = parsed.get("children", {})

    def walk(nodes: list) -> None:
        for n in nodes:
            ff = n.get("fill_from", "")
            if ff.startswith("dir:"):
                key = ff.split(":", 1)[1]
                existing = {c["path"].rstrip("/") for c in (n.get("children") or [])}
                n.setdefault("children", [])
                for name in spec.get(key, []):
                    if name.rstrip("/") in existing:
                        continue
                    n["children"].append({
                        "path": name,
                        "kind": "dir" if name.endswith("/") else "file",
                        "role": "B07 声明",
                        "note": "由 B07 目录骨架填入",
                    })
                    existing.add(name.rstrip("/"))
            if n.get("children"):
                walk(n["children"])

    walk(tree)
    return tree


def build_rows(tree: list, parsed: dict, depth: int = 0, prefix_last: Optional[list] = None) -> list:
    """把目录树摊平成渲染行；同时把 B07 的实际内容注入对应节点。"""
    if prefix_last is None:
        prefix_last = []
    rows = []
    total = len(tree)
    for i, node in enumerate(tree):
        last = (i == total - 1)
        path = node["path"]
        note = node.get("note", "")
        role = node.get("role", "")
        fill_from = node.get("fill_from", "")

        # 用 B07 实际内容覆盖范例要点
        filled = False
        if fill_from.startswith("dir:"):
            key = fill_from.split(":", 1)[1]
            actual = parsed.get(f"alloc_{key}") or parsed.get(key, "")
            if actual:
                note = actual
                filled = True
        elif fill_from == "skeleton":
            segs = parsed.get("segments", {})
            if segs:
                note = f"五段骨架已填 {len(segs)}/{len(SKELETON_SEGMENTS)} 段"
                filled = True

        rows.append({
            "type": "node",
            "depth": depth,
            "path": path,
            "kind": node.get("kind", "file"),
            "role": role,
            "note": note,
            "filled": filled,
            "last": last,
            "guides": prefix_last + [last],
        })

        # SKILL.md 后紧跟五段章节骨架块
        if fill_from == "skeleton":
            rows.append({"type": "skeleton", "depth": depth + 1, "segments": parsed.get("segments", {})})

        children = node.get("children") or []
        if children:
            rows.extend(build_rows(children, parsed, depth + 1, prefix_last + [last]))
    return rows


# ───────────────────────── SVG 渲染 ─────────────────────────

def escape_xml(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def clip(s: str, n: int) -> str:
    s = s.strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def measure(s: str, size: float, mono: bool = False) -> float:
    """估算文本宽度：CJK 按全角、ASCII 按比例（等宽字体更宽）。"""
    ratio = 0.60 if mono else 0.52
    w = 0.0
    for ch in s:
        w += size if ord(ch) > 0x2E80 else size * ratio
    return w


def clip_to_width(s: str, maxw: float, size: float, mono: bool = False) -> str:
    """按像素宽度截断（比按字符数截断更准，中文不会被切得太短）。"""
    s = s.strip()
    if measure(s, size, mono) <= maxw:
        return s
    out, w = "", 0.0
    for ch in s:
        cw = measure(ch, size, mono)
        if w + cw > maxw - size:
            return out + "…"
        out += ch
        w += cw
    return out


def render_svg(arch: dict, rows: list, meta: dict, parsed: dict, theme: str, mode: str) -> str:
    c = COLORS[theme]
    W = 980
    margin_x = 34
    row_h = 32
    dir_h = 36
    indent = 24
    header_h = 96
    legend_h = 52

    # 高度计算
    body_h = 0
    for r in rows:
        if r["type"] == "node":
            body_h += dir_h if r["kind"] == "dir" else row_h
        else:
            body_h += 24 + len(SKELETON_SEGMENTS) * 21 + 12
    H = header_h + body_h + legend_h + 20

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
        f'font-family="-apple-system, \'Segoe UI\', \'Microsoft YaHei\', sans-serif">',
        f'  <rect width="{W}" height="{H}" fill="{c["bg"]}" rx="14"/>',
        f'  <rect x="12" y="12" width="{W - 24}" height="{H - 24}" fill="{c["panel"]}" stroke="{c["border"]}" stroke-width="1.5" rx="12"/>',
        # 标题
        f'  <text x="{margin_x}" y="46" font-size="18" font-weight="700" fill="{c["text"]}">{escape_xml(meta["title"])} — 文件结构图</text>',
        f'  <text x="{margin_x}" y="68" font-size="12" fill="{c["sub"]}">结构框架 {escape_xml(arch["name"])}（{escape_xml(arch["id"])}） · 平台 {escape_xml(meta["platform"])} · 通道 {escape_xml(meta["channel"])} · 模式 {escape_xml(mode)}</text>',
        f'  <text x="{margin_x}" y="86" font-size="11" fill="{c["faint"]}">{escape_xml(clip(arch["one_liner"], 96))}</text>',
        f'  <line x1="{margin_x}" y1="{header_h - 8}" x2="{W - margin_x}" y2="{header_h - 8}" stroke="{c["border"]}" stroke-width="1"/>',
    ]

    y = header_h + 6
    mono = "'JetBrains Mono', 'Cascadia Code', Consolas, monospace"

    for r in rows:
        if r["type"] == "node":
            depth = r["depth"]
            x_text = margin_x + depth * indent + 16
            is_dir = r["kind"] == "dir"
            h = dir_h if is_dir else row_h
            cy = y + h / 2

            # 层级引导线
            for d in range(depth):
                gx = margin_x + d * indent + 6
                if not r["guides"][d]:
                    lines.append(f'  <line x1="{gx}" y1="{y - 4}" x2="{gx}" y2="{y + h}" stroke="{c["line"]}" stroke-width="1"/>')
            if depth > 0:
                px = margin_x + (depth - 1) * indent + 6
                lines.append(f'  <line x1="{px}" y1="{cy}" x2="{px + indent - 4}" y2="{cy}" stroke="{c["line"]}" stroke-width="1"/>')

            # 节点徽标
            if is_dir:
                lines.append(f'  <rect x="{x_text - 6}" y="{cy - 9}" width="20" height="18" fill="{c["dir_bg"]}" stroke="{c["dir"]}" stroke-width="1" rx="4"/>')
                lines.append(f'  <text x="{x_text + 4}" y="{cy + 4}" font-size="10" font-weight="700" fill="{c["dir"]}" text-anchor="middle">DIR</text>')
                x_text += 24
            else:
                tag_col = c["filled"] if r["filled"] else (c["file"] if r["note"] else c["pending"])
                lines.append(f'  <circle cx="{x_text}" cy="{cy}" r="3.5" fill="{tag_col}"/>')
                x_text += 14

            # 路径名
            weight = "700" if is_dir else "600"
            size = "13" if is_dir else "12.5"
            col = c["dir"] if is_dir else c["file"]
            lines.append(
                f'  <text x="{x_text}" y="{cy + 4}" font-size="{size}" font-weight="{weight}" '
                f'fill="{col}" font-family="{mono}">{escape_xml(r["path"])}</text>'
            )
            x_text += measure(r["path"], float(size), mono=True) + 14

            # role 标签
            if r["role"]:
                role_txt = clip_to_width(r["role"], 190.0, 10.0)
                rw = measure(role_txt, 10.0) + 14
                bg = c["filled_bg"] if r["filled"] else c["legend"]
                fg = c["filled"] if r["filled"] else c["sub"]
                lines.append(f'  <rect x="{x_text}" y="{cy - 9}" width="{rw}" height="18" fill="{bg}" rx="9"/>')
                lines.append(f'  <text x="{x_text + rw / 2}" y="{cy + 4}" font-size="10" fill="{fg}" text-anchor="middle">{escape_xml(role_txt)}</text>')
                x_text += rw + 12

            # note（内容要点）
            if r["note"]:
                left = W - margin_x - x_text - 6
                note_col = c["filled"] if r["filled"] else c["faint"]
                prefix = "✓ " if r["filled"] else ""
                lines.append(
                    f'  <text x="{x_text}" y="{cy + 4}" font-size="10.5" fill="{note_col}">'
                    f'{escape_xml(clip_to_width(prefix + r["note"], left, 10.5))}</text>'
                )
            y += h

        else:  # 五段章节骨架块
            segs = r["segments"]
            bx = margin_x + r["depth"] * indent + 16
            bw = W - bx - margin_x
            bh = 16 + len(SKELETON_SEGMENTS) * 21 + 10
            lines.append(f'  <rect x="{bx}" y="{y}" width="{bw}" height="{bh}" fill="{c["skeleton_bg"]}" stroke="{c["skeleton_border"]}" stroke-width="1" rx="8"/>')
            lines.append(f'  <text x="{bx + 14}" y="{y + 18}" font-size="10.5" font-weight="700" fill="{c["skeleton_text"]}">SKILL.md 五段章节骨架</text>')
            filled_n = len(segs)
            lines.append(f'  <text x="{bx + bw - 14}" y="{y + 18}" font-size="10" fill="{c["faint"]}" text-anchor="end">已填 {filled_n}/{len(SKELETON_SEGMENTS)}</text>')
            for i, (seg, hint) in enumerate(SKELETON_SEGMENTS):
                sy = y + 38 + i * 21
                got = segs.get(seg, "")
                ok = bool(got)
                dot = c["filled"] if ok else c["pending"]
                lines.append(f'  <circle cx="{bx + 18}" cy="{sy - 4}" r="3" fill="{dot}"/>')
                lines.append(f'  <text x="{bx + 30}" y="{sy}" font-size="11" font-weight="600" fill="{c["skeleton_text"]}" font-family="{mono}">{escape_xml(seg)}</text>')
                content = got if ok else hint
                col = c["text"] if ok else c["faint"]
                cx = bx + 30 + measure(seg, 11.0, mono=True) + 12
                cw = bw - (cx - bx) - 20
                lines.append(f'  <text x="{cx}" y="{sy}" font-size="10.5" fill="{col}">{escape_xml(clip_to_width(content, cw, 10.5))}</text>')
            y += bh + 6

    # 图例
    ly = H - legend_h + 6
    lines.append(f'  <line x1="{margin_x}" y1="{ly - 12}" x2="{W - margin_x}" y2="{ly - 12}" stroke="{c["border"]}" stroke-width="1"/>')
    items = [
        (c["dir"], c["dir_bg"], "目录"),
        (c["file"], None, "文件（范例要点）"),
        (c["filled"], c["filled_bg"], "已按 B07 填入实际内容"),
    ]
    lx = margin_x
    for fg, bg, label in items:
        if bg:
            lines.append(f'  <rect x="{lx}" y="{ly}" width="14" height="14" fill="{bg}" stroke="{fg}" stroke-width="1" rx="3"/>')
        else:
            lines.append(f'  <circle cx="{lx + 7}" cy="{ly + 7}" r="3.5" fill="{fg}"/>')
        lines.append(f'  <text x="{lx + 20}" y="{ly + 11}" font-size="10.5" fill="{c["sub"]}">{escape_xml(label)}</text>')
        lx += measure(label, 10.5) + 48

    tip = clip(arch.get("tip", ""), 60)
    if tip:
        lines.append(f'  <text x="{W - margin_x}" y="{ly + 11}" font-size="10" fill="{c["faint"]}" text-anchor="end">💡 {escape_xml(tip)}</text>')

    lines.append("</svg>")
    return "\n".join(lines)


# ───────────────────────── Markdown 渲染 ─────────────────────────

def render_md(arch: dict, rows: list, meta: dict, mode: str) -> str:
    out = [
        f"# {meta['title']} — 文件结构图",
        "",
        f"> 结构框架：**{arch['name']}**（`{arch['id']}`） · 模式：{mode}",
        f"> {arch['one_liner']}",
        "",
        "```",
        f"{meta['title']}/",
    ]
    for r in rows:
        if r["type"] == "node":
            pad = "    " * r["depth"]
            branch = "└── " if r["last"] else "├── "
            name = r["path"] if (r["path"].endswith("/") or r["kind"] != "dir") else r["path"] + "/"
            note = r["note"]
            mark = "[已填] " if r["filled"] else ""
            role = f"{r['role']} | " if r.get("role") else ""
            out.append(f"{pad}{branch}{name:<28} # {mark}{role}{note}")
        else:
            pad = "    " * r["depth"]
            out.append(f"{pad}└── 【SKILL.md 五段章节骨架】")
            for seg, hint in SKELETON_SEGMENTS:
                got = r["segments"].get(seg, "")
                out.append(f"{pad}      • {seg}：{(got if got else '（待填）' + hint)}")
    out += ["```", "", f"💡 {arch.get('tip', '')}", ""]
    return "\n".join(out)


# ───────────────────────── 主流程 ─────────────────────────

def main() -> int:
    ap = argparse.ArgumentParser(
        description="把 skill 文件结构渲染成积木式 SVG 结构图",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="示例：\n"
               "  python scripts/render_structure.py ./bp/my-skill -o structure.svg\n"
               "  python scripts/render_structure.py --archetype full -o full-example.svg\n"
               "  python scripts/render_structure.py ./bp/my-skill --format md -o structure.md\n"
               "  python scripts/render_structure.py --list",
    )
    ap.add_argument("blueprint_dir", nargs="?", default="", help="蓝图目录（含 07-计划.md）")
    ap.add_argument("--output", "-o", help="输出文件路径（默认 stdout，仅 svg/md）")
    ap.add_argument("--archetype", "-a", help="强制指定结构框架 id（不读蓝图）")
    ap.add_argument("--format", "-f", choices=("svg", "md", "all"), default="svg", help="输出格式")
    ap.add_argument("--theme", choices=("light", "dark"), default="light", help="主题")
    ap.add_argument("--list", action="store_true", help="列出所有结构框架")
    ap.add_argument("--json", action="store_true", help="输出结构化 JSON 摘要")
    args = ap.parse_args()

    try:
        data = load_archetypes()
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"[render_structure] {e}", file=sys.stderr)
        return 1

    if args.list:
        print(f"{'ID':<12}{'名称':<26}一句话定位")
        print("-" * 96)
        for a in data.get("archetypes", []):
            print(f"{a['id']:<12}{a['name']:<26}{a['one_liner'][:56]}")
        print("\n选型规则：")
        for r in data.get("selection_rules", []):
            print(f"  {r['if']}  →  {r['then']}")
        print(f"\n{data.get('selection_note', '')}")
        return 0

    bp_dir = Path(args.blueprint_dir).resolve() if args.blueprint_dir else None
    parsed: dict = {"archetype": "", "scripts": "", "references": "", "assets": "",
                    "alloc_scripts": "", "alloc_references": "", "alloc_assets": "", "segments": {}}
    meta = {"title": "Skill 结构", "platform": "—", "channel": "—"}

    if bp_dir:
        if not bp_dir.is_dir():
            print(f"[render_structure] 蓝图目录不存在: {bp_dir}", file=sys.stderr)
            return 1
        b07 = bp_dir / "07-计划.md"
        if b07.exists():
            parsed = parse_b07(read_text_robust(b07) or "")
        meta = parse_index_meta(bp_dir)
        mode = "已按蓝图填充"
    else:
        meta["title"] = f"结构框架范例 · {args.archetype or 'minimal'}"
        mode = "空白范例（未读蓝图）"

    try:
        arch = get_archetype(data, args.archetype or parsed.get("archetype") or None)
    except ValueError as e:
        print(f"[render_structure] {e}", file=sys.stderr)
        return 1

    rows = build_rows(merge_tree(arch.get("tree", []), parsed), parsed)

    if args.json:
        print(json.dumps({
            "archetype": arch["id"], "archetype_name": arch["name"], "mode": mode,
            "meta": meta, "parsed_from_b07": parsed,
            "nodes": [{"path": r["path"], "role": r.get("role", ""), "note": r.get("note", ""),
                       "filled": r.get("filled", False)} for r in rows if r["type"] == "node"],
            "skeleton_filled": len(parsed.get("segments", {})),
        }, ensure_ascii=False, indent=2))
        return 0

    outputs = []
    if args.format in ("svg", "all"):
        outputs.append(("svg", render_svg(arch, rows, meta, parsed, args.theme, mode)))
    if args.format in ("md", "all"):
        outputs.append(("md", render_md(arch, rows, meta, mode)))

    if not args.output:
        print(outputs[0][1])
        return 0

    out_path = Path(args.output)
    if len(outputs) == 1:
        out_path.write_text(outputs[0][1], encoding="utf-8")
        print(f"已生成结构图: {out_path}")
    else:
        for ext, content in outputs:
            p = out_path.with_suffix(f".{ext}")
            p.write_text(content, encoding="utf-8")
            print(f"已生成结构图: {p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
