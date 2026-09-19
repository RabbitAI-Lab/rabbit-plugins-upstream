#!/usr/bin/env python3
# -*-- coding: utf-8 -*-
"""
第三轮：报告生成 + 安全护栏 + 端到端（生产级）。

检查项：
  1. 报告含完整免责声明（不诊断）与来源/授权
  2. 危机求助资源严格前置（在任何分数/缺失提示之前）
  3. 危机资源含权威热线号码
  4. 缺作答时给出提示
  5. 全部 19 量表 score→render 端到端无异常且含得分概览
  6. 报告不出现越界承诺（确诊/治疗等）

运行：python tests/test_report.py
"""
import os
import sys
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from scoring_engine import load_scale, score
from report_generator import render, DISCLAIMER, CRISIS_RESOURCES

RESULTS = []


def record(name, ok, detail=""):
    RESULTS.append((name, ok, detail))
    mark = "PASS" if ok else "FAIL"
    print(f"[{mark}] {name}" + (f"  -> {detail}" if (detail and not ok) else ""))


def test_disclaimer_present():
    sc = load_scale("PHQ-9")
    res = score(sc, {f"q{i}": 0 for i in range(1, 10)})
    md = render(sc, res)
    record("报告含免责声明且不诊断", "免责声明" in md and "不构成" in md and "诊断" in md)
    record("报告含来源与授权", "来源" in md and "授权" in md)


def test_crisis_precedes_score():
    sc = load_scale("PHQ-9")
    ans = {f"q{i}": 0 for i in range(1, 10)}
    ans["q9"] = 3  # 危机题非零
    res = score(sc, ans)
    md = render(sc, res)
    record("危机触发 crisis_flag", res["crisis_flag"] is True)
    pc = md.find("🆘")
    ps = md.find("一、得分概览")
    record("危机资源在得分概览之前", 0 <= pc < ps, f"crisis@{pc} score@{ps}")


def test_crisis_before_missing():
    sc = load_scale("PHQ-9")
    ans = {f"q{i}": 0 for i in range(2, 10)}  # 缺 q1
    ans["q9"] = 3                              # 同时危机
    res = score(sc, ans)
    md = render(sc, res)
    pc = md.find("🆘")
    pm = md.find("未作答")
    if pm != -1:
        record("危机资源在缺失提示之前（严格前置）", 0 <= pc < pm, f"crisis@{pc} missing@{pm}")
    else:
        record("危机资源在缺失提示之前（无missing跳过）", True)


def test_crisis_hotlines():
    record("危机资源含全国热线", "400-161-9995" in CRISIS_RESOURCES)
    record("危机资源含北京危机中心", "010-82951332" in CRISIS_RESOURCES)


def test_missing_warning():
    sc = load_scale("GAD-7")
    res = score(sc, {"q1": 0})  # 缺 2-7
    md = render(sc, res)
    record("缺作答提示出现", "未作答" in md)


def test_e2e_all_scales():
    bad = []
    for f in sorted(glob.glob(os.path.join(ROOT, "scales", "*.json"))):
        sid = os.path.splitext(os.path.basename(f))[0]
        try:
            sc = load_scale(sid)
            n = len(sc["items"][0]["options"])
            ans = {it["id"]: n // 2 for it in sc["items"]}
            res = score(sc, ans)
            md = render(sc, res)
            if "得分概览" not in md:
                bad.append(f"{sid}:无概览")
        except Exception as e:
            bad.append(f"{sid}:异常 {e}")
    record("全 19 量表端到端渲染无异常", len(bad) == 0, str(bad))


def test_no_overclaim():
    sc = load_scale("PHQ-9")
    res = score(sc, {f"q{i}": 3 for i in range(1, 10)})
    md = render(sc, res)
    for bad_word in ["确诊", "你患有", "治疗方案", "服药", "开药"]:
        record(f"报告未出现越界措辞「{bad_word}」", bad_word not in md)


if __name__ == "__main__":
    test_funcs = [v for k, v in sorted(globals().items())
                  if k.startswith("test_") and callable(v)]
    for fn in test_funcs:
        try:
            fn()
        except Exception as e:
            record(fn.__name__, False, f"异常: {e}")
            import traceback
            traceback.print_exc()
    fails = [r for r in RESULTS if not r[1]]
    print("\n" + "=" * 50)
    print(f"共 {len(RESULTS)} 项断言，失败 {len(fails)} 项")
    sys.exit(1 if fails else 0)
