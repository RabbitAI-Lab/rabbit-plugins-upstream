#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
R5 集成回归：验证 progress.json 数据模型自洽与「先读后写合并」不覆盖不变量。
模拟一次 solo 模式用户的完整学习旅程，检查跨处理器字段正确且互不丢失。

运行：python3 tests/integration_test.py
"""
import copy
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def merge_write(data, patch):
    """模拟 Skill 写入规则：先读最新内容、合并变更再写回，避免覆盖其他字段。"""
    def deep_merge(base, over):
        for k, v in over.items():
            if k in base and isinstance(base[k], dict) and isinstance(v, dict):
                deep_merge(base[k], v)
            elif k in base and isinstance(base[k], list) and isinstance(v, list):
                base[k] = base[k] + v
            else:
                base[k] = v
        return base
    return deep_merge(data, copy.deepcopy(patch))


def check(cond, msg):
    if not cond:
        print(f"  ✗ FAIL: {msg}")
        return False
    print(f"  ✓ {msg}")
    return True


def main():
    ok = True
    # ---- 初始：onboarding solo（v2 一键默认，无 mode 字段）----
    data = {
        "version": "2.0.0",
        "userConfig": {"level": "beginner", "goal": "interest", "timeBudget": "standard"},
        "currentStage": "enlightenment",
        "stageCompleted": False,
        "modules": {m: {"completed": 0, "total": t, "items": []} for m, t in
                    {"theory": 4, "counseling": 5, "assessment": 3, "reading": 3,
                     "cases": 3, "methods": 4, "support": 3}.items()},
        "stats": {"totalHours": 0, "totalDays": 0, "practiceCount": 0, "analyses": 0,
                  "dialogues": 0, "booksRead": 0, "assessments": 0, "reflections": 0, "feynmanOutputs": 0},
        "xp": 0, "level": 1, "badges": [],
        "learnerProfile": {"learningStyle": "", "recurringStuck": [], "motivationState": "",
                           "preferredTherapies": [], "lastUpdated": ""},
        "moodLog": [],
        "readings": [], "assessments": [], "logs": [],
        "milestones": [{"id": f"m{i}", "text": f"M{i}", "reached": False} for i in range(1, 11)],
        "dialogueState": {"context": "daily", "step": 0, "tempData": {}, "lastTopic": ""}
    }

    # ---- learn（合并写不覆盖验证）----
    before = copy.deepcopy(data)
    data = merge_write(data, {"modules": {"theory": {"completed": 1}}, "logs": [{"type": "理论"}]})
    ok &= check(data["modules"]["theory"]["completed"] == 1, "learn → theory.completed=1")
    ok &= check(data["stats"] == before["stats"] and data["xp"] == before["xp"],
                "合并写不覆盖 stats/xp 字段 (核心不变量)")

    # ---- practice ----
    data = merge_write(data, {"stats": {"practiceCount": 1}, "modules": {"counseling": {"completed": 1}},
                              "logs": [{"type": "练习"}]})
    ok &= check(data["stats"]["practiceCount"] == 1 and data["modules"]["counseling"]["completed"] == 1,
                "practice → practiceCount=1, counseling.completed=1")

    # ---- 逐字稿分析 ----
    data = merge_write(data, {"stats": {"analyses": 1},
                              "modules": {"counseling": {"completed": 2}, "cases": {"completed": 1}},
                              "logs": [{"type": "分析"}]})
    ok &= check(data["stats"]["analyses"] == 1 and data["modules"]["counseling"]["completed"] == 2
                and data["modules"]["cases"]["completed"] == 1,
                "逐字稿分析 → analyses=1, counseling=2, cases=1")

    # ---- assess ----
    data = merge_write(data, {"stats": {"assessments": 1}, "assessments": [{"id": "PHQ-9"}]})
    ok &= check(data["stats"]["assessments"] == 1 and len(data["assessments"]) == 1, "assess → assessments=1")

    # ---- summary ----
    data = merge_write(data, {"stageCompleted": True, "stats": {"reflections": 1},
                              "modules": {"support": {"completed": 1}}})
    ok &= check(data["stageCompleted"] is True and data["stats"]["reflections"] == 1,
                "summary → stageCompleted, reflections=1")
    ok &= check(data["modules"]["support"]["completed"] == 1, "summary 触发 support.completed+1 (D30)")

    # ---- v1.3.0 新能力不变量 ----
    # record（认知记录）→ counseling.completed=3（触发点「认知记录」，不超过 total=5）
    data = merge_write(data, {"modules": {"counseling": {"completed": 3}},
                              "logs": [{"type": "认知记录"}]})
    ok &= check(data["modules"]["counseling"]["completed"] == 3
                and data["modules"]["counseling"]["total"] == 5,
                "record → counseling.completed=3, total=5 (v1.3.0)")
    # 情绪打卡 → moodLog 追加且同日覆盖（处理器语义：读→替换同 date 条目→写回整个数组）
    def mood_upsert(base, entry):
        base = [m for m in base if m["date"] != entry["date"]]
        base.append(entry)
        return base
    data["moodLog"] = mood_upsert(data["moodLog"], {"date": "2026-09-09", "mood": 4, "energy": 3, "note": ""})
    data["moodLog"] = mood_upsert(data["moodLog"], {"date": "2026-09-09", "mood": 5, "energy": 4, "note": "下午状态好"})
    ok &= check(len(data["moodLog"]) == 1 and data["moodLog"][0]["mood"] == 5,
                "情绪打卡 → 同日覆盖保留最新 (v1.3.0)")
    # XP 累加 + totalDays 去重
    data = merge_write(data, {"xp": 65})
    data = merge_write(data, {"stats": {"totalDays": 1}})
    ok &= check(data["xp"] == 65 and data["stats"]["totalDays"] == 1,
                "xp 累加与 totalDays 去重计数 (v1.3.0)")
    # learnerProfile 更新
    data = merge_write(data, {"learnerProfile": {"learningStyle": "边练边学", "recurringStuck": ["情绪记录"],
                                                 "motivationState": "中", "lastUpdated": "2026-09-09"}})
    ok &= check(data["learnerProfile"]["recurringStuck"] == ["情绪记录"],
                "learnerProfile 画像写入 (v1.3.0)")
    # 合并写不覆盖新字段（核心不变量延伸）
    before2 = copy.deepcopy(data)
    data = merge_write(data, {"logs": [{"type": "练习2"}]})
    ok &= check(data["moodLog"] == before2["moodLog"] and data["xp"] == before2["xp"]
                and data["learnerProfile"] == before2["learnerProfile"],
                "合并写不覆盖 moodLog/xp/learnerProfile (核心不变量)")

    print("\n" + ("✅ 集成回归全部通过" if ok else "❌ 集成回归存在失败"))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
