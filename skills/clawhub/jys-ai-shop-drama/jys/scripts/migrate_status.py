#!/usr/bin/env python3
"""Safely migrate a legacy JYS status.md to schema version 2."""

from __future__ import annotations

import argparse
import json
import os
import re
from datetime import datetime
from pathlib import Path


def legacy_step(text: str, step: str) -> str:
    match = re.search(rf"^\|\s*{re.escape(step)}\s*\|\s*([^|]+?)\s*\|", text, re.MULTILINE)
    if not match:
        return "not_started"
    value = match.group(1).strip()
    return "confirmed" if value in {"是", "已完成", "完成", "confirmed"} else "not_started"


def has_v2_frontmatter(text: str) -> bool:
    if not text.startswith("---\n"):
        return False
    end = text.find("\n---\n", 4)
    if end < 0:
        return False
    return bool(re.search(r"^schema_version:\s*2\s*$", text[4:end], re.MULTILINE))


def infer_s4(workspace: Path) -> tuple[str, str]:
    path = workspace / "s4-workspace.md"
    if not path.is_file():
        return "not_started", "not_started"
    text = path.read_text(encoding="utf-8")
    script_markers = ("人物：", "【段落", "【第一", "完整剧本")
    if any(marker in text for marker in script_markers):
        return "confirmed", "in_progress"
    return "in_progress", "not_started"


def choose_route(s1: str, s2: str, s3: str, s4_outline: str, s4_script: str) -> tuple[str, str, str, str]:
    if s1 != "confirmed":
        return "S1", "jys-s1", "恢复并确认套路内核和变体", "套路内核和变体确认"
    if s2 != "confirmed" and s3 != "confirmed":
        return "ROUTE", "jys", "读取已选内核，确定普通路线或产品强绑定路线", ""
    if s2 != "confirmed":
        return "S2", "jys-s2", "继续完成替换方案和定制化剧情骨架", ""
    if s3 != "confirmed":
        return "S3", "jys-s3", "选择并确认当前项目的带货产品", "产品确认"
    if s4_script != "confirmed":
        action = "继续确认事件级大纲" if s4_outline != "confirmed" else "继续逐段完成剧本"
        return "S4", "jys-s4", action, ""
    return "S5", "jys-s5", "整理并交付最终拍摄模板", ""


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def render_frontmatter(status_path: Path, text: str, project_name: str, project_root: str) -> str:
    s1 = legacy_step(text, "S1")
    s2 = legacy_step(text, "S2")
    s3 = legacy_step(text, "S3")
    s4_outline, s4_script = infer_s4(status_path.parent)
    stage, next_skill, next_action, waiting_for = choose_route(s1, s2, s3, s4_outline, s4_script)
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    fields = [
        "---",
        "schema_version: 2",
        f"project_name: {yaml_string(project_name)}",
        f"project_root: {yaml_string(project_root)}",
        'jys_workspace: "jys-workspace"',
        f"current_stage: {stage}",
        f"current_skill: {next_skill}",
        f"next_skill: {next_skill}",
        f"next_action: {yaml_string(next_action)}",
        f"waiting_for: {yaml_string(waiting_for)}",
        f"s1: {s1}",
        f"s2: {s2}",
        f"s3: {s3}",
        f"s4_outline: {s4_outline}",
        f"s4_script: {s4_script}",
        "s5_delivery: not_started",
        "final_confirmation: pending",
        f"last_updated: {yaml_string(now)}",
        "---",
        "",
    ]
    return "\n".join(fields) + text.lstrip("\ufeff")


def main() -> None:
    parser = argparse.ArgumentParser(description="Migrate a legacy JYS status.md to schema version 2 without deleting its body.")
    parser.add_argument("status", type=Path, help="Path to JYS_WORKSPACE/status.md")
    parser.add_argument("--project-name", default="旧版JYS项目")
    parser.add_argument("--project-root", help="Confirmed project root; defaults to status.md grandparent")
    parser.add_argument("--dry-run", action="store_true", help="Print the migrated result without writing files")
    args = parser.parse_args()

    status = args.status.resolve()
    if not status.is_file():
        raise SystemExit(f"status file not found: {status}")
    text = status.read_text(encoding="utf-8")
    if has_v2_frontmatter(text):
        print(json.dumps({"ok": True, "changed": False, "reason": "already schema_version 2", "status": str(status)}, ensure_ascii=False))
        return

    project_root = args.project_root or str(status.parent.parent)
    migrated = render_frontmatter(status, text, args.project_name, project_root)
    if args.dry_run:
        print(migrated)
        return

    backup = status.with_name("status.v1.backup.md")
    if not backup.exists():
        backup.write_text(text, encoding="utf-8")
    temp = status.with_name("status.md.tmp")
    temp.write_text(migrated, encoding="utf-8")
    temp.read_text(encoding="utf-8")
    os.replace(temp, status)
    print(json.dumps({"ok": True, "changed": True, "status": str(status), "backup": str(backup)}, ensure_ascii=False))


if __name__ == "__main__":
    main()

