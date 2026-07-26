#!/usr/bin/env python3
"""
黄金追踪 - 提醒去重器
去除提醒文件中的重复条目。
零第三方依赖。
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ALERTS_DIR = ROOT / "alerts"


def dedup_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")

    pattern = r'(##\s*\[\d{2}:\d{2}\][^\n]*\n.*?)(?=##\s*\[\d{2}:\d{2}\]|\Z)'
    records = re.findall(pattern, text, re.DOTALL)

    if not records:
        return 0

    seen = set()
    unique = []
    removed = 0

    for rec in records:
        price_m = re.search(r'当前价\s*\|\s*\$?([\d,\.]+)', rec)
        change_m = re.search(r'变动\s*\|\s*([\-\+]?\d+\.?\d*)%', rec)
        key = None
        if price_m and change_m:
            key = f"{price_m.group(1)}-{change_m.group(1)}"

        if key and key in seen:
            removed += 1
            continue
        if key:
            seen.add(key)
        unique.append(rec.strip())

    if removed == 0:
        return 0

    header = "# 金价异动提醒\n\n" if "# 金价异动" in text else ""
    new_text = header + "\n\n---\n\n".join(unique) + "\n"

    path.with_suffix(path.suffix + ".bak").write_text(text, encoding="utf-8")
    path.write_text(new_text, encoding="utf-8")
    return removed


def main():
    if not ALERTS_DIR.exists():
        print("[信息] alerts/ 目录不存在")
        return

    total_removed = 0
    for f in sorted(ALERTS_DIR.iterdir()):
        if f.suffix != ".md" or f.name.endswith(".bak"):
            continue
        n = dedup_file(f)
        if n:
            print(f"[已修复] {f.name}: 移除 {n} 条重复")
            total_removed += n
        else:
            print(f"[通过]  {f.name}: 无重复")

    print(f"\n[完成] 共移除 {total_removed} 条重复记录")


if __name__ == "__main__":
    main()
