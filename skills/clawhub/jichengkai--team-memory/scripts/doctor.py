#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from task_utils import parse_tasks_md
from team_memory_paths import (
    TeamMemoryPathError,
    candidate_data_dirs,
    data_stats,
    print_warnings,
    read_config_data_path,
    read_root_lock,
    rel_path,
    resolve_paths,
    resolve_skill_dir,
    same_path,
)


EVENT_RE = re.compile(r"^####\s+.+\s+\[((?:OBS|DLG|FBK)-[A-Z0-9-]+)\]\s*$")
FIELD_RE = re.compile(r"^\*\*(?P<label>[^*]+)\*\*:\s*(?P<value>.*)$")


def report_path_for(skill_dir: Path, data_dir: Path | None) -> Path:
    base = data_dir if data_dir and data_dir.exists() else skill_dir
    reports_dir = base / ".reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return reports_dir / f"doctor-report-{stamp}.md"


def write_report(skill_dir: Path, primary_data_dir: Path | None, lines: list[str]) -> Path:
    path = report_path_for(skill_dir, primary_data_dir)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def field_value(lines: list[str], label: str) -> str:
    values: list[str] = []
    for line in lines:
        match = FIELD_RE.match(line.strip())
        if match and match.group("label") == label:
            values.append(match.group("value").strip())
    return " / ".join(values)


def scan_timeline(path: Path, data_dir: Path, owner_type: str, owner_id: str) -> list[dict[str, object]]:
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    events: list[dict[str, object]] = []
    idx = 0
    while idx < len(lines):
        match = EVENT_RE.match(lines[idx].strip())
        if not match:
            idx += 1
            continue
        event_id = match.group(1)
        start_line = idx + 1
        block = [lines[idx]]
        idx += 1
        while idx < len(lines):
            stripped = lines[idx].strip()
            if stripped.startswith("### ") or stripped.startswith("#### "):
                break
            block.append(lines[idx])
            idx += 1
        source_file = rel_path(path, data_dir)
        events.append(
            {
                "event_id": event_id,
                "event_key": f"{source_file}:{event_id}",
                "owner_type": owner_type,
                "owner_id": owner_id,
                "source_file": source_file,
                "source_line": start_line,
                "feedback_type": field_value(block, "反馈类型"),
                "evidence_level": field_value(block, "证据等级"),
                "verification_status": field_value(block, "核实状态"),
                "related_members": field_value(block, "涉及成员"),
                "related_event": field_value(block, "关联事件"),
                "raw": "\n".join(block),
            }
        )
    return events


def collect_markdown_events(data_dir: Path) -> list[dict[str, object]]:
    events: list[dict[str, object]] = []
    members_dir = data_dir / "members"
    if members_dir.exists():
        for child in sorted(members_dir.iterdir()):
            if child.is_dir() and child.name.startswith("member-"):
                events.extend(scan_timeline(child / "timeline.md", data_dir, "member", child.name))
            elif child.is_file() and child.name.endswith("-时间轴.md"):
                events.extend(scan_timeline(child, data_dir, "member", child.name.removesuffix("-时间轴.md")))
    stakeholders_dir = data_dir / "stakeholders"
    if stakeholders_dir.exists():
        for child in sorted(stakeholders_dir.iterdir()):
            if child.is_dir() and child.name.startswith("stakeholder-"):
                events.extend(scan_timeline(child / "timeline.md", data_dir, "stakeholder", child.name))
    return events


def check_data_consistency(data_dir: Path) -> list[str]:
    events = collect_markdown_events(data_dir)
    event_ids = {str(event["event_id"]) for event in events}
    event_key_groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    event_id_groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for event in events:
        event_key_groups[str(event["event_key"])].append(event)
        event_id_groups[str(event["event_id"])].append(event)
    lines: list[str] = ["", "## 数据一致性检查", ""]
    findings: list[str] = []

    duplicate_keys = sorted(event_key for event_key, group in event_key_groups.items() if len(group) > 1)
    if duplicate_keys:
        findings.append(f"- 必须修复：同一文件内重复事件 ID {len(duplicate_keys)} 个；这些记录会产生相同 event_key。")
        for event_key in duplicate_keys[:10]:
            locations = [
                f"{event['source_file']}:{event['source_line']}"
                for event in event_key_groups[event_key]
            ]
            findings.append(f"  - `{event_key}`: {', '.join(locations)}")

    cross_file_duplicate_ids = sorted(
        event_id
        for event_id, group in event_id_groups.items()
        if len({str(event["source_file"]) for event in group}) > 1
    )
    if cross_file_duplicate_ids:
        findings.append(
            f"- 发现跨文件重复事件 ID {len(cross_file_duplicate_ids)} 个；索引会用 event_key 区分，但人工引用时需留意。"
        )
        for event_id in cross_file_duplicate_ids[:10]:
            locations = [
                f"{event['source_file']}:{event['source_line']}"
                for event in event_id_groups[event_id]
            ]
            findings.append(f"  - `{event_id}`: {', '.join(locations)}")

    for event in events:
        if not str(event["event_id"]).startswith("FBK-"):
            continue
        missing = [
            label
            for label, key in [("反馈类型", "feedback_type"), ("证据等级", "evidence_level"), ("核实状态", "verification_status")]
            if not str(event.get(key, "")).strip()
        ]
        if missing:
            findings.append(
                f"- `FBK` 缺少必填字段 {', '.join(missing)}: {event['source_file']}:{event['source_line']} `{event['event_id']}`"
            )
        related_members = str(event.get("related_members", "")).strip()
        if related_members:
            back_refs = [
                item
                for item in events
                if item["owner_type"] == "member" and str(event["event_id"]) in str(item.get("related_event", ""))
            ]
            if not back_refs:
                findings.append(
                    f"- `FBK` 涉及成员但未发现成员侧关联记录: {event['source_file']}:{event['source_line']} `{event['event_id']}`"
                )

    for event in events:
        refs = re.findall(r"(?:OBS|DLG|FBK)-[A-Z0-9-]+", str(event.get("related_event", "")))
        for ref in refs:
            if ref not in event_ids:
                findings.append(
                    f"- 关联事件不存在: {event['source_file']}:{event['source_line']} `{event['event_id']}` -> `{ref}`"
                )

    task_file = data_dir / "tasks" / "tasks.md"
    tasks = parse_tasks_md(task_file)
    for task in tasks:
        for source_event in task.source_events:
            if source_event and source_event != "无" and source_event not in event_ids:
                findings.append(f"- 待办 `{task.task_id}` 来源事件不存在: `{source_event}`")
        for source_file in task.source_files:
            raw_path = source_file.split(":", 1)[0]
            if raw_path and raw_path != "无" and not (data_dir / raw_path).exists():
                findings.append(f"- 待办 `{task.task_id}` 来源文件不存在: `{source_file}`")

    low_evidence_patterns = ["证据等级**: 线索", "证据等级**: 反馈", "线索级", "反馈级"]
    members_dir = data_dir / "members"
    if members_dir.exists():
        for distill in members_dir.glob("member-*/distill.md"):
            text = distill.read_text(encoding="utf-8", errors="replace")
            if any(pattern in text for pattern in low_evidence_patterns):
                findings.append(f"- 成员蒸馏中出现低证据等级内容，请确认未作为长期结论: {rel_path(distill, data_dir)}")

    if findings:
        lines.extend(findings)
    else:
        lines.append("未发现明显一致性问题。")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Team Memory root lock, data paths, and duplicate data directories.")
    parser.add_argument("--skill-dir", default=None, help="team-memory skill directory")
    args = parser.parse_args()

    skill_dir = resolve_skill_dir(args.skill_dir)
    lock = read_root_lock(skill_dir)
    primary_data_dir: Path | None = None
    lock_error = ""
    paths = None

    try:
        paths = resolve_paths(skill_dir, require_lock=bool(lock), allow_missing_data=True)
        primary_data_dir = paths.data_dir
    except TeamMemoryPathError as exc:
        lock_error = str(exc)

    candidates = candidate_data_dirs(skill_dir)
    lines: list[str] = [
        "# Team Memory 主库检查报告",
        "",
        f"- 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- Skill 目录: `{skill_dir}`",
        f"- 主库锁定文件: `{skill_dir / '.team-memory-root.json'}`",
        f"- 锁定状态: {'已锁定' if lock else '未锁定'}",
    ]

    if primary_data_dir:
        members, events, primary_ids = data_stats(primary_data_dir)
        lines.extend(
            [
                f"- 当前主库: `{primary_data_dir}`",
                f"- 主库成员数: {members}",
                f"- 主库事件总数: {events}",
                f"- 主库唯一事件 ID 数: {len(primary_ids)}",
            ]
        )
    else:
        primary_ids = set()
        lines.append("- 当前主库: 未确认")

    config_data_path = read_config_data_path(skill_dir / "skill-config.yaml")
    if config_data_path:
        lines.append(f"- skill-config.yaml data-path: `{config_data_path}`")
    if lock_error:
        lines.extend(["", "## 锁定/配置问题", "", f"- {lock_error}"])
    if paths and paths.warnings:
        lines.extend(["", "## 警告", ""])
        lines.extend(f"- {item}" for item in paths.warnings)

    lines.extend(["", "## 候选数据目录", ""])
    if not candidates:
        lines.append("未发现任何候选数据目录。")
    else:
        lines.extend(["| 位置 | 成员数 | 事件总数 | 唯一事件 ID 数 | 是否主库 |", "|---|---:|---:|---:|---|"])
        for candidate in candidates:
            is_primary = primary_data_dir is not None and same_path(candidate.data_dir, primary_data_dir)
            lines.append(
                f"| `{candidate.data_dir}` | {candidate.members} | {candidate.events} | {candidate.unique_event_ids} | {'是' if is_primary else '否'} |"
            )

    if primary_data_dir and len(candidates) > 1:
        lines.extend(["", "## 多目录差异", ""])
        for candidate in candidates:
            if same_path(candidate.data_dir, primary_data_dir):
                continue
            _, _, ids = data_stats(candidate.data_dir)
            duplicate_ids = sorted(primary_ids.intersection(ids))
            primary_only = sorted(primary_ids - ids)
            candidate_only = sorted(ids - primary_ids)
            lines.extend(
                [
                    f"### {candidate.data_dir}",
                    f"- 与主库重复事件 ID: {len(duplicate_ids)}",
                    f"- 只在主库的事件 ID: {len(primary_only)}",
                    f"- 只在该目录的事件 ID: {len(candidate_only)}",
                ]
            )
            if duplicate_ids:
                lines.append(f"- 重复样例: `{', '.join(duplicate_ids[:10])}`")
            if candidate_only:
                lines.append(f"- 该目录独有样例: `{', '.join(candidate_only[:10])}`")

    if primary_data_dir and primary_data_dir.exists():
        lines.extend(check_data_consistency(primary_data_dir))

    lines.extend(
        [
            "",
            "## 建议",
            "",
            "- 没有主库锁定文件时，不要写入；先运行 `scripts/init.sh` 或 `scripts/adopt-data.py`。",
            "- 发现多套数据时，不要自动合并；先确认哪一套是主库。",
            "- SQLite/JSONL 只作为可重建索引，Markdown 才是可信源。",
        ]
    )

    report_path = write_report(skill_dir, primary_data_dir, lines)
    if paths:
        print_warnings(paths.warnings)
    print(f"检查报告: {report_path}")
    if primary_data_dir:
        print(f"当前主库: {primary_data_dir}")
    if lock_error:
        print(f"ERROR: {lock_error}")
        return 1
    if candidates:
        print("候选数据目录:")
        for candidate in candidates:
            marker = " (主库)" if primary_data_dir and same_path(candidate.data_dir, primary_data_dir) else ""
            print(
                f"- {candidate.data_dir}{marker}: 成员 {candidate.members}, "
                f"事件 {candidate.events}, 唯一事件 ID {candidate.unique_event_ids}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
