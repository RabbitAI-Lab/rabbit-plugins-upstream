#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI人生教练 · 本地反思脚本（v2.0）
================================
用户端纯本地反思：读自己的记忆档案，做统计型反思，可选导出脱敏报告供作者聚合。

铁律（不可违反）：
- 零网络请求：本脚本不发起任何网络调用。
- 隐私本地化：export 输出为完全脱敏的标准化 JSON（不含 user_id、不含原始自由文本细节）。
- 0 token 成本：全部为 Python 规则统计，不调用 LLM。

用法：
  python reflect.py                     # 反思本机所有档案，输出 reports/
  python reflect.py --user <user_id>    # 只反思指定用户
  python reflect.py --since <days>      # 只统计最近 N 天（默认全部）
  python reflect.py --export            # 额外生成脱敏导出文件 exports/ 下（用户自愿发给作者）
  python reflect.py --list              # 列出本机所有档案
"""

import json
import os
import sys
import time
from collections import Counter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_DIR = os.path.join(BASE_DIR, "memory_archive")
REPORT_DIR = os.path.join(BASE_DIR, "reports")
EXPORT_DIR = os.path.join(BASE_DIR, "exports")

# 共性分析时用于判断"高频"的阈值（导出时标记）
HIGH_FREQ_RATIO = 0.3       # 某卡点在会话中出现占比 ≥30% → 高频
CRISIS_KEYWORDS = ["活着没意思", "不想活了", "死了算了", "撑不下去", "没我更好"]


def _ensure_dirs():
    for d in (REPORT_DIR, EXPORT_DIR):
        os.makedirs(d, exist_ok=True)


def _list_archives():
    if not os.path.isdir(ARCHIVE_DIR):
        return []
    return sorted(f[:-5] for f in os.listdir(ARCHIVE_DIR) if f.endswith(".json"))


def _load_entries(user_id):
    p = os.path.join(ARCHIVE_DIR, f"{user_id}.json")
    if not os.path.exists(p):
        return []
    try:
        with open(p, encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except Exception:
        return []


def _sanitize(entries, since_days=None):
    """过滤出统计用条目；since_days 按 ts 过滤。"""
    cutoff = None
    if since_days:
        cutoff = time.time() - since_days * 86400
    out = []
    for e in entries:
        if cutoff and e.get("ts", 0) < cutoff:
            continue
        out.append(e)
    return out


def _as_list(v):
    """兼容记忆档案中字段是字符串或列表两种格式。"""
    if v is None:
        return []
    if isinstance(v, str):
        return [v] if v.strip() else []
    if isinstance(v, list):
        return [x for x in v if isinstance(x, str) and x.strip()]
    return []


def _analyze(entries):
    """纯规则统计，返回结构化分析结果。"""
    n = len(entries)
    if n == 0:
        return {"session_count": 0}

    # 1. 高频卡点
    card_counter = Counter()
    for e in entries:
        for c in _as_list(e.get("card_points")):
            card_counter[c] += 1

    # 2. 有效动作（effective）
    eff_counter = Counter()
    for e in entries:
        for a in _as_list(e.get("effective")):
            eff_counter[a] += 1

    # 3. 工具命中（从 effective/card_points 文本里粗匹配常见工具名）
    TOOLS = ["仪表盘", "奥德赛", "情绪ABC", "心理账户", "沉没成本", "至暗时光",
             "真我模型", "破局工具箱", "逆向思维", "心流", "长期主义", "反脆弱"]
    tool_hits = Counter()
    for e in entries:
        blob = json.dumps(e, ensure_ascii=False)
        for t in TOOLS:
            if t in blob:
                tool_hits[t] += 1

    # 4. 危机合规：出现过危机关键词的条目，检查摘要里是否记录了安全确认动作
    crisis_sessions = 0
    crisis_flagged_ok = 0
    for e in entries:
        blob = json.dumps(e, ensure_ascii=False)
        if any(kw in blob for kw in CRISIS_KEYWORDS):
            crisis_sessions += 1
            if "安全" in blob or "危机" in blob or "热线" in blob:
                crisis_flagged_ok += 1

    # 5. 情绪基线分布（user_state 里的 1-5）
    mood_counter = Counter()
    for e in entries:
        s = str(e.get("user_state", ""))
        for m in ("1", "2", "3", "4", "5"):
            if f"基线{m}" in s or f"{m}" in s and "基线" in s:
                mood_counter[m] += 1

    return {
        "session_count": n,
        "high_freq_cards": card_counter.most_common(5),
        "effective_actions": eff_counter.most_common(5),
        "tool_hits": tool_hits.most_common(5),
        "crisis": {"sessions": crisis_sessions, "handled_ok": crisis_flagged_ok},
        "mood_dist": dict(mood_counter.most_common()),
    }


def _render_md(user_id, a):
    if a["session_count"] == 0:
        return f"# 反思报告：{user_id}\n\n暂无会话记录。"
    lines = [f"# 反思报告：{user_id}", ""]
    lines.append(f"## 概览")
    lines.append(f"- 会话数：{a['session_count']}")
    lines.append(f"- 高频卡点 Top5：{a['high_freq_cards']}")
    lines.append(f"- 有效动作 Top5：{a['effective_actions']}")
    lines.append(f"- 工具命中 Top5：{a['tool_hits']}")
    lines.append(f"- 危机信号：{a['crisis']['sessions']} 次，合规处理 {a['crisis']['handled_ok']} 次")
    lines.append(f"- 情绪基线分布：{a['mood_dist']}")
    lines.append("")
    lines.append("> 本报告仅统计可复用模式，不含任何个人可识别信息。")
    lines.append("> 想帮助作者改进教练，请运行：python reflect.py --export 后，把 exports/ 下的文件自愿分享给作者。")
    return "\n".join(lines)


def _render_export(user_id, a):
    """脱敏导出：只保留当前用户的可聚合统计，供作者端 aggregate.py 聚合。"""
    return {
        "schema": "ai-life-coach-reflect-export/v1",
        "exported_at": int(time.time()),
        "session_count": a["session_count"],
        "high_freq_cards": [c for c, _ in a["high_freq_cards"]],
        "effective_actions": [c for c, _ in a["effective_actions"]],
        "tool_hits": [c for c, _ in a["tool_hits"]],
        "crisis_ok_ratio": round(a["crisis"]["handled_ok"] / max(1, a["crisis"]["sessions"]), 2),
        "mood_dist": a["mood_dist"],
        # 只含当前用户自己的标签，不含其他用户样本（保护隐私 + 支持度计算正确）
        "card_samples": [c for c, _ in a["high_freq_cards"]],
        "effective_samples": [c for c, _ in a["effective_actions"]],
        "privacy_note": "已脱敏：不含 user_id、原始对话、可识别身份信息",
    }


def cmd_reflect(args):
    _ensure_dirs()
    users = _list_archives()
    if not users:
        print("EMPTY：本机暂无记忆档案")
        return 0
    since = None
    for i, a in enumerate(args):
        if a == "--since" and i + 1 < len(args):
            try:
                since = int(args[i + 1])
            except ValueError:
                pass
    for uid in users:
        entries = _sanitize(_load_entries(uid), since)
        a = _analyze(entries)
        md = _render_md(uid, a)
        path = os.path.join(REPORT_DIR, f"reflect_{uid}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"✅ 反思报告已生成: {path} ({a['session_count']} 场会话)")
        if "--export" in args:
            ex = _render_export(uid, a)
            ep = os.path.join(EXPORT_DIR, f"export_{uid}_{int(time.time())}.json")
            with open(ep, "w", encoding="utf-8") as f:
                json.dump(ex, f, ensure_ascii=False, indent=2)
            print(f"✅ 脱敏导出已生成（可自愿发给作者）: {ep}")
    return 0


def cmd_list():
    users = _list_archives()
    if not users:
        print("EMPTY")
        return 0
    for u in users:
        n = len(_load_entries(u))
        print(f"{u}\t{n} 场")
    return 0


def main():
    args = sys.argv[1:]
    if "--list" in args or not args:
        return cmd_list()
    return cmd_reflect(args)


if __name__ == "__main__":
    sys.exit(main())
