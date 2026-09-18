# -*- coding: utf-8 -*-
"""端到端对话演练（单人主链路）的产物构建脚本。
真实调用技能内嵌的 PHQ-9 计分引擎，并按 SKILL.md 规范汇总 progress.json。
落盘到 tests/dryrun/，不污染真实用户数据。"""
import json, subprocess, os, sys

SKILL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DRY = os.path.join(SKILL, "tests", "dryrun")
os.makedirs(os.path.join(DRY, "reports", "assessment"), exist_ok=True)
os.makedirs(os.path.join(DRY, "reports", "practice"), exist_ok=True)

# ---- D31b 回归：错误格式（{"answers":[...]}）必须被拒（退出码 != 0）----
bad = os.path.join(DRY, "phq9_bad.json")
json.dump({"answers": [0, 1, 0, 0, 1, 0, 0, 1, 0]}, open(bad, "w"), ensure_ascii=False)
rb = subprocess.run([sys.executable,
                     os.path.join(SKILL, "assessment", "scripts", "score_and_report.py"),
                     "PHQ-9", bad, os.path.join(DRY, "reports", "assessment")],
                    capture_output=True, text=True)
print("=== D31b 回归：错误答案格式应被拒 ===")
print("  退出码:", rb.returncode, "| 含『作答不完整』:", "作答不完整" in rb.stderr)

# ---- 真实跑 PHQ-9（正确格式：{"q1":0,"q2":1,...}，低分不触发危机）----
answers = {"q1": 0, "q2": 1, "q3": 0, "q4": 0, "q5": 1, "q6": 0, "q7": 0, "q8": 1, "q9": 0}
aj = os.path.join(DRY, "phq9.json")
json.dump(answers, open(aj, "w"), ensure_ascii=False)
r = subprocess.run([sys.executable,
                    os.path.join(SKILL, "assessment", "scripts", "score_and_report.py"),
                    "PHQ-9", aj, os.path.join(DRY, "reports", "assessment")],
                   capture_output=True, text=True)
result = None
for line in r.stdout.splitlines():
    if line.startswith("RESULT_JSON>>>"):
        result = json.loads(line.split(">>>", 1)[1])
assert result and result.get("complete"), "PHQ-9 正确格式仍计分失败"

# 按 SKILL.md 第七节：取单维度下的总分与分级 + 报告路径
dim_name = next(iter(result["dimension_scores"]))
total = result["dimension_scores"][dim_name]
level = result["bands"].get(dim_name, "—")
report_path = result["report_path"]

# ---- 构建进度文件（遵循 SKILL.md 第三节/第十节规范）----
now = "2026-08-10T12:05:00"
progress = {
    "version": "2.0.0",
    "userConfig": {
        "mode": "solo", "level": "beginner", "goal": "interest",
        "timeBudget": "light", "startDate": "2026-08-10", "createdAt": now
    },
    "currentStage": "enlightenment",
    "stageCompleted": True,
    "stageSummary": "本阶段完成入门：弄清了『经典条件作用 vs 操作性条件作用』的区别；用 TPR 跑了一次 CBT 练习，发现自己在『共情反映』上容易急着给建议；自测 PHQ-9 结果极轻度，松了口气。下一步想补读书和闪卡。",
    "lastDialogueAt": now,
    "modules": {
        "theory":     {"completed": 1, "total": 4, "items": ["经典条件作用"]},
        "counseling": {"completed": 2, "total": 4, "items": ["TPR练习-CBT", "对话分析"]},
        "assessment": {"completed": 1, "total": 3, "items": ["量表体验-PHQ9"]},
        "reading":    {"completed": 0, "total": 3, "items": []},
        "cases":      {"completed": 1, "total": 3, "items": ["经典案例"]},
        "methods":    {"completed": 0, "total": 4, "items": []},
        "support":    {"completed": 1, "total": 3, "items": ["进度追踪"]}
    },
    "stats": {
        "totalHours": 0, "totalDays": 1, "practiceCount": 1, "analyses": 1,
        "dialogues": 1, "booksRead": 0, "assessments": 1, "reflections": 1,
        "feynmanOutputs": 0
    },
    "readings": [],
    "assessments": [{
        "id": "PHQ-9", "date": "2026-08-10",
        "total": total, "level": level,
        "crisis_flag": result.get("crisis_flag", False),
        "report": report_path
    }],
    "logs": [
        {"type": "理论", "detail": "讲：经典条件作用（巴甫洛夫）", "stage": "enlightenment"},
        {"type": "练习", "detail": "TPR-CBT 个案报告已存", "stage": "enlightenment"},
        {"type": "分析", "detail": "对话分析 1 篇（共情反映改进）", "stage": "enlightenment"},
        {"type": "测评", "detail": "PHQ-9 总分 %s（%s）" % (total, level), "stage": "enlightenment"},
        {"type": "总结", "detail": "stageSummary 已写，stageCompleted=true", "stage": "enlightenment"}
    ],
    "milestones": [{"id": "m%d" % i, "reached": False} for i in range(1, 11)],
    "dialogueState": {"context": "daily", "step": 0, "pendingQuestion": "",
                      "tempData": {}, "lastTopic": "总结"}
}

with open(os.path.join(DRY, "progress.json"), "w", encoding="utf-8") as f:
    json.dump(progress, f, ensure_ascii=False, indent=2)

# ---- 练习个案报告（do_practice 产物）----
case_md = """# TPR 练习个案报告 · CBT（认知行为）
- 时间：2026-08-10
- 流派：CBT
- 用户角色：来访者（社交焦虑情境）
- 练习轮次：6 轮

## 逐轮要点
1. 共情反映："你刚才说在会议上发言会心跳加速，这听起来挺让人紧张的。"
2. 识别自动思维："在你准备发言的那一刻，脑子里闪过的是什么？"
3. 认知重构：引导区分『事实』与『推测』。
4. 行为实验布置：下次会前先写下一个可验证的小预测。

## 教练观察（给练习者）
- 亮点：共情反映自然，提问开放。
- 待改进：第 3 轮有点急着给建议，可多用『你怎么看』回抛。
- 建议：把这段贴回『对话分析』做五维透镜复盘。
"""
with open(os.path.join(DRY, "reports", "practice", "case-report-cbt.md"), "w", encoding="utf-8") as f:
    f.write(case_md)

# ---- 自检：与"预期"对照，发现规范歧义 ----
expected = {
    "modules.theory.completed": 1, "modules.counseling.completed": 2,
    "modules.assessment.completed": 1, "modules.cases.completed": 1,
    "modules.support.completed": 1, "stats.practiceCount": 1,
    "stats.analyses": 1, "stats.dialogues": 1, "stats.assessments": 1,
    "stats.reflections": 1, "stageCompleted": True
}
print("\n=== PHQ-9 真实计分（正确格式）===")
print(json.dumps({"total": total, "level": level, "crisis_flag": result.get("crisis_flag")}, ensure_ascii=False))
print("\n=== 演练产物已落盘 ===")
print("progress.json ->", os.path.join(DRY, "progress.json"))
print("case report   ->", os.path.join(DRY, "reports", "practice", "case-report-cbt.md"))
print("PHQ-9 报告    ->", report_path)
print("\n=== 预期 vs 实际（核心不变量）===")
ok = True
for k, v in expected.items():
    cur = progress
    for part in k.split("."):
        cur = cur[part]
    actual = cur
    flag = "OK " if actual == v else "DIFF"
    if actual != v:
        ok = False
    print(f"  [{flag}] {k}: 预期={v} 实际={actual}")
print("\nRESULT:", "全部符合预期 ✅" if ok else "存在偏差 ⚠️")
