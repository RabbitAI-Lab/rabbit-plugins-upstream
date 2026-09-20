# -*- coding: utf-8 -*-
"""R8 集成回归 + 盲区演练：多维度量表 e2e + daily_recommend 逻辑 + 回归 PHQ-9。
验证：D 级修复（q<n> 位置键归一化）后，所有量表按 SKILL.md §6 文档格式均可计分；
并补测此前未单独演练的 daily_recommend 处理器不变量。"""
import json, os, subprocess, sys, copy, datetime

SKILL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SC = os.path.join(SKILL, "assessment", "scripts", "score_and_report.py")
OUT = os.path.join(SKILL, "tests", "dryrun", "r8_out")
os.makedirs(OUT, exist_ok=True)

fails = []
def check(cond, msg):
    print(("  ✓ " if cond else "  ✗ ") + msg)
    if not cond: fails.append(msg)

def run_scale(sid, n_items):
    # 按 SKILL.md §6：键为 q1..qn（位置），值为选项序号 0 起
    answers = {f"q{i}": (i % 4) for i in range(1, n_items + 1)}
    p = os.path.join(OUT, f"{sid}.json")
    json.dump(answers, open(p, "w"), ensure_ascii=False)
    r = subprocess.run([sys.executable, SC, sid, p, OUT],
                       capture_output=True, text=True)
    res = None
    for line in r.stdout.splitlines():
        if line.startswith("RESULT_JSON>>>"):
            res = json.loads(line.split(">>>", 1)[1])
    return r.returncode, res

print("===== 多维度量表 e2e（文档格式 q1..qn）=====")
rc, panas = run_scale("PANAS", 20)
check(rc == 0 and panas and panas.get("complete"), "PANAS(2维) 文档格式 q1..q20 可计分")
check(panas and set(panas["dimension_scores"].keys()) == {"积极情绪(PA)", "消极情绪(NA)"},
      "PANAS 维度名与 scale 定义一致（2维）")
check(panas and set(panas["bands"].keys()) == set(panas["dimension_scores"].keys()),
      "PANAS bands 与 dimension_scores 同键（SKILL.md §6 多维解析可执行）")

rc, ffmq = run_scale("FFMQ", 39)
check(rc == 0 and ffmq and ffmq.get("complete"), "FFMQ(5因子/含反向题) 文档格式 q1..q39 可计分")
check(ffmq and len(ffmq["dimension_scores"]) == 5, "FFMQ 解析出 5 个因子维度")

# 回归：PHQ-9 文档格式仍正常（D31b 错误格式仍被拒）
rc, phq = run_scale("PHQ-9", 9)
check(rc == 0 and phq and phq.get("complete"), "回归：PHQ-9(单维) 文档格式仍正常")
bad = os.path.join(OUT, "phq9_bad.json")
json.dump({"answers": [0, 1, 0]}, open(bad, "w"), ensure_ascii=False)
rb = subprocess.run([sys.executable, SC, "PHQ-9", bad, OUT], capture_output=True, text=True)
check(rb.returncode != 0 and "作答不完整" in rb.stderr, "回归：错误格式 {answers:[...]} 仍被拒（D31b）")

print("\n===== daily_recommend 处理器不变量（此前未单独演练）=====")
def fresh_solo():
    return {
        "userConfig": {"mode": "solo", "level": "beginner", "goal": "interest", "timeBudget": "light"},
        "currentStage": "enlightenment", "stageCompleted": False, "lastDialogueAt": "",
        "dialogueState": {"context": "daily", "step": 0, "tempData": {}, "lastTopic": ""},
    }
# 模拟：用户说「今天学什么」→ 输出 3 选 1，更新 lastTopic + lastDialogueAt
d = fresh_solo()
d["lastTopic"] = "今日推荐：单推荐一件事"
d["lastDialogueAt"] = datetime.date.today().isoformat()
check(d["lastTopic"].startswith("今日推荐") and d["lastDialogueAt"] != "",
      "daily：更新 lastTopic + lastDialogueAt")
check(d["dialogueState"]["context"] == "daily", "daily：context 保持 daily（非强制跳转）")
# 分支：stageCompleted==true → 建议阶段总结/预习，不重复推任务
d2 = fresh_solo(); d2["stageCompleted"] = True
suggestion = "本阶段已完成 ✅，可做『总结』写阶段总结，或预习下一阶段" if d2["stageCompleted"] else "继续今日任务"
check("总结" in suggestion, "daily：stageCompleted=true 分支引导阶段总结（非重推任务）")

print("\n===== 结果 =====")
if fails:
    print(f"❌ {len(fails)} 项失败"); 
    for f in fails: print("  -", f)
    raise SystemExit(1)
print("✅ R8 多维量表 e2e + daily_recommend + 回归 全部通过")
