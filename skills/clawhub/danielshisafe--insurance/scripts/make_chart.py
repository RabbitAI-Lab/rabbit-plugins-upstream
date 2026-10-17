#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_chart.py —— 保险计划书分析大师·理财类双轴折线图生成器（零依赖，纯 SVG）

输入：scripts/irr.py 产出的 CSV（一个或多个），输出自包含 SVG（双 Y 轴）。
  - 横坐标：持有年度（保单年度，非被保人年龄）
  - 左纵坐标：总利益（元）
  - 右纵坐标：XIRR（%）
  - 多产品：不同颜色区分；同一产品内「总利益」用实线、「IRR」用虚线。

用法：
  python make_chart.py --input irr_A.csv --out chart.svg
  python make_chart.py --input irr_A.csv irr_B.csv --names A B --out chart.svg
  python make_chart.py --input irr_A.csv --out chart.svg --mode both   # 同时画保证+演示

说明：
  - 默认 --mode demo（画演示口径的总利益与 IRR）；guaranteed 只画保证；both 两者都画。
  - CSV 首列为「持有年度」，其余列名为「总利益(保证) / XIRR(保证)% / 总利益(演示) / XIRR(演示)%」。
  - IRR 为 NA（早期无符号变化）的年度自动跳过，折线断开。
"""
import argparse
import csv
import sys

W, H = 960, 560
ML, MR, MT, MB = 78, 78, 64, 56          # 边距（左留给总利益，右留给 IRR）
PALETTE = ["#2563eb", "#dc2626", "#16a34a", "#d97706",
           "#7c3aed", "#0891b2", "#db2777", "#65a30d"]


def find_col(header, *keys):
    for i, h in enumerate(header):
        if all(k in h for k in keys):
            return i
    return None


def load(path):
    with open(path, encoding="utf-8-sig") as f:
        data = list(csv.reader(f))
    if not data:
        return None
    header = data[0]
    out = {"years": [], "total_g": [], "irr_g": [], "total_d": [], "irr_d": []}
    ig = find_col(header, "总利益", "保证")
    idg = find_col(header, "XIRR", "保证")
    idd = find_col(header, "总利益", "演示")
    iddr = find_col(header, "XIRR", "演示")
    for row in data[1:]:
        if not row:
            continue
        try:
            y = int(float(row[0]))
        except ValueError:
            continue
        out["years"].append(y)

        def get(i):
            if i is None or i >= len(row):
                return None
            v = row[i].strip()
            if v == "" or v.upper() == "NA":
                return None
            try:
                return float(v)
            except ValueError:
                return None

        out["total_g"].append(get(ig))
        out["irr_g"].append(get(idg))
        out["total_d"].append(get(idd))
        out["irr_d"].append(get(iddr))
    return out


def scale(v, lo, hi, a, b):
    if hi == lo:
        return (a + b) / 2
    return a + (v - lo) / (hi - lo) * (b - a)


def fmt_money(v):
    if abs(v) >= 1e8:
        return f"{v/1e8:.1f}亿"
    if abs(v) >= 1e4:
        return f"{v/1e4:.0f}万"
    return f"{v:.0f}"


def main():
    ap = argparse.ArgumentParser(description="理财类双轴折线图（总利益 + IRR）")
    ap.add_argument("--input", nargs="+", required=True, help="irr.py 产出的 CSV（可多个）")
    ap.add_argument("--names", nargs="+", help="各 CSV 对应产品名（不填用文件名）")
    ap.add_argument("--out", required=True, help="输出 SVG 路径")
    ap.add_argument("--mode", default="demo",
                    choices=["demo", "guaranteed", "both"],
                    help="画演示/保证/两者")
    args = ap.parse_args()

    series = []
    for idx, p in enumerate(args.input):
        d = load(p)
        if not d or not d["years"]:
            sys.stderr.write(f"跳过无效/空 CSV: {p}\n")
            continue
        name = (args.names[idx] if args.names and idx < len(args.names)
                else p.split("/")[-1].rsplit(".", 1)[0])
        series.append((name, d))

    if not series:
        sys.stderr.write("没有可用数据，退出。\n")
        sys.exit(1)

    # 坐标范围
    all_years = sorted({y for _, d in series for y in d["years"]})
    x_min, x_max = min(all_years), max(all_years)

    total_vals, irr_vals = [], []
    for _, d in series:
        for key in ("total_g", "total_d"):
            total_vals += [v for v in d[key] if v is not None]
        for key in ("irr_g", "irr_d"):
            irr_vals += [v for v in d[key] if v is not None]
    t_max = max(total_vals) if total_vals else 1
    t_min = min(0, min(total_vals)) if total_vals else 0
    i_max = max(irr_vals) if irr_vals else 1
    i_min = min(0, min(irr_vals)) if irr_vals else 0
    # 留白
    t_max *= 1.08
    i_span = (i_max - i_min) or 1
    i_min -= i_span * 0.08
    i_max += i_span * 0.08

    px0, px1 = ML, W - MR
    py0, py1 = H - MB, MT            # py0 底部, py1 顶部

    def X(y):
        return scale(y, x_min, x_max, px0, px1)

    def YL(v):
        return scale(v, t_min, t_max, py0, py1)

    def YR(v):
        return scale(v, i_min, i_max, py0, py1)

    parts = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" font-family="-apple-system,Segoe UI,Microsoft YaHei,sans-serif">')
    parts.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
    # 标题
    title = "理财类产品 · 总利益与 IRR 走势（横坐标=持有年度）"
    parts.append(f'<text x="{W/2}" y="26" text-anchor="middle" font-size="16" '
                 f'font-weight="700" fill="#111827">{title}</text>')

    # 网格 + 左轴刻度（总利益）
    for k in range(6):
        v = t_min + (t_max - t_min) * k / 5
        y = YL(v)
        parts.append(f'<line x1="{px0}" y1="{y:.1f}" x2="{px1}" y2="{y:.1f}" '
                     f'stroke="#e5e7eb" stroke-width="1"/>')
        parts.append(f'<text x="{px0-8}" y="{y+4:.1f}" text-anchor="end" '
                     f'font-size="11" fill="#374151">{fmt_money(v)}</text>')
    # 右轴刻度（IRR）
    for k in range(6):
        v = i_min + (i_max - i_min) * k / 5
        y = YR(v)
        parts.append(f'<text x="{px1+8}" y="{y+4:.1f}" text-anchor="start" '
                     f'font-size="11" fill="#6b7280">{v:.1f}%</text>')
    # X 轴刻度
    xticks = min(8, len(all_years))
    for k in range(xticks):
        yv = all_years[int(k * (len(all_years) - 1) / max(1, xticks - 1))]
        x = X(yv)
        parts.append(f'<line x1="{x:.1f}" y1="{py0}" x2="{x:.1f}" y2="{py1}" '
                     f'stroke="#f3f4f6" stroke-width="1"/>')
        parts.append(f'<text x="{x:.1f}" y="{py0+18}" text-anchor="middle" '
                     f'font-size="11" fill="#374151">{yv}年</text>')
    # 轴线
    parts.append(f'<line x1="{px0}" y1="{py1}" x2="{px0}" y2="{py0}" stroke="#9ca3af" stroke-width="1.5"/>')
    parts.append(f'<line x1="{px1}" y1="{py1}" x2="{px1}" y2="{py0}" stroke="#9ca3af" stroke-width="1.5"/>')
    parts.append(f'<line x1="{px0}" y1="{py0}" x2="{px1}" y2="{py0}" stroke="#9ca3af" stroke-width="1.5"/>')
    # 轴标题
    parts.append(f'<text x="{px0-58}" y="{MT-14}" font-size="11" fill="#374151">总利益(元)</text>')
    parts.append(f'<text x="{px1+8}" y="{MT-14}" font-size="11" fill="#6b7280">IRR(%)</text>')
    # IRR=0 基准线
    if i_min < 0 < i_max:
        yz = YR(0)
        parts.append(f'<line x1="{px0}" y1="{yz:.1f}" x2="{px1}" y2="{yz:.1f}" '
                     f'stroke="#fca5a5" stroke-width="1" stroke-dasharray="3 3"/>')

    # 画折线
    def poly(pts):
        return " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)

    legend = []
    for si, (name, d) in enumerate(series):
        color = PALETTE[si % len(PALETTE)]
        yr = d["years"]
        # 总利益
        if args.mode in ("demo", "both"):
            pts = [(X(yr[i]), YL(d["total_d"][i])) for i in range(len(yr))
                   if d["total_d"][i] is not None]
            if pts:
                parts.append(f'<polyline points="{poly(pts)}" fill="none" '
                             f'stroke="{color}" stroke-width="2.5"/>')
        if args.mode in ("guaranteed", "both"):
            pts = [(X(yr[i]), YL(d["total_g"][i])) for i in range(len(yr))
                   if d["total_g"][i] is not None]
            if pts:
                parts.append(f'<polyline points="{poly(pts)}" fill="none" '
                             f'stroke="{color}" stroke-width="2" stroke-dasharray="1 0" opacity="0.75"/>')
        # IRR（虚线）
        if args.mode in ("demo", "both"):
            pts = [(X(yr[i]), YR(d["irr_d"][i])) for i in range(len(yr))
                   if d["irr_d"][i] is not None]
            if pts:
                parts.append(f'<polyline points="{poly(pts)}" fill="none" '
                             f'stroke="{color}" stroke-width="2" stroke-dasharray="6 4"/>')
        if args.mode in ("guaranteed", "both"):
            pts = [(X(yr[i]), YR(d["irr_g"][i])) for i in range(len(yr))
                   if d["irr_g"][i] is not None]
            if pts:
                parts.append(f'<polyline points="{poly(pts)}" fill="none" '
                             f'stroke="{color}" stroke-width="1.6" stroke-dasharray="6 4" opacity="0.7"/>')
        legend.append((color, name))

    # 图例
    lx = px0 + 6
    ly = py1 + 4
    for color, name in legend:
        parts.append(f'<rect x="{lx}" y="{ly-9}" width="14" height="4" fill="{color}"/>')
        parts.append(f'<line x1="{lx}" y1="{ly-7}" x2="{lx+14}" y2="{ly-7}" '
                     f'stroke="{color}" stroke-width="2"/>')
        parts.append(f'<text x="{lx+20}" y="{ly-3}" font-size="11" fill="#111827">{name} '
                     f'(实线=总利益 虚线=IRR)</text>')
        lx += 40 + len(name) * 13
        if lx > px1 - 120:
            lx = px0 + 6
            ly += 16

    parts.append('</svg>')

    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"已生成图表: {args.out}（{len(series)} 款产品, 模式={args.mode}）")


if __name__ == "__main__":
    try:
        from _feedback_hook import install; install()
    except Exception:
        pass
    main()
