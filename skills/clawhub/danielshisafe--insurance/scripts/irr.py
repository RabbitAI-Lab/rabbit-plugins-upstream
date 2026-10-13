#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
保险计划书分析大师 — 收益测算脚本
=====================================================================
计算：总利益（保证/演示）逐年表、IRR（XIRR，多持有期）、回本年限。

使用方式
-------------------------------------------------------------------
  python irr.py --input policy.json [--years 5,10,20,30] [--out result.csv]

输入 JSON 字段说明（数组下标 n = 保单年度，n=0 为投保时/第0年末）：
  start_date             可选，"YYYY-MM-DD"，默认今天（仅影响 XIRR 日期）
  premiums               各保单年度初缴纳的保费列表；premiums[n] 发生在 t=n 年
                         （n=0 即投保时，n=1 为第 2 保单年度初…）
                         计算第 N 年末 IRR 时只计入 n<N 的保费（未缴保费不入现金流）
  cv_guaranteed         保证现金价值；cv_guaranteed[n] = 第 n 年末现金价值
  cv_demo               可选，演示现金价值
  benefit_guaranteed    可选，各年末领取的生存金/年金/满期金（保证）；benefit[n] = 第 n 年末领取
  benefit_demo          可选，演示领取
  benefit_in_universal  可选，bool。**生存金/年金是否自动转入万能账户**（默认 False）。
                         ★ 为 True 时，年金已在 universal 里复利，**不得再累加 Σbenefit**，
                           否则同一笔钱计两次。年金+万能组合必须显式置 True。
  dividend_cv_guaranteed 可选，红利现金价值（**累积生息**的累积红利，含息），按存量计入
  dividend_cv_demo      可选
  dividend_cash_guaranteed 可选，**现金领取**的当年红利（按流逐年计入，非存量）
  dividend_cash_demo      可选
  universal_guaranteed  可选，万能账户价值（**非保额**；优先用可领取的账户现金价值）
  universal_demo        可选
  terminal_bonus_guaranteed 可选，终了红利（累积值，按存量计入）
  terminal_bonus_demo      可选

总利益(N) = cv[N] + Σbenefit[1..N] + dividend_cv[N] + Σdividend_cash[1..N]
            + universal[N] + terminal_bonus[N]

★ 给付去向互斥铁律（同一笔钱只能计一次，见 SKILL.md §7.11）：
  - 年金/生存金进万能（benefit_in_universal=True）→ 不计 Σbenefit，只计 universal[N]
  - 红利进万能               → 不计 dividend_cv，只计 universal[N]
  - 红利现金领取             → 用 dividend_cash（流），不用 dividend_cv（存量）
  - 满期金与满年末现金价值   → 取其一（满期终止时现价归零，不可相加）

XIRR(N)：现金流 = 各年**已缴**保费流出（t<N）+ 各年领取流入（t≤N）
          + 第 N 年末退保/满期价值流入。
注意：用二分法稳健求解，避免大模型心算误差。
=====================================================================
"""
import argparse
import json
import math
import sys
from datetime import date, timedelta


def parse_date(s):
    if not s:
        return date.today()
    return date.fromisoformat(s)


def arr(policy, base, mode):
    """取某口径某基的数组，缺失返回空列表。mode = guaranteed | demo"""
    return policy.get(f"{base}_{mode}", [])


def premium_base(policy):
    """premiums 数组的下标基准。

    0 = premiums[n] 是「第 n+1 年」年初缴的保费（build_policy.py 产出、irr.py 文档约定，
        首期在 t=0）。例：5 年交 → premiums[0..4]，缴费期 = 第 1~5 年。
    1 = premiums[0] 是占位 0，premiums[n] 是「第 n 年」保费（部分手工 JSON 的写法）。
        例：10 年交 → premiums[1..10]，缴费期 = 第 1~10 年。

    ★ 必须做基准探测：手工 JSON 若在 premiums[0] 放 0，连续前缀会在第 0 位就断掉，
      payment_span 返回 0 → 整个缴费期遮罩静默失效（表上又出现 -30% 这种数）。
    """
    pre = policy.get("premiums") or []
    if pre and to_float(pre[0]) > 0:
        return 0
    return 1


def payment_span(policy):
    """缴费期年数 P：第 1..P 年每年都有保费。返回 0 表示没有缴费期。

    ★ 用「**连续缴费前缀**」而不是「最后一期保费所在的年度」，
      否则「3 年交 + 第 10 年追加」这类保单会把第 4~9 年也误判成缴费期，
      白白遮掉 6 个有正常 IRR 的年度。
    ★ 只影响**展示层**：现金流仍由 build_flows 逐年完整计入，保费一笔不漏。
    """
    pre = policy.get("premiums") or []
    base = premium_base(policy)
    p = 0
    for v in pre[base:]:
        if to_float(v) > 0:
            p += 1
        else:
            break
    return p


def in_payment_period(policy, N, span=None):
    """第 N 年末是否仍处于缴费期（是则 IRR 不展示数值，显示「缴费期」）。"""
    if span is None:
        span = payment_span(policy)
    return span > 0 and N <= span


def to_float(v):
    """把「1,000,000」/ 1000 / None 之类统一成 float。

    ★ 真实抽取结果常把数字存成带千分位的字符串，或缺失项为 None；
      直接参与运算会抛 TypeError 崩溃（用户只看到一屏 traceback）。
    """
    if v is None or v == "":
        return 0.0
    if isinstance(v, bool):
        return 0.0
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace(",", "").replace("，", "")
    try:
        return float(s)
    except ValueError:
        return 0.0


# 价值类数组（不含 premiums —— 保费数组只覆盖交费期，天然比价值数组短）
VALUE_ARRAYS = ("cv_guaranteed", "cv_demo", "dividend_cv_guaranteed", "dividend_cv_demo",
                "dividend_annual_guaranteed", "dividend_annual_demo",
                "terminal_bonus_guaranteed", "terminal_bonus_demo",
                "benefit_guaranteed", "benefit_demo",
                "universal_guaranteed", "universal_demo",
                "annuity_guaranteed", "annuity_demo")
NUM_ARRAYS = ("premiums",) + VALUE_ARRAYS


def sanitize_policy(policy):
    """清洗并体检 policy：数值化 + 长度一致性 + 现金流有效性。

    ★ 返回 (policy, warnings)。所有异常都变成明确的 ERROR/WARNING，
      绝不静默产出无意义的数字（IRR 算错却看不出来，比报错危险得多）。
    """
    warns = []
    for k in NUM_ARRAYS:
        if k in policy and isinstance(policy[k], list):
            raw = policy[k]
            conv = [to_float(v) for v in raw]
            if any((not isinstance(v, (int, float))) or isinstance(v, bool)
                   for v in raw if v is not None and v != ""):
                warns.append(f"WARNING: {k} 含非数值项（已按 0 处理），请核对抽取结果。")
            policy[k] = conv
        elif k in policy:
            warns.append(f"WARNING: {k} 不是数组，已忽略。")
            policy.pop(k)

    # 价值数组之间必须等长；长度不等意味着年度错位，IRR 会静默算错
    lens = {k: len(policy[k]) for k in VALUE_ARRAYS if k in policy}
    if lens:
        mx = max(lens.values())
        odd = {k: v for k, v in lens.items() if v != mx}
        if odd:
            warns.append(
                f"WARNING: 价值数组长度不一致（最长 {mx}）：{odd}。"
                "各数组按索引对齐年度，长度不同通常意味着数据行错位，结果不可信。")

    # 注：价值数组「内部空洞」的体检放在 main()（要用 total_benefit，
    # 单看 cv 会把「年金开始领取后现价递减到 0」误判成空洞，见 fuyou 案例）。
    return policy, warns


def xnpv(rate, flows):
    """不规则现金流现值（XNPV）。

    用 a·exp(−t·ln(1+rate)) 替代 a/(1+rate)**t，避免长持有期在极端负利率
    (rate→-100%) 时 (1+rate)**t 下溢为 0.0 触发 ZeroDivisionError；
    指数越界时映射为 ±inf / 0.0（与原 a/(1+rate)**t 语义一致），不影响二分法收敛。
    """
    d0 = flows[0][0]
    base = 1.0 + rate
    if base <= 0:
        # 折现因子无定义（rate≤-100%）：按符号返回 ±inf（二分法据此判边界）
        for d, a in flows:
            if a == 0:
                continue
            t = (d - d0).days / 365.0
            return float("inf") if ((a > 0) == (t > 0)) else float("-inf")
    logb = math.log(base)

    def disc(a, t):
        x = -logb * t
        if x > 700.0:
            return math.copysign(float("inf"), a)   # 原 a/(1+r)**t 溢出方向
        if x < -700.0:
            return 0.0                              # 下溢为 0
        return a * math.exp(x)

    total = 0.0
    for d, a in flows:
        t = (d - d0).days / 365.0
        total += disc(a, t)
    return total


def xirr(flows, lo=-0.9999, hi=10.0, tol=1e-9, max_iter=200):
    """不规则现金流 XIRR，二分法。无符号变化返回 None。"""
    if not flows:
        return None

    def f(r):
        return xnpv(r, flows)

    flo, fhi = f(lo), f(hi)
    if flo == 0:
        return lo
    if fhi == 0:
        return hi
    if flo * fhi > 0:
        return None
    for _ in range(max_iter):
        mid = (lo + hi) / 2.0
        fm = f(mid)
        if abs(fm) < tol:
            return mid
        if flo * fm < 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2.0


def into_universal(policy):
    """生存金/年金是否已自动转入万能账户（其价值已在 universal 里复利）。

    ★ 为 True 时 benefit 只用来表达「钱流向万能」这一事实，不再作为独立流入计入，
      否则年金会被计两次（一次在 Σbenefit，一次在 universal[N]）。
    """
    return bool(policy.get("benefit_in_universal", False))


def warn_double_count(policy):
    """启发式自检：疑似重复计入时返回提示串，否则 None。

    年金流与万能账户同时长期非零，极可能是「年金进万能却未声明 benefit_in_universal」。
    """
    uni = arr(policy, "universal", "guaranteed")
    ben = arr(policy, "benefit", "guaranteed")
    if into_universal(policy) or not uni or not ben:
        return None
    n = min(len(uni), len(ben))
    both = sum(1 for t in range(1, n) if (uni[t] or 0) and (ben[t] or 0))
    if both >= 3:
        return (
            f"⚠ 疑似重复计入：benefit 与 universal 同时非零的年度达 {both} 个。"
            "若年金/生存金是自动转入万能账户的，请在 policy 里设 \"benefit_in_universal\": true，"
            "否则年金会被计两次（总利益与 IRR 双双虚高）。"
        )
    return None


def build_flows(policy, N, mode):
    """构造「持有至第 N 年末退保/终止」的现金流。

    ★ 保费截断（重要）：只计入 t < N 的保费（premiums[n] 发生在 t=n）。
    第 N 年末退保时，第 N 年初以后的保费尚未缴纳，不能计入现金流；
    若不截断，早期年度（N < 缴费期）会把未缴保费算成流出，
    使 NPV 全区间同号 → XIRR 误返回 NA（或算出失真的极低值）。

    ★ 给付去向互斥：年金进万能时不计 Σbenefit；现金领取红利按流逐年计入。
    """
    pre = policy.get("premiums", [])
    cv = arr(policy, "cv", mode)
    ben = arr(policy, "benefit", mode)
    div = arr(policy, "dividend_cv", mode)
    dcash = arr(policy, "dividend_cash", mode)
    uni = arr(policy, "universal", mode)
    tb = arr(policy, "terminal_bonus", mode)
    skip_ben = into_universal(policy)
    sd = parse_date(policy.get("start_date"))
    flows = []
    for n, p in enumerate(pre):
        if p and n < N:
            flows.append((sd + timedelta(days=365 * n), -float(p)))
    if not skip_ben:
        for t in range(1, N + 1):
            if t < len(ben) and ben[t]:
                flows.append((sd + timedelta(days=365 * t), float(ben[t])))
    for t in range(1, N + 1):
        if t < len(dcash) and dcash[t]:
            flows.append((sd + timedelta(days=365 * t), float(dcash[t])))
    val = 0.0
    if N < len(cv):
        val += cv[N]
    if N < len(div):
        val += div[N]
    if N < len(uni):
        val += uni[N]
    if N < len(tb):
        val += tb[N]
    if val:
        flows.append((sd + timedelta(days=365 * N), float(val)))
    return flows


def total_benefit(policy, N, mode):
    """第 N 年末「在保生存总利益」（未退保口径，不含身故赔付）。"""
    cv = arr(policy, "cv", mode)
    ben = arr(policy, "benefit", mode)
    div = arr(policy, "dividend_cv", mode)
    dcash = arr(policy, "dividend_cash", mode)
    uni = arr(policy, "universal", mode)
    tb = arr(policy, "terminal_bonus", mode)
    cv_v = cv[N] if N < len(cv) else 0.0
    ben_v = 0.0 if into_universal(policy) else (sum(ben[1 : N + 1]) if ben else 0.0)
    div_v = div[N] if N < len(div) else 0.0
    dcs_v = sum(dcash[1 : N + 1]) if dcash else 0.0
    uni_v = uni[N] if N < len(uni) else 0.0
    tb_v = tb[N] if N < len(tb) else 0.0
    return cv_v + ben_v + div_v + dcs_v + uni_v + tb_v


def main():
    ap = argparse.ArgumentParser(description="保险收益测算：总利益 / IRR / 回本")
    ap.add_argument("--input", required=True, help="保单 JSON 路径")
    ap.add_argument("--years", help="逗号分隔的持有年限，默认全部")
    ap.add_argument("--out", help="输出 CSV 路径（可选）")
    args = ap.parse_args()

    # ★ 友好错误：文件不存在 / 非法 JSON 时给出可行动的提示，而不是原始 traceback
    try:
        with open(args.input, encoding="utf-8") as f:
            policy = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: 找不到输入文件：{args.input}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERROR: 输入文件不是合法 JSON：{args.input}\n  {e}\n"
              "  请用 examples/*.json 对照 policy 格式。", file=sys.stderr)
        sys.exit(1)
    if not isinstance(policy, dict):
        print("ERROR: policy JSON 顶层必须是对象（参考 examples/*.json）", file=sys.stderr)
        sys.exit(1)

    policy, _swarns = sanitize_policy(policy)
    for _w in _swarns:
        print(_w, file=sys.stderr)
    if _swarns:
        print(file=sys.stderr)

    # ★ 没有保费支出就没有现金流出，IRR 在数学上无意义 —— 硬失败而不是输出垃圾
    _tot = sum(p for p in policy.get("premiums", []) if p)
    if _tot <= 0:
        print("ERROR: premiums 缺失或全为 0，没有现金流出就无法计算 IRR。"
              "请确认保费数组（趸交填在第 1 年）。", file=sys.stderr)
        sys.exit(1)

    w = warn_double_count(policy)
    if w:
        print(w, file=sys.stderr)
        print(file=sys.stderr)

    max_n = len(arr(policy, "cv", "guaranteed")) - 1
    if max_n < 1:
        print("ERROR: cv_guaranteed 缺失或为空", file=sys.stderr)
        sys.exit(1)

    years = (
        [int(y) for y in args.years.split(",")]
        if args.years
        else list(range(1, max_n + 1))
    )
    has_demo = "cv_demo" in policy

    # ★ 价值空洞体检：某年「总利益」= 0 而前后年度都有值 → 该年 IRR 必然失真。
    #   只查 cv_guaranteed 会误报：年金险开始领取后现金价值本就逐年递减到 0
    #   （如 fuyou 第 39 年起 cv=0），但那些年度有生存金流入，总利益 > 0，不是空洞。
    #   故统一用 total_benefit 判定——它已处理年金进万能等互斥规则。
    _hole_warns = []
    for mode, label in (("guaranteed", "保证"), ("demo", "演示")):
        if mode == "demo" and not has_demo:
            continue
        series = {n: total_benefit(policy, n, mode) for n in range(1, max_n + 1)}
        nz = [n for n in range(1, max_n + 1) if series[n] > 0]
        if len(nz) < 2:
            continue
        holes = [n for n in range(nz[0], nz[-1]) if series[n] <= 0]
        if holes:
            _hole_warns.append(
                f"WARNING: {label}总利益在第 {nz[0]}~{nz[-1]} 年之间有 {len(holes)} 个空洞"
                f"（第 {holes[:8]}{'…' if len(holes) > 8 else ''} 年为 0）。"
                "这些年度 IRR 会显示 NA 或极端负值，不可信。"
                "请补齐逐年数据，或用 --years 只取有数据的年度。")
    for _h in _hole_warns:
        print(_h, file=sys.stderr)
    if _hole_warns:
        print(file=sys.stderr)

    total_prem = sum(p for p in policy.get("premiums", []) if p)

    def breakeven(mode):
        for n in range(1, max_n + 1):
            if total_prem > 0 and total_benefit(policy, n, mode) >= total_prem:
                return n
        return None

    be_g = breakeven("guaranteed")
    be_d = breakeven("demo") if has_demo else None

    header = ["持有年度", "总利益(保证)", "XIRR(保证)%"]
    if has_demo:
        header += ["总利益(演示)", "XIRR(演示)%"]
    rows = [header]

    # ★ 缴费期口径：第 1..pay_span 年的 IRR 一律显示「缴费期」而不是数值。
    #   这些年度保费尚未交完，IRR 必然是很深的负值（实测可到 -20%），
    #   既不能反映产品收益，又极易被读成「亏了 20%」，所以不展示数值。
    #   ★ 但保费现金流仍逐年完整进入 build_flows —— 只是不显示，
    #     后续年度的 IRR 一分不少地包含缴费期的全部流出。
    pay_span = payment_span(policy)

    def show_irr(r, paying):
        if paying:
            return "缴费期"
        return round(r * 100, 3) if r is not None else "NA"

    for N in years:
        if N > max_n:
            continue
        paying = in_payment_period(policy, N, pay_span)
        tg = total_benefit(policy, N, "guaranteed")
        rg = xirr(build_flows(policy, N, "guaranteed"))
        row = [N, round(tg, 2), show_irr(rg, paying)]
        if has_demo:
            td = total_benefit(policy, N, "demo")
            rd = xirr(build_flows(policy, N, "demo"))
            row += [round(td, 2), show_irr(rd, paying)]
        rows.append(row)

    print(f"总保费: {total_prem}")
    if pay_span:
        print(f"缴费期: 第 1–{pay_span} 年 → 该区间 IRR 列显示「缴费期」"
              "（保费未交完，IRR 无参考意义；现金流仍逐年完整计入，仅不展示数值）")
    print(f"回本年限(保证总利益): {be_g}")
    if has_demo:
        print(f"回本年限(演示总利益): {be_d}")
    print()
    widths = [max(len(str(r[i])) for r in rows) for i in range(len(header))]
    for r in rows:
        print("  ".join(str(x).ljust(widths[i]) for i, x in enumerate(r)))

    if args.out:
        import csv

        with open(args.out, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f)
            w.writerows(rows)
        print(f"\n已写出: {args.out}")


if __name__ == "__main__":
    try:
        from _feedback_hook import install; install()
    except Exception:
        pass
    main()
