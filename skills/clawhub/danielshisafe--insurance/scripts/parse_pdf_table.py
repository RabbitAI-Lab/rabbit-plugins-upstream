#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
parse_pdf_table.py —— 文本层 PDF 利益演示表「坐标重建」解析器
=====================================================================
适用：保险计划书 PDF 有文字层、但 `extract.py` 抽不出表格（tables 为 0），
      且数字被打断成多行片段（如 `1,000,00` 与 `0` 分属两行）的场景。

原理（三步）
-------------------------------------------------------------------
1. `pdfplumber.extract_words(x_tolerance=1.2, y_tolerance=2.0)` 取每个词的坐标。
2. **按 top 聚类成逻辑行**：真实报告书中，「同一逻辑行内被拆行的数字片段」间距约 4pt，
   「相邻逻辑行」间距约 18pt。取阈值 ROW_GAP 介于两者之间（默认 10.0），
   即可把断行片段归并回同一逻辑行。
3. **行内按 x 区间重叠合并单元格**：碎片与已有单元格 x 有交集即视为同一格，
   格内 token 按 top 排序后拼接 → `1,000,00` + `0` 还原为 `1,000,000`。

使用方式
-------------------------------------------------------------------
  # 1) 先看某页的表头与列位（默认 top < 200 视作表头区）
  python parse_pdf_table.py <file.pdf> --page 12 --header

  # 2) 看某页数据行（每格带 x0 坐标，用于确定列序）
  python parse_pdf_table.py <file.pdf> --page 12 --dump

  # 3) 全文档扫描，导出 {保单年度: [各列数值]} 的 JSON
  python parse_pdf_table.py <file.pdf> --scan --out rows.json

  # 4) 扫描并打印列宽分布 / 缺年诊断（推荐先跑这一步）
  python parse_pdf_table.py <file.pdf> --scan

可调参数
-------------------------------------------------------------------
  --row-gap    float  逻辑行 top 间隔阈值，默认 10.0（实测 4.1 < 10 < 18.7）
  --min-cols   int    判定为数据行的最少单元格数，默认 9
  --header-top float  表头行的 top 上界，默认 200

输出 JSON 结构（--out）
-------------------------------------------------------------------
  {"12": {"page": 12, "vals": [1.0, 31.0, 1000000.0, ...]}, ...}
  键为保单年度（字符串），vals 为该行各列的数值（"--"/"-" 解析为 0.0，非数字为 None）。

★ 解析后必须做的三件事（防错）
-------------------------------------------------------------------
  1. 校验 1..N **无缺年**（有缺年说明 ROW_GAP 或页面范围不对）。
  2. 用表头确认**每一列的含义**再建模，尤其要定位「总现金价值 / 生存总利益」列（§7.11 铁律①）。
  3. 用行内恒等式交叉校验（如「基本保额现价 + 累积红利保额现价 = 总现金价值」）。
"""
import argparse
import json
import re
import sys

try:
    import pdfplumber
except ImportError:  # pragma: no cover
    sys.exit("需要 pdfplumber：pip install pdfplumber")

ROW_GAP = 10.0
MIN_COLS = 9
HEADER_TOP = 200.0
YEAR_RE = re.compile(r"\d{1,3}")


# ---------------------------------------------------------------- 核心
def cluster_rows(words, row_gap=ROW_GAP):
    """按 top 聚类成逻辑行；断行片段（间距 ~4pt）会并入同一行。"""
    ws = sorted(words, key=lambda w: (round(w["top"], 1), w["x0"]))
    rows, cur, last = [], [], None
    for w in ws:
        if last is None or w["top"] - last <= row_gap:
            cur.append(w)
        else:
            rows.append(cur)
            cur = [w]
        last = w["top"]
    if cur:
        rows.append(cur)
    return rows


def row_cells(row):
    """行内按 x 区间重叠聚成单元格，格内 token 按 top 排序后拼接。"""
    cells = []
    for w in sorted(row, key=lambda w: w["x0"]):
        placed = False
        for c in cells:
            if w["x0"] <= c["x1"] + 0.5 and w["x1"] >= c["x0"] - 0.5:
                c["toks"].append(w)
                c["x0"] = min(c["x0"], w["x0"])
                c["x1"] = max(c["x1"], w["x1"])
                placed = True
                break
        if not placed:
            cells.append({"x0": w["x0"], "x1": w["x1"], "toks": [w]})
    cells.sort(key=lambda c: c["x0"])
    out = []
    for c in cells:
        c["toks"].sort(key=lambda w: w["top"])
        out.append({
            "x0": round(c["x0"], 1),
            "x1": round(c["x1"], 1),
            "top": round(min(t["top"] for t in c["toks"]), 1),
            "text": "".join(t["text"] for t in c["toks"]),
        })
    return out


def page_rows(page, y_min=0.0, y_max=1e9, row_gap=ROW_GAP):
    words = page.extract_words(x_tolerance=1.2, y_tolerance=2.0)
    words = [w for w in words if y_min <= w["top"] <= y_max]
    res = [row_cells(r) for r in cluster_rows(words, row_gap)]
    return [r for r in res if r]


def is_data_row(r, min_cols=MIN_COLS):
    """数据行：单元格够多，且首格是 1~3 位纯数字（保单年度）。"""
    return len(r) >= min_cols and YEAR_RE.fullmatch(r[0]["text"].strip()) is not None


def to_num(s):
    s = s.strip().replace(",", "").replace("，", "")
    if s in ("--", "-", "", "—", "–"):
        return 0.0
    try:
        return float(s)
    except ValueError:
        return None


# ---------------------------------------------------------------- 子命令
def cmd_header(pdf, pno, args):
    for r in page_rows(pdf.pages[pno - 1], 0.0, args.header_top):
        print(f"[top={r[0]['top']:>6.1f}] n={len(r)}")
        for c in r:
            print(f"     x0={c['x0']:>7.1f} x1={c['x1']:>7.1f}  {c['text']}")


def cmd_dump(pdf, pno, args):
    for r in page_rows(pdf.pages[pno - 1], args.header_top):
        if not is_data_row(r, args.min_cols):
            continue
        print(f"--- 保单年度 {r[0]['text']}  top={r[0]['top']:.1f}  n={len(r)}")
        for i, c in enumerate(r):
            print(f"   [{i:>2}] x0={c['x0']:>7.1f}  {c['text']}")


def cmd_scan(pdf, args):
    rows, first_page = {}, None
    for pno, page in enumerate(pdf.pages, 1):
        for r in page_rows(page, 0.0, 1e9, args.row_gap):
            if not is_data_row(r, args.min_cols):
                continue
            try:
                y = int(float(r[0]["text"]))
            except ValueError:
                continue
            if y in rows:
                continue                       # 跨页重复行，保留首次
            rows[y] = {"page": pno, "vals": [to_num(c["text"]) for c in r]}

    if not rows:
        print("未找到数据行。试试调小 --min-cols 或调大 --row-gap。")
        return rows

    ys = sorted(rows)
    widths = sorted({len(v["vals"]) for v in rows.values()})
    print(f"行数 = {len(ys)}   年度 {ys[0]} ~ {ys[-1]}   列宽分布 = {widths}")
    if len(widths) > 1:
        print("  !! 列宽不一致：可能有页的行被切碎，请用 --dump 检查对应页")
    missing = [y for y in range(ys[0], ys[-1] + 1) if y not in rows]
    if missing:
        print(f"  !! 缺年度 {missing[:20]}{' ...' if len(missing) > 20 else ''}（共 {len(missing)} 个）")
    else:
        print(f"  ✓ 年度连续无缺失（{ys[0]}–{ys[-1]}）")
    print(f"  数据页：{sorted({v['page'] for v in rows.values()})}")

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump({str(y): rows[y] for y in ys}, f, ensure_ascii=False)
        print(f"已写出: {args.out}")
    return rows


def main():
    ap = argparse.ArgumentParser(description="文本层 PDF 利益演示表坐标重建解析器")
    ap.add_argument("file", help="计划书 PDF 路径")
    ap.add_argument("--page", type=int, help="页号（1 起），配合 --header / --dump")
    ap.add_argument("--header", action="store_true", help="打印该页表头区（top < --header-top）")
    ap.add_argument("--dump", action="store_true", help="打印该页数据行的每格内容与 x0")
    ap.add_argument("--scan", action="store_true", help="全文档扫描并导出 JSON")
    ap.add_argument("--out", help="--scan 的输出 JSON 路径")
    ap.add_argument("--row-gap", type=float, default=ROW_GAP, help=f"逻辑行 top 阈值，默认 {ROW_GAP}")
    ap.add_argument("--min-cols", type=int, default=MIN_COLS, help=f"数据行最少列数，默认 {MIN_COLS}")
    ap.add_argument("--header-top", type=float, default=HEADER_TOP, help=f"表头 top 上界，默认 {HEADER_TOP}")
    args = ap.parse_args()

    if not any([args.header, args.dump, args.scan]):
        ap.error("需指定 --header / --dump / --scan 之一")

    with pdfplumber.open(args.file) as pdf:
        if args.header or args.dump:
            if args.page is None:
                ap.error("--header / --dump 需要 --page")
            if args.header:
                cmd_header(pdf, args.page, args)
            if args.dump:
                cmd_dump(pdf, args.page, args)
        if args.scan:
            cmd_scan(pdf, args)


if __name__ == "__main__":
    try:
        from _feedback_hook import install; install()
    except Exception:
        pass
    main()
