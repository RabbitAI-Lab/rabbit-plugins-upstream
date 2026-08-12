#!/usr/bin/env python3
"""
探测本机 Agent 会话日志的结构，判断能否从中挖出 skill 触发与标注信号。

隐私优先：只输出字段名、类型、计数和长度，**不输出任何业务内容**。
唯一的例外是 --sample-keys，也只打印键名。

用法:
    python3 probe_logs.py
    python3 probe_logs.py --path ~/some/other/logs
    python3 probe_logs.py --skill-name my-skill   # 看该名字在日志里出现几次
"""

import argparse
import json
import os
from collections import Counter
from pathlib import Path

CANDIDATE_DIRS = [
    "~/.claude/projects",
    "~/.claude/history",
    "~/.codex/sessions",
    "~/.codex/history",
    "~/.openclaw/sessions",
    "~/.cc-switch/sessions",
]


def walk_json_lines(path: Path, limit=4000):
    """逐行读 jsonl；非 json 行跳过。"""
    n = 0
    try:
        with path.open("r", encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except json.JSONDecodeError:
                    continue
                n += 1
                if n >= limit:
                    return
    except OSError:
        return


def flatten_keys(obj, prefix="", out=None, depth=0):
    if out is None:
        out = set()
    if depth > 4:
        return out
    if isinstance(obj, dict):
        for k, v in obj.items():
            key = f"{prefix}.{k}" if prefix else k
            out.add(key)
            flatten_keys(v, key, out, depth + 1)
    elif isinstance(obj, list) and obj:
        flatten_keys(obj[0], prefix + "[]", out, depth + 1)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", action="append", default=[])
    ap.add_argument("--skill-name", help="检查该 skill 名在日志中出现的次数")
    ap.add_argument("--max-files", type=int, default=40)
    args = ap.parse_args()

    dirs = [Path(os.path.expanduser(d)) for d in CANDIDATE_DIRS + args.path]
    found_dirs = [d for d in dirs if d.is_dir()]

    print("=== 日志目录 ===")
    if not found_dirs:
        print("未找到。用 --path 指定，或告诉我你的宿主把会话存在哪。")
        return
    for d in found_dirs:
        files = list(d.rglob("*.jsonl")) + list(d.rglob("*.json"))
        print(f"  {d}  ({len(files)} 个文件)")

    all_files = []
    for d in found_dirs:
        all_files += sorted(d.rglob("*.jsonl"), key=lambda p: -p.stat().st_mtime)
        all_files += sorted(d.rglob("*.json"), key=lambda p: -p.stat().st_mtime)
    all_files = all_files[: args.max_files]

    if not all_files:
        print("\n目录存在但没有 json/jsonl 文件。")
        return

    keys = Counter()
    roles = Counter()
    types = Counter()
    records = 0
    skill_hits = 0
    skill_word_hits = 0

    for fp in all_files:
        for rec in walk_json_lines(fp):
            records += 1
            for k in flatten_keys(rec):
                keys[k] += 1
            if isinstance(rec, dict):
                for field in ("role", "type", "event"):
                    v = rec.get(field)
                    if isinstance(v, str):
                        (roles if field == "role" else types)[f"{field}={v}"] += 1
            blob = json.dumps(rec, ensure_ascii=False)
            if "skill" in blob.lower():
                skill_word_hits += 1
            if args.skill_name and args.skill_name in blob:
                skill_hits += 1

    print(f"\n=== 概览 ===")
    print(f"  扫描文件 {len(all_files)} 个，记录 {records} 条")
    print(f"  含 'skill' 字样的记录：{skill_word_hits} "
          f"({skill_word_hits/max(records,1)*100:.1f}%)")
    if args.skill_name:
        print(f"  含 '{args.skill_name}' 的记录：{skill_hits}")

    print(f"\n=== 出现最多的字段（仅键名）===")
    for k, c in keys.most_common(35):
        print(f"  {c:6}  {k}")

    print(f"\n=== 角色 / 类型枚举 ===")
    for k, c in (roles + types).most_common(20):
        print(f"  {c:6}  {k}")

    print("\n=== 判断要点 ===")
    has_role = any(k.endswith("role") for k in keys)
    has_tool = any("tool" in k.lower() for k in keys)
    has_ts = any(("timestamp" in k.lower() or k.endswith("time")) for k in keys)
    print(f"  能区分用户/助手轮次： {'是' if has_role else '否 —— 挖不出纠正信号'}")
    print(f"  有工具调用记录：     {'是' if has_tool else '否'}")
    print(f"  有时间戳：           {'是' if has_ts else '否'}")
    print(f"  能识别 skill 激活：  "
          f"{'可能，需人工看一条样本确认' if skill_word_hits else '否 —— 需要网关方案'}")
    print("\n本脚本不输出任何业务内容。要确认字段含义，请自己打开一条记录查看。")


if __name__ == "__main__":
    main()
