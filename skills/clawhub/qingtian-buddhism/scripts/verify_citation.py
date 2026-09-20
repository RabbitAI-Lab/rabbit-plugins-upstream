#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_citation.py — 青田·原始佛教修学助手 引用核验（防幻觉护栏）

借鉴 FoJin 的「确定性引用护栏」：回答中引用的经文，发送前用本脚本核验
「引用文本」确实存在于标注的语料文件中，避免 LLM 凭记忆编造或错位引用。

核验口径：
  - 文件路径按 CANON_DIR（data/corpus/<译本目录>）解析；rel 与 chunks/source 中一致。
  - 文本先做归一化：NFC + 折叠空白（\\s+ → 单个空格）+ 拉丁字母小写（中文不受影响），
    再在目标文本（可选限定行号区间）中做包含匹配。
  - 命中输出所在行号与片段；未命中退出码 1 并给出最接近的行，便于人工复核。

用法：
  python scripts/verify_citation.py --file "义注/经藏义注/小部义注/法句义注_2026-06-21.txt" \
      --quote "此身实不久，将卧于地上；被弃无意识，无用如碎木。"
  python scripts/verify_citation.py --file "三藏经文/经藏/相应部/大品（相应部）_2026-06-21.txt" \
      --quote-file quote.txt --lines "7718-7890"
  # --quote 也可直接从引用行粘贴多行；建议配合 --lines 精确限定行号区间。

退出码：0 = 引文核验通过；1 = 未找到；2 = 用法/环境错误。
环境变量：CANON_TOP（默认「巴利三藏巴利-中文对照译本（2026-06-21） txt」）。
"""

import os
import sys
import re
import argparse
import unicodedata


HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.abspath(os.path.join(HERE, ".."))
CANON_TOP = os.environ.get(
    "CANON_TOP", "巴利三藏巴利-中文对照译本（2026-06-21） txt"
)
CANON_DIR = os.path.join(SKILL_ROOT, "data", "corpus", CANON_TOP)

_WS_RE = re.compile(r"\s+")


def normalize(text):
    """归一化：NFC + 折叠空白（\\s+→单个空格）+ 拉丁小写（保留标点）。"""
    text = unicodedata.normalize("NFC", text)
    text = _WS_RE.sub(" ", text).strip()
    return text.lower()


def normalize_nospace(text):
    """第二档：全部空白去掉（处理引文跨行、粘贴时换行变空格等差异）。"""
    text = unicodedata.normalize("NFC", text)
    return re.sub(r"\s+", "", text).lower()


def load_lines(rel):
    """读取 rel 文件（相对 CANON_DIR），返回 LF 归一化后的行列表与全文。"""
    if not os.path.exists(rel):
        cand = os.path.join(CANON_DIR, *rel.split(os.sep))
        if not os.path.exists(cand):
            raise FileNotFoundError(
                f"找不到语料文件：{rel}\n"
                f"（已尝试 CANON_DIR 下：{cand}）\n"
                f"请确认 rel 路径正确，或先运行 python scripts/setup_corpus.py"
            )
        rel = cand
    with open(rel, encoding="utf-8", errors="replace") as f:
        text = f.read().replace("\r\n", "\n")
    lines = text.split("\n")
    return lines, text


def verify(rel, quote, lines_range=None):
    """核验引文。返回 (found: bool, detail: dict)。"""
    lines, text = load_lines(rel)
    q = normalize(quote)
    if not q:
        raise ValueError("引用文本为空")

    if lines_range:
        a, b = lines_range
        seg = "\n".join(lines[a - 1:b])
    else:
        seg = text

    # 匹配策略：① 折叠空白精确匹配 → ② 去全部空白匹配（引文跨行/换行变空格）
    for strategy, (q_n, s_n) in (
        ("collapse", (normalize(quote), normalize(seg))),
        ("nospace", (normalize_nospace(quote), normalize_nospace(seg))),
    ):
        idx = s_n.find(q_n)
        if idx >= 0:
            return True, {"match": True, "strategy": strategy,
                          "quote_norm": normalize(quote)}

    # 未命中：给出包含引用首段的最接近行，便于人工复核
    probe = normalize_nospace(quote)[:24]
    best = None
    best_pos = -1
    for i, ln in enumerate(lines, 1):
        if lines_range and not (lines_range[0] <= i <= lines_range[1]):
            continue
        n_ln = normalize_nospace(ln)
        p = n_ln.find(probe)
        if p >= 0 and (best_pos < 0 or p < best_pos):
            best = i
            best_pos = p
    return False, {
        "match": False,
        "quote_norm": normalize(quote),
        "nearest_line": best,
        "nearest_snippet": (lines[best - 1].strip()[:120] if best else None),
    }


def _cli():
    ap = argparse.ArgumentParser(description="巴利三藏引用核验（防幻觉护栏）")
    ap.add_argument("--file", required=True, help="语料文件 rel 路径（相对 CANON_DIR）")
    ap.add_argument("--quote", help="引用文本（多行可用 \\n；与 --quote-file 二选一）")
    ap.add_argument("--quote-file", help="从文件读取引用文本")
    ap.add_argument("--lines", help="限定行号区间，如 2231-2261（1 起始）")
    args = ap.parse_args()

    if not args.quote and not args.quote_file:
        print("[verify_citation] 必须提供 --quote 或 --quote-file", file=sys.stderr)
        return 2
    if args.quote and args.quote_file:
        print("[verify_citation] --quote 与 --quote-file 只能选其一", file=sys.stderr)
        return 2

    quote = args.quote
    if args.quote_file:
        try:
            with open(args.quote_file, encoding="utf-8") as f:
                quote = f.read()
        except OSError as e:
            print(f"[verify_citation] 读取引用文件失败：{e}", file=sys.stderr)
            return 2

    lines_range = None
    if args.lines:
        try:
            a, b = (int(x) for x in args.lines.split("-"))
            lines_range = (a, b)
        except ValueError:
            print("[verify_citation] --lines 格式应为 A-B，如 2231-2261", file=sys.stderr)
            return 2

    try:
        found, detail = verify(args.file, quote, lines_range)
    except FileNotFoundError as e:
        print(f"[verify_citation] {e}", file=sys.stderr)
        return 2
    except ValueError as e:
        print(f"[verify_citation] {e}", file=sys.stderr)
        return 2

    if found:
        print(f"✅ 引文核验通过：{args.file}"
              + (f"（行 {lines_range[0]}–{lines_range[1]}）" if lines_range else ""))
        strat = "折叠空白匹配" if detail.get("strategy") == "collapse" else "去空白匹配（引文跨行）"
        print(f"   匹配方式：{strat}")
        print(f"   归一化引文：{detail['quote_norm'][:80]}{'…' if len(detail['quote_norm'])>80 else ''}")
        return 0

    print(f"❌ 未在 {args.file} 中找到该引文"
          + (f"（行 {lines_range[0]}–{lines_range[1]}）" if lines_range else ""))
    print(f"   归一化引文：{detail['quote_norm'][:80]}{'…' if len(detail['quote_norm'])>80 else ''}")
    if detail.get("nearest_line"):
        print(f"   最接近行 {detail['nearest_line']}：{detail['nearest_snippet']}")
    else:
        print("   未找到任何近似行（可能文件/行号/译文版本不符，或引文确属编造）")
    return 1


if __name__ == "__main__":
    sys.exit(_cli())
