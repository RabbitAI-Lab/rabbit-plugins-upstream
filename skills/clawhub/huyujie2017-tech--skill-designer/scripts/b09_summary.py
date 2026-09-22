"""
b09_summary.py — 自动生成 B09 结果积木摘要图

读取 09-结果.md 中的蓝图完备度（IQS）、外部价值分（EVS）、综合评分、
BR-5 五维就绪度（设计期口径）与外部 TRACE 返评（发布期口径）及改进项，
生成一张 SVG 摘要图，用于快速展示质量门结果。

评分口径：
    IQS  = 蓝图完备度（B01–B10 每格 10 分，满分 100）
    EVS  = BR-5 均分 × 20（五维各 1–5 分 → 20–100）
    综合 = IQS × EVS / 100

BR-5 未填写时，右侧面板自动回退显示外部 TRACE 返评（向后兼容旧蓝图）。

用法：
    python scripts/b09_summary.py <蓝图目录> --output <summary.svg> [--theme light|dark]
    python scripts/b09_summary.py <蓝图目录> --json
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

COLORS = {
    "light": {
        # 积木原木色系——主 #d4a574 木 + 辅 #5b7bf0 蓝 + 点睛 #e07b5c 珊瑚
        "bg": "#faf6f0",
        "panel": "#ffffff",
        "border": "#e3d8c2",
        "text": "#2b2418",
        "sub": "#6b5e48",
        "bar_iqs": "#d4a574",    # IQS 用木色（内部）
        "bar_evs": "#5b7bf0",    # EVS 用蓝色（外部）
        "bar_trace": "#b8854f",  # TRACE 用深木（发布期口径）
        "low": "#d94c4c",        # 最低分项用警示红
        "accent": "#b8854f",
    },
    "dark": {
        "bg": "#1f1a14",
        "panel": "#2a2418",
        "border": "#4a3f2e",
        "text": "#f5ecdb",
        "sub": "#a39476",
        "bar_iqs": "#e0b884",
        "bar_evs": "#7b93f7",
        "bar_trace": "#e0b884",
        "low": "#f87171",
        "accent": "#e0b884",
    },
}


def extract_number(text: str, keys: list[str]) -> Optional[float]:
    """解析形如「键名：85」的分数。

    兼容三种写法：
      1. 冒号式：外部价值分（EVS）：90
      2. 等号+冒号混合（blocks.py 生成的默认格式）：综合评分 = 内部 × 外部 / 100：76.5
      3. 纯双等号式：综合评分 = IQS × EVS / 100 = 76.5
    未填写（占位符 ______）时返回 None，不会把公式里的常数（如 / 100）误当成分数。
    """
    for key in keys:
        # 优先冒号：只认 : 或 ： 为分隔，避免把公式里的 = 后数字误当分数
        pat = rf"{re.escape(key)}[^:：\n]*[:：]\s*(\d+(?:\.\d+)?)"
        m = re.search(pat, text)
        if m:
            return float(m.group(1))
        # 兜底：无冒号时，取同一行内最后一个等号后的数字
        line = next((ln for ln in text.splitlines() if key in ln), None)
        if line:
            tail = line.split(key, 1)[1]
            m = re.search(r"=\s*(\d+(?:\.\d+)?)\s*$", tail)
            if m:
                return float(m.group(1))
    return None


def _parse_tvr_scores(text: str, prefix: str) -> dict[str, float]:
    """解析 T/R/A/C/E 五维分数。prefix 为行首标识（如「外部评分」或「BR-5」）。

    同时兼容两种写法：
      BR-5 均分：4.5（T=5 / R=4 / A=4.5 / C=4.5 / E=4.5）
      BR-5：T=5 / R=4 / A=4.5 / C=4.5 / E=4.5
    """
    pat = (
        rf"{re.escape(prefix)}[^:：\n]*[:：]\s*(?:均分\s*)?(?:\d+(?:\.\d+)?\s*)?[（(]?\s*"
        r"T\s*=\s*(\d+(?:\.\d+)?)\s*/\s*R\s*=\s*(\d+(?:\.\d+)?)\s*/\s*"
        r"A\s*=\s*(\d+(?:\.\d+)?)\s*/\s*C\s*=\s*(\d+(?:\.\d+)?)\s*/\s*E\s*=\s*(\d+(?:\.\d+)?)"
    )
    m = re.search(pat, text)
    if m:
        return dict(zip(("T", "R", "A", "C", "E"), map(float, m.groups())))
    return {}


def extract_br5(text: str) -> dict[str, float]:
    """设计期口径：BR-5 蓝图就绪度五维。"""
    return _parse_tvr_scores(text, "BR-5")


def extract_trace_scores(text: str) -> dict[str, float]:
    """发布期口径：外部平台（SkillHub TRACE 等）返评五维。"""
    return _parse_tvr_scores(text, "外部评分")


def extract_improvements(text: str) -> list[str]:
    m = re.search(r"指向的改进项[^:：\n]*[:：]\s*(.+?)(?:\n|$)", text)
    if not m:
        return []
    raw = m.group(1).strip()
    # 去掉模板自带的填写提示，避免「（评分必须指向具体改进，而非一个数字）」混入改进项
    raw = re.sub(r"（评分必须指向具体改进[^）]*）\s*$", "", raw).strip()
    # 支持中文分号、英文分号、逗号分隔；过滤未填写的占位符
    items = [i.strip() for i in re.split(r"[;；,，]", raw) if i.strip()]
    return [i for i in items if "______" not in i]


def extract_lowest_trace(scores: dict[str, float]) -> tuple[str, float] | None:
    if not scores:
        return None
    dim = min(scores, key=scores.get)
    return dim, scores[dim]


def compute_iqs(bp_dir: Path) -> tuple[int | None, dict]:
    """机器算 IQS 蓝图完备度——复用 check_blueprint 的逐格打分，口径完全一致。

    09-结果.md 没填 IQS 时调用，让 B09 出图不必先手填分数。
    check_blueprint 不可用时返回 (None, {})，退化为「未填」，不阻塞出图。
    """
    try:
        from blocks import dims_for_block
        from check_blueprint import BLOCKS, block_iqs, read, unchecked
    except ImportError:
        return None, {}

    detail: dict[str, dict] = {}
    total = 0
    for bid, fname in BLOCKS.items():
        text = read(bp_dir / fname)
        score, note = block_iqs(bid, fname, bool(text.strip()), text, unchecked(text))
        detail[bid] = {"score": score, "note": note, "dims": dims_for_block(bid)}
        total += score
    return total, detail


def parse_b09(bp_dir: Path) -> dict:
    b09_path = bp_dir / "09-结果.md"
    if not b09_path.exists():
        raise FileNotFoundError(f"蓝图目录缺少 09-结果.md: {bp_dir}")

    text = read_text_robust(b09_path) or ""

    iqs = extract_number(text, ["内部质量分"])
    evs = extract_number(text, ["外部价值分"])
    overall = extract_number(text, ["综合评分"])
    br5 = extract_br5(text)
    trace = extract_trace_scores(text)
    improvements = extract_improvements(text)
    lowest = extract_lowest_trace(br5) or extract_lowest_trace(trace)

    br5_avg = round(sum(br5.values()) / len(br5), 2) if br5 else None

    # 没填的分数交给机器算——B09 只需人工评 BR-5 五维，其余全部自动推出：
    #   IQS  ← check_blueprint 逐格打分（口径完全一致）
    #   EVS  ← BR-5 均分 × 20（口径里的定义式）
    #   综合 ← IQS × EVS / 100
    iqs_source, iqs_detail = "手填" if iqs is not None else "", {}
    if iqs is None:
        computed, iqs_detail = compute_iqs(bp_dir)
        if computed is not None:
            iqs, iqs_source = float(computed), "机器算"

    evs_source = "手填" if evs is not None else ""
    if evs is None and br5_avg is not None:
        evs, evs_source = round(br5_avg * 20, 1), "由 BR-5 换算"

    overall_source = "手填" if overall is not None else ""
    if overall is None and iqs is not None and evs is not None:
        overall, overall_source = round(iqs * evs / 100, 1), "机器算"

    return {
        "skill_name": bp_dir.name,
        "iqs": iqs,
        "iqs_source": iqs_source,
        "iqs_detail": iqs_detail,
        "evs": evs,
        "evs_source": evs_source,
        "overall": overall,
        "overall_source": overall_source,
        "br5": br5,
        "br5_avg": br5_avg,
        "trace": trace,
        "improvements": improvements,
        "lowest": lowest,
        "lowest_br5": extract_lowest_trace(br5),
        "lowest_trace": extract_lowest_trace(trace),
    }


def escape_xml(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_svg(data: dict, theme: str = "light") -> str:
    c = COLORS[theme]
    width, height = 720, 440

    iqs = data["iqs"] or 0
    evs = data["evs"] or 0
    overall = data["overall"] or 0
    br5 = data.get("br5") or {}
    trace = data["trace"] or {}
    improvements = data["improvements"] or []
    lowest = data.get("lowest")

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" font-family="-apple-system, \'Segoe UI\', \'Microsoft YaHei\', sans-serif">',
        f'  <rect width="{width}" height="{height}" fill="{c["bg"]}" rx="14"/>',
        f'  <rect x="12" y="12" width="{width - 24}" height="{height - 24}" fill="{c["panel"]}" stroke="{c["border"]}" stroke-width="1.5" rx="12"/>',
        # 标题
        f'  <text x="36" y="44" font-size="17" font-weight="700" fill="{c["text"]}">{escape_xml(data["skill_name"])} — B09 质量门摘要</text>',
        # 综合评分大数字（机器算出的标注来源，避免用户误以为是手填值）
        f'  <text x="620" y="50" font-size="28" font-weight="700" fill="{c["accent"]}" text-anchor="middle">{overall:.0f}</text>',
        f'  <text x="620" y="68" font-size="10" fill="{c["sub"]}" text-anchor="middle">综合评分</text>',
    ]
    if data.get("overall_source") == "机器算":
        lines.append(
            f'  <text x="620" y="82" font-size="10" fill="{c["sub"]}" text-anchor="middle">机器算</text>')

    # 左侧：设计期双维评分（蓝图完备度 × BR-5 换算）
    lines.append(f'  <text x="36" y="84" font-size="12" font-weight="600" fill="{c["accent"]}">设计期评分（IQS × EVS）</text>')
    bar_max = 190
    iqs_w = int(bar_max * (iqs / 100)) if iqs else 0
    evs_w = int(bar_max * (evs / 100)) if evs else 0
    br5_avg = data.get("br5_avg")

    lines += [
        f'  <text x="36" y="112" font-size="11" fill="{c["sub"]}">蓝图完备度 IQS</text>',
        f'  <rect x="130" y="102" width="{bar_max}" height="12" fill="{c["border"]}" rx="6"/>',
        f'  <rect x="130" y="102" width="{iqs_w}" height="12" fill="{c["bar_iqs"]}" rx="6"/>',
        f'  <text x="{130 + bar_max + 8}" y="112" font-size="11" fill="{c["text"]}">{iqs:.0f}</text>',
        f'  <text x="36" y="136" font-size="11" fill="{c["sub"]}">外部价值 EVS</text>',
        f'  <rect x="130" y="126" width="{bar_max}" height="12" fill="{c["border"]}" rx="6"/>',
        f'  <rect x="130" y="126" width="{evs_w}" height="12" fill="{c["bar_evs"]}" rx="6"/>',
        f'  <text x="{130 + bar_max + 8}" y="136" font-size="11" fill="{c["text"]}">{evs:.0f}</text>',
    ]
    sub = f"BR-5 均分 {br5_avg:.2f} × 20" if br5_avg else "待填 BR-5 五维"
    if data.get("iqs_source") == "机器算":
        sub += "　｜　IQS 机器算（未写入文件）"
    lines.append(f'  <text x="36" y="158" font-size="10" fill="{c["sub"]}">{sub}</text>')

    # 右侧：优先 BR-5 五维（设计期主用），未填则回退显示外部 TRACE 返评
    if br5:
        panel_title = "BR-5 五维就绪度（设计期）"
        names = {"T": "边界可信", "R": "失败可控", "A": "触发可辨", "C": "结构可解", "E": "验证可证"}
        primary, low, empty_hint = br5, data["lowest_br5"], ""
    else:
        panel_title = "外部平台 TRACE 评分"
        names = {"T": "Trust", "R": "Reliability", "A": "Adaptability", "C": "Convention", "E": "Effectiveness"}
        primary, low = trace, data["lowest_trace"]
        empty_hint = "尚未填入 BR-5 五维或 TRACE 外部评分"

    lines.append(f'  <text x="410" y="84" font-size="12" font-weight="600" fill="{c["accent"]}">{panel_title}</text>')
    if primary:
        bar_max_t = 200
        for i, dim in enumerate(("T", "R", "A", "C", "E")):
            score = primary.get(dim, 0)
            bar_w = int(bar_max_t * (score / 5))
            y = 106 + i * 22
            color = c["low"] if low and dim == low[0] else c["bar_trace"]
            lines += [
                f'  <text x="410" y="{y}" font-size="10" fill="{c["sub"]}" text-anchor="end">{dim} {names[dim]}</text>',
                f'  <rect x="420" y="{y - 8}" width="{bar_max_t}" height="10" fill="{c["border"]}" rx="5"/>',
                f'  <rect x="420" y="{y - 8}" width="{bar_w}" height="10" fill="{color}" rx="5"/>',
                f'  <text x="{420 + bar_max_t + 6}" y="{y}" font-size="10" fill="{c["text"]}">{score:.1f}</text>',
            ]
        if low:
            lines.append(f'  <text x="410" y="220" font-size="10" fill="{c["low"]}">最低分项：{low[0]} = {low[1]:.1f}（优先补强）</text>')
    else:
        lines.append(f'  <text x="410" y="110" font-size="11" fill="{c["sub"]}">{empty_hint}</text>')

    # 底部：改进项
    lines.append(f'  <text x="36" y="266" font-size="12" font-weight="600" fill="{c["accent"]}">指向的改进项</text>')
    if improvements:
        for i, item in enumerate(improvements[:4]):
            y = 288 + i * 20
            lines.append(f'  <text x="36" y="{y}" font-size="11" fill="{c["sub"]}">{i + 1}. {escape_xml(item[:70])}{"..." if len(item) > 70 else ""}</text>')
    else:
        lines.append(f'  <text x="36" y="288" font-size="11" fill="{c["sub"]}">未检测到改进项，请先完成 B09 评分。</text>')

    # 页脚
    footer = "综合评分 = 蓝图完备度 IQS × 外部价值 EVS / 100；EVS = BR-5 均分 × 20（设计期口径）。"
    if data.get("iqs_source") == "机器算":
        footer += " IQS 机器现算未写入文件，跑 check_blueprint.py --write-iqs 可回填。"
    lines.append(f'  <text x="36" y="416" font-size="10" fill="{c["sub"]}">{footer}</text>')
    lines.append("</svg>")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="自动生成 B09 结果积木摘要图")
    ap.add_argument("blueprint_dir", help="蓝图目录（含 09-结果.md）")
    ap.add_argument("--output", "-o", help="输出 SVG 文件路径（默认 stdout）")
    ap.add_argument("--theme", choices=("light", "dark"), default="light", help="主题")
    ap.add_argument("--json", action="store_true", help="输出结构化 JSON 摘要")
    args = ap.parse_args()

    bp_dir = Path(args.blueprint_dir).resolve()
    try:
        data = parse_b09(bp_dir)
    except FileNotFoundError as e:
        print(f"[b09_summary] {e}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return 0

    svg = render_svg(data, theme=args.theme)
    if args.output:
        out = Path(args.output)
        out.write_text(svg, encoding="utf-8")
        print(f"已生成 B09 摘要图: {out}")
    else:
        print(svg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
