"""从工作区根目录冻结受评文件，或只读核对一个阶段的评审回执。"""

import argparse
import hashlib
import json
from pathlib import Path


def digest(name):
    path = Path(name)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"受评路径须相对同一工作区：{name}")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(receipt, phase):
    if not isinstance(receipt, dict) or receipt.get("phase") != phase:
        raise ValueError(f"缺少 {phase} 的评审回执或阶段不符")
    for key in ("reviewer", "standards", "requirements"):
        if not isinstance(receipt.get(key), str) or not receipt[key].strip():
            raise ValueError(f"评审回执缺少 {key}")
    inputs = receipt.get("inputs")
    if not isinstance(inputs, dict) or not inputs:
        raise ValueError("缺少评审时冻结的输入")
    for name, expected in inputs.items():
        if digest(name) != expected:
            raise ValueError(f"受评输入变化：{name}，先比较前后内容并重审受影响部分")
    findings = receipt.get("findings")
    if not isinstance(findings, list):
        raise ValueError("缺少发现及裁决记录")
    for item in findings:
        if not isinstance(item, dict) or not isinstance(item.get("issue"), str) or not item["issue"].strip():
            raise ValueError("发现缺少具体问题")
        decision = item.get("decision")
        if decision in ("dismissed", "驳回") and isinstance(item.get("reason"), str) and item["reason"].strip():
            continue
        raise ValueError(f"尚不能采用本次评审：{item['issue']}（{decision or '待裁决'}）。核对裁决、修复或新回执")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_subparsers(dest="action", required=True)
    freeze = actions.add_parser("inputs", help="输出本次评审覆盖文件的 SHA-256")
    freeze.add_argument("files", nargs="+", help="工作区相对文件路径")
    verify = actions.add_parser("check", help="核对当前文件与原评审回执")
    verify.add_argument("receipt", type=Path)
    verify.add_argument("--phase", required=True)
    args = parser.parse_args()
    try:
        if args.action == "inputs":
            print(json.dumps({name: digest(name) for name in args.files}, ensure_ascii=False, indent=2))
        else:
            check(json.loads(args.receipt.read_text(encoding="utf-8")), args.phase)
            print("已登记的受评输入一致，裁决无遗留。继续核对独立测试及阶段验收。")
    except (ValueError, OSError) as error:
        parser.exit(1, f"{error}\n")
