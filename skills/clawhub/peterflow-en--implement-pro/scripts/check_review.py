"""Freeze reviewed files or verify a phase review receipt from the workspace root."""

import argparse
import hashlib
import json
from pathlib import Path


def digest(name):
    path = Path(name)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Review input must be a workspace-relative path: {name}")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(receipt, phase):
    if not isinstance(receipt, dict) or receipt.get("phase") != phase:
        raise ValueError(f"Expected a review receipt for {phase}")
    for key in ("reviewer", "standards", "requirements"):
        if not isinstance(receipt.get(key), str) or not receipt[key].strip():
            raise ValueError(f"Missing receipt field: {key}")
    inputs = receipt.get("inputs")
    if not isinstance(inputs, dict) or not inputs:
        raise ValueError("Expected input digests frozen at review time")
    for name, expected in inputs.items():
        if digest(name) != expected:
            raise ValueError(f"Reviewed input changed: {name}. Compare snapshots and review affected changes")
    findings = receipt.get("findings")
    if not isinstance(findings, list):
        raise ValueError("Missing findings and decisions")
    for item in findings:
        if not isinstance(item, dict) or not isinstance(item.get("issue"), str) or not item["issue"].strip():
            raise ValueError("Finding has no specific issue")
        decision = item.get("decision")
        if decision in ("dismissed", "驳回") and isinstance(item.get("reason"), str) and item["reason"].strip():
            continue
        raise ValueError(f"Unresolved finding: {item['issue']} ({decision or 'pending'}). Check decision, fix or new receipt")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_subparsers(dest="action", required=True)
    freeze = actions.add_parser("inputs", help="Print SHA-256 digests of the reviewed files")
    freeze.add_argument("files", nargs="+", help="Workspace-relative paths")
    verify = actions.add_parser("check", help="Check current files against a review receipt")
    verify.add_argument("receipt", type=Path)
    verify.add_argument("--phase", required=True)
    args = parser.parse_args()
    try:
        if args.action == "inputs":
            print(json.dumps({name: digest(name) for name in args.files}, ensure_ascii=False, indent=2))
        else:
            check(json.loads(args.receipt.read_text(encoding="utf-8")), args.phase)
            print("Registered inputs match and findings are resolved. Check independent testing and phase acceptance separately.")
    except (ValueError, OSError) as error:
        parser.exit(1, f"{error}\n")
