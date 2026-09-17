#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""进度数据备份/恢复工具（导出/导入 progress.json）。

用法：
    python3 tools/progress-backup.py export <progress.json> [out_dir]
        # 复制 progress.json 到 out_dir（默认同目录），文件名带时间戳
    python3 tools/progress-backup.py import <progress.json> <backup.json>
        # 导入备份：先把当前 progress.json 备份为 .bak-<时间戳>，再用 backup.json 覆盖

示例（在用户工作区）：
    python3 "<SKILL_ROOT>/tools/progress-backup.py" export .workbuddy/psychology-study/progress.json
    python3 "<SKILL_ROOT>/tools/progress-backup.py" import .workbuddy/psychology-study/progress.json ./progress-backup-20260909.json
"""
import json
import os
import shutil
import sys
from datetime import datetime


def _ts():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def export(src, out_dir=None):
    if not os.path.exists(src):
        print(f"错误：找不到进度文件 {src}")
        sys.exit(1)
    try:
        with open(src, "r", encoding="utf-8-sig") as f:  # utf-8-sig 兼容 Windows 记事本 BOM
            json.load(f)
    except Exception as e:
        print(f"错误：进度文件不是合法 JSON，已中止导出（避免备份损坏数据）：{e}")
        sys.exit(1)
    out_dir = out_dir or os.path.dirname(os.path.abspath(src))
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, f"progress-{_ts()}.json")
    shutil.copy2(src, dst)
    print(f"已导出进度备份 -> {dst}")


def restore(src, backup):
    if not os.path.exists(backup):
        print(f"错误：找不到备份文件 {backup}")
        sys.exit(1)
    try:
        with open(backup, "r", encoding="utf-8-sig") as f:  # utf-8-sig 兼容 Windows 记事本 BOM
            json.load(f)
    except Exception as e:
        print(f"错误：备份文件不是合法 JSON，已中止导入：{e}")
        sys.exit(1)
    if os.path.exists(src):
        bak = f"{src}.bak-{_ts()}"
        shutil.copy2(src, bak)
        print(f"已把当前进度备份为 {bak}")
    shutil.copy2(backup, src)
    print(f"已从 {backup} 恢复进度 -> {src}")


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    cmd = sys.argv[1]
    if cmd == "export" and len(sys.argv) >= 3:
        export(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
    elif cmd == "import" and len(sys.argv) == 4:
        restore(sys.argv[2], sys.argv[3])
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main()
