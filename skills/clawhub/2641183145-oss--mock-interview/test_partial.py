#!/usr/bin/env python3
"""中途退出场景:只答 3 题就打分,报告应标为低置信度。"""
import copy
import json
import os
import subprocess
import sys

import console  # noqa: F401

ROOT = os.path.dirname(os.path.abspath(__file__))


def main():
    session = json.load(open("data/session.example.json", encoding="utf-8"))
    scores = json.load(open("data/scores.example.json", encoding="utf-8"))

    # 只留前 3 题的回答
    session["answers"] = [
        {"qid": "q1", "text": "第一题的回答,压测发现 p99 800ms。",
         "input_mode": "voice", "duration_sec": 60,
         "submitted_at": "2026-08-27 14:30:00"},
        {"qid": "q2", "text": "第二题的回答,wrk 压的 5000 QPS。",
         "input_mode": "text", "duration_sec": None,
         "submitted_at": "2026-08-27 14:33:00"},
        {"qid": "q3", "text": "第三题的回答,代码我一个人写的。",
         "input_mode": "text", "duration_sec": None,
         "submitted_at": "2026-08-27 14:36:00"},
    ]
    session["status"] = "awaiting_answers"  # 用户直接关了页面,没答完
    json.dump(session, open("data/session.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    # 评分也只覆盖 3 题,并重算 overall
    partial = copy.deepcopy(scores)
    partial["per_question"] = partial["per_question"][:3]
    dims = ("substance", "structure", "relevance", "credibility", "differentiation")
    for d in dims:
        vals = [q["scores"][d] for q in partial["per_question"]]
        partial["overall"][d] = round(sum(vals) / len(vals), 1)
    lowest = min(dims, key=lambda d: partial["overall"][d])
    partial["bottleneck"]["dimension"] = lowest
    partial["bottleneck"].pop("label", None)
    partial["bottleneck"].pop("score", None)
    json.dump(partial, open("data/scores.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    r = subprocess.run([sys.executable, "build_report.py"],
                       capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
    print(r.stdout.strip())
    if r.stderr.strip():
        print("stderr:", r.stderr.strip())
    if r.returncode != 0:
        print("✗ build_report 失败")
        return 1

    import re
    html = open("data/score-report.html", encoding="utf-8").read()
    m = re.search(r'<script id="score-data"[^>]*>(.*?)</script>', html, re.S)
    d = json.loads(m.group(1).replace("<\\/", "</"))

    ok = True
    if not d["partial"]:
        print("✗ partial 应为 True")
        ok = False
    if d["answered_count"] != 3:
        print(f"✗ answered_count 应为 3,实得 {d['answered_count']}")
        ok = False
    if len(d["per_question"]) != 3:
        print(f"✗ per_question 应为 3 条,实得 {len(d['per_question'])}")
        ok = False
    if d["bottleneck"].get("label") is None:
        print("✗ bottleneck.label 未回填")
        ok = False

    if ok:
        print(f"✓ partial=True, answered=3/5, 瓶颈={d['bottleneck']['label']} "
              f"({d['bottleneck']['score']})")
        print("✓ 低置信度路径正常")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
