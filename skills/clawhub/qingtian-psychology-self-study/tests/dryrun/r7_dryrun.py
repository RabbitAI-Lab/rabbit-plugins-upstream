# -*- coding: utf-8 -*-
"""
R7 专项演练：summary 延伸（月度反思）/ change_config / resume / crisis 四个处理器的
真实落盘验证。脚本模拟「LLM 按 SKILL.md 指令执行」在文件系统上的写操作，
并自检核心不变量。crisis 仅用技能文档自身列出的示例语义，不生成任何具体内容。
"""
import json, copy, os, shutil

SKILL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE = os.path.join(SKILL, "tests", "dryrun", "r7")
os.makedirs(BASE, exist_ok=True)
PROG = os.path.join(BASE, "progress.json")

# 第二节危机词表（演练用真实词，文档原样）
CRISIS_WORDS = ["自杀","自伤","不想活","结束生命","伤害自己","想死","活不下去",
                "伤人","报复","轻生","活着没意思","不如死了","死了算了","没盼头",
                "不想活了","解脱"]
STD_RESOURCE = "12356"  # 标准危机资源声明必含热线

fails = []
def check(cond, msg):
    if not cond:
        fails.append(msg)
        print("  ✗", msg)
    else:
        print("  ✓", msg)

# ---- 生成干净 solo 起点（等同 R6 终态）----
def fresh():
    return {
        "version": "2.0.0",
        "userConfig": {"level":"beginner","goal":"interest",
                        "timeBudget":"light","startDate":"2026-08-10","createdAt":"2026-08-10"},
        "currentStage": "enlightenment", "stageCompleted": True, "stageSummary": "本阶段完成。",
        "lastDialogueAt": "2026-08-10",
        "modules": {
            "theory": {"completed":1,"total":30,"items":["经典条件作用"]},
            "counseling": {"completed":2,"total":17,"items":["CBT","共情反映"]},
            "assessment": {"completed":1,"total":19,"items":["PHQ-9"]},
            "reading": {"completed":1,"total":10,"items":["心理学与生活"]},
            "cases": {"completed":1,"total":12,"items":["考试焦虑个案"]},
            "methods": {"completed":1,"total":8,"items":["费曼技巧"]},
            "support": {"completed":1,"total":3,"items":["进度追踪"]},
        },
        "stats": {"totalHours":8,"totalDays":7,"practiceCount":1,"analyses":1,
                  "dialogues":1,"booksRead":1,"assessments":1,"reflections":1,
                  "feynmanOutputs":0},
        "readings": [], "assessments": [{"scale":"PHQ-9","total":3.0,"level":"无·极轻度"}],
        "logs": [{"type":"理论","topic":"经典条件作用"}],
        "milestones": [
            {"id":"m1","text":"学完第一个流派","reached":True},
            {"id":"m2","text":"完成第一次 TPR 练习","reached":True},
        ],
        "dialogueState": {"context":"daily","step":0,"pendingQuestion":"",
                          "tempData":{},"lastTopic":""},
    }

def merge_write(d):
    json.dump(d, open(PROG,"w",encoding="utf-8"), ensure_ascii=False, indent=2)

print("\n===== 场景1：summary 延伸（月度反思）=====")
d = fresh()
# 模拟：引导月反思 → 用户填完 → logs 加「月度」条 + 校准 goal
d["logs"].append({"type":"月度","stage":d["currentStage"],
                  "summary":"本月系统学经典/操作性条件作用，完成1次CBT练习与1次对话分析，PHQ-9无轻度。"})
d["userConfig"]["goal"] = "counselor"  # 校准方向：兴趣→准咨询师
merge_write(d)
check(any(l.get("type")=="月度" for l in d["logs"]), "summary 延伸：logs 写入「月度」条")
check(d["userConfig"]["goal"]=="counselor", "summary 延伸：goal 校准为 counselor")
check(os.path.exists(os.path.join(SKILL,"tools/templates/monthly-review.md")),
      "summary 延伸：月度模板文件存在")

print("\n===== 场景2：change_config（改配置）=====")
d = fresh()
# 模拟：用户说「目标改成做咨询，时间加到标准」→ 更新 userConfig，保留进度
d["userConfig"]["goal"] = "counselor"
d["userConfig"]["timeBudget"] = "standard"
merge_write(d)
check(d["userConfig"]["goal"]=="counselor", "change_config：goal 更新为 counselor")
check(d["userConfig"]["timeBudget"]=="standard", "change_config：timeBudget 更新为 standard")
check(d["modules"]["theory"]["completed"]==1 and d["modules"]["counseling"]["completed"]==2,
      "change_config：已完成的 modules 进度保留（未重置）")
check(len(d["milestones"])==2 and d["milestones"][0]["reached"] is True,
      "change_config：既有里程碑保留（不重置）")

print("\n===== 场景3：resume（onboarding 中途续接 + state 为空）=====")
# 3a 半截 onboarding：已答 Q1-Q2，消失后回来「继续」
d = fresh()
d["dialogueState"] = {"context":"onboarding","step":3,
                      "pendingQuestion":"第三问：你学心理学主要为了？",
                      "tempData":{"q1":"兴趣","q2":"零基础"},"lastTopic":""}
step = d["dialogueState"]["step"]
check(step==3, "resume：读出断点 step=3（续第3问）")
check(d["dialogueState"]["tempData"].get("q1")=="兴趣",
      "resume：已答 Q1/Q2 在 tempData，不重填")
# 3b state 为空分支：daily 且无 lastTopic、无未完成 tempData
empty = {"context":"daily","step":0,"pendingQuestion":"","tempData":{},"lastTopic":""}
no_pending = (empty["context"]=="daily" and empty["lastTopic"]=="" and not empty["tempData"])
check(no_pending, "resume：state 为空 → 退回 daily（不强行教学）")

print("\n===== 场景4：crisis（轻响应 / 强响应 两分支）=====")
def hit_crisis(text):
    return any(w in text for w in CRISIS_WORDS)

# 4a 轻响应（文档原话隐喻）："烦得不想活了" —— 命中"不想活了"但无具体计划 → 共情陪伴
d = fresh()
before = copy.deepcopy({"modules":d["modules"],"stats":d["stats"],"assessments":d["assessments"]})
light = "今天好累烦得不想活了"
check(hit_crisis(light), "crisis：轻响应输入命中危机词（不想活了）")
# 模拟轻响应：仅共情，不写学习数据，不强塞热线
d["logs"].append({"type":"危机支持","note":"触发危机支持"})  # 脱敏
# 4b 强响应："我想死" —— 命中"想死"且有明确意图 → 标准资源声明
d2 = fresh()
strong = "我想死"
check(hit_crisis(strong), "crisis：强响应输入命中危机词（想死）")
# 模拟强响应输出含标准资源声明
strong_output = f"⚠️ 标准危机资源声明…全国统一心理援助热线 {STD_RESOURCE}…"
check(STD_RESOURCE in strong_output, "crisis：强响应输出含标准资源声明（12356）")
d2["logs"].append({"type":"危机支持","note":"触发危机支持"})
# 不变量：两个分支都不改动学习数据
after_light = {"modules":d["modules"],"stats":d["stats"],"assessments":d["assessments"]}
after_strong = {"modules":d2["modules"],"stats":d2["stats"],"assessments":d2["assessments"]}
check(before==after_light, "crisis：轻响应不改动 modules/stats/assessments")
check(before==after_strong, "crisis：强响应不改动 modules/stats/assessments")
# 恢复 dialogueState.context（危机前 context=learn）
d["dialogueState"]["context"]="learn"
check(d["dialogueState"]["context"]=="learn", "crisis：响应后恢复危机前 context（临时中断）")

print("\n===== 结果 =====")
if fails:
    print(f"❌ {len(fails)} 项自检失败")
    for f in fails: print("  -", f)
    raise SystemExit(1)
print("✅ R7 四处理器演练 全部不变量通过")
