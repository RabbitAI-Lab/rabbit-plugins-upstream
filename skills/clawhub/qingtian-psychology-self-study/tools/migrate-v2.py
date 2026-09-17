# -*- coding: utf-8 -*-
"""
v2.0 迁移工具：把 v1.x（周制）progress.json 迁移到 v2.0（阶段制）。

变更映射：
- currentWeek(int)      -> currentStage(str) 阶段id（按 userConfig.level 映射）
- weekCompleted(bool)   -> stageCompleted
- weeklySummary(str)    -> stageSummary
- tempData.weekPlan     -> tempData.stagePlan（其余 tempData 如 flow 保留）
- version               -> 2.0.0

用法：
  python tools/migrate-v2.py <progress.json> [--keep-bak]
默认迁移前自动备份原文件为 <同名>.bak-<ts>；迁移后的文件直接写回。
"""
import io
import json
import os
import sys
import time

LEVEL_TO_STAGE = {"beginner": "enlightenment", "intermediate": "schools", "advanced": "integration"}


def migrate(data):
    """原地迁移 dict，返回迁移说明列表。"""
    notes = []
    # version
    data["version"] = "2.0.0"
    # currentWeek -> currentStage
    if "currentWeek" in data:
        level = (data.get("userConfig") or {}).get("level", "beginner")
        data["currentStage"] = LEVEL_TO_STAGE.get(level, "enlightenment")
        del data["currentWeek"]
        notes.append(f"currentWeek -> currentStage={data['currentStage']}")
    else:
        data.setdefault("currentStage", "enlightenment")
    # weekCompleted -> stageCompleted
    if "weekCompleted" in data:
        data["stageCompleted"] = data.pop("weekCompleted")
        notes.append("weekCompleted -> stageCompleted")
    else:
        data.setdefault("stageCompleted", False)
    # weeklySummary -> stageSummary
    if "weeklySummary" in data:
        data["stageSummary"] = data.pop("weeklySummary")
        notes.append("weeklySummary -> stageSummary")
    else:
        data.setdefault("stageSummary", "")
    # tempData.weekPlan -> stagePlan
    ds = data.setdefault("dialogueState", {})
    td = ds.setdefault("tempData", {})
    if "weekPlan" in td:
        td["stagePlan"] = td.pop("weekPlan")
        notes.append("tempData.weekPlan -> tempData.stagePlan")
    return notes


def main():
    if len(sys.argv) < 2:
        print("用法: python tools/migrate-v2.py <progress.json>")
        sys.exit(2)
    path = os.path.abspath(sys.argv[1])
    if not os.path.exists(path):
        print(f"文件不存在: {path}")
        sys.exit(1)
    with io.open(path, "r", encoding="utf-8-sig") as f:
        data = json.load(f)
    if data.get("version", "").startswith("2."):
        print("已是 v2.x，无需迁移")
        return
    # 备份
    bak = f"{path}.bak-{time.strftime('%Y%m%d%H%M%S')}"
    with io.open(bak, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    notes = migrate(data)
    with io.open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"迁移完成: {path}")
    print(f"备份: {bak}")
    for n in notes:
        print("  ✓", n)


if __name__ == "__main__":
    main()
