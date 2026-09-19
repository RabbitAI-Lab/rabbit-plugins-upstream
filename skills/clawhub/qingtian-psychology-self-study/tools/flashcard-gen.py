#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把概念列表生成为 Anki 兼容的 CSV 闪卡。

用法：
    python3 tools/flashcard-gen.py <concepts.json> <out.csv>

concepts.json 格式（数组）：
    [
      {"front": "概念名", "back": "定义/解释", "tag": "流派或章节"},
      ...
    ]

输出：UTF-8 (BOM) CSV，三列 front,back,tag，自动处理引号/逗号转义，供 Anki 导入。
技能根目录定位：脚本基于 __file__ 自动解析，不依赖任何硬编码绝对路径。
"""

import json
import os
import sys
import csv


def main():
    if len(sys.argv) != 3:
        print("用法: python3 tools/flashcard-gen.py <concepts.json> <out.csv>")
        sys.exit(2)

    src, dst = sys.argv[1], sys.argv[2]

    if not os.path.exists(src):
        print(f"错误：找不到概念文件 {src}")
        sys.exit(1)

    try:
        with open(src, encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"解析 JSON 失败：{e}")
        sys.exit(1)

    if not isinstance(data, list):
        print("错误：concepts.json 顶层应为对象数组")
        sys.exit(1)

    out_dir = os.path.dirname(os.path.abspath(dst))
    os.makedirs(out_dir, exist_ok=True)

    n = 0
    with open(dst, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["front", "back", "tag"])
        for item in data:
            if not isinstance(item, dict):
                continue
            front = str(item.get("front", "")).strip()
            back = str(item.get("back", "")).strip()
            tag = str(item.get("tag", "")).strip()
            if not front or not back:
                continue
            w.writerow([front, back, tag])
            n += 1

    print(f"已生成 {n} 张闪卡 -> {dst}")


if __name__ == "__main__":
    main()
