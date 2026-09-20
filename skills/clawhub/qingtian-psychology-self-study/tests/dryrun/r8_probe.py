# -*- coding: utf-8 -*-
"""R8 探针：验证「作答键格式」与计分引擎的一致性（复现 D 级缺陷）。
按 SKILL.md §6 文档约定：答案键应为 q1..qn（与 items 顺序一致）。
引擎 score() 当前按 item_id 匹配。本脚本两者都试，证明多维度量表的文档格式会失败。
"""
import json, os, subprocess, sys

SKILL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SC = os.path.join(SKILL, "assessment", "scripts", "score_and_report.py")
OUT = os.path.join(SKILL, "tests", "dryrun", "r8_out")
os.makedirs(OUT, exist_ok=True)

def run(sid, answers):
    p = os.path.join(OUT, f"{sid}_answers.json")
    json.dump(answers, open(p, "w"), ensure_ascii=False)
    r = subprocess.run([sys.executable, SC, sid, p, OUT],
                       capture_output=True, text=True)
    res = None
    for line in r.stdout.splitlines():
        if line.startswith("RESULT_JSON>>>"):
            res = json.loads(line.split(">>>", 1)[1])
    return r.returncode, res

# PANAS 20 题，文档格式 q1..q20（SKILL.md §6 让 LLM 这么写）
doc_ans = {f"q{i}": (i % 5) for i in range(1, 21)}
# 同份答案，按 item_id 重写（pa1..pa10, na1..na10，与 items 顺序一致）
scale = json.load(open(os.path.join(SKILL, "assessment", "scales", "PANAS.json"), encoding="utf-8"))
id_ans = {}
for i, it in enumerate(scale["items"]):
    id_ans[it["id"]] = doc_ans[f"q{i+1}"]

print("=== PANAS · 文档格式 q1..q20（SKILL.md §6 约定）===")
rc, res = run("PANAS", doc_ans)
print(f"  退出码={rc}  完整={res.get('complete') if res else None}  缺失项数={len(res.get('missing_items', [])) if res else 'N/A'}")
print("  结论:", "✅ 可计分" if (rc == 0 and res and res.get("complete")) else "❌ 计分失败（缺失全部题目）")

print("\n=== PANAS · item_id 格式（pa1/na1…）===")
rc2, res2 = run("PANAS", id_ans)
print(f"  退出码={rc2}  dimension_scores={list(res2['dimension_scores'].keys()) if res2 else None}")
print("  结论:", "✅ 可计分" if (rc2 == 0 and res2 and res2.get("complete")) else "❌ 计分失败")

print("\n=== 关键判定 ===")
print("  若『文档格式 q1..q20』计分失败而『item_id 格式』成功 → 证实：")
print("  SKILL.md §6 的 q1..qn 作答约定 与 引擎按 item_id 匹配 不一致，")
print("  除 PHQ-9（恰好用 q1..q9 作 item id）外，所有量表按文档作答都将失败。")
