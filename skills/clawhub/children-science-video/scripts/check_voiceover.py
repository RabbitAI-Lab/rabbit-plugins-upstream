#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_voiceover.py — 分镜表配音文案字数机检

规则：每个配音文案需满足
    45 < 总字符数 <= 50   且   汉字数 >= 45
（正常语速约 4.5-5 字/秒，50 字 ≈ 10 秒口播）

用法：
    python check_voiceover.py <分镜表.md> [更多.md ...]

输出每个分镜的字数明细与 PASS/FAIL，全部通过退出码 0，否则 1。
"""
import re
import sys

HANZI_RE = re.compile(r"[\u4e00-\u9fff]")


def find_column(header_cells, keyword):
    for i, cell in enumerate(header_cells):
        if keyword in cell:
            return i
    return -1


def check_file(path):
    print(f"== {path} ==")
    lines = Path_read(path)
    col = -1
    rows = []
    for raw in lines:
        line = raw.rstrip("\n")
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            continue  # 分隔行
        if col == -1:
            col = find_column(cells, "配音文案")
            if col == -1:
                print("  [ERROR] 未找到「配音文案」列表头")
                return False
            continue
        if len(cells) > col and cells[col]:
            rows.append(cells)
    if not rows:
        print("  [ERROR] 未解析到任何分镜数据行")
        return False
    ok = True
    for cells in rows:
        shot = cells[0] if cells else "?"
        text = cells[col]
        total = len(text)
        hanzi = len(HANZI_RE.findall(text))
        passed = (45 < total <= 50) and (hanzi >= 45)
        ok = ok and passed
        mark = "PASS" if passed else "FAIL"
        print(f"  [{mark}] {shot}: 总字符={total} 汉字={hanzi} | {text}")
    print(f"  --> {'全部通过' if ok else '存在不合格项，请修改'}")
    return ok


def Path_read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    all_ok = True
    for p in sys.argv[1:]:
        all_ok = check_file(p) and all_ok
    print("RESULT:", "PASS" if all_ok else "FAIL")
    return 0 if all_ok else 1


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    sys.exit(main())
