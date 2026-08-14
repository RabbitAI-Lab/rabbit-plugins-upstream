#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""stats —— 统计分析（纯 Python，无 scipy/numpy 依赖）。

对 CSV/JSON 数据集做：描述统计（均值/中位数/分位数/标准差）、数值列间
Pearson 相关矩阵、以及两样本 Welch t 检验（不等方差）。输出 JSON 摘要。

用法：
  python stats.py --data <file.csv|.json> --out summary.json [--group 列] [--value 数值列]
"""
import os, sys, json, csv, argparse, statistics as st, math


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
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def describe(vals):
    vals = sorted(vals)
    n = len(vals)
    def pct(p):
        if n == 1:
            return vals[0]
        k = (n - 1) * p
        f = math.floor(k)
        c = math.ceil(k)
        if f == c:
            return vals[int(k)]
        return vals[f] * (c - k) + vals[c] * (k - f)
    return {
        "n": n, "mean": round(st.mean(vals), 4), "median": round(st.median(vals), 4),
        "std": round(st.pstdev(vals), 4) if n > 1 else 0,
        "min": round(min(vals), 4), "max": round(max(vals), 4),
        "p25": round(pct(0.25), 4), "p75": round(pct(0.75), 4),
    }


def pearson(x, y):
    n = len(x)
    mx, my = st.mean(x), st.mean(y)
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    dx = math.sqrt(sum((a - mx) ** 2 for a in x))
    dy = math.sqrt(sum((b - my) ** 2 for b in y))
    return num / (dx * dy) if dx and dy else 0.0


def welch_t(a, b):
    """两样本 Welch t 检验，返回 t 与近似自由度。"""
    na, nb = len(a), len(b)
    ma, mb = st.mean(a), st.mean(b)
    va = st.variance(a) if na > 1 else 0.0
    vb = st.variance(b) if nb > 1 else 0.0
    se = math.sqrt(va / na + vb / nb)
    if se == 0:
        return 0.0, 0.0, 0.0
    t = (ma - mb) / se
    # Welch–Satterthwaite 自由度
    num = (va / na + vb / nb) ** 2
    den = (va / na) ** 2 / (na - 1) + (vb / nb) ** 2 / (nb - 1) if (na - 1) and (nb - 1) else 1
    df = num / den if den else 1.0
    return round(t, 4), round(df, 2), round(ma - mb, 4)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", default="")
    ap.add_argument("--group", default="", help="分组列（用于 t 检验）")
    ap.add_argument("--value", default="", help="t 检验的数值列")
    args = ap.parse_args()

    rows = load_rows(args.data)
    cols = list(rows[0].keys()) if rows else []
    summary = {"n_rows": len(rows), "describe": {}, "correlation": {}}

    numeric = {c: [float(r[c]) for r in rows if is_number(r.get(c, ""))] for c in cols}
    numeric = {c: v for c, v in numeric.items() if len(v) >= 2}
    for c, v in numeric.items():
        summary["describe"][c] = describe(v)

    ncols = list(numeric.keys())
    for i in range(len(ncols)):
        summary["correlation"][ncols[i]] = {
            ncols[j]: round(pearson(numeric[ncols[i]], numeric[ncols[j]]), 3)
            for j in range(len(ncols))
        }

    if args.group and args.value:
        groups = {}
        for r in rows:
            if is_number(r.get(args.value, "")):
                groups.setdefault(r.get(args.group, "?"), []).append(float(r[args.value]))
        keys = [k for k in groups if len(groups[k]) >= 2]
        if len(keys) >= 2:
            a, b = groups[keys[0]], groups[keys[1]]
            t, df, diff = welch_t(a, b)
            summary["welch_ttest"] = {
                "group_col": args.group, "value_col": args.value,
                "group_a": keys[0], "group_b": keys[1],
                "n_a": len(a), "n_b": len(b),
                "mean_a": round(st.mean(a), 4), "mean_b": round(st.mean(b), 4),
                "t": t, "df": df, "mean_diff": diff,
            }

    if args.out:
        json.dump(summary, open(args.out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"✅ 统计摘要写入 {args.out}")
    else:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"数值列 {len(numeric)} 个，描述统计+相关矩阵完成"
          + (f"，t 检验: {args.group}→{args.value}" if args.group else ""))


if __name__ == "__main__":
    main()
