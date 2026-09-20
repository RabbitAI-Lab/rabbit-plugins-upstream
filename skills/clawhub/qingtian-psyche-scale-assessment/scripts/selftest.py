#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""快速冒烟测试：覆盖正向/反向/标准分/危机/多维度/判级（带断言）。

⚠️ 作答口径：answers 的值是“选项序号（0 起）”，不是分值。
   例如 PHQ-9 第 0 项是「完全不会」(0分)，第 2 项是「一半以上的天数」(2分)。

完整回归套件见 tests/ 目录：
    python tests/test_engine.py   计分核心 + 输入校验
    python tests/test_schema.py   19 量表 Schema 完整性
    python tests/test_report.py   报告生成 + 安全护栏
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from scoring_engine import load_scale, score


def approx(a, b, tol=0.01):
    return abs(float(a) - float(b)) <= tol


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f"  {detail}" if (detail and not cond) else ""))
    return cond


def main():
    ok = True

    # 1) PHQ-9 危机 + 中重度（全序号2 = score各2，q9非零触发危机）
    sc = load_scale("PHQ-9")
    res = score(sc, {f"q{i}": 2 for i in range(1, 10)})
    ok &= check("PHQ-9 全序号2 总分=18", res["dimension_scores"]["抑郁总分"] == 18)
    ok &= check("PHQ-9 crisis_flag", res["crisis_flag"] is True)
    ok &= check("PHQ-9 中重度抑郁", res["bands"]["抑郁总分"] == "中重度抑郁")

    # 2) GAD-7 全序号1（score1）→ 7 → 轻度
    sc = load_scale("GAD-7")
    res = score(sc, {f"q{i}": 1 for i in range(1, 8)})
    ok &= check("GAD-7 全序号1 总分=7", res["dimension_scores"]["焦虑总分"] == 7)
    ok &= check("GAD-7 轻度焦虑", res["bands"]["焦虑总分"] == "轻度焦虑")

    # 3) SAS 反向+标准分（全序号1 = score2）：正向15*2=30，反向5*(1+4-2=3)=15 → 原始45 → 标准56.25
    sc = load_scale("SAS")
    res = score(sc, {f"q{i}": 1 for i in range(1, 21)})
    ok &= check("SAS 全序号1 原始分=45", res["dimension_scores"]["原始总分"] == 45)
    ok &= check("SAS 标准分=56.25", approx(res["standard_scores"]["原始总分"], 56.25))
    ok &= check("SAS 轻度焦虑(标准分判级)", res["bands"]["原始总分"] == "轻度焦虑")

    # 4) SDS 反向+标准分（全序号1 = score2）：正向10*2=20，反向10*(1+4-2=3)=30 → 原始50 → 标准62.5
    sc = load_scale("SDS")
    res = score(sc, {f"q{i}": 1 for i in range(1, 21)})
    ok &= check("SDS 全序号1 原始分=50", res["dimension_scores"]["原始总分"] == 50)
    ok &= check("SDS 标准分=62.5", approx(res["standard_scores"]["原始总分"], 62.5))
    ok &= check("SDS 轻度抑郁(标准分判级)", res["bands"]["原始总分"] == "轻度抑郁")

    # 5) MAAS 全序号5（从不 = score6）→ 均分6 → 高（注意传的是序号不是分值）
    sc = load_scale("MAAS")
    res = score(sc, {f"q{i}": 5 for i in range(1, 16)})
    ok &= check("MAAS 全序号5 均分=6.0", approx(res["dimension_scores"]["正念均分"], 6.0))
    ok &= check("MAAS 高", res["bands"]["正念均分"] == "高")

    # 6) PSS-10 反向（全序号0 = 从不 score0）：正向6*0=0，反向4*(0+4-0=4)=16 → 总分16 → 中等
    sc = load_scale("PSS-10")
    res = score(sc, {f"q{i}": 0 for i in range(1, 11)})
    ok &= check("PSS-10 全序号0 总分=16", res["dimension_scores"]["压力总分"] == 16)
    ok &= check("PSS-10 中等", res["bands"]["压力总分"] == "中等感知压力")

    # 7) 异常输入必须报错（越界 / 无效字符串）
    sc = load_scale("PHQ-9")
    try:
        score(sc, {"q1": 99})
        ok &= check("越界作答报错", False, "未报错")
    except Exception:
        ok &= check("越界作答报错", True)
    try:
        score(sc, {"q1": "X"})
        ok &= check("无效作答报错", False, "未报错")
    except Exception:
        ok &= check("无效作答报错", True)

    print("\n冒烟测试：", "全部通过 ✅" if ok else "存在失败 ❌")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
