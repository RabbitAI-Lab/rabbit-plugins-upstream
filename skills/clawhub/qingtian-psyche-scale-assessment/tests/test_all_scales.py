#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
强化回归：覆盖全部 19 个量表的 score -> render 端到端，
并对「全选最小 / 全选最大 / PHQ-9 高分危机」三种形态做断言。

目标：保证每个量表在极值作答下都能正确判级（不出现'未分级'），
且危机信号（PHQ-9 高分）在报告中严格前置，HTML 关键章节齐全。

运行：python tests/test_all_scales.py
"""
import os
import sys
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from scoring_engine import load_scale, score
from report_generator import render

RESULTS = []


def record(name, ok, detail=""):
    RESULTS.append((name, ok, detail))
    mark = "PASS" if ok else "FAIL"
    print(f"[{mark}] {name}" + (f"  -> {detail}" if (detail and not ok) else ""))


def all_answers(sc, mode):
    """mode=0 全选最小序号；mode=1 全选最大序号。"""
    return {it["id"]: (0 if mode == 0 else len(it["options"]) - 1)
            for it in sc["items"]}


def check_scale_extremes(sid):
    sc = load_scale(sid)
    bad = []
    for mode, label in ((0, "最小"), (1, "最大")):
        try:
            res = score(sc, all_answers(sc, mode))
            md = render(sc, res)
            for dim, lv in res["bands"].items():
                if lv == "未分级":
                    bad.append(f"{label}:{dim}=未分级")
            if "得分概览" not in md:
                bad.append(f"{label}:无概览")
            if "免责声明" not in md:
                bad.append(f"{label}:无免责声明")
        except Exception as e:
            bad.append(f"{label}:异常 {e}")
    record(f"[{sid}] 全选最小/最大 判级完整且渲染正常", len(bad) == 0, str(bad))


def check_phq9_high_crisis():
    """PHQ-9 总分很高但 q9=0（无自伤）也应经 high_risk 规则触发危机并前置。"""
    sc = load_scale("PHQ-9")
    n = len(sc["items"][0]["options"])
    ans = {it["id"]: n - 1 for it in sc["items"]}
    ans["q9"] = 0
    res = score(sc, ans)
    md = render(sc, res)
    ok = (res["crisis_flag"] is True
          and "🆘" in md
          and md.find("🆘") < md.find("一、得分概览"))
    record("PHQ-9 高分(q9=0) high_risk 危机触发且前置", ok,
           f"crisis={res['crisis_flag']}")


def check_phq9_selfharm_crisis():
    """PHQ-9 q9 非零（自伤）必须触发危机。"""
    sc = load_scale("PHQ-9")
    ans = {it["id"]: 0 for it in sc["items"]}
    ans["q9"] = 3
    res = score(sc, ans)
    md = render(sc, res)
    record("PHQ-9 q9 非零 危机触发", res["crisis_flag"] is True and "🆘" in md)


def check_sas_sds_correct_band():
    """SAS/SDS 标准分判级须与权威常模一致（回归锁）。"""
    for sid, expect in (("SAS", "轻度焦虑"), ("SDS", "轻度抑郁")):
        sc = load_scale(sid)
        # 全选序号1（score2）→ SAS 原始45/标准56.25；SDS 原始50/标准62.5
        res = score(sc, {it["id"]: 1 for it in sc["items"]})
        lv = res["bands"]["原始总分"]
        record(f"[{sid}] 标准分判级={expect}", lv == expect, lv)


if __name__ == "__main__":
    for f in sorted(glob.glob(os.path.join(ROOT, "scales", "*.json"))):
        sid = os.path.splitext(os.path.basename(f))[0]
        check_scale_extremes(sid)
    check_phq9_high_crisis()
    check_phq9_selfharm_crisis()
    check_sas_sds_correct_band()

    fails = [r for r in RESULTS if not r[1]]
    print("\n" + "=" * 50)
    print(f"共 {len(RESULTS)} 项断言，失败 {len(fails)} 项")
    sys.exit(1 if fails else 0)
