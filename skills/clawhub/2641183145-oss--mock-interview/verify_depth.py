#!/usr/bin/env python3
"""量一下点评到底变长了多少 —— 用户反馈「太短」,得能证明改到位了。"""
import json
import re
import sys

import console  # noqa: F401


def main():
    html = open("data/score-report.html", encoding="utf-8").read()
    m = re.search(r'<script\b[^>]*\bid=["\']score-data["\'][^>]*>(.*?)</script>',
                  html, re.S)
    d = json.loads(m.group(1).replace("<\\/", "</"))

    print("=== 结构化字段是否齐全 ===")
    ok = True
    for q in d["per_question"]:
        qid = q["qid"]
        n_s = len(q.get("strengths") or [])
        n_w = len(q.get("weaknesses") or [])
        has_rw = bool((q.get("rewrite") or {}).get("after"))
        if not (n_s and n_w and has_rw):
            print(f"✗ {qid}: strengths={n_s} weaknesses={n_w} rewrite={has_rw}")
            ok = False
        else:
            print(f"✓ {qid}: {n_s} 条优点, {n_w} 条问题, 有改写示范")

    print("\n=== 每题点评字数(合成后的 evidence + fix)===")
    total = 0
    for q in d["per_question"]:
        n = len(q.get("evidence") or "") + len(q.get("fix") or "")
        total += n
        bar = "█" * (n // 60)
        print(f"  {q['qid']}: {n:>4} 字 {bar}")

    n_sum = len(d.get("summary") or "")
    bn = d["bottleneck"]
    n_bn = (len(bn.get("root_cause") or "")
            + sum(len(s) for s in bn.get("improvement_plan") or [])
            + sum(len(e.get("note") or "") for e in bn.get("evidence_across_questions") or []))

    print(f"\n  全局 summary: {n_sum} 字")
    print(f"  瓶颈分析:     {n_bn} 字(根因 + 3 步计划 + 跨题证据)")
    print(f"  逐题合计:     {total} 字")
    print(f"  ── 报告总计:  {total + n_sum + n_bn} 字")

    print("\n=== 引用覆盖率 ===")
    session = json.load(open("data/session.json", encoding="utf-8"))
    answers = {a["qid"]: a["text"] for a in session["answers"]}
    n_quotes = 0
    for q in d["per_question"]:
        qs = [s["quote"] for s in q.get("strengths") or []]
        qs += [w["quote"] for w in q.get("weaknesses") or []]
        rw = q.get("rewrite") or {}
        if rw.get("before"):
            qs.append(rw["before"])
        n_quotes += len(qs)
    n_quotes += len(bn.get("evidence_across_questions") or [])
    print(f"  共引用用户原话 {n_quotes} 处,覆盖 {len(answers)} 道题")
    print(f"  平均每题 {n_quotes / len(d['per_question']):.1f} 处引用")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
