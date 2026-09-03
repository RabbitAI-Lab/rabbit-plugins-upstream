#!/usr/bin/env python3
"""校验器的负向测试。

build_report.py 的校验是防 LLM 出错的唯一一道闸,得确认它真的拦得住。
"""
import copy
import json
import sys

import console  # noqa: F401
from build_report import check_consistency, validate

GOOD = json.load(open("data/scores.example.json", encoding="utf-8"))

CASES = []


def case(name, mutate, expect_substr):
    d = copy.deepcopy(GOOD)
    mutate(d)
    CASES.append((name, d, expect_substr))


def _set_overall(d, dim, val):
    d["overall"][dim] = val


case("overall 缺维度", lambda d: d["overall"].pop("differentiation"), "differentiation")
case("overall 超范围", lambda d: _set_overall(d, "substance", 7.0), "超出 1-5")
case("overall 非数字", lambda d: _set_overall(d, "structure", "高"), "不是数字")
case("逐题分数非整数", lambda d: d["per_question"][0]["scores"].__setitem__("substance", 3.5), "必须是整数")
case("逐题分数超范围", lambda d: d["per_question"][1]["scores"].__setitem__("relevance", 0), "超出 1-5")
case("fix 缺失", lambda d: d["per_question"][3].pop("fix"), "fix 为空")
case("fix 太短(空话)", lambda d: d["per_question"][3].__setitem__("fix", "注意量化。"), "fix 太短")
case("per_question 为空", lambda d: d.__setitem__("per_question", []), "per_question")
case("bottleneck 缺失", lambda d: d.pop("bottleneck"), "bottleneck")
case("bottleneck 维度非法", lambda d: d["bottleneck"].__setitem__("dimension", "attitude"), "必须是")

# ---- 新增:点评深度相关 ----
case("strengths 缺失", lambda d: d["per_question"][0].pop("strengths"), "strengths 缺失")
case("strengths 为空数组", lambda d: d["per_question"][0].__setitem__("strengths", []), "strengths 缺失")
case("strength.quote 为空",
     lambda d: d["per_question"][0]["strengths"][0].__setitem__("quote", ""), "quote 为空")
case("strength.why 太短",
     lambda d: d["per_question"][0]["strengths"][0].__setitem__("why", "很好"), "why 太短")
case("weaknesses 缺失", lambda d: d["per_question"][1].pop("weaknesses"), "weaknesses 缺失")
case("weakness.problem 太短",
     lambda d: d["per_question"][1]["weaknesses"][0].__setitem__("problem", "缺量化"), "problem 太短")
case("weakness.dimension 非法",
     lambda d: d["per_question"][1]["weaknesses"][0].__setitem__("dimension", "tone"), "dimension 必须是")
case("rewrite 缺失", lambda d: d["per_question"][2].pop("rewrite"), "rewrite 缺失")
case("rewrite.after 为空",
     lambda d: d["per_question"][2]["rewrite"].__setitem__("after", ""), "rewrite.after 为空")
case("rewrite.what_changed 太短",
     lambda d: d["per_question"][2]["rewrite"].__setitem__("what_changed", "改了"), "what_changed 太短")
case("summary 缺失", lambda d: d.pop("summary"), "缺少 summary")
case("summary 太短", lambda d: d.__setitem__("summary", "总体还不错,继续努力。"), "summary 太短")
case("root_cause 太短",
     lambda d: d["bottleneck"].__setitem__("root_cause", "差异化不足。"), "root_cause 太短")
case("evidence_across_questions 只有一条",
     lambda d: d["bottleneck"].__setitem__("evidence_across_questions",
                                           d["bottleneck"]["evidence_across_questions"][:1]),
     "至少两条")
case("evidence_across_questions 缺失",
     lambda d: d["bottleneck"].pop("evidence_across_questions"), "至少两条")
case("improvement_plan 不是 3 步",
     lambda d: d["bottleneck"].__setitem__("improvement_plan",
                                           d["bottleneck"]["improvement_plan"][:2]),
     "必须是 3 步")
case("improvement_plan 步骤太短",
     lambda d: d["bottleneck"]["improvement_plan"].__setitem__(0, "多练习"), "太短")

WARN_CASES = []


def warn_case(name, mutate, expect_substr):
    d = copy.deepcopy(GOOD)
    mutate(d)
    WARN_CASES.append((name, d, expect_substr))


warn_case("overall 与逐题均值不符", lambda d: _set_overall(d, "substance", 5.0), "逐题均值")
warn_case("bottleneck 不是最低分维度",
          lambda d: d["bottleneck"].__setitem__("dimension", "credibility"), "最低分维度")


# ---- 引用落地:模型编造用户没说过的话 ----
GROUNDED_SESSION = {
    "answers": [
        {"qid": "q1", "text": "我测了本地缓存、Redis、多级缓存三种方案,最后选 Redis。"},
        {"qid": "q2", "text": "压测环境测的,5000 QPS 打了十分钟。"},
    ]
}


def quote_cases():
    from build_report import check_quotes_grounded
    results = []

    # 正样本:引用能在原文找到
    good = {
        "per_question": [{
            "qid": "q1",
            "strengths": [{"quote": "测了本地缓存、Redis、多级缓存三种方案", "why": "x" * 30}],
            "weaknesses": [{"quote": "最后选 Redis", "problem": "y" * 40, "dimension": "substance"}],
            "rewrite": {"before": "最后选 Redis", "after": "...", "what_changed": "z" * 40},
        }],
        "bottleneck": {"evidence_across_questions": [
            {"qid": "q2", "quote": "5000 QPS 打了十分钟", "note": "n"}]},
    }
    results.append(("引用能对上原文", check_quotes_grounded(good, GROUNDED_SESSION), 0))

    # 负样本:编造的引用
    bad = copy.deepcopy(good)
    bad["per_question"][0]["strengths"][0]["quote"] = "我还做了服务网格改造"
    results.append(("编造的 strength 引用", check_quotes_grounded(bad, GROUNDED_SESSION), 1))

    bad2 = copy.deepcopy(good)
    bad2["bottleneck"]["evidence_across_questions"][0]["quote"] = "我用了 Kafka 削峰"
    results.append(("编造的 bottleneck 引用", check_quotes_grounded(bad2, GROUNDED_SESSION), 1))

    # 标点差异不该误报
    punct = copy.deepcopy(good)
    punct["per_question"][0]["strengths"][0]["quote"] = "测了本地缓存,Redis,多级缓存三种方案"
    results.append(("中英标点差异不误报", check_quotes_grounded(punct, GROUNDED_SESSION), 0))

    return results


def main():
    failed = 0

    print("=== 正样本 ===")
    errs = validate(GOOD)
    if errs:
        print(f"✗ 正常数据被误报: {errs}")
        failed += 1
    else:
        print("✓ scores.example.json 通过校验")
    if check_consistency(GOOD):
        print(f"✗ 正常数据触发一致性警告: {check_consistency(GOOD)}")
        failed += 1
    else:
        print("✓ 无一致性警告")

    print("\n=== 负样本(应全部被拦)===")
    for name, data, expect in CASES:
        errs = validate(data)
        hit = any(expect in e for e in errs)
        if hit:
            print(f"✓ {name}")
        else:
            print(f"✗ {name} —— 没拦住(期望含 {expect!r},实得 {errs})")
            failed += 1

    print("\n=== 一致性警告(应提示但不阻断)===")
    for name, data, expect in WARN_CASES:
        warns = check_consistency(data)
        if any(expect in w for w in warns):
            print(f"✓ {name}")
        else:
            print(f"✗ {name} —— 没警告(期望含 {expect!r},实得 {warns})")
            failed += 1

    print("\n=== 引用落地(防模型编造用户原话)===")
    qcases = quote_cases()
    for name, warns, expect_n in qcases:
        if (len(warns) > 0) == (expect_n > 0):
            print(f"✓ {name}")
        else:
            print(f"✗ {name} —— 期望{'有' if expect_n else '无'}警告,实得 {warns}")
            failed += 1

    print()
    total = 2 + len(CASES) + len(WARN_CASES) + len(qcases)
    if failed:
        print(f"✗ {failed}/{total} 项未通过")
        return 1
    print(f"✓ 全部 {total} 项通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
