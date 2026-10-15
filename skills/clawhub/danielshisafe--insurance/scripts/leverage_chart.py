#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
leverage_chart.py —— 杠杆寿（定额终身寿）杠杆率走势图（零依赖，纯 SVG）

★ 为什么不用 make_chart.py：那个是理财类"总利益 + IRR"双轴图，输入是 irr.py 的 CSV，
  与杠杆寿的数据结构（累计保费 / 身故赔付 / 杠杆率）不同，硬塞进去会破坏它的输入协议。

单品模式（默认）：
  横坐标：保单年度
  左纵坐标（金额，元）：累计已交保费 · 一般身故赔付 · 基本保额（水平参考线）
  右纵坐标（倍数）：杠杆率 = 一般身故赔付 ÷ 累计已交保费

  ★ 保额放左轴而不是右轴：保额本质是金额，与累计保费同量纲；
    若与杠杆率（1~40 倍）共用右轴，二者量级差 4 个数量级，必有一条被压成直线。
  ★ 画"身故赔付"而非只画"保额"：身故赔付含无条件附加（关爱金），
    能直观看出附加责任到期时的**断崖式跳变**（实测德华安顾 71 岁由 150 万掉到 100 万）。

多品模式（--mode compare）：
  横坐标：保单年度
  纵坐标（倍数）：每款一条杠杆率曲线（金额线在多品下会互相干扰，故不画）

用法：
  python leverage_chart.py --extract A.json --out lev_A.svg
  python leverage_chart.py --policy p.json --out lev.svg
  python leverage_chart.py --extract A.json B.json --policy p.json --mode compare --out cmp.svg
  python leverage_chart.py --extract A.json --out lev.svg --annotate 1,20,41
"""
import argparse
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import classify_life as CL  # noqa: E402

W, H = 980, 580
ML, MR, MT, MB = 92, 86, 74, 62
PALETTE = ["#2563eb", "#dc2626", "#16a34a", "#d97706",
           "#7c3aed", "#0891b2", "#db2777", "#65a30d"]

C_PREM = "#2563eb"      # 累计保费
C_DEATH = "#dc2626"     # 身故赔付
C_SA = "#9ca3af"        # 基本保额参考线
C_LEV = "#059669"       # 杠杆率


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


def build(src, sum_assured=None, is_policy=False):
    """复用 classify_life 的抽取/判定，取出画图所需的逐年序列。"""
    r, err = CL.analyze(src, sum_assured)
    if err:
        return None, err
    prems = list(r["prems"])
    n = r["n"]
    cum, acc = [], 0.0
    for p in prems:
        acc += p
        cum.append(acc)
    d_all = list(r["d_all"])
    sa = r["lev"].get("sum_assured") or (d_all[0] if d_all else 0)
    lev = []
    for i in range(n):
        c = cum[i] if i < len(cum) else 0
        d = d_all[i] if i < len(d_all) else 0
        lev.append(d / c if c > 0 and d > 0 else None)
    # 身故赔付出现显著下降的年度 = 附加责任到期（关爱金归零）
    drop_year = None
    for i in range(1, n):
        if d_all[i - 1] > 0 and d_all[i] > 0 and d_all[i] < d_all[i - 1] * 0.9:
            drop_year = i + 1
            break
    # ★ 最后一个「还在变化」的年度：累计保费与身故赔付都恒定之后，
    #   杠杆率必然也恒定，再往下画就是一条直线，纯占画布。
    #   实测德华安顾：第 41 年（71 岁）关爱金到期后恒定 → 截断到第 44 年（74 岁），
    #   与「75 岁之后没必要展示」的直觉一致。
    last_chg = 1
    for i in range(1, n):
        c0 = cum[i - 1] if i - 1 < len(cum) else 0
        c1 = cum[i] if i < len(cum) else 0
        d0 = d_all[i - 1] if i - 1 < len(d_all) else 0
        d1 = d_all[i] if i < len(d_all) else 0
        if abs(c1 - c0) > 1e-6 or abs(d1 - d0) > 1e-6:
            last_chg = i + 1
    ages = [int(a) for a in (r.get("ages") or [])]
    # ★ 演示表常只给抽样年度（实测德华安顾只给 1–15、25、35、45、55、65、70），
    #   横轴必须用真实年度，否则曲线按「数据点序号」铺开，年度与年龄会全错位。
    yrs = [int(v) for v in (r.get("years") or [])]
    if len(yrs) != n:
        yrs = list(range(1, n + 1))

    def to_year(idx1):
        """索引(1-based) → 真实年度（抽样年度表必须转换）。"""
        if idx1 and 0 < idx1 <= len(yrs):
            return yrs[idx1 - 1]
        return idx1

    return {
        "name": r["name"], "n": n, "years": yrs,
        "cum": cum, "d_all": d_all, "sa": sa, "lev": lev,
        "annual_prem": (cum[0] if cum else 0),
        "pay_years": r["lev"].get("pay_years", 0),
        "drop_year": to_year(drop_year), "ages": ages,
        "last_chg": to_year(last_chg),
        "entry_age": r.get("entry_age"),
        "shape": r["shape"],
    }, None


def polyline(xs, ys, color, width=2.2, dash=None):
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in zip(xs, ys))
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<polyline points="{pts}" fill="none" stroke="{color}" '
            f'stroke-width="{width}" stroke-linejoin="round" '
            f'stroke-linecap="round"{d}/>')


def head(title, sub):
    p = []
    p.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
             f'viewBox="0 0 {W} {H}" '
             f'font-family="-apple-system,Segoe UI,Microsoft YaHei,sans-serif">')
    p.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
    p.append(f'<text x="{W/2}" y="28" text-anchor="middle" font-size="16.5" '
             f'font-weight="700" fill="#111827">{title}</text>')
    p.append(f'<text x="{W/2}" y="48" text-anchor="middle" font-size="12" '
             f'fill="#6b7280">{sub}</text>')
    return p


def text_w(s, fs=11.5):
    """中文按全角、西文按 0.55 倍估算宽度——图例换行定位用，估窄了会重叠。"""
    return sum(fs if ord(ch) > 0x2E80 else fs * 0.55 for ch in s)


def legend(px0, py1, items, max_x=None):
    """items: [(颜色, 文本, 是否虚线)]；超出 max_x 自动换行。"""
    p = []
    x, y = px0, py1 - 14
    limit = max_x or (W - 12)
    for color, text, dashed in items:
        w = 34 + text_w(text)
        if x + w > limit:                      # 换行
            x, y = px0, y + 18
        d = ' stroke-dasharray="5,3"' if dashed else ""
        p.append(f'<line x1="{x}" y1="{y:.1f}" x2="{x+22}" y2="{y:.1f}" '
                 f'stroke="{color}" stroke-width="2.6"{d}/>')
        p.append(f'<text x="{x+28}" y="{y+4:.1f}" font-size="11.5" '
                 f'fill="#374151">{text}</text>')
        x += w
    return p


def log_ticks(lo, hi):
    """对数轴刻度：1, 2, 5, 10, 20, 50, 100 …"""
    out = []
    e = 0
    while e <= 6:
        for m in (1, 2, 5):
            v = m * (10 ** e)
            if lo <= v <= hi:
                out.append(v)
        if 10 ** e > hi:
            break
        e += 1
    return out


def axes(px0, px1, py0, py1, x_min, x_max, left_ticks, right_ticks,
         left_title, right_title, x_title, show_left=True, truncated=False):
    """left_ticks / right_ticks: [(y 像素, 标签文本)]。

    ★ 左右轴刻度各自独立计算——线性时两者恰好对齐（都从 0 起），
      对数时不对齐，这在双轴图里是正常的；右轴标签旁画小 tick 线帮助定位。
    """
    p = []
    for y, lab in left_ticks:
        p.append(f'<line x1="{px0}" y1="{y:.1f}" x2="{px1}" y2="{y:.1f}" '
                 f'stroke="#eef1f5" stroke-width="1"/>')
        if show_left:
            p.append(f'<text x="{px0-9}" y="{y+4:.1f}" text-anchor="end" '
                     f'font-size="11" fill="#374151">{lab}</text>')
    for y, lab in right_ticks:
        p.append(f'<line x1="{px1}" y1="{y:.1f}" x2="{px1+4}" y2="{y:.1f}" '
                 f'stroke="{C_LEV}" stroke-width="1.2"/>')
        p.append(f'<text x="{px1+9}" y="{y+4:.1f}" text-anchor="start" '
                 f'font-size="11" fill="{C_LEV}">{lab}</text>')
    # 轴标题
    if show_left and left_title:
        p.append(f'<text x="{px0-9}" y="{py1-12}" text-anchor="end" font-size="11.5" '
                 f'font-weight="600" fill="#374151">{left_title}</text>')
    p.append(f'<text x="{px1+9}" y="{py1-12}" text-anchor="start" font-size="11.5" '
             f'font-weight="600" fill="{C_LEV}">{right_title}</text>')
    # 边框
    p.append(f'<line x1="{px0}" y1="{py0}" x2="{px1}" y2="{py0}" '
             f'stroke="#d1d5db" stroke-width="1.2"/>')
    p.append(f'<line x1="{px0}" y1="{py0}" x2="{px0}" y2="{py1}" '
             f'stroke="#d1d5db" stroke-width="1.2"/>')
    p.append(f'<line x1="{px1}" y1="{py0}" x2="{px1}" y2="{py1}" '
             f'stroke="#d1d5db" stroke-width="1.2"/>')
    # X 轴刻度
    step = max(1, round((x_max - x_min) / 10))
    y = x_max
    while y >= x_min:
        x = scale(y, x_min, x_max, px0, px1)
        p.append(f'<line x1="{x:.1f}" y1="{py0}" x2="{x:.1f}" y2="{py0+5}" '
                 f'stroke="#9ca3af" stroke-width="1"/>')
        p.append(f'<text x="{x:.1f}" y="{py0+20}" text-anchor="middle" '
                 f'font-size="11" fill="#6b7280">{y}</text>')
        y -= step
    p.append(f'<text x="{(px0+px1)/2}" y="{py0+42}" text-anchor="middle" '
             f'font-size="11.5" fill="#6b7280">{x_title}</text>')
    # ★ 截断符号：轴末端两条斜线，提示「后面还有，但已经恒定不变」
    if truncated:
        for dx in (-1, 6):
            p.append(f'<line x1="{px1-4+dx:.1f}" y1="{py0+7}" '
                     f'x2="{px1+4+dx:.1f}" y2="{py0-5}" '
                     f'stroke="#6b7280" stroke-width="1.6"/>')
    return p


def draw_single(d, out, annotate, use_log=False, tail=3, xmax=None):
    px0, px1 = ML, W - MR
    py0, py1 = H - MB, MT + 34
    n = d["n"]
    # ★ 抽样年度表（1–15、25、35…）里「数据点数 n」≠「真实年度上限」，
    #   截断与「是否截断」必须按真实年度算，否则会截错位置。
    y_full = max(d["years"]) if d["years"] else n
    x_min = 1
    # ★ 横轴截断：只画到「最后一个还在变化的年度 + tail 年」，
    #   之后累计保费与身故赔付都恒定，杠杆率是一条直线，画了纯占画布。
    x_max = int(xmax) if xmax else min(y_full, d["last_chg"] + tail)
    x_max = max(2, min(y_full, x_max))
    truncated = x_max < y_full

    l_max = max([max(d["cum"]), max(d["d_all"]), d["sa"]] or [1]) * 1.10
    l_min = 0.0
    lev_vals = [v for v in d["lev"] if v is not None]
    if use_log:
        # 对数轴取到 10 的整数次幂，避免出现 1.3x 这种怪刻度
        lo = min(lev_vals) if lev_vals else 1
        hi = max(lev_vals) if lev_vals else 10
        r_min = 10 ** math.floor(math.log10(max(lo, 1e-6)))
        r_max = 10 ** math.ceil(math.log10(max(hi, r_min * 10)))
    else:
        r_max = (max(lev_vals) if lev_vals else 1) * 1.10
        r_min = 0.0

    def X(v):
        return scale(v, x_min, x_max, px0, px1)

    def YL(v):
        return scale(v, l_min, l_max, py0, py1)

    def YR(v):
        if use_log:
            return scale(math.log10(max(v, 1e-6)), math.log10(r_min),
                         math.log10(r_max), py0, py1)
        return scale(v, r_min, r_max, py0, py1)

    left_ticks = [(YL(l_min + (l_max - l_min) * k / 5),
                   fmt_money(l_min + (l_max - l_min) * k / 5))
                  for k in range(6)]
    if use_log:
        right_ticks = [(YR(v), f"{v:g}x") for v in log_ticks(r_min, r_max)]
    else:
        right_ticks = [(YR(r_min + (r_max - r_min) * k / 5),
                        f"{r_min + (r_max - r_min) * k / 5:.1f}x")
                       for k in range(6)]

    title = f"杠杆率走势 · {d['name'][:34]}"
    sub = ("左轴=金额（累计保费 / 一般身故赔付 / 基本保额）　"
           "右轴=杠杆率（一般身故赔付 ÷ 累计已交保费"
           + ("，对数刻度）" if use_log else "）")
           + "　横轴=保单年度")
    p = head(title, sub)
    p += axes(px0, px1, py0, py1, x_min, x_max, left_ticks, right_ticks,
              "金额（元）", "杠杆率（倍）",
              "保单年度" + (f"　※ 第 {x_max} 年后各指标恒定，已截断"
                            f"（实际保障至第 {y_full} 年）" if truncated else ""),
              truncated=truncated)

    # 只画 x_max 以内的真实数据点（抽样年度表不插值、不补点）
    m = sum(1 for y in d["years"] if y <= x_max)
    xs = [X(y) for y in d["years"][:m]]
    # 基本保额水平参考线
    ysa = YL(d["sa"])
    p.append(f'<line x1="{px0}" y1="{ysa:.1f}" x2="{px1}" y2="{ysa:.1f}" '
             f'stroke="{C_SA}" stroke-width="1.8" stroke-dasharray="6,4"/>')
    p.append(f'<text x="{px1-4}" y="{ysa-6:.1f}" text-anchor="end" font-size="10.5" '
             f'fill="{C_SA}">基本保额 {fmt_money(d["sa"])}</text>')
    # 累计保费
    p.append(polyline(xs, [YL(v) for v in d["cum"][:m]], C_PREM, 2.4))
    # 身故赔付
    p.append(polyline(xs, [YL(v) for v in d["d_all"][:m]], C_DEATH, 2.4))
    # 杠杆率（右轴）
    lv = [(X(y), YR(v)) for y, v in zip(d["years"][:m], d["lev"][:m])
          if v is not None]
    if lv:
        p.append(polyline([a for a, _ in lv], [b for _, b in lv],
                          C_LEV, 2.4, dash="7,4"))

    # 关键年度标注
    marks = []
    if annotate:
        marks = [a for a in annotate if 1 <= a <= x_max]
    else:
        marks = sorted({1, d["pay_years"], d["drop_year"], x_max} -
                       {None, 0})
    for y in marks:
        # ★ 抽样年度表：年度 y 对应的不是索引 y-1，要取「不超过 y 的最后一个数据点」
        _idxs = [k for k, yy in enumerate(d["years"]) if yy <= y]
        if not _idxs:
            continue
        i = _idxs[-1]
        y = d["years"][i]
        x = X(y)
        p.append(f'<line x1="{x:.1f}" y1="{py1}" x2="{x:.1f}" y2="{py0}" '
                 f'stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3,4"/>')
        lv_v = d["lev"][i]
        if lv_v is not None:
            yy = YR(lv_v)
            p.append(f'<circle cx="{x:.1f}" cy="{yy:.1f}" r="3.6" '
                     f'fill="#fff" stroke="{C_LEV}" stroke-width="2"/>')
            p.append(f'<text x="{x+6:.1f}" y="{yy-7:.1f}" font-size="10.5" '
                     f'font-weight="600" fill="{C_LEV}">第{y}年 {lv_v:.1f}x</text>')
        dd = d["d_all"][i]
        if dd:
            yd = YL(dd)
            p.append(f'<circle cx="{x:.1f}" cy="{yd:.1f}" r="3.6" '
                     f'fill="#fff" stroke="{C_DEATH}" stroke-width="2"/>')

    # 附加责任到期断崖提示
    if d["drop_year"] and d["drop_year"] <= x_max:
        _idxs = [k for k, yy in enumerate(d["years"]) if yy <= d["drop_year"]]
        i = _idxs[-1] if _idxs else 0
        x = X(d["drop_year"])
        yd = YL(d["d_all"][i])
        p.append(f'<circle cx="{x:.1f}" cy="{yd:.1f}" r="5" fill="none" '
                 f'stroke="{C_DEATH}" stroke-width="1.4" opacity="0.75"/>')
        p.append(f'<text x="{x+8:.1f}" y="{yd+16:.1f}" font-size="10.5" '
                 f'fill="{C_DEATH}">附加责任到期（{fmt_money(d["d_all"][i-1])}'
                 f'→{fmt_money(d["d_all"][i])}）</text>')

    p += legend(px0, py1 - 16, [
        (C_PREM, "累计已交保费（左轴）", False),
        (C_DEATH, "一般身故赔付（左轴）", False),
        (C_SA, "基本保额（左轴，水平参考）", True),
        (C_LEV, "杠杆率（右轴）", True),
    ])
    p.append("</svg>")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(p))
    return out


def draw_compare(ds, out, annotate, use_log=False, tail=3, xmax=None):
    px0, px1 = ML, W - MR
    py0, py1 = H - MB, MT + 34
    x_min = 1
    # ★ 抽样年度表：真实年度上限 ≠ 数据点数，取各款 years 的最大值
    n_full = max([max(d["years"]) if d["years"] else d["n"] for d in ds] or [1])
    # ★ 多品取「各款稳定年的最大值」再留 tail 年，保证每款的断崖都在图内
    x_max = int(xmax) if xmax else min(n_full, max(d["last_chg"] for d in ds) + tail)
    x_max = max(2, min(n_full, x_max))
    truncated = x_max < n_full
    lev_all = [v for d in ds for y, v in zip(d["years"], d["lev"])
               if v is not None and y <= x_max]
    if use_log:
        lo = min(lev_all) if lev_all else 1
        hi = max(lev_all) if lev_all else 10
        r_min = 10 ** math.floor(math.log10(max(lo, 1e-6)))
        r_max = 10 ** math.ceil(math.log10(max(hi, r_min * 10)))
    else:
        r_max = (max(lev_all) if lev_all else 1) * 1.10
        r_min = 0.0

    def X(v):
        return scale(v, x_min, x_max, px0, px1)

    def YR(v):
        if use_log:
            return scale(math.log10(max(v, 1e-6)), math.log10(r_min),
                         math.log10(r_max), py0, py1)
        return scale(v, r_min, r_max, py0, py1)

    if use_log:
        left_ticks = [(YR(v), f"{v:g}x") for v in log_ticks(r_min, r_max)]
    else:
        left_ticks = [(YR(r_min + (r_max - r_min) * k / 5),
                       f"{r_min + (r_max - r_min) * k / 5:.1f}x")
                      for k in range(6)]
    right_ticks = left_ticks

    title = f"杠杆率走势对比（{len(ds)} 款 · 均为定额终身寿）"
    sub = ("纵轴=杠杆率（一般身故赔付 ÷ 累计已交保费，倍"
           + ("，对数刻度）" if use_log else "）")
           + "　横轴=保单年度　"
           "★ 杠杆随缴费推进自然衰减，缴费结束后趋于平稳")
    p = head(title, sub)
    p += axes(px0, px1, py0, py1, x_min, x_max, left_ticks, right_ticks,
              "", "杠杆率（倍）",
              "保单年度" + (f"　※ 第 {x_max} 年后各款均恒定，已截断"
                            f"（实际保障至第 {n_full} 年）" if truncated else ""),
              show_left=False, truncated=truncated)

    items = []
    for i, d in enumerate(ds):
        color = PALETTE[i % len(PALETTE)]
        m = sum(1 for y in d["years"] if y <= x_max)
        lv = [(X(y), YR(v)) for y, v in zip(d["years"][:m], d["lev"][:m])
              if v is not None]
        if not lv:
            continue
        p.append(polyline([a for a, _ in lv], [b for _, b in lv], color, 2.4))
        # 末端标签（取截断区间的末值，不是全期末值）
        lx, ly = lv[-1]
        p.append(f'<text x="{lx-6:.1f}" y="{ly-8:.1f}" text-anchor="end" '
                 f'font-size="11" font-weight="600" fill="{color}">'
                 f'#{i+1} {d["lev"][m-1]:.2f}x</text>')
        items.append((color, f"#{i+1} {d['name'][:18]}（年交 "
                             f"{fmt_money(d['annual_prem'])}）", False))

    # 缴费期末竖线（各款不同则标第一款）
    py = ds[0]["pay_years"]
    if py and 1 <= py <= x_max:
        x = X(py)
        p.append(f'<line x1="{x:.1f}" y1="{py1}" x2="{x:.1f}" y2="{py0}" '
                 f'stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4,4"/>')
        p.append(f'<text x="{x+5:.1f}" y="{py1+14}" font-size="10.5" '
                 f'fill="#64748b">缴费结束（第 {py} 年）</text>')

    p += legend(px0, py1 - 16, items)
    p.append("</svg>")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(p))
    return out


def main():
    ap = argparse.ArgumentParser(description="杠杆寿杠杆率走势图（零依赖纯 SVG）")
    ap.add_argument("--extract", nargs="*", help="extract.py 产出的 JSON（可多个）")
    ap.add_argument("--policy", nargs="*", help="手工 policy JSON（可多个）")
    ap.add_argument("--sum-assured", type=float, help="手工指定基本保额")
    ap.add_argument("--mode", default="single", choices=["single", "compare"])
    ap.add_argument("--log", action="store_true",
                    help="杠杆率轴用对数刻度（★ 杠杆率是 1/x 衰减，线性轴下后期会挤在底部）")
    ap.add_argument("--tail", type=int, default=3,
                    help="横轴截断时在「最后一个变化年」之后再留几年（默认 3）")
    ap.add_argument("--xmax", type=int,
                    help="手动指定横轴最大保单年度（不填则自动截断）")
    ap.add_argument("--annotate", help="标注的保单年度，逗号分隔（默认自动选关键点）")
    ap.add_argument("--out", required=True, help="输出 SVG 路径（多款且 single 时自动加序号）")
    a = ap.parse_args()

    srcs = [(p, False) for p in (a.extract or [])] + \
           [(p, True) for p in (a.policy or [])]
    if not srcs:
        ap.print_help()
        return 1

    anno = None
    if a.annotate:
        anno = [int(x) for x in a.annotate.split(",") if x.strip().isdigit()]

    ds = []
    for p, _ in srcs:
        if not os.path.exists(p):
            sys.stderr.write(f"[错误] 文件不存在：{p}\n")
            continue
        d, err = build(p, a.sum_assured)
        if err:
            sys.stderr.write(err + "\n")
            continue
        ds.append(d)

    if not ds:
        sys.stderr.write("没有可用数据，退出。\n")
        return 1

    kw = dict(tail=a.tail, xmax=a.xmax)
    if a.mode == "compare":
        out = draw_compare(ds, a.out, anno, a.log, **kw)
        print(f"已生成：{out}")
    elif len(ds) == 1:
        out = draw_single(ds[0], a.out, anno, a.log, **kw)
        print(f"已生成：{out}")
    else:
        # 多款 + single：逐个出图，文件名自动加序号
        base, ext = os.path.splitext(a.out)
        for i, d in enumerate(ds, 1):
            out = draw_single(d, f"{base}_{i}{ext}", anno, a.log, **kw)
            print(f"已生成：{out}　（#{i} {d['name'][:24]}）")
    for d in ds:
        # ★ 抽样年度表：全期是 years 的最大值，不是数据点数 n
        yfull = max(d["years"]) if d["years"] else d["n"]
        print(f"  · {d['name'][:26]}：最后变化年 第 {d['last_chg']} 年"
              f"（{d['entry_age'] + d['last_chg'] if d['entry_age'] else '?'} 岁），"
              f"全期 {yfull} 年（表中 {d['n']} 个数据点）")
    return 0


if __name__ == "__main__":
    main()
