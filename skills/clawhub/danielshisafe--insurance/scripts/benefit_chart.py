#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
benefit_chart.py —— 健康险（重疾 / 医疗 / 意外 / 定寿）**保障额度走势图**（零依赖纯 SVG）

★ 为什么需要它（SKILL §10.3）
  健康险真正随年龄变化的是**保障额度**，不是现金价值。典型情形：
  · 身故责任「61 岁前赔保额、61 岁后只赔已交保费/现价」→ **断崖**
  · 重疾/身故按「max(保额, 现价, 已交保费)」给付 → **后期随现价抬高**
  · 附加责任「18~70 周岁」有效 → **到期归零**
  这些用表格看不出来，必须画图。

★ 与另两个图表脚本的区别（三个脚本，别混用）
  · make_chart.py    → 理财类「总利益 + IRR」双轴图，输入 irr.py 的 CSV
  · leverage_chart.py→ 杠杆寿「杠杆率」图，输入 classify_life 的 extract/policy
  · benefit_chart.py → 健康险「保障额度」图，输入手工 policy 的 benefits 字典

用法：
  # compare（默认）：一个责任一张图，每款产品一条线
  python benefit_chart.py --policy A.json B.json C.json D.json --out 保障走势.svg
  # 只画指定责任
  python benefit_chart.py --policy *.json --benefits 身故/全残,重大疾病 --out b.svg
  # single：一款产品一张图，每个责任一条线
  python benefit_chart.py --policy A.json --mode single --out A_保障.svg
  # 横轴用年龄而非保单年度
  python benefit_chart.py --policy *.json --x-age --out b.svg
  # ★ 推荐：重/中/轻症叠成一张「疾病保障走势图」，再单独出一张身故图（共两张，不要出四张）
  python benefit_chart.py --policy *.json --combine 重大疾病,中症,轻症 --out 疾病保障.svg
  python benefit_chart.py --policy *.json --benefits 身故/全残 --out 身故保障.svg

policy JSON 字段：
{
  "name": "太保真爱3号·无身故",
  "insured": "女 35 岁",
  "entry_age": 35,
  "years": [1, 2, ..., 70],
  "ages":   [36, 37, ..., 105],
  "benefits": {
    "身故/全残": [0, 0, ...],        // 没有该责任就写全 0（会画在 0 线上，一眼看出缺口）
    "重大疾病": [500000, ...],
    "中症":     [300000, ...],
    "轻症":     [150000, ...]
  }
}
★ benefits 的值也可以只写一个数（常数责任），脚本自动铺满全期，
  例如 "重大疾病": 500000 —— 省得手写 70 遍还容易数错。
"""

import argparse
import io
import json
import os
import re
import sys

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

W, H = 980, 560
ML, MR, MT, MB = 92, 172, 74, 68

COLORS = ["#1f6feb", "#1a7f37", "#d97706", "#b42318",
          "#7c3aed", "#0891b2", "#be185d", "#65a30d"]
BAD_CHARS = re.compile(r'[\\/:*?"<>|\s]+')


def esc(s):
    return (str(s or "").replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;"))


def text_w(s, size=11.5):
    """估算文本宽度：CJK 记全宽，其余约 0.55 倍（图例换行要用）。"""
    w = 0.0
    for ch in str(s or ""):
        w += size if ord(ch) > 0x2E80 else size * 0.55
    return w


def safe_name(s):
    return BAD_CHARS.sub("_", str(s or "")).strip("_") or "benefit"


def load(path):
    with io.open(path, encoding="utf-8") as f:
        d = json.load(f)
    years = [int(v) for v in (d.get("years") or [])]
    ages = [int(v) for v in (d.get("ages") or [])]
    ent = d.get("entry_age")
    raw = d.get("benefits") or {}
    n = max([len(years)] + [len(v) if isinstance(v, list) else 0
                            for v in raw.values()] or [0])
    if not years:
        years = list(range(1, n + 1))
    if not ages:
        ages = [(ent + y) if ent is not None else 0 for y in years]
    benefits = {}
    for k, v in raw.items():
        if isinstance(v, list):
            vals = [float(x) if isinstance(x, (int, float)) else 0.0 for x in v]
            vals += [0.0] * (len(years) - len(vals))
        else:                       # 常数责任：只写一个数，自动铺满
            vals = [float(v or 0)] * len(years)
        benefits[k] = vals[:len(years)]
    return {"name": d.get("name") or os.path.basename(path),
            "insured": d.get("insured", ""),
            "years": years, "ages": ages, "benefits": benefits}


def draw_multi(title, subtitle, panels, xs, xlabel, out_path, annotate=True):
    """★ 多格合一：一个 SVG 里纵向堆叠若干格（如 重疾 / 中症 / 轻症），共用同一 X 轴。

    使用人要求「重疾、轻症、中症的走势可以在同一张图里，不需要做那么多图」——
    于是重/中/轻三格叠成一张「疾病保障走势图」，再配一张「身故保障走势图」，共两张。

    ★ 各格**共用同一个 Y 轴刻度**（取整图最大值），这样 50 万 / 30 万 / 15 万
      三格的相对高低才是可比的；各自独立缩放会让三格看起来"一样高"，反而误导。
    """
    n = len([p for p in panels if p.get("series")])
    if n == 0:
        return 0
    ML, MR = 84, 28
    PH, GAP = 150, 30
    MT, MB = 96, 62
    H = MT + MB + n * PH + (n - 1) * GAP
    PW = W - ML - MR

    allv = [v for p in panels for s in p["series"] for v in s["vals"]]
    hi = (max(allv) if allv else 1.0) * 1.12 or 1.0
    xmin, xmax = min(xs), max(xs)

    def X(v):
        return ML + PW * (v - xmin) / float(max(xmax - xmin, 1))

    p = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
         'viewBox="0 0 %d %d" font-family="-apple-system,Segoe UI,'
         'Microsoft YaHei,sans-serif">' % (W, H, W, H)]
    p.append('<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H))
    p.append('<text x="%.1f" y="30" font-size="17" font-weight="700" '
             'fill="#1b1f24" text-anchor="middle">%s</text>'
             % (W / 2.0, esc(title)))
    p.append('<text x="%.1f" y="50" font-size="12" fill="#5b6470" '
             'text-anchor="middle">%s</text>' % (W / 2.0, esc(subtitle)))

    # 图例：横向一排（多格共用同一套图例，放右侧会浪费一大条宽度）
    lx = ML
    for s in panels[0]["series"]:
        p.append('<line x1="%.1f" y1="66" x2="%.1f" y2="66" stroke="%s" '
                 'stroke-width="2.6"/>' % (lx, lx + 22, s["color"]))
        p.append('<text x="%.1f" y="70" font-size="11.5" fill="#374151">%s</text>'
                 % (lx + 27, esc(s["name"])))
        lx += 27 + text_w(s["name"]) + 22

    tops = []
    idx = 0
    for pan in panels:
        series = pan["series"]
        if not series:
            continue
        top = MT + idx * (PH + GAP)
        tops.append(top)

        def Y(v, top=top):
            return top + PH * (1 - (v - 0.0) / float(hi))

        # 每格只画 0 / 中位 / 顶 三条参考线，保持清爽
        for t in (0, hi / 2.0, hi):
            y = Y(t)
            p.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s"/>'
                     % (ML, y, ML + PW, y, "#1b1f24" if t == 0 else "#e3e7ec"))
            p.append('<text x="%.1f" y="%.1f" font-size="10.8" fill="#5b6470" '
                     'text-anchor="end">%g 万</text>'
                     % (ML - 6, y + 4, round(t / 10000.0, 1)))
        # 格标题
        p.append('<text x="%.1f" y="%.1f" font-size="12.5" font-weight="700" '
                 'fill="#1b1f24">%s</text>' % (ML + 6, top + 15, esc(pan["label"])))
        # 竖向网格（贯穿所有格，便于对齐读数）
        span = xmax - xmin
        step = 10 if span > 40 else (5 if span > 15 else 1)
        t = int(xmin // step) * step
        while t <= xmax:
            if t >= xmin:
                p.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
                         'stroke="#f1f3f6"/>' % (X(t), top, X(t), top + PH))
            t += step

        notes = []
        for s in series:
            pts = " ".join("%.1f,%.1f" % (X(xs[i]), Y(v))
                           for i, v in enumerate(s["vals"]))
            p.append('<polyline points="%s" fill="none" stroke="%s" '
                     'stroke-width="2.2" stroke-linejoin="round"/>'
                     % (pts, s["color"]))
            if not annotate:
                continue
            if max(s["vals"]) <= 0:
                notes.append((s, "无此责任", xs[len(s["vals"]) // 2], 0))
                continue
            drops = []
            for i in range(1, len(s["vals"])):
                a, b = s["vals"][i - 1], s["vals"][i]
                if a <= 0:
                    continue
                if b <= 0:
                    drops.append((1e9, "归零", xs[i], 0))
                elif b < a * 0.90:
                    drops.append(((a - b) / a * 100,
                                  "断崖 -%.0f%%" % ((a - b) / a * 100), xs[i], b))
            drops.sort(key=lambda z: -z[0])
            for _, label, x, v in drops[:2]:
                p.append('<circle cx="%.1f" cy="%.1f" r="4.2" fill="#fff" '
                         'stroke="%s" stroke-width="2.3"/>' % (X(x), Y(v), s["color"]))
                notes.append((s, label, x, v))
        notes.sort(key=lambda z: X(z[2]))
        used = []
        for s, label, x, v in notes[:3]:
            ty = Y(v) - 9
            while any(abs(ty - u) < 13 for u in used):
                ty -= 13
            used.append(ty)
            p.append('<text x="%.1f" y="%.1f" font-size="10.2" font-weight="700" '
                     'fill="%s" text-anchor="middle">%s %s</text>'
                     % (X(x), max(ty, top + 26), s["color"], esc(s["short"]), esc(label)))
        idx += 1

    # 共用 X 轴（画在最底格下方）
    yb = MT + (n - 1) * (PH + GAP) + PH
    p.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#1b1f24"/>'
             % (ML, yb, ML + PW, yb))
    span = xmax - xmin
    step = 10 if span > 40 else (5 if span > 15 else 1)
    t = int(xmin // step) * step
    while t <= xmax:
        if t >= xmin:
            p.append('<text x="%.1f" y="%.1f" font-size="11.5" fill="#5b6470" '
                     'text-anchor="middle">%d</text>' % (X(t), yb + 17, t))
        t += step
    p.append('<text x="%.1f" y="%.1f" font-size="12" fill="#5b6470" '
             'text-anchor="middle">%s</text>'
             % (ML + PW / 2.0, H - 14, esc(xlabel)))
    p.append("</svg>")
    with io.open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(p))
    return os.path.getsize(out_path)


def nice_ticks(lo, hi, want=6):
    """把 [lo,hi] 切成好看的刻度（1/2/5 × 10^k）。"""
    if hi <= lo:
        hi = lo + 1
    raw = (hi - lo) / float(want)
    mag = 10 ** (len(str(int(raw))) - 1) if raw >= 1 else 1
    for m in (1, 2, 2.5, 5, 10):
        if raw <= m * mag:
            step = m * mag
            break
    else:
        step = 10 * mag
    start = (int(lo / step)) * step
    out, v = [], start
    while v <= hi + step * 0.5:
        if v >= lo - step * 0.5:
            out.append(v)
        v += step
    return out


def draw(title, subtitle, series, xs, xlabel, out_path, annotate=True):
    """series: [{"name":..,"vals":[..],"color":..}]，xs 为横轴坐标值列表。"""
    PW, PH = W - ML - MR, H - MT - MB
    allv = [v for s in series for v in s["vals"]]
    lo, hi = 0.0, max(allv) if allv else 1.0
    hi = hi * 1.12 if hi > 0 else 1.0
    xmin, xmax = min(xs), max(xs)

    def X(v):
        return ML + PW * (v - xmin) / float(max(xmax - xmin, 1))

    def Y(v):
        return MT + PH * (1 - (v - lo) / float(hi - lo))

    p = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
         'viewBox="0 0 %d %d" font-family="-apple-system,Segoe UI,'
         'Microsoft YaHei,sans-serif">' % (W, H, W, H)]
    p.append('<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H))
    p.append('<text x="%.1f" y="30" font-size="17" font-weight="700" '
             'fill="#1b1f24" text-anchor="middle">%s</text>'
             % (W / 2.0, esc(title)))
    p.append('<text x="%.1f" y="50" font-size="12" fill="#5b6470" '
             'text-anchor="middle">%s</text>' % (W / 2.0, esc(subtitle)))

    # Y 轴（万元）
    for t in nice_ticks(0, hi / 10000.0):
        v = t * 10000
        y = Y(v)
        p.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s"/>'
                 % (ML, y, ML + PW, y, "#1b1f24" if t == 0 else "#e3e7ec"))
        p.append('<text x="%.1f" y="%.1f" font-size="11.5" fill="#5b6470" '
                 'text-anchor="end">%s</text>'
                 % (ML - 8, y + 4, ("%g" % t)))
    p.append('<text x="20" y="%.1f" font-size="12" fill="#5b6470" '
             'transform="rotate(-90 20 %.1f)" text-anchor="middle">'
             '保障额度（万元）</text>' % (MT + PH / 2.0, MT + PH / 2.0))

    # X 轴
    p.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#1b1f24"/>'
             % (ML, MT + PH, ML + PW, MT + PH))
    span = xmax - xmin
    step = 10 if span > 40 else (5 if span > 15 else 1)
    t = int(xmin // step) * step
    while t <= xmax:
        if t >= xmin:
            x = X(t)
            p.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
                     'stroke="#e3e7ec"/>' % (x, MT, x, MT + PH))
            p.append('<text x="%.1f" y="%.1f" font-size="11.5" fill="#5b6470" '
                     'text-anchor="middle">%d</text>' % (x, MT + PH + 17, t))
        t += step
    p.append('<text x="%.1f" y="%.1f" font-size="12" fill="#5b6470" '
             'text-anchor="middle">%s</text>'
             % (ML + PW / 2.0, H - 14, esc(xlabel)))

    # 曲线 + 断崖/归零标注
    notes = []
    for s in series:
        pts = " ".join("%.1f,%.1f" % (X(xs[i]), Y(v))
                       for i, v in enumerate(s["vals"]))
        p.append('<polyline points="%s" fill="none" stroke="%s" '
                 'stroke-width="2.5" stroke-linejoin="round"/>'
                 % (pts, s["color"]))
        if not annotate:
            continue
        # 全程为 0 = 根本没有这项责任（如 C 无身故、B 无中症），直接标出来，
        # 否则读者只看到一条贴在 0 轴上的线，不知道是"没有"还是"为 0"。
        if max(s["vals"]) <= 0:
            mid = len(s["vals"]) // 2
            notes.append((s, "无此责任", xs[mid], 0))
            continue
        drops = []
        for i in range(1, len(s["vals"])):
            a, b = s["vals"][i - 1], s["vals"][i]
            if a <= 0:
                continue
            if b <= 0:
                drops.append((1e9, "归零", xs[i], 0))       # 归零优先
            elif b < a * 0.90:                               # 只标 ≥10% 的断崖
                drops.append(((a - b) / a * 100,
                              "断崖 -%.0f%%" % ((a - b) / a * 100), xs[i], b))
        # ★ 一条线最多标 2 个（取跌幅最大的），否则后期现价回落段会刷出一堆注解
        drops.sort(key=lambda z: -z[0])
        for _, label, x, v in drops[:2]:
            p.append('<circle cx="%.1f" cy="%.1f" r="4.6" fill="#fff" '
                     'stroke="%s" stroke-width="2.4"/>'
                     % (X(x), Y(v), s["color"]))
            notes.append((s, label, x, v))

    # 断崖/归零文字（错开行，避免叠在一起）
    notes.sort(key=lambda z: X(z[2]))
    used = []
    for s, label, x, v in notes[:8]:
        ty = Y(v) - 10
        while any(abs(ty - u) < 14 for u in used):
            ty -= 14
        used.append(ty)
        p.append('<text x="%.1f" y="%.1f" font-size="10.8" font-weight="700" '
                 'fill="%s" text-anchor="middle">%s %s</text>'
                 % (X(x), ty, s["color"], esc(s["short"]), esc(label)))

    # 图例（自动换行）
    lx, ly = ML + PW + 16, MT + 8
    maxw = W - lx - 10
    for s in series:
        label = s["name"]
        while text_w(label) > maxw - 30 and len(label) > 4:
            label = label[:-1]
        p.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                 'stroke-width="2.6"/>' % (lx, ly, lx + 22, ly, s["color"]))
        p.append('<text x="%.1f" y="%.1f" font-size="11.5" fill="#374151">%s</text>'
                 % (lx + 27, ly + 4, esc(label)))
        ly += 21

    p.append("</svg>")
    with io.open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(p))
    return os.path.getsize(out_path)


def short_name(name, i):
    """图例/标注用的短名：去掉书名号与公司全称里的冗余，最多 12 字。"""
    s = re.sub(r"[（(].*?[)）]", "", str(name or ""))
    s = s.strip()
    return (s[:12] if len(s) > 12 else s) or ("产品%d" % (i + 1))


def main():
    ap = argparse.ArgumentParser(
        description="健康险保障额度走势图（零依赖纯 SVG）",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--policy", nargs="+", required=True, help="手工 policy JSON（可多个）")
    ap.add_argument("--out", required=True, help="输出 SVG 路径")
    ap.add_argument("--mode", default="compare", choices=["compare", "single"],
                    help="compare=一个责任一张图（每款一条线，默认）；"
                         "single=一款一张图（每个责任一条线）")
    ap.add_argument("--benefits", default=None,
                    help="只画这些责任，逗号分隔（默认画全部）")
    ap.add_argument("--combine", default=None,
                    help="把若干责任叠成**一张图**（多格纵向共用 X 轴），逗号分隔；"
                         "如 --combine 重大疾病,中症,轻症。用于「一张疾病保障图 + 一张身故图」"
                         "而不是一个责任出一张图")
    ap.add_argument("--x-age", action="store_true", help="横轴用年龄而非保单年度")
    ap.add_argument("--no-annotate", action="store_true", help="不标断崖/归零点")
    a = ap.parse_args()

    pols = [load(p) for p in a.policy]
    want = [s.strip() for s in a.benefits.split(",")] if a.benefits else None
    base, ext = os.path.splitext(a.out)
    if not ext:
        ext = ".svg"
    out = []

    def xs_of(pol):
        return pol["ages"] if a.x_age else pol["years"]

    if a.mode == "compare" and a.combine:
        # ★ 多格合一：一个 SVG 里纵向堆叠，共用 X 轴
        keys = [k.strip() for k in a.combine.split(",")]
        panels = []
        for k in keys:
            series = []
            for i, pol in enumerate(pols):
                if k not in pol["benefits"]:
                    continue
                series.append({"name": pol["name"], "short": short_name(pol["name"], i),
                               "vals": pol["benefits"][k],
                               "color": COLORS[i % len(COLORS)], "years": xs_of(pol)})
            if series:
                panels.append({"label": k, "series": series})
        if not panels:
            print("✗ --combine 里的责任在 policy 中都不存在：%s" % a.combine)
            return 1
        xs = max((s["years"] for p in panels for s in p["series"]), key=len)
        path = base + ext
        n = draw_multi("疾病保障额度走势 · %s" % " / ".join(p["label"] for p in panels),
                       "横轴=%s　|　各格共用同一纵轴刻度，可直接比高低"
                       % ("年龄" if a.x_age else "保单年度"),
                       panels, xs,
                       "年龄（岁）" if a.x_age else "保单年度",
                       path, annotate=not a.no_annotate)
        out.append((path, n))
        print("已生成：%s（%d 格：%s，%d 字节）"
              % (path, len(panels), "、".join(p["label"] for p in panels), n))
    elif a.mode == "compare":
        keys = []
        for pol in pols:
            for k in pol["benefits"]:
                if k not in keys and (want is None or k in want):
                    keys.append(k)
        single = (len(keys) == 1)
        for k in keys:
            series = []
            for i, pol in enumerate(pols):
                if k not in pol["benefits"] or (want and k not in want):
                    continue
                series.append({"name": pol["name"], "short": short_name(pol["name"], i),
                               "vals": pol["benefits"][k],
                               "color": COLORS[i % len(COLORS)], "years": xs_of(pol)})
            if not series:
                continue
            xs = max((s["years"] for s in series), key=len)
            sub = "；".join("%s（%s）" % (s["name"], pols[i].get("insured", ""))
                            for i, s in enumerate(series) if i < len(pols))[:150]
            # ★ 只有一个责任时不再加后缀，否则会出现「身故保障走势_身故_全残.svg」这种冗余文件名
            path = (base + ext) if single else "%s_%s%s" % (base, safe_name(k), ext)
            n = draw("%s · 保障额度走势" % k,
                     "横轴=%s　|　%s" % ("年龄" if a.x_age else "保单年度", sub),
                     series, xs,
                     "年龄（岁）" if a.x_age else "保单年度",
                     path, annotate=not a.no_annotate)
            out.append((path, n))
            print("已生成：%s（%s，%d 字节）" %
                  (path, "、".join(s["name"] for s in series), n))
    else:
        for i, pol in enumerate(pols):
            series = []
            for j, (k, vals) in enumerate(pol["benefits"].items()):
                if want and k not in want:
                    continue
                series.append({"name": k, "short": k, "vals": vals,
                               "color": COLORS[j % len(COLORS)],
                               "years": xs_of(pol)})
            if not series:
                continue
            path = "%s_%s%s" % (base, safe_name(pol["name"]), ext)
            n = draw("%s · 保障额度走势" % pol["name"],
                     "%s　|　横轴=%s" % (pol.get("insured", ""),
                                        "年龄" if a.x_age else "保单年度"),
                     series, xs_of(pol),
                     "年龄（岁）" if a.x_age else "保单年度",
                     path, annotate=not a.no_annotate)
            out.append((path, n))
            print("已生成：%s（%d 字节）" % (path, n))

    if not out:
        print("✗ 没有可画的责任：检查 policy 的 benefits 字段与 --benefits 过滤条件")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
