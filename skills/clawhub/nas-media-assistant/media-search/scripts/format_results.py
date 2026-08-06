#!/usr/bin/env python3
"""检索结果格式化器（人读版）。

把 search_dispatcher 的 JSON 输出转成稳定列宽的带号列表，
供 agent 直接 echo 给用户，避免 LLM 自行渲染时格式漂移。

用法:
  search_dispatcher.py '<query>' | format_results.py [--query "..."] [--top N]
  format_results.py --input results.json [--query "..."] [--top N]

列定义:
  [N]  评分  分辨率  大小[/集均]  关键标签  标题  〔来源〕

退出码: 0 永远，方便 agent 透传；解析失败输出原 JSON 与一行提示。
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

# ---------- 工具 ----------

def _human_size(n: int | None) -> str:
    """字节数 -> 人类可读（GB/MB）。None/0 -> "?"。"""
    if not n:
        return "?"
    for unit in ("GB", "MB", "KB"):
        step = {"GB": 1024 ** 3, "MB": 1024 ** 2, "KB": 1024}[unit]
        if n >= step:
            v = n / step
            return f"{v:.2f}GB".replace(".00GB", "GB") if unit == "GB" else (
                f"{v:.0f}{unit}" if v >= 10 else f"{v:.1f}{unit}"
            )
    return f"{n}B"


def _per_ep(total: int | None, eps: int | None) -> str | None:
    if not total or not eps or eps <= 0:
        return None
    return f"{_human_size(total // eps)}/集"


def _truncate(s: str, n: int) -> str:
    if len(s) <= n:
        return s
    return s[: n - 1] + "…"


def _strip_noise(t: str) -> str:
    """去方括号里的发布组/广告等噪声，便于在窄列里看清主体。"""
    return re.sub(r"^\s*\[(高清影视之家发布|BBTTBA\.COM|BT下载)[^\]]*\]\s*", "", t, flags=re.I)


_RES_RE = re.compile(r"\d{3,4}p|4K|8K", re.I)


def _resolution(c: dict) -> str:
    qt = c.get("quality_tags") or []
    for t in qt:
        if _RES_RE.search(str(t)):
            return str(t)
    return "-"


def _fmt_tags(c: dict) -> str:
    """标签列：与分辨率列去重后展示编码/帧率/音频/HDR 等附加属性。"""
    res = _resolution(c)
    qt = c.get("quality_tags") or []
    bits: list[str] = []
    for t in qt:
        ts = str(t)
        if ts == res:
            continue  # 已在分辨率列展示，不重复
        bits.append(ts)
        if len(bits) >= 3:
            break
    return "·".join(bits)


def _note(c: dict, full: bool) -> str:
    """候选尾注：缺大小/高码/单集等提示。"""
    n = c.get("title") or ""
    notes: list[str] = []
    if not c.get("size_bytes"):
        notes.append("无大小")
    if c.get("is_high_bitrate"):
        notes.append("高码")
    if c.get("is_single_episode"):
        notes.append("单集")
    if c.get("size_overflow"):
        notes.append("过大")
    return "·".join(notes)


# ---------- 渲染 ----------

def render(payload: dict, query: str = "", top: int = 10) -> str:
    cands = payload.get("candidates") or []
    if not cands:
        msg = payload.get("summary") or "未检索到候选磁力"
        return f"⚠️  {msg}\n  建议：换关键词 / 放宽清晰度 / 检查网络\n"

    lines: list[str] = []
    header = f"🔍 检索: {query}" if query else "🔍 检索结果"
    lines.append(header)
    lines.append("─" * max(40, len(header) + 4))

    shown = cands[:top]
    for i, c in enumerate(shown, 1):
        score = c.get("quality_score")
        score_s = f"{score:5.1f}" if isinstance(score, (int, float)) else "  -  "
        res = _resolution(c).ljust(6)
        size = _human_size(c.get("size_bytes")).ljust(8)
        per_ep = _per_ep(c.get("size_bytes"), c.get("episode_count"))
        size_cell = f"{size}/{per_ep}" if per_ep else size
        tags = _fmt_tags(c).ljust(14)
        title = _truncate(_strip_noise(c.get("title") or ""), 60)
        src = c.get("source_id") or c.get("source") or "?"
        note = _note(c, full=False)
        suffix = f"  〔{src}〕"
        if note:
            suffix += f"  [{note}]"
        lines.append(f"  [{i}] {score_s}  {res}  {size_cell:<14}  {tags:<14}  {title}{suffix}")

    extra = len(cands) - len(shown)
    if extra > 0:
        lines.append(f"  …还有 {extra} 条候选未显示（用 --top N 调高上限）")

    excl = payload.get("excluded") or []
    if excl:
        lines.append("")
        lines.append(f"  已过滤: {len(excl)} 条（低质/低相关/死链，详见 excluded）")

    stats = payload.get("stats") or {}
    tiers = stats.get("tiers") or []
    if tiers:
        lines.append(f"  分层: {','.join(tiers)} · 命中: {stats.get('final', len(cands))} 条")

    lines.append("")
    lines.append("  👉 选号下载：回复编号（如 `1` / `下 2` / `下载第 3 个`）即开始派发该资源")
    return "\n".join(lines) + "\n"


# ---------- 入口 ----------

def main() -> int:
    p = argparse.ArgumentParser(description="把 search_dispatcher 的 JSON 渲染成带号列表")
    p.add_argument("--input", "-i", help="JSON 文件路径（默认从 stdin 读）")
    p.add_argument("--query", "-q", default="", help="原查询字符串，用于表头")
    p.add_argument("--top", "-n", type=int, default=10, help="显示前 N 条（默认 10）")
    args = p.parse_args()

    raw: str
    if args.input:
        raw = Path(args.input).read_text(encoding="utf-8")
    else:
        raw = sys.stdin.read()
    raw = raw.strip()
    if not raw:
        print("⚠️  空输入（未读取到 JSON）", file=sys.stderr)
        return 0

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"⚠️  JSON 解析失败: {e}", file=sys.stderr)
        print(raw[:500], file=sys.stderr)
        return 0

    try:
        sys.stdout.write(render(data, query=args.query, top=args.top))
    except Exception as e:
        print(f"⚠️  渲染异常: {e}", file=sys.stderr)
        print(json.dumps(data, ensure_ascii=False, indent=2)[:1000])
    return 0


if __name__ == "__main__":
    sys.exit(main())
