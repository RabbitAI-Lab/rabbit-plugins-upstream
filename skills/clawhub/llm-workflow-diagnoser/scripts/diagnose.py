#!/usr/bin/env python3
"""diagnose.py - 辅助脚本：打印追问清单与报告骨架。

不会修改任何正式资产；不连网；不调用任何 LLM。
用法：
    python scripts/diagnose.py question-bank
    python scripts/diagnose.py report-template
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFERENCES = ROOT / "references"


def print_file(label: str, relative: str) -> None:
    target = REFERENCES / relative
    if not target.exists():
        print(f"[error] {label} 不存在: {target}", file=sys.stderr)
        sys.exit(1)
    print(f"# === {label} ({relative}) ===")
    print(target.read_text(encoding="utf-8"))


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "question-bank":
        print_file("追问清单", "question_bank.md")
    elif cmd == "report-template":
        print_file("报告骨架", "report_template.md")
    elif cmd == "scoring-rubric":
        print_file("评分 Rubric", "scoring_rubric.md")
    else:
        print(f"[error] 未知命令: {cmd}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()