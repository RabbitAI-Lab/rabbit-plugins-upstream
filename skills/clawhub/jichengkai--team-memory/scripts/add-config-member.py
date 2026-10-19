#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def validate_member(config_path: Path, member_id: str) -> str:
    text = config_path.read_text(encoding="utf-8")
    if re.search(rf"(?m)^\s*-\s+id:\s*['\"]?{re.escape(member_id)}['\"]?\s*$", text):
        raise RuntimeError(f"配置已存在成员 ID: {member_id}")
    if not re.search(r"(?m)^members:\s*$", text):
        raise RuntimeError("skill-config.yaml 缺少 members 顶层段。")
    return text


def add_member(config_path: Path, member_id: str, name: str, role: str, join_date: str) -> None:
    text = validate_member(config_path, member_id)
    lines = text.splitlines()
    members_line = next(idx for idx, line in enumerate(lines) if re.match(r"^members:\s*$", line))
    insert_at = len(lines)
    for idx in range(members_line + 1, len(lines)):
        line = lines[idx]
        if line and not line[0].isspace() and not line.lstrip().startswith("#"):
            insert_at = idx
            while insert_at > members_line + 1 and (
                not lines[insert_at - 1].strip() or lines[insert_at - 1].lstrip().startswith("#")
            ):
                insert_at -= 1
            break
    block = [
        f"  - id: {yaml_string(member_id)}",
        f"    name: {yaml_string(name)}",
        '    alias: ""',
        f"    role: {yaml_string(role)}",
        '    level: ""',
        '    team: ""',
        f"    join-date: {yaml_string(join_date)}",
        '    manager-notes: ""',
        "",
    ]
    output = lines[:insert_at] + block + lines[insert_at:]
    temporary = config_path.with_name(f".{config_path.name}.member.tmp")
    temporary.write_text("\n".join(output).rstrip() + "\n", encoding="utf-8")
    temporary.replace(config_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Add one member to Team Memory skill-config.yaml.")
    parser.add_argument("--config", required=True)
    parser.add_argument("--id", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--role", required=True)
    parser.add_argument("--join-date", required=True)
    parser.add_argument("--check", action="store_true", help="validate only; do not edit the config")
    args = parser.parse_args()
    try:
        if args.check:
            validate_member(Path(args.config), args.id)
            return 0
        add_member(Path(args.config), args.id, args.name, args.role, args.join_date)
    except RuntimeError as exc:
        print(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
