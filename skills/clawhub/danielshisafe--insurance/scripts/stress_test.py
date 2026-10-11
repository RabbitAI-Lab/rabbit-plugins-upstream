#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
stress_test.py —— 分红实现率压力测试（IRR + 翻倍年数 + 临界实现率）
=====================================================================
回答一个演示表永远不告诉你的问题：

> 如果红利只兑现到演示的 X%，这份保单还值不值？

**为什么要做**：分红险的演示利益里，非保证部分往往占一半以上。只报「演示 IRR」
等于默认 100% 实现率；只报「保证 IRR」又等于默认 0%。真实情况在两者之间，
而**压力测试把这段区间摊开给你看**，让「演示 ≠ 保证」从一句免责声明变成可比较的数字。

压力测试定义（组件线性缩放）
-------------------------------------------------------------------
    stressed(N, X) = guaranteed(N) + X × [ demo(N) − guaranteed(N) ]

对每一个可缩放组件（现金价值 / 累积红利 / 生存金 / 万能 / 终了红利）分别缩放后求和。
`benefit`（年金领取）按**流**处理（Σ benefit[1..N]），其余按**存量**处理（取第 N 年末值）。

★ X = 0 即「红利为零」，结果应等于纯保证口径（可用 irr.py 交叉验证）。
★ X = 1 即「100% 实现」，结果应等于演示口径。

复利修正（reaccum 模式）
-------------------------------------------------------------------
若红利是**累积生息**型（红利留存在公司以某利率复利），线性缩放「累积红利」会略有偏差，
因为复利是非线性的。此时应改为：

    acc[y] = acc[y−1] × (1 + r) + 当年红利[y] × X

脚本在 policy 提供 `dividend_annual_demo`（当年红利）时自动启用（--mode auto，默认）。
储存生息利率 r 若未给（--rate），脚本会从 `dividend_cv_demo` 与 `dividend_annual_demo`
**自动反推**并打印（多年度取中位数）。

输出三项指标
-------------------------------------------------------------------
1. **IRR(N)%**    —— 该实现率下持有至第 N 年末的 XIRR（口径同 irr.py，含保费截断）。
2. **翻倍年数**   —— 总利益首次达到「累计已缴保费 × K」的保单年度（K 默认 2，--times 可调）。
                     K=1 即回本年数。若 N 年内未达到则记 `>N`。
3. **总利益(N)**  —— 该实现率下第 N 年末的总利益金额。
4. **临界实现率** —— 使 IRR 追平指定目标所需的最低 X（--target-irr 或 --benchmark）。
                     这是最有决策价值的一列：它把「要不要赌红利」变成一个阈值判断。

使用方式
-------------------------------------------------------------------
  # 基本：多产品、默认 0/25/50/75/100% 五档
  python stress_test.py --input A.json B.json --names "A" "B" --years 75

  # 追平某款无分红产品（用它的保证 IRR 当目标）
  python stress_test.py --input A.json B.json --benchmark C.json --years 75

  # 指定 IRR 目标（百分点，不带 %）
  python stress_test.py --input A.json --target-irr 2.0 --years 75

  # 自定义档位 + 看 3 倍年数 + 导出 CSV
  python stress_test.py --input A.json --rates 0,30,60,100 --times 3 --out stress.csv

  # 关闭复利修正（线性缩放）
  python stress_test.py --input A.json --mode simple

policy JSON 字段（在 irr.py 基础上新增两个可选字段）
-------------------------------------------------------------------
  dividend_annual_guaranteed   当年现金红利（保证），数组，下标 = 保单年度
  dividend_annual_demo         当年现金红利（演示），数组，下标 = 保单年度
  其余字段同 scripts/irr.py（premiums / cv_* / benefit_* / dividend_cv_* / ...）

★ 给付去向互斥（与 irr.py 同源，同一笔钱只计一次）
-------------------------------------------------------------------
  - 年金/生存金自动转入万能账户 → 必须设 "benefit_in_universal": true，
    此时年金只在 universal[N] 里计一次，不再累加 Σbenefit（否则总利益与 IRR 双双虚高）。
  - 现金领取的红利 → 用 dividend_cash_*（按流），不要用 dividend_cv_*（按存量，会低估 IRR）。
  - 满期金与满年末现金价值 → 取其一，不可相加。

注意
-------------------------------------------------------------------
- 实现率是本技能做的**假设压力测试**，**不是**对保险公司历史分红实现率的评价
  （见 SKILL.md §十二.7：本技能无实时实现率数据库，不抓取、不对比历史实现率）。
- 报告中必须写明这是「假设情景」，且 X=0 不代表红利真会为零。
"""
import argparse
import csv
import json
import math
import sys

# 存量组件（取第 N 年末值）；FLOW 里的按「流」逐年累加
STOCK = ["cv", "dividend_cv", "universal", "terminal_bonus"]
FLOW = ["benefit", "dividend_cash"]


# ---------------------------------------------------------------- 基础工具
def arr(pol, base, mode):
    """取某口径某基的数组，缺失回退到 guaranteed，再缺失返回空列表。"""
    return pol.get(f"{base}_{mode}") or pol.get(f"{base}_guaranteed") or []


def into_universal(pol):
    """生存金/年金是否已自动转入万能账户（价值已在 universal 里复利）。

    ★ 与 irr.py 同源铁律：为 True 时不得再累加 Σbenefit，否则年金计两次。
    """
    return bool(pol.get("benefit_in_universal", False))


def flow_at(pol, mode, N, X):
    """第 1..N 年「领取流」之和（按实现率 X 线性缩放）。

    年金进万能时跳过 benefit（已在 universal 存量里）；现金领取红利始终按流计入。
    """
    tot = 0.0
    for base in FLOW:
        if base == "benefit" and into_universal(pol):
            continue
        g, d = arr(pol, base, "guaranteed"), arr(pol, base, mode)
        for n in range(1, N + 1):
            tot += at(g, n) + X * (at(d, n) - at(g, n))
    return tot


def warn_double_count(pol):
    """启发式自检：年金流与万能账户长期同时非零 → 疑似未声明 benefit_in_universal。"""
    if into_universal(pol):
        return None
    uni, ben = arr(pol, "universal", "guaranteed"), arr(pol, "benefit", "guaranteed")
    if not uni or not ben:
        return None
    both = sum(1 for t in range(1, min(len(uni), len(ben)))
               if (at(uni, t) or 0) and (at(ben, t) or 0))
    if both >= 3:
        return (f"疑似重复计入：benefit 与 universal 同时非零达 {both} 个年度。"
                "若年金自动转入万能，请设 \"benefit_in_universal\": true。")
    return None


def at(a, n):
    return a[n] if n < len(a) else 0.0


def paid_upto(prems, N):
    """第 N 年末累计已缴保费（★ 保费截断铁律：只计 t < N 的保费）。"""
    return sum(float(p) for n, p in enumerate(prems) if n < N and p)


def disc(base, a, t):
    """折现因子，exp 形式 + 溢出 clamp（长年期 r→-100% 时 (1+r)**t 会下溢/溢出）。"""
    x = -math.log(base) * t
    if x > 700.0:
        return math.copysign(float("inf"), a)
    if x < -700.0:
        return 0.0
    return a * math.exp(x)


def xirr(fy, lo=-0.999999, hi=10.0, iters=400):
    """fy: [(t_years, amount)]。二分法求解，无解返回 None。"""
    def npv(r):
        if 1.0 + r <= 0:
            return float("inf")
        return sum(disc(1.0 + r, a, t) for t, a in fy)
    if not fy or npv(lo) * npv(hi) > 0:
        return None
    for _ in range(iters):
        mid = (lo + hi) / 2
        if npv(lo) * npv(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


# ---------------------------------------------------------------- 总利益
def components(pol, mode, N, X=1.0, acc=None):
    """返回「存量之和」与「领取流之和」。X 为实现率，acc 为复利重算后的累积红利数组。

    ★ acc 不为 None 时，**只替换 dividend_cv 这一个组件**（避免与 cv_demo 里已含的
      增额红利重复计入），其余组件仍按线性缩放。
    """
    def scaled(base, n):
        g = at(arr(pol, base, "guaranteed"), n)
        d = at(arr(pol, base, mode), n)
        return g + X * (d - g)

    stock = scaled("cv", N) + scaled("universal", N) + scaled("terminal_bonus", N)
    stock += at(acc, N) if acc is not None else scaled("dividend_cv", N)

    return stock, flow_at(pol, mode, N, X)


def total(pol, mode, N, X=1.0, acc=None):
    s, f = components(pol, mode, N, X, acc)
    return s + f


def irr_at(pol, N, X=1.0, acc=None, prems=None):
    """第 N 年末 IRR。现金流 = 已缴保费(t<N) + 各年领取(t≤N) + 第 N 年末终端价值。"""
    prems = prems if prems is not None else pol.get("premiums", [])
    stock, _ = components(pol, "demo", N, X, acc)
    fy = [(n, -float(p)) for n, p in enumerate(prems) if n < N and p]
    for base in FLOW:
        if base == "benefit" and into_universal(pol):
            continue
        g, d = arr(pol, base, "guaranteed"), arr(pol, base, "demo")
        for n in range(1, N + 1):
            v = at(g, n) + X * (at(d, n) - at(g, n))
            if v:
                fy.append((n, v))
    fy.append((N, stock))
    if min(a for _, a in fy) >= 0 or max(a for _, a in fy) <= 0:
        return None
    return xirr(fy)


def doubling_year(pol, N, X=1.0, acc=None, times=2.0, prems=None):
    """总利益首次 ≥ times × 累计已缴保费 的保单年度；未达到返回 None。"""
    prems = prems if prems is not None else pol.get("premiums", [])
    for n in range(1, N + 1):
        need = times * paid_upto(prems, n)
        if need <= 0:
            continue
        if total(pol, "demo", n, X, acc) >= need:
            return n
    return None


# ---------------------------------------------------------------- 复利修正
def infer_rate(pol):
    """从 累积红利 与 当年红利 反推储存生息利率（取中位数）。"""
    acc = pol.get("dividend_cv_demo") or []
    ann = pol.get("dividend_annual_demo") or []
    rs = []
    for y in range(2, min(len(acc), len(ann))):
        prev, cur, cur_d = acc[y - 1], acc[y], ann[y]
        if prev and prev > 1000:
            r = (cur - cur_d) / prev - 1
            if -0.5 < r < 0.5:
                rs.append(r)
    if not rs:
        return None
    rs.sort()
    return rs[len(rs) // 2]


def reaccum(pol, X, rate, nmax):
    """按 当年红利 × X 重新累积（复利修正）。返回累积红利数组。"""
    g_ann = pol.get("dividend_annual_guaranteed") or []
    d_ann = pol.get("dividend_annual_demo") or []
    out = [0.0]
    for y in range(1, nmax + 1):
        ga, da = at(g_ann, y), at(d_ann, y)
        out.append(out[-1] * (1.0 + rate) + (ga + X * (da - ga)))
    return out


def has_dividend(pol):
    """是否含任何非保证红利（无分红产品直接跳过临界实现率求解）。"""
    for base in STOCK + FLOW:
        g, d = arr(pol, base, "guaranteed"), arr(pol, base, "demo")
        n = max(len(g), len(d))
        for i in range(n):
            if abs(at(d, i) - at(g, i)) > 1e-6:
                return True
    if pol.get("dividend_annual_demo"):
        return True
    return False


# ---------------------------------------------------------------- 主流程
def _pf(v):
    """保费单元格 → float（兼容带千分位的字符串 / None / 缺失项）。"""
    if v is None or v == "" or isinstance(v, bool):
        return 0.0
    try:
        return float(str(v).strip().replace(",", "").replace("，", ""))
    except (TypeError, ValueError):
        return 0.0


def payment_span(pol):
    """缴费期年数：第 1..P 年每年都有保费（**连续前缀**）。

    与 irr.py 同一口径。两点：
    - 用连续前缀而非「最后一期保费所在年度」，避免「3 年交 + 第 10 年追加」
      把第 4~9 年也误判成缴费期；
    - 做 premiums 下标基准探测（premiums[0] 可能是占位 0），
      否则连续前缀在第 0 位就断掉，遮罩静默失效。
    ★ 只影响展示层，irr_at 的现金流不做任何裁剪。
    """
    pre = pol.get("premiums") or []
    base = 0 if (pre and _pf(pre[0]) > 0) else 1
    p = 0
    for v in pre[base:]:
        if _pf(v) > 0:
            p += 1
        else:
            break
    return p


def main():
    ap = argparse.ArgumentParser(description="分红实现率压力测试（IRR / 翻倍年数 / 临界实现率）")
    ap.add_argument("--input", nargs="+", required=True, help="policy JSON（可多个），格式同 irr.py")
    ap.add_argument("--names", nargs="*", help="产品简称，顺序与 --input 一致")
    ap.add_argument("--years", type=int, help="评估年度 N，默认取各产品数据长度的最小值")
    ap.add_argument("--rates", default="0,25,50,75,100", help="实现率档位（百分数），默认 0,25,50,75,100")
    ap.add_argument("--times", type=float, default=2.0, help="翻倍倍数 K，默认 2（--times 1 即回本年数）")
    ap.add_argument("--mode", choices=["auto", "simple", "reaccum"], default="auto",
                    help="复利修正开关，默认 auto（有当年红利列时自动启用）")
    ap.add_argument("--rate", type=float, help="储存生息/累积利率（如 0.0175）；不给则自动反推")
    ap.add_argument("--target-irr", type=float, help="IRR 目标（百分点，如 1.75）")
    ap.add_argument("--benchmark", help="基准产品 policy JSON：用它的保证 IRR(N) 作为目标")
    ap.add_argument("--out", help="输出 CSV 路径")
    args = ap.parse_args()

    pols, names = [], []
    for i, path in enumerate(args.input):
        with open(path, encoding="utf-8") as f:
            pol = json.load(f)
        pols.append(pol)
        names.append(args.names[i] if args.names and i < len(args.names)
                     else pol.get("name", path.rsplit("/", 1)[-1]))
        if warn_double_count(pol):
            print(f"⚠ {names[-1]}：{warn_double_count(pol)}", file=sys.stderr)

    bench_pol = None
    if args.benchmark:
        with open(args.benchmark, encoding="utf-8") as f:
            bench_pol = json.load(f)

    def maxn(pol):
        return max(len(arr(pol, b, "guaranteed")) for b in STOCK + FLOW) - 1

    N = args.years or min(maxn(p) for p in pols)

    rates = [float(r) / 100.0 for r in args.rates.split(",")]

    # ---- 复利修正准备（每个产品的模式与利率只算一次）----
    mode_of, rate_of = [], []
    for pol in pols:
        if args.mode == "reaccum" or (args.mode == "auto" and pol.get("dividend_annual_demo")):
            r = args.rate if args.rate is not None else infer_rate(pol)
            if r is not None:
                mode_of.append("reaccum")
                rate_of.append(r)
            else:
                mode_of.append("simple")
                rate_of.append(None)
        else:
            mode_of.append("simple")
            rate_of.append(None)

    def acc_of(i, X):
        """第 i 个产品在实现率 X 下的累积红利数组；不做复利修正时返回 None。"""
        if mode_of[i] != "reaccum":
            return None
        return reaccum(pols[i], X, rate_of[i], N)

    print(f"评估年度：第 {N} 保单年度    翻倍倍数：K={args.times:g}    档位：{args.rates}")
    print("复利修正：" + "  ".join(
        f"{nm}={'reaccum(' + format(r*100, '.4f') + '%)' if m == 'reaccum' else 'simple'}"
        for nm, m, r in zip(names, mode_of, rate_of)))

    # 缴费期遮罩：与 irr.py 同一口径（连续缴费前缀）
    spans = [payment_span(p) for p in pols]
    for nm, s in zip(names, spans):
        if s > 0 and N <= s:
            print(f"缴费期：{nm} 第 1–{s} 年 → 第 {N} 年 IRR 列显示「缴费期」"
                  "（保费未交完，IRR 无参考意义；现金流仍完整计入，仅不展示数值）")
    print()

    # ---- 主表 ----
    header = ["实现率"]
    for nm in names:
        header += [f"{nm} IRR%", f"{nm} {args.times:g}倍年", f"{nm} 总利益"]
    rows = [header]

    for X in rates:
        row = [f"{X*100:.0f}%"]
        for i, pol in enumerate(pols):
            acc = acc_of(i, X)
            r = irr_at(pol, N, X, acc)
            dbl = doubling_year(pol, N, X, acc, args.times)
            tv = total(pol, "demo", N, X, acc)
            # 缴费期内只遮 IRR 单元格；irr_at 仍跑完整现金流（保费一笔不漏）
            irr_txt = "缴费期" if (spans[i] > 0 and N <= spans[i]) else (
                f"{r*100:.3f}" if r is not None else "NA")
            row += [irr_txt,
                    str(dbl) if dbl else f">{N}",
                    f"{tv:,.0f}"]
        rows.append(row)

    # ---- 临界实现率 ----
    target = args.target_irr
    if target is None and bench_pol is not None:
        br = irr_at(bench_pol, N, 0.0)
        if br is not None:
            target = br * 100
            bn = bench_pol.get("name", "基准产品")
            print(f"目标 IRR：{target:.3f}%（= {bn} 第 {N} 年保证口径 IRR）\n")
    if target is not None:
        crit = [f"临界实现率(追平{target:.3f}%)"]
        for i, pol in enumerate(pols):
            if not has_dividend(pol):
                crit += ["无分红", "—", ""]
                continue

            def f(X, i=i):
                r = irr_at(pol, N, X, acc_of(i, X))
                return r * 100 if r is not None else -1e9

            lo, hi = 0.0, 3.0
            if f(0.0) >= target:
                crit += ["0%（保证即达标）", "—", ""]
                continue
            if f(hi) < target:
                crit += [">300%", "—", ""]
                continue
            for _ in range(200):
                mid = (lo + hi) / 2
                if f(mid) < target:
                    lo = mid
                else:
                    hi = mid
            crit += [f"{(lo+hi)/2*100:.1f}%", "—", ""]
        rows.append(crit)

    widths = [max(len(str(r[i])) for r in rows) for i in range(len(header))]
    for r in rows:
        print("  ".join(str(x).ljust(widths[i]) for i, x in enumerate(r)))

    print()
    print("读法：")
    print(f"  · 实现率 0%   = 红利为零，等同纯保证口径（应与 irr.py 的保证 IRR 一致）")
    print(f"  · 实现率 100% = 完全兑现演示，等同演示口径（应与 irr.py 的演示 IRR 一致）")
    print(f"  · 「{args.times:g}倍年」= 总利益首次达到累计已缴保费 {args.times:g} 倍的保单年度；'>{N}' 表示 {N} 年内未达到")
    print("  · 「临界实现率」= 追平目标 IRR 所需的最低实现率；这是把「要不要赌红利」变成阈值判断的关键一列")
    print("  ⚠ 实现率是本脚本做的假设压力测试，不是对保险公司历史分红实现率的评价，")
    print("    报告中必须写明这是假设情景，且 0% 不代表红利真会为零。")

    if args.out:
        with open(args.out, "w", newline="", encoding="utf-8-sig") as f:
            csv.writer(f).writerows(rows)
        print(f"\n已写出: {args.out}")


if __name__ == "__main__":
    try:
        from _feedback_hook import install; install()
    except Exception:
        pass
    main()
