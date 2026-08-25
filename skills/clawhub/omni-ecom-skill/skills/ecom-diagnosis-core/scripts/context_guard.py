#!/usr/bin/env python3
"""Check that a run's inputs stay inside an explicitly allowed client scope."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


TEXT_SUFFIXES = {".csv", ".json", ".md", ".txt", ".yaml", ".yml", ".py", ".ps1"}


def inside(root: Path, candidate: Path) -> bool:
    try:
        candidate.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def files_under(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    if path.is_dir():
        return [item for item in path.rglob("*") if item.is_file()]
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description="校验电商任务的客户上下文路径隔离")
    parser.add_argument("--client-scope", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--allowed-root", action="append", required=True)
    parser.add_argument("--path", action="append", required=True)
    parser.add_argument("--forbid-term", action="append", default=[])
    parser.add_argument("--output")
    args = parser.parse_args()

    allowed = [Path(value).resolve() for value in args.allowed_root]
    errors: list[str] = []
    scanned: list[str] = []
    for root in allowed:
        if not root.exists():
            errors.append(f"allowed-root 不存在: {root}")
    for raw_path in args.path:
        path = Path(raw_path).resolve()
        if not any(inside(root, path) for root in allowed):
            errors.append(f"路径越过允许根目录: {path}")
            continue
        if not path.exists():
            errors.append(f"输入路径不存在: {path}")
            continue
        for file_path in files_under(path):
            scanned.append(str(file_path))
            if file_path.suffix.casefold() not in TEXT_SUFFIXES:
                continue
            try:
                text = file_path.read_text(encoding="utf-8-sig")
            except (OSError, UnicodeDecodeError):
                continue
            for term in args.forbid_term:
                if term and term.casefold() in text.casefold():
                    errors.append(f"命中禁止跨范围词: {file_path} -> {term}")

    result = {
        "status": "PASS" if not errors else "BLOCKED",
        "client_scope": args.client_scope,
        "run_id": args.run_id,
        "allowed_roots": [str(path) for path in allowed],
        "scanned_files": len(scanned),
        "errors": errors,
    }
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        output = Path(args.output).resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8")
        print(output)
    else:
        print(payload, end="")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
