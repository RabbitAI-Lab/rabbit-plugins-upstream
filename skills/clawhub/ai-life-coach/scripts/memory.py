#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI人生教练 · 本地记忆脚本（v1.3）
================================
用途：跨会话记忆的确定性读写工具——把"读/写记忆"从模型自由裁量变成可执行命令。

铁律（不可违反）：
- 零网络请求：本脚本不发起任何网络调用，数据只读写本机文件。
- 隐私本地化：记忆内容不含姓名/单位/城市/联系方式/财务数字等可识别身份信息。
- 护栏：单文件 ≤50KB、保留最近 20 条，超出自动裁剪。

用法：
  python memory.py read <user_id>
  python memory.py write <user_id> <json_string>
  python memory.py snapshot <user_id> <json_string>   # 中断兜底快照（同 write）
  python memory.py list                                 # 列出本机所有档案（不含内容）
"""

import json
import os
import sys
import time

# 档案目录 = 本脚本所在目录下 memory_archive/（随 skill 一起，仅本机）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_DIR = os.path.join(BASE_DIR, "memory_archive")

MAX_ENTRIES = 20          # 最近 20 条
MAX_BYTES = 50 * 1024     # 单档案 ≤50KB


def _ensure_dir():
    os.makedirs(ARCHIVE_DIR, exist_ok=True)


def _path(user_id):
    # 用户 ID 只允许字母数字-_，防路径穿越
    safe_id = "".join(c for c in user_id if c.isalnum() or c in "-_") or "default"
    return os.path.join(ARCHIVE_DIR, f"{safe_id}.json")


def _load(user_id):
    p = _path(user_id)
    if not os.path.exists(p):
        return []
    try:
        with open(p, encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except Exception:
        return []


def _save(user_id, entries):
    _ensure_dir()
    p = _path(user_id)
    # 裁剪：先按条数，再按字节
    if len(entries) > MAX_ENTRIES:
        entries = entries[-MAX_ENTRIES:]
    payload = json.dumps(entries, ensure_ascii=False, indent=2)
    if len(payload.encode("utf-8")) > MAX_BYTES:
        entries = entries[-10:]
        payload = json.dumps(entries, ensure_ascii=False, indent=2)
    with open(p, "w", encoding="utf-8") as f:
        f.write(payload)


def cmd_read(user_id):
    entries = _load(user_id)
    if not entries:
        print("NO_MEMORY")
        return 0
    # 输出最近一条摘要（最相关），并标注总数
    latest = entries[-1]
    print(json.dumps({"count": len(entries), "latest": latest}, ensure_ascii=False))
    return 0


def cmd_write(user_id, json_str):
    try:
        entry = json.loads(json_str)
    except Exception as e:
        print(f"ERROR: 无效 JSON: {e}")
        return 1
    if not isinstance(entry, dict):
        print("ERROR: 条目必须是 JSON 对象")
        return 1
    entry.setdefault("ts", int(time.time()))
    entries = _load(user_id)
    entries.append(entry)
    _save(user_id, entries)
    print("OK")
    return 0


def cmd_list():
    _ensure_dir()
    files = sorted(f for f in os.listdir(ARCHIVE_DIR) if f.endswith(".json"))
    if not files:
        print("EMPTY")
        return 0
    for f in files:
        size = os.path.getsize(os.path.join(ARCHIVE_DIR, f))
        print(f"{f[:-5]}\t{size}B")
    return 0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    cmd = sys.argv[1]
    if cmd == "read" and len(sys.argv) >= 3:
        return cmd_read(sys.argv[2])
    if cmd in ("write", "snapshot") and len(sys.argv) >= 4:
        return cmd_write(sys.argv[2], sys.argv[3])
    if cmd == "list":
        return cmd_list()
    print(f"ERROR: 未知命令 {cmd}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
