#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""生存总利益「计法判定器」——把 SKILL.md §7.16 的决策树自动化。

设计思路（用户的原话）
-------------------------------------------------------------------
生存总利益怎么算，**不是背公式，是一道自上而下的逻辑判断题**：

  ① 大形态是什么？（增额寿 / 年金 / 两全 / 投连）
  ② 是不是分红型？
  ③ 分红有哪几种？（现金红利 / 增额红利 / 终了红利 / 特别红利，可多选）
  ④ 每种红利的去向？（现金领取 / 累积生息 / 进入万能 / 已含在现价里）
  ⑤ 有没有万能账户？若有，**只有一件事要搞清楚：哪些现金流进了万能**
     —— 进了万能的，在万能之外就不再单独计（这是全部重复计入的唯一来源）。

走完这五步，每一项「该不该加、按流还是按存量」就是唯一确定的，
不需要记忆任何公式，也不会漏项或双算。

使用方式
-------------------------------------------------------------------
  # A. 从列名判断（最强：解析 PDF/Excel 拿到的第一批信息就是列名）
  python scripts/classify_policy.py --columns "保单年度,现金价值,生存保险金,当年红利,累积现金红利"
  python scripts/classify_policy.py --name "XX年金保险（分红型）" --columns "..."

  # B. 从已构造的 policy.json 反查（检查字段有没有填错）
  python scripts/classify_policy.py --policy policy.json

  # C. 两者都给（最准：列名定构成 + policy 查实际填值）
  python scripts/classify_policy.py --policy policy.json --columns "..."

只做判定与建议，**不修改任何文件**；冲突以告警形式输出。
=====================================================================
"""
import argparse
import json
import sys


# ---------------------------------------------------------------- 关键词库
# 大形态
KW = {
    "两全": ["两全"],
    "年金": ["年金"],
    "增额终身寿": ["终身寿险", "增额"],
    "投连": ["投资连结", "投连"],
}
KW_ENDow = ["满期金", "满期保险金", "满期生存金"]
KW_ANN = ["生存金", "生存保险金", "养老年金", "年金给付", "特别生存金"]
KW_CV = ["现金价值", "退保金", "生存总利益", "总利益", "账户价值合计"]

# 红利类型（★ 判定顺序不可调换：先「保额」后「现金」，因为
#   「累积红利**保额**」= 增额红利，而「累积**现金**红利」= 现金红利）
KW_DIV_PU = ["红利保额", "增额红利", "交清增额", "红利保险金额"]
KW_DIV_TERM = ["终了红利"]
KW_DIV_SPEC = ["特别红利", "特别生存金红利"]
KW_DIV_CASH = ["现金红利", "当年红利", "年度红利", "累积红利", "红利"]

KW_UNIV = ["万能", "结算利率", "保证利率"]
KW_ACC = ["累积", "累计", "含息", "储存生息", "累积生息"]
# ★ 合计型列：红利已含在内，命中即走 §7.11 铁律①「直接用，不要组件求和」
KW_SUM = ["生存总利益", "总利益", "总现金价值", "账户价值合计"]


def has(text, kws):
    return any(k in text for k in kws)


def cls_dividend(col):
    """把一列归类到某种红利；返回 cash / pu / term / spec / None。

    ★ 先判「保额」——否则「累积红利保额」会被误判成现金红利。
    """
    if "红利" not in col and "交清增额" not in col:
        return None
    if has(col, KW_DIV_PU):
        return "pu"
    if has(col, KW_DIV_TERM):
        return "term"
    if has(col, KW_DIV_SPEC):
        return "spec"
    if has(col, ["现金"]) or has(col, KW_DIV_CASH):
        return "cash"
    return "cash"


# ---------------------------------------------------------------- 第①步 大形态
def shape_of(name, cols):
    txt = (name or "") + " " + " ".join(cols)
    if has(txt, KW["投连"]):
        return "投连"
    if has(txt, KW["两全"]):
        return "两全"
    if has(txt, KW["年金"]):
        return "年金"
    if has(txt, KW["增额终身寿"]):
        return "增额终身寿"
    # 无名称时靠列：有生存金列 → 年金；有满期金列 → 两全
    if any(has(c, KW_ANN) for c in cols):
        return "年金"
    if any(has(c, KW_ENDow) for c in cols):
        return "两全"
    return "未知"


# ---------------------------------------------------------------- 第③④步 红利
def dividends_of(cols, pol):
    found = {"cash": [], "pu": [], "term": [], "spec": []}
    for c in cols:
        k = cls_dividend(c)
        if k:
            found[k].append(c)
    if pol:
        for k, keys in (("cash", ["dividend_cv", "dividend_cash", "dividend_annual"]),
                        ("pu", []), ("term", ["terminal_bonus"]), ("spec", [])):
            for key in keys:
                for suffix in ("_guaranteed", "_demo"):
                    f = key + suffix
                    if any(pol.get(f) or []) and "policy字段:" + f not in found[k]:
                        found[k].append("policy字段:" + f)
    return found


def cash_div_dest(cols, pol):
    """现金红利的去向：accum 累积生息 / withdraw 现金领取 / universal 进万能 / 未知。"""
    joined = " ".join(cols)
    has_univ = any(has(c, KW_UNIV) for c in cols) or bool(pol and _pol_univ(pol))
    if has_univ and has(joined, ["红利"]) and has(joined, ["进入万能", "转入万能", "红利转万能"]):
        return "universal"
    if has(joined, KW_ACC):
        return "accum"
    if has(joined, ["现金领取", "领取红利", "直接领取"]):
        return "withdraw"
    if pol is not None:
        if any(pol.get(f) or [] for f in ("dividend_cash_guaranteed", "dividend_cash_demo")):
            return "withdraw"
        if any(pol.get(f) or [] for f in ("dividend_cv_guaranteed", "dividend_cv_demo")):
            return "accum"
    return "未知"


def _pol_univ(pol):
    return any(pol.get(f) or [] for f in
               ("universal_guaranteed", "universal_demo"))


# ---------------------------------------------------------------- 第⑤步 万能
def univ_of(cols, pol):
    ucols = [c for c in cols if has(c, KW_UNIV)]
    has_u = bool(ucols) or bool(pol and _pol_univ(pol))
    if not has_u:
        return False, []
    flows = []
    if any(has(c, KW_ANN) for c in cols) or (pol and any(pol.get(f) or [] for f in
                                                         ("benefit_guaranteed", "benefit_demo"))):
        flows.append("年金/生存金")
    if cash_div_dest(cols, pol) == "universal":
        flows.append("现金红利")
    return True, flows


# ---------------------------------------------------------------- 输出
def emit(name, cols, pol):
    W = 74
    print("═" * W)
    print("生存总利益 · 计法判定（SKILL.md §7.16 决策树）")
    print("═" * W)

    shape = shape_of(name, cols)
    print(f"\n① 大形态：{shape}")
    if shape == "投连":
        print("   → 投连险不纳入 IRR / 总利益测算，走底层资产穿透（§7.13）。判定结束。")
        return
    ev = []
    if name and has(name, KW.get(shape, [])):
        ev.append(f"名称含「{[k for k in KW.get(shape, []) if k in name][0]}」")
    if any(has(c, KW_ANN) for c in cols):
        ev.append("存在生存金/年金列")
    if any(has(c, KW_ENDow) for c in cols):
        ev.append("存在满期金列")
    if ev:
        print("   依据：" + "；".join(ev))

    is_div = ("分红" in (name or "")) or any(cls_dividend(c) for c in cols) or bool(
        pol and any(pol.get(f) or [] for f in
                    ("dividend_cv_guaranteed", "dividend_cv_demo",
                     "dividend_cash_guaranteed", "dividend_cash_demo",
                     "dividend_annual_guaranteed", "dividend_annual_demo")))
    print(f"\n② 是否分红：{'是' if is_div else '否'}")

    d = dividends_of(cols, pol)
    dest = cash_div_dest(cols, pol) if d["cash"] else None
    if is_div:
        print("\n③ 分红构成（勾选）：")
        label = {"cash": "现金红利", "pu": "增额红利/交清增额",
                 "term": "终了红利", "spec": "特别红利"}
        for k in ("cash", "pu", "term", "spec"):
            mark = "√" if d[k] else " "
            print(f"    [{mark}] {label[k]:<16}", end="")
            if d[k]:
                print("列：" + "、".join(d[k][:3]))
            else:
                print()

        if d["cash"]:
            dest_txt = {"accum": "累积生息", "withdraw": "现金领取",
                        "universal": "进入万能账户", "未知": "★ 未知，必须回计划书确认"}[dest]
            print(f"\n④ 现金红利去向：{dest_txt}")
            if dest == "未知":
                print("    → 去向决定计法，未确认前不要算：")
                print("      累积生息 → dividend_cv_*（存量）  现金领取 → dividend_cash_*（流）")
                print("      进入万能 → 不填红利字段，只计 universal_*")

    has_u, uflows = univ_of(cols, pol)
    print(f"\n⑤ 万能账户：{'有' if has_u else '无'}")
    if has_u:
        if uflows:
            print(f"   进入万能的现金流：{'、'.join(uflows)}")
            print("   ★ 这些流在万能之外**一律不再单独计**（双算的唯一来源）")
        else:
            print("    ★ 未识别出进入万能的现金流 → 回计划书确认年金/红利是否自动转入")

    # -------- 零保额铁律：把保额列显式点名，防止人工构造时误取 --------
    sa_cols = [c for c in cols
               if ("保额" in c or "保险金额" in c) and "现金价值" not in c]
    if sa_cols:
        print("\n" + "─" * W)
        print("⛔ 保额型列（§7.1 零保额铁律 · **禁止取值**）")
        print("─" * W)
        for c in sa_cols:
            print(f"  {c}")
        print("  这些列只是**保险金额**，不是能拿回的钱，一律不得填进 policy 的任何价值字段。")
        print("  「保额」字样仅用于识别红利种类（如「累积红利保额」= 增额红利）；")
        print("  要取的数必须来自对应的**现金价值**列，或直接用合计列。")
        print("  实测误用后果：总利益虚高 42.9%、IRR 虚高约 1.45pp、回本年限提前 2 年。")

    # -------- 字段映射建议 --------
    print("\n" + "─" * W)
    print("建议 policy 字段映射")
    print("─" * W)
    # ★ 合计列优先（§7.11 铁律①）
    sumc = next((c for c in cols if has(c, KW_SUM) and "身故" not in c and "全残" not in c), None)
    if sumc:
        print(f"  ★★ 文档已给合计列「{sumc}」→ 按 §7.11 铁律① **直接抓该列**，不要组件求和；")
        print(f"      列名已含「总/合计」= 红利已含在内，红利类字段**全部留空**，否则重复计入。")
        print(f"      下面仅为校验用的参考映射：")
    cv_col = next((c for c in cols if "现金价值" in c and "红利" not in c
                   and not has(c, KW_SUM)), None) or "现金价值(保证)"
    print(f"  cv_guaranteed              ← {cv_col}" + ("   [保证口径]" if sumc else ""))
    if sumc:
        print(f"  cv_demo                    ← {sumc}   [演示口径 = 保证+红利]")
    if shape in ("年金", "两全"):
        bc = next((c for c in cols if has(c, KW_ANN + KW_ENDow)), None) or "生存保险金/满期金"
        print(f"  benefit_guaranteed         ← {bc}")
        if shape == "两全":
            print("  cv[满期年]                 ← **填 0**（满期终止现价归零，与满期金不可相加）")
    if d["cash"]:
        dest = cash_div_dest(cols, pol)
        if dest == "accum":
            print("  dividend_cv_guaranteed     ← 累积现金红利(含息)   [存量]")
            print("  dividend_annual_guaranteed ← 当年现金红利         [供 reaccum 复利修正]")
        elif dest == "withdraw":
            print("  dividend_cash_guaranteed   ← 当年现金红利         [流，逐年计入]")
            print("  ✗ 不要填 dividend_cv_*      （现金领走了，不是存量）")
        elif dest == "universal":
            print("  ✗ 不要填任何 dividend_*     （红利已进万能，只计 universal_*）")
    if d["pu"]:
        if sumc:
            print("  增额红利                    ← **不另加**（已含在合计列里）")
            cvp = next((c for c in cols if "红利保额" in c and "现金价值" in c), None)
            if cvp and cv_col:
                print(f"  列位校验                    ← {cv_col} + {cvp} 应 = {sumc}")
                print("                                （对不上就是列位认错了，回 §7.14 重判）")
        else:
            print("  增额红利                    ← 若表已单列「增额红利现金价值」则加；")
            print("                                若已含进 cv 列则**不另加**（用总利益列校验）")
    if d["term"]:
        print("  terminal_bonus_guaranteed  ← 终了红利现金价值（**累积值**，非当年值）")
    if d["spec"]:
        print("  特别红利                    ← 按给付时点计入（归 benefit 或 terminal_bonus）")
    if has_u:
        print("  universal_guaranteed       ← 万能账户**现金价值**（非保额；优先可领取额）")
        print(f"  benefit_in_universal       = {'true' if '年金/生存金' in uflows else 'false'}"
              "   ← 年金是否已在万能里")

    # -------- 总利益公式 --------
    parts = ["cv(N)"]
    if sumc:
        parts = [f"「{sumc}」列直接取值(N)"]
        if shape in ("年金", "两全") and not (has_u and "年金/生存金" in uflows):
            parts.append("Σbenefit(1..N)")
        if has_u:
            parts.append("universal(N)")
    else:
        if shape in ("年金", "两全") and not (has_u and "年金/生存金" in uflows):
            parts.append("Σbenefit(1..N)")
        if has_u:
            parts.append("universal(N)")
        if d["cash"]:
            dest = cash_div_dest(cols, pol)
            if dest == "accum":
                parts.append("dividend_cv(N)")
            elif dest == "withdraw":
                parts.append("Σdividend_cash(1..N)")
            elif dest == "universal":
                pass
        if d["term"]:
            parts.append("terminal_bonus(N)")
    print("\n" + "─" * W)
    print("生存总利益(N) = " + " + ".join(parts))
    print("─" * W)

    # -------- 冲突检查 --------
    warn = []
    # 万能 + 现金红利并存：列名分不清「红利留在主险累积生息」还是「红利也转进了万能」，
    # 而这两种情形的计法完全相反，是双算的高发处，必须显式确认。
    if has_u and dest in ("accum", "未知"):
        warn.append("万能账户与现金红利并存：列名无法区分「红利留在主险累积生息」还是"
                    "「红利也转入万能」。\n       若红利确实进万能 → 删掉 dividend_* 字段，只计 universal_*；"
                    "留在主险才加 dividend_cv(N)。\n       请回计划书「红利领取方式」确认，或直接看 "
                    "万能账户价值曲线是否已被红利抬高。")
    if has_u and "年金/生存金" in uflows and pol is not None:
        if not pol.get("benefit_in_universal"):
            warn.append("年金已进万能账户，但 policy 未设 benefit_in_universal=true → "
                        "Σbenefit 会被重复计入（实测虚高可达 70%+）")
    if pol is not None:
        if any(pol.get(f) or [] for f in ("dividend_cv_guaranteed", "dividend_cv_demo")) and \
           any(pol.get(f) or [] for f in ("dividend_cash_guaranteed", "dividend_cash_demo")):
            warn.append("dividend_cv_*(存量) 与 dividend_cash_*(流) 同时非零 → "
                        "同一笔红利被计了两次")
        if has_u and not pol.get("benefit_in_universal"):
            bg, ug = pol.get("benefit_guaranteed") or [], pol.get("universal_guaranteed") or []
            both = sum(1 for t in range(1, min(len(bg), len(ug))) if (bg[t] or 0) and (ug[t] or 0))
            if both >= 3:
                warn.append(f"benefit 与 universal 同时非零达 {both} 个年度 → 疑似重复计入")
        if shape == "两全":
            cv = pol.get("cv_guaranteed") or []
            ben = pol.get("benefit_guaranteed") or []
            if cv and ben and len(cv) == len(ben):
                n = len(cv) - 1
                if n > 0 and (cv[n] or 0) > 0 and (ben[n] or 0) > 0:
                    warn.append(f"满期年(n={n}) cv={cv[n]:,.0f} 与 benefit={ben[n]:,.0f} 同时非零 → "
                                "满期金与满年末现价只能取其一，不可相加")
    print("\n冲突检查：" + ("未发现重复计入风险 ✓" if not warn else ""))
    for i, w in enumerate(warn, 1):
        print(f"  ⚠ {i}. {w}")
    print()


def main():
    ap = argparse.ArgumentParser(
        description="生存总利益计法判定器（§7.16 决策树自动化）")
    ap.add_argument("--policy", help="已构造的 policy.json（反查字段是否填错）")
    ap.add_argument("--name", help="产品名称，如「XX年金保险（分红型）」")
    ap.add_argument("--columns", help="逗号分隔的列名/表头，如 保单年度,现金价值,生存保险金")
    args = ap.parse_args()

    if not args.policy and not args.columns and not args.name:
        ap.error("至少给 --columns 或 --policy 之一")

    pol = None
    name = args.name
    if args.policy:
        with open(args.policy, encoding="utf-8") as f:
            pol = json.load(f)
        name = name or pol.get("name", "")
    cols = [c.strip() for c in args.columns.split(",")] if args.columns else []
    emit(name, cols, pol)


if __name__ == "__main__":
    try:
        from _feedback_hook import install; install()
    except Exception:
        pass
    main()
