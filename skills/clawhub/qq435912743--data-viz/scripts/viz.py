#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""viz —— 数据可视化（纯 Python，无 matplotlib/pandas 依赖）。

读 CSV/JSON 数据集，自动推断列类型，生成 SVG 图表（柱状/直方图/散点/折线）
与一个聚合的 HTML 看板。全部用标准库，离线可运行、可验证。

用法：
  python viz.py --data <file.csv|.json> --out <输出目录> [--topn 12]
"""
import os, sys, json, csv, argparse, statistics as st
from datetime import datetime

W, H = 640, 400
PAD = 56


def is_number(s):
    try:
        float(s)
        return True
    except Exception:
        return False


def load_rows(path):
    if path.lower().endswith(".json"):
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            data = data.get("rows") or data.get("data") or [data]
        return data
    rows = []
    with open(path, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows


def infer_types(rows):
    cols = list(rows[0].keys()) if rows else []
    types = {}
    for c in cols:
        vals = [r.get(c, "") for r in rows if r.get(c, "") != ""]
        nums = [v for v in vals if is_number(v)]
        types[c] = "numeric" if (vals and len(nums) / len(vals) > 0.8) else "categorical"
    return cols, types


def svg_frame(title):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
             f'<text x="{W/2}" y="22" font-size="15" text-anchor="middle" fill="#222">{title}</text>',
             f'<line x1="{PAD}" y1="{H-PAD}" x2="{W-PAD}" y2="{H-PAD}" stroke="#888"/>',
             f'<line x1="{PAD}" y1="{PAD}" x2="{PAD}" y2="{H-PAD}" stroke="#888"/>']


def bar_chart(title, cats, vals):
    s = svg_frame(title)
    if not vals:
        return "".join(s) + "</svg>"
    mx = max(vals) or 1
    n = len(vals)
    bw = (W - 2 * PAD) / max(n, 1)
    for i, (c, v) in enumerate(zip(cats, vals)):
        h = (v / mx) * (H - 2 * PAD)
        x = PAD + i * bw
        y = H - PAD - h
        s.append(f'<rect x="{x+2:.1f}" y="{y:.1f}" width="{bw-4:.1f}" height="{h:.1f}" fill="#4C8BF5"/>')
        if i < 12:
            s.append(f'<text x="{x+bw/2:.1f}" y="{H-PAD+14}" font-size="9" text-anchor="middle" fill="#555">{str(c)[:6]}</text>')
        s.append(f'<text x="{x+bw/2:.1f}" y="{y-3:.1f}" font-size="9" text-anchor="middle" fill="#333">{v:.1f}</text>')
    s.append(f'<text x="{PAD-6}" y="{PAD+(H-2*PAD)/2:.0f}" font-size="9" fill="#888" transform="rotate(-90 {PAD-6} {H/2})" text-anchor="middle">value</text>')
    return "".join(s) + "</svg>"


def histogram(title, vals):
    s = svg_frame(title)
    if not vals:
        return "".join(s) + "</svg>"
    import math
    nb = min(12, max(4, int(math.sqrt(len(vals)))))
    lo, hi = min(vals), max(vals)
    span = (hi - lo) or 1
    bins = [0] * nb
    for v in vals:
        idx = min(nb - 1, int((v - lo) / span * nb))
        bins[idx] += 1
    mx = max(bins) or 1
    bw = (W - 2 * PAD) / nb
    for i, cnt in enumerate(bins):
        h = (cnt / mx) * (H - 2 * PAD)
        x = PAD + i * bw
        y = H - PAD - h
        s.append(f'<rect x="{x+1:.1f}" y="{y:.1f}" width="{bw-2:.1f}" height="{h:.1f}" fill="#34A853"/>')
    s.append(f'<text x="{PAD}" y="{H-PAD+30}" font-size="9" fill="#555">{lo:.1f}</text>')
    s.append(f'<text x="{W-PAD}" y="{H-PAD+30}" font-size="9" text-anchor="end" fill="#555">{hi:.1f}</text>')
    return "".join(s) + "</svg>"


def scatter(title, xs, ys):
    s = svg_frame(title)
    if not xs:
        return "".join(s) + "</svg>"
    xlo, xhi = min(xs), max(xs)
    ylo, yhi = min(ys), max(ys)
    xspan, yspan = (xhi - xlo) or 1, (yhi - ylo) or 1
    for x, y in zip(xs, ys):
        px = PAD + (x - xlo) / xspan * (W - 2 * PAD)
        py = H - PAD - (y - ylo) / yspan * (H - 2 * PAD)
        s.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="2.5" fill="#A142F5" opacity="0.7"/>')
    return "".join(s) + "</svg>"


def line_chart(title, xs, ys):
    s = svg_frame(title)
    if not xs:
        return "".join(s) + "</svg>"
    xlo, xhi = min(xs), max(xs)
    ylo, yhi = min(ys), max(ys)
    xspan, yspan = (xhi - xlo) or 1, (yhi - ylo) or 1
    pts = []
    for x, y in zip(xs, ys):
        px = PAD + (x - xlo) / xspan * (W - 2 * PAD)
        py = H - PAD - (y - ylo) / yspan * (H - 2 * PAD)
        pts.append(f"{px:.1f},{py:.1f}")
    s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#FBBC05" stroke-width="2"/>')
    return "".join(s) + "</svg>"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--topn", type=int, default=12)
    args = ap.parse_args()

    rows = load_rows(args.data)
    if not rows:
        print("⚠️ 空数据集")
        sys.exit(1)
    cols, types = infer_types(rows)
    os.makedirs(args.out, exist_ok=True)
    charts = []
    summary = {"columns": types, "n_rows": len(rows)}

    numeric_cols = [c for c, t in types.items() if t == "numeric"]
    cat_cols = [c for c, t in types.items() if t == "categorical"]

    # 1) 每个数值列直方图
    for c in numeric_cols[:6]:
        vals = [float(r[c]) for r in rows if is_number(r.get(c, ""))]
        fn = f"hist_{c}.svg"
        open(os.path.join(args.out, fn), "w", encoding="utf-8").write(histogram(f"分布：{c}", vals))
        charts.append(fn)
        if vals:
            summary[c] = {"mean": round(st.mean(vals), 3), "min": round(min(vals), 3),
                          "max": round(max(vals), 3), "std": round(st.pstdev(vals), 3) if len(vals) > 1 else 0}

    # 2) 数值列之间散点（前 2 对）
    for i in range(min(2, len(numeric_cols) - 1)):
        a, b = numeric_cols[i], numeric_cols[i + 1]
        xs = [float(r[a]) for r in rows if is_number(r.get(a, "")) and is_number(r.get(b, ""))]
        ys = [float(r[b]) for r in rows if is_number(r.get(a, "")) and is_number(r.get(b, ""))]
        fn = f"scatter_{a}_vs_{b}.svg"
        open(os.path.join(args.out, fn), "w", encoding="utf-8").write(scatter(f"散点：{a} vs {b}", xs, ys))
        charts.append(fn)

    # 3) 分类列 × 数值列：柱状（各类均值，取 topn）
    for cat in cat_cols[:3]:
        for num in numeric_cols[:2]:
            groups = {}
            for r in rows:
                if not is_number(r.get(num, "")):
                    continue
                groups.setdefault(r.get(cat, "?"), []).append(float(r[num]))
            if not groups:
                continue
            items = sorted(groups.items(), key=lambda kv: st.mean(kv[1]), reverse=True)[:args.topn]
            cats = [k for k, _ in items]
            vals = [st.mean(v) for _, v in items]
            fn = f"bar_{cat}_{num}.svg"
            open(os.path.join(args.out, fn), "w", encoding="utf-8").write(bar_chart(f"均值：{num} by {cat}", cats, vals))
            charts.append(fn)
            break  # 每个分类列只配一个数值列，控制图表数

    # HTML 看板
    cards = "".join(
        f'<div class="card"><img src="{fn}" alt="{fn}"/></div>' for fn in charts
    )
    html = f"""<!doctype html><html lang="zh"><head><meta charset="utf-8">
<title>数据可视化看板</title><style>
body{{font-family:system-ui,'Microsoft YaHei',sans-serif;background:#f5f7fa;margin:0;padding:20px}}
h1{{font-size:18px;color:#222}}.grid{{display:flex;flex-wrap:wrap;gap:16px}}
.card{{background:#fff;border:1px solid #e3e8ef;border-radius:10px;padding:10px;box-shadow:0 1px 3px rgba(0,0,0,.06)}}
.card img{{width:640px;max-width:100%;height:auto}}</style></head>
<body><h1>数据可视化看板 · {len(rows)} 行 · {len(cols)} 列</h1>
<div class="grid">{cards}</div></body></html>"""
    open(os.path.join(args.out, "index.html"), "w", encoding="utf-8").write(html)
    json.dump(summary, open(os.path.join(args.out, "summary.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"✅ 生成 {len(charts)} 张图 + index.html，输出目录 {args.out}")


if __name__ == "__main__":
    main()
