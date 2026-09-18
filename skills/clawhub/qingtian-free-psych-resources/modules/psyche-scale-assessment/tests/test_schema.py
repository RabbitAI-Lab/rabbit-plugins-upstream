#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第二轮：19 量表 Schema 完整性 + 边界计分校验（生产级）。

检查项：
  1. 所有量表可 load
  2. 顶层必填字段 / item 必填 / option 必填
  3. 维度引用的题目 id 都存在
  4. 反向计分题数量与权威描述（scale_authority.md）一致
  5. 每个维度的 interpretation.bands 完整覆盖 [min,max] 且无实质重叠
  6. 全部量表“全选最小 / 全选最大”边界作答可正常计分

运行：python tests/test_schema.py
"""
import os
import sys
import json
import glob
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SCALES_DIR = os.path.join(ROOT, "scales")
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from scoring_engine import load_scale, score

# 来源：references/scale_authority.md 中明确给出的反向题数
EXPECTED_REVERSE = {
    "SAS": 5,        # q5,q9,q13,q17,q19
    "SDS": 10,
    "PSS-10": 4,     # q4,q5,q7,q8
    "Rosenberg": 5,
    "CES-D": 4,
    "MAAS": 0,       # 计分方向已内置，严禁反向
}
# 权威来源明确“含反向”的量表：反向题数应 > 0
KNOWN_HAS_REVERSE = {"FFMQ", "ECR"}

REQUIRED_TOP = ["id", "name", "category", "items", "dimensions",
                "interpretation", "safety"]
REQUIRED_ITEM = ["id", "text", "options"]
REQUIRED_OPT = ["label", "score"]

problems = []


def problem(sid, msg):
    problems.append(f"[{sid}] {msg}")


files = sorted(glob.glob(os.path.join(SCALES_DIR, "*.json")))
for f in files:
    sid = os.path.splitext(os.path.basename(f))[0]
    try:
        sc = load_scale(sid)
    except Exception as e:
        problem(sid, f"load 失败: {e}")
        continue

    # 1) 顶层必填
    for k in REQUIRED_TOP:
        if k not in sc:
            problem(sid, f"缺少顶层字段 {k}")

    items = sc.get("items", [])
    if not items:
        problem(sid, "items 为空")
    item_ids = set()
    for it in items:
        for k in REQUIRED_ITEM:
            if k not in it:
                problem(sid, f"题 {it.get('id','?')} 缺少字段 {k}")
        opts = it.get("options", [])
        if len(opts) < 2:
            problem(sid, f"题 {it.get('id')} options 不足 2 项")
        for o in opts:
            for k in REQUIRED_OPT:
                if k not in o:
                    problem(sid, f"题 {it.get('id')} 选项缺少 {k}")
        item_ids.add(it.get("id"))

    # 2) 反向题计数与权威来源一致性
    rev = sum(1 for it in items if it.get("reverse"))
    if sid in EXPECTED_REVERSE and rev != EXPECTED_REVERSE[sid]:
        problem(sid, f"reverse 题数={rev}, 权威期望 {EXPECTED_REVERSE[sid]}")
    if sid in KNOWN_HAS_REVERSE and rev == 0:
        problem(sid, "权威来源称含反向计分，但实际 0 个 reverse 题")
    # description 内“X 道反向”声明核对
    desc = sc.get("description", "")
    m = re.search(r"(\d+)\s*道?反向", desc)
    if m and sid in EXPECTED_REVERSE and int(m.group(1)) != EXPECTED_REVERSE[sid]:
        problem(sid, f"description 声称 {m.group(1)} 道反向, 期望 {EXPECTED_REVERSE[sid]}")

    # 3) 维度引用存在性
    for dim in sc.get("dimensions", []):
        for iid in dim.get("items", []):
            if iid not in item_ids:
                problem(sid, f"维度 {dim.get('name')} 引用不存在的题 {iid}")

    # 4) bands 覆盖与重叠
    bands = sc.get("interpretation", {}).get("bands", [])

    # 4b) SAS/SDS 标准分 band 阈值回归锁（防止被再次误乘 1.25）
    if sid in ("SAS", "SDS"):
        scoped = [b for b in bands if b.get("dimension") in (None, "原始总分")]
        expected_min = 50.0 if sid == "SAS" else 53.0
        light = next((b for b in scoped if "轻度" in b.get("level", "")), None)
        if light is None:
            problem(sid, "未找到'轻度' band，无法校验标准分阈值")
        elif abs(float(light["min"]) - expected_min) > 0.01:
            problem(sid, f"轻度 band min={light['min']}, 应为权威标准分阈值 "
                          f"{expected_min}（曾被误乘 1.25 得 {expected_min*1.25}）")
    std = sc.get("standard_score")
    slope = float(std.get("slope", 1.0)) if std else 1.0
    intercept = float(std.get("intercept", 0.0)) if std else 0.0
    std_target = std.get("dimension") if std else None
    TOL = 1.0  # 允许相邻 band 衔接（整数步长=1；浮点缝隙≤0.01），仅显著间隙/重叠才报错
    for dim in sc.get("dimensions", []):
        dmin, dmax = dim.get("min"), dim.get("max")
        if dmin is None or dmax is None:
            continue
        scoped = [b for b in bands if b.get("dimension") in (None, dim["name"])]
        if not scoped:
            problem(sid, f"维度 {dim['name']} 无任何 scoped band（会判为未分级）")
            continue
        # 该维度判级取值：有 standard_score 且作用于本维度时按标准分，否则按原始分
        use_std = bool(std) and (std_target is None or std_target == dim["name"])
        vmin = (dmin * slope + intercept) if use_std else dmin
        vmax = (dmax * slope + intercept) if use_std else dmax
        scoped_sorted = sorted(scoped, key=lambda b: b["min"])
        if scoped_sorted[0]["min"] - vmin > TOL:
            problem(sid, f"维度 {dim['name']} bands 起始缺口（判级域 {vmin} 起，首 band {scoped_sorted[0]['min']}）")
            continue
        merged_max = scoped_sorted[0]["max"]
        gap = False
        for b in scoped_sorted[1:]:
            if b["min"] - merged_max > TOL:
                gap = True
                break
            merged_max = max(merged_max, b["max"])
        if gap or vmax - merged_max > TOL:
            problem(sid, f"维度 {dim['name']} bands 未完整覆盖判级值域 [{vmin},{vmax}]"
                          f"（缺口/越界，可能判为未分级）")
        for i in range(len(scoped_sorted) - 1):
            if scoped_sorted[i]["max"] - scoped_sorted[i + 1]["min"] > TOL:
                problem(sid, f"维度 {dim['name']} bands 重叠: "
                              f"{scoped_sorted[i]['min']}~{scoped_sorted[i]['max']} / "
                              f"{scoped_sorted[i+1]['min']}~{scoped_sorted[i+1]['max']}")

    # 5) 边界计分：全选最小 / 最大
    try:
        score(sc, {it["id"]: 0 for it in items})
        score(sc, {it["id"]: len(it["options"]) - 1 for it in items})
    except Exception as e:
        problem(sid, f"边界计分异常: {e}")

if problems:
    print(f"发现 {len(problems)} 个问题：")
    for p in problems:
        print("  -", p)
    sys.exit(1)
else:
    print(f"✅ 全部 {len(files)} 个量表 Schema 校验通过"
          f"（字段/维度引用/bands覆盖/反向一致性/边界计分）")
    sys.exit(0)
