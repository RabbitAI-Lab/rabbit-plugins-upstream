#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
通用心理量表计分引擎。

设计原则：量表即数据。本引擎不依赖任何具体量表，只读取 scales/<id>.json。
支持能力：
  - 正向 / 反向计分（reverse 题按选项分值端点翻转）
  - 子量表（维度）聚合：sum / average，可设 cap（如 PSQI 成分封顶 3）
  - 标准分换算（standard_score：slope / intercept）
  - 按 interpretation.bands 判级
  - 危机检测（crisis 题 + safety 规则）
  - 缺失题检测

可作为模块 import，也可命令行运行做批处理 / 自测：
    python scoring_engine.py <scale_id> <answers_json>
其中 answers_json 形如 {"q1": 2, "q2": 0, ...}（值为选项序号，0 起；或原始分值）
"""

import json
import os
import re
import sys

SCALES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scales")


def _normalize_id(s):
    """归一化量表 id：转小写并丢弃所有非字母数字字符。

    用于容错匹配：'PHQ-9' / 'phq9' / 'phq-9' / 'PHQ9' 视为同一量表，
    避免在不同文件系统（Linux 大小写敏感）下因命名差异而加载失败。
    """
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def _read_scale_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_scale(scale_id):
    """读取 scales/<scale_id>.json。

    先按精确文件名查找；若失败，再按「小写+去标点」归一化做大小写/连字符容错匹配，
    保证在大小写敏感的（Linux/skillhub/CI）环境下也能正确加载。
    """
    exact = os.path.join(SCALES_DIR, f"{scale_id}.json")
    if os.path.exists(exact):
        return _read_scale_file(exact)
    target = _normalize_id(scale_id)
    if target:
        for fn in os.listdir(SCALES_DIR):
            base, ext = os.path.splitext(fn)
            if ext.lower() == ".json" and _normalize_id(base) == target:
                return _read_scale_file(os.path.join(SCALES_DIR, fn))
    raise FileNotFoundError(
        f"未找到量表文件：{exact}（可用量表见 scales/ 目录）"
    )


def _item_bounds(item):
    """返回该题选项分值的最小/最大值。"""
    scores = [o["score"] for o in item["options"]]
    return min(scores), max(scores)


def _resolve_raw(item, ans):
    """把用户的作答解析为原始分值（未处理反向）。

    约定：ans 为选项序号（0 起）；序号合法则取其对应 score。
    兼容直接传入原始分值（须落在选项分值区间内）。
    任何非法输入均抛出 ValueError，绝不静默吞掉或当作 0 分。
    """
    opts = item["options"]
    scores = [o["score"] for o in opts]
    lo, hi = min(scores), max(scores)
    if isinstance(ans, bool):
        raise ValueError(f"题 {item['id']} 作答非法：不能是布尔值 {ans!r}")
    if isinstance(ans, int) and 0 <= ans < len(opts):
        return float(opts[ans]["score"])
    try:
        f = float(ans)
    except (TypeError, ValueError):
        raise ValueError(
            f"题 {item['id']} 作答 {ans!r} 非法：应为 0~{len(opts) - 1} 的选项序号"
        )
    if lo <= f <= hi:
        return f
    raise ValueError(
        f"题 {item['id']} 作答 {f} 超出合法分值区间 [{lo}, {hi}]"
    )


def _normalize_answers(scale, answers):
    """统一作答键：同时支持 item_id（如 pa1）与题号 q1..qn（按 items 顺序）。

    背景：SKILL.md §6 规定 LLM 产出 {"q1":0,"q2":1,…} 位置键，与 items 顺序一致；
    但各量表 item id 命名不统一（PHQ-9=q1..q9，PANAS=pa1/na1，FFMQ=ob1…）。
    本函数把 q<n> 映射到第 n 个 item 的 id，使文档约定的格式对所有量表均可计分。
    item_id 键原样透传；越界 q<n> 忽略（不计入缺失）。
    """
    items = scale["items"]
    norm = {}
    for k, v in answers.items():
        m = re.match(r"^q(\d+)$", str(k).strip(), re.IGNORECASE)
        if m:
            idx = int(m.group(1)) - 1
            if 0 <= idx < len(items):
                norm[items[idx]["id"]] = v
        else:
            norm[k] = v
    return norm


def score(scale, answers):
    """核心计分函数。

    :param scale: 量表定义 dict
    :param answers: {item_id 或 q1..qn: 选项序号(int) 或 原始分(float)}
    :return: 结构化结果 dict
    """
    answers = _normalize_answers(scale, answers)
    items_by_id = {it["id"]: it for it in scale["items"]}
    item_scores = {}          # item_id -> 计分项得分（已处理反向）
    raw_selected = {}         # item_id -> 选项原始分值（未反向，用于危机判定）
    missing = []

    for it in scale["items"]:
        iid = it["id"]
        if iid not in answers:
            missing.append(iid)
            continue
        lo, hi = _item_bounds(it)
        raw = _resolve_raw(it, answers[iid])
        raw_selected[iid] = raw
        if it.get("reverse"):
            raw = lo + hi - raw
        item_scores[iid] = raw

    # 维度聚合
    # method 支持：sum（默认）/ average / count（阳性题数统计，按 raw 原始分值计阈值，
    # 阈值取 dim["count_threshold"]，默认 1；用于 ASRS 等"≥N 题达阈值判阳性"的官方计分法）
    dimension_scores = {}
    for dim in scale.get("dimensions", []):
        vals = [item_scores[i] for i in dim["items"] if i in item_scores]
        if not vals:
            continue
        if dim.get("method") == "average":
            agg = sum(vals) / len(vals)
        elif dim.get("method") == "count":
            thr = float(dim.get("count_threshold", 1))
            agg = sum(1 for i in dim["items"]
                      if i in raw_selected and raw_selected[i] >= thr)
        else:
            agg = sum(vals)
        if dim.get("cap") is not None:
            agg = min(agg, dim["cap"])
        dimension_scores[dim["name"]] = round(agg, 2)

    # 标准分换算
    standard_scores = {}
    std = scale.get("standard_score")
    if std:
        slope = float(std.get("slope", 1.0))
        intercept = float(std.get("intercept", 0.0))
        target = std.get("dimension")
        if target and target not in dimension_scores:
            raise ValueError(
                f"standard_score.dimension '{target}' 不存在于 dimensions，"
                f"请检查量表数据（现有维度：{list(dimension_scores)}）"
            )
        if target:
            if target in dimension_scores:
                standard_scores[target] = round(dimension_scores[target] * slope + intercept, 2)
        else:
            for k, v in dimension_scores.items():
                standard_scores[k] = round(v * slope + intercept, 2)

    # 判级：标准分优先于同名原始分（SAS/SDS 等按标准分判级）
    combined = {**dimension_scores, **standard_scores}
    bands = scale.get("interpretation", {}).get("bands", [])
    band_results = {}
    for dim_name, val in combined.items():
        matched = None
        for b in bands:
            dim_scope = b.get("dimension")
            if dim_scope in (None, dim_name) and b["min"] <= val <= b["max"]:
                matched = b
                break
        band_results[dim_name] = matched["level"] if matched else "未分级"

    # 危机检测
    crisis_flag = False
    crisis_notes = []
    safety = scale.get("safety", {})
    for iid in safety.get("crisis_items", []):
        if iid not in raw_selected:
            continue
        raw = raw_selected[iid]
        rule = safety.get("crisis_rule", "")
        triggered = False
        m = re.search(r"≥\s*(\d+(?:\.\d+)?)", rule)
        if m:
            triggered = raw >= float(m.group(1))
        else:
            triggered = raw >= 1  # 默认：非零即触发
        if triggered:
            crisis_flag = True
            crisis_notes.append(f"危机题「{items_by_id[iid].get('text','')[:24]}…」得 {int(raw)} 分")

    # 高风险规则（如 "抑郁总分 ≥ 15 或 q9 ≥ 1"）
    # 标识符正则需同时支持中文维度名（如「抑郁总分」）与英文字段（如 q9）。
    hr = safety.get("high_risk_rule", "")
    for m in re.findall(r"([\u4e00-\u9fffA-Za-z0-9_]+)\s*≥\s*(\d+(?:\.\d+)?)", hr):
        key, thr = m[0], float(m[1])
        if key in dimension_scores and dimension_scores[key] >= thr:
            crisis_flag = True
        if key in raw_selected and raw_selected[key] >= thr:
            crisis_flag = True

    return {
        "scale_id": scale["id"],
        "scale_name": scale["name"],
        "item_scores": {k: round(v, 2) for k, v in item_scores.items()},
        "dimension_scores": dimension_scores,
        "standard_scores": standard_scores,
        "bands": band_results,
        "crisis_flag": crisis_flag,
        "crisis_notes": crisis_notes,
        "missing_items": missing,
        "complete": len(missing) == 0,
    }


def main():
    if len(sys.argv) < 3:
        print("Usage: python scoring_engine.py <scale_id> <answers_json_file>")
        sys.exit(1)
    scale = load_scale(sys.argv[1])
    with open(sys.argv[2], "r", encoding="utf-8") as f:
        answers = json.load(f)
    result = score(scale, answers)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
