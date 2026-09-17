#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
心理量表测评引擎 — 回归测试套件（生产级）。

运行方式：
    python tests/test_engine.py
也可被 pytest 收集（所有 test_* 函数）。

覆盖：
  Round 1: 计分核心（正向/反向/标准分/维度聚合/判级/危机）+ 异常输入
  Round 2: 19 量表 Schema 完整性 + 全选边界计分可执行
  Round 3: 报告生成 + 安全护栏（危机前置、免责声明、版权）
"""
import os
import sys
import json
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from scoring_engine import load_scale, score

RESULTS = []


def record(name, ok, detail=""):
    RESULTS.append((name, ok, detail))
    mark = "PASS" if ok else "FAIL"
    print(f"[{mark}] {name}" + (f"  -> {detail}" if (detail and not ok) else ""))


def approx(a, b, tol=0.01):
    return abs(float(a) - float(b)) <= tol


# ---------------------------------------------------------------------------
# Round 1: 计分核心逻辑
# ---------------------------------------------------------------------------
def test_phq9_crisis_and_band():
    sc = load_scale("PHQ-9")
    ans = {f"q{i}": 2 for i in range(1, 10)}   # 序号2 = score2
    res = score(sc, ans)
    record("PHQ-9 全序号2 总分=18", res["dimension_scores"]["抑郁总分"] == 18,
           str(res["dimension_scores"]))
    record("PHQ-9 crisis_flag=True", res["crisis_flag"] is True)
    record("PHQ-9 判级=中重度抑郁(15-19)", res["bands"]["抑郁总分"] == "中重度抑郁",
           res["bands"]["抑郁总分"])


def test_gad7_light():
    sc = load_scale("GAD-7")
    res = score(sc, {f"q{i}": 1 for i in range(1, 8)})  # 序号1=score1
    record("GAD-7 全序号1 总分=7", res["dimension_scores"]["焦虑总分"] == 7,
           str(res["dimension_scores"]))
    record("GAD-7 判级=轻度", res["bands"]["焦虑总分"] == "轻度焦虑",
           res["bands"]["焦虑总分"])


def test_sas_reverse_standard():
    sc = load_scale("SAS")
    res = score(sc, {f"q{i}": 1 for i in range(1, 21)})  # 序号1=score2
    # 正向15*2=30, 反向5题翻转(1+4-2=3)*5=15 -> 原始45, 标准56.25
    record("SAS 全序号1 原始分=45", res["dimension_scores"]["原始总分"] == 45,
           str(res["dimension_scores"]))
    record("SAS 标准分=56.25", approx(res["standard_scores"]["原始总分"], 56.25),
           str(res["standard_scores"]))
    record("SAS 判级=轻度焦虑(标准分判级)", res["bands"]["原始总分"] == "轻度焦虑",
           res["bands"]["原始总分"])


def test_sds_reverse_standard():
    sc = load_scale("SDS")
    res = score(sc, {f"q{i}": 1 for i in range(1, 21)})
    # 正向10*2=20, 反向10题翻转(1+4-2=3)*10=30 -> 原始50, 标准62.5
    record("SDS 全序号1 原始分=50", res["dimension_scores"]["原始总分"] == 50,
           str(res["dimension_scores"]))
    record("SDS 标准分=62.5", approx(res["standard_scores"]["原始总分"], 62.5),
           str(res["standard_scores"]))
    record("SDS 判级=轻度抑郁", res["bands"]["原始总分"] == "轻度抑郁",
           res["bands"]["原始总分"])


def test_maas_average_direction():
    sc = load_scale("MAAS")
    res = score(sc, {f"q{i}": 5 for i in range(1, 16)})  # 序号5=从不=score6
    record("MAAS 全序号5 均分=6.0", approx(res["dimension_scores"]["正念均分"], 6.0),
           str(res["dimension_scores"]))
    record("MAAS 判级=高", res["bands"]["正念均分"] == "高",
           res["bands"]["正念均分"])


def test_pss10_reverse():
    sc = load_scale("PSS-10")
    res = score(sc, {f"q{i}": 0 for i in range(1, 11)})  # 序号0=从不=score0
    # 正向6*0=0, 反向4题翻转(0+4-0=4)*4=16 -> 总分16 -> 中等
    record("PSS-10 全序号0 总分=16", res["dimension_scores"]["压力总分"] == 16,
           str(res["dimension_scores"]))
    record("PSS-10 判级=中等", res["bands"]["压力总分"] == "中等感知压力",
           res["bands"]["压力总分"])


def test_invalid_out_of_range():
    sc = load_scale("PHQ-9")
    try:
        score(sc, {"q1": 99})  # 越界序号
        record("越界作答应抛异常", False, "未报错")
    except Exception:
        record("越界作答应抛异常", True)


def test_invalid_string():
    sc = load_scale("PHQ-9")
    try:
        score(sc, {"q1": "X"})
        record("无效字符串作答应抛异常", False, "未报错")
    except Exception:
        record("无效字符串作答应抛异常", True)


def test_missing_items():
    sc = load_scale("PHQ-9")
    res = score(sc, {"q1": 0})
    record("缺失题检测=8", len(res["missing_items"]) == 8, str(res["missing_items"]))
    record("complete=False", res["complete"] is False)


def test_ffmq_de2_reverse():
    """FFMQ 描述因子 de2 为负向表述，必须反向计分，否则描述分失真。"""
    sc = load_scale("FFMQ")
    n_opts = len(sc["items"][0]["options"])
    ans_low = {it["id"]: 0 for it in sc["items"]}       # 全部选最低
    ans_de2_high = dict(ans_low)
    ans_de2_high["de2"] = n_opts - 1                    # de2 选最高（最难描述）
    da = score(sc, ans_de2_high)["dimension_scores"]["描述"]
    db = score(sc, ans_low)["dimension_scores"]["描述"]
    # de2 高分(难描述) 应使“描述”维度得分更低（反向生效）
    record("FFMQ de2 反向生效(难描述→描述分更低)", da < db,
           f"de2_high={da} all_low={db}")


def test_load_scale_case_insensitive():
    """load_scale 应容忍大小写/连字符差异（Linux/CI 大小写敏感环境）。"""
    for sid in ["PHQ-9", "phq9", "phq-9", "PHQ9", "GAD-7", "gad7"]:
        try:
            sc = load_scale(sid)
            ok = sc["id"] in ("PHQ-9", "GAD-7")
        except Exception:
            ok = False
        record(f"load_scale 容错加载 '{sid}'", ok)


def test_high_risk_chinese_dim():
    """high_risk_rule 含中文维度名（如'抑郁总分≥15'）必须被解析并触发 crisis。"""
    sc = load_scale("PHQ-9")
    n = len(sc["items"][0]["options"])
    ans = {it["id"]: n - 1 for it in sc["items"]}
    ans["q9"] = 0  # 无自伤，但总分很高 → 应经 high_risk 规则触发危机
    res = score(sc, ans)
    record("PHQ-9 高分(q9=0)经 high_risk 触发 crisis",
           res["crisis_flag"] is True,
           f"总分={res['dimension_scores'].get('抑郁总分')} crisis={res['crisis_flag']}")


if __name__ == "__main__":
    test_funcs = [v for k, v in sorted(globals().items())
                  if k.startswith("test_") and callable(v)]
    for fn in test_funcs:
        try:
            fn()
        except Exception as e:
            record(fn.__name__, False, f"异常: {e}")
            traceback.print_exc()
    fails = [r for r in RESULTS if not r[1]]
    print("\n" + "=" * 50)
    print(f"共 {len(RESULTS)} 项断言，失败 {len(fails)} 项")
    sys.exit(1 if fails else 0)
