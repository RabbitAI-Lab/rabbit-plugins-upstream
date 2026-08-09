#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sqlite3
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from task_utils import parse_tasks_md, tasks_path, tasks_to_jsonl
from team_memory_paths import TeamMemoryPathError, print_warnings, rel_path, resolve_paths


WEEKDAYS = "一二三四五六日"


@dataclass
class Member:
    member_id: str
    name: str = ""
    alias: str = ""
    role: str = ""
    level: str = ""
    team: str = ""


@dataclass
class Stakeholder:
    stakeholder_id: str
    name: str = ""
    department: str = ""
    role: str = ""
    kind: str = ""


def clean_value(raw: str) -> str:
    raw = raw.split("#", 1)[0].strip()
    if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
        return raw[1:-1]
    return raw


def parse_config_members(config_path: Path) -> dict[str, Member]:
    if not config_path.exists():
        return {}
    text = config_path.read_text(encoding="utf-8")
    members: dict[str, Member] = {}
    current: dict[str, str] | None = None
    in_members = False

    def finish_current() -> None:
        nonlocal current
        if not current:
            return
        member_id = current.get("id", "")
        if member_id:
            members[member_id] = Member(
                member_id=member_id,
                name=current.get("name", ""),
                alias=current.get("alias", ""),
                role=current.get("role", ""),
                level=current.get("level", ""),
                team=current.get("team", ""),
            )
        current = None

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        is_top_level = bool(line) and not line[0].isspace()
        if is_top_level and re.match(r"^[A-Za-z0-9_-]+:", stripped) and not stripped.startswith("- "):
            section = stripped.split(":", 1)[0]
            if section != "members":
                finish_current()
            in_members = section == "members"
            continue
        if not in_members:
            continue
        if stripped.startswith("- "):
            finish_current()
            current = {}
            rest = stripped[2:].strip()
            if ":" in rest:
                key, value = rest.split(":", 1)
                current[key.strip()] = clean_value(value)
            continue
        if current is not None and ":" in stripped:
            key, value = stripped.split(":", 1)
            current[key.strip()] = clean_value(value)

    finish_current()
    return members


def field_value(lines: list[str], label: str) -> str:
    pattern = re.compile(rf"^\*\*{re.escape(label)}\*\*:\s*(.*)$")
    values: list[str] = []
    for line in lines:
        match = pattern.match(line.strip())
        if match:
            values.append(match.group(1).strip())
    return " / ".join(values)


def field_section(lines: list[str], label: str) -> str:
    pattern = re.compile(rf"^\*\*{re.escape(label)}\*\*:\s*(.*)$")
    values: list[str] = []
    collecting = False
    for line in lines:
        stripped = line.strip()
        match = pattern.match(stripped)
        if match:
            collecting = True
            inline = match.group(1).strip()
            if inline:
                values.append(inline)
            continue
        if collecting:
            if stripped.startswith("**") and "**:" in stripped:
                break
            if stripped.startswith("### ") or stripped.startswith("#### "):
                break
            if stripped:
                values.append(re.sub(r"^[-*]\s+", "", stripped))
    return " / ".join(values)


def parse_tags(raw: str) -> list[str]:
    return re.findall(r"#[\w\u4e00-\u9fff-]+", raw)


def compact(raw: str, limit: int = 220) -> str:
    text = re.sub(r"\s+", " ", raw).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def event_key(source_file: str, event_id: str) -> str:
    return f"{source_file}:{event_id}"


def parse_profile_field(path: Path, label: str) -> str:
    if not path.exists():
        return ""
    return field_value(path.read_text(encoding="utf-8", errors="replace").splitlines(), label)


def parse_stakeholder_profile(path: Path, stakeholder_id: str) -> Stakeholder:
    return Stakeholder(
        stakeholder_id=stakeholder_id,
        name=parse_profile_field(path, "名称") or parse_profile_field(path, "姓名") or stakeholder_id,
        department=parse_profile_field(path, "部门"),
        role=parse_profile_field(path, "职责") or parse_profile_field(path, "角色"),
        kind=parse_profile_field(path, "类型"),
    )


def parse_timeline(path: Path, member_id: str, member: Member, data_dir: Path) -> list[dict[str, object]]:
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    events: list[dict[str, object]] = []
    current_date = ""
    idx = 0

    while idx < len(lines):
        line = lines[idx]
        date_match = re.match(r"^###\s+(\d{4}-\d{2}-\d{2})", line.strip())
        if date_match:
            current_date = date_match.group(1)
            idx += 1
            continue

        event_match = re.match(r"^####\s+(.+?)\s+\[((?:OBS|DLG)-[A-Z0-9-]+)\]\s*$", line.strip())
        if not event_match:
            idx += 1
            continue

        title = event_match.group(1).strip()
        event_id = event_match.group(2).strip()
        start_line = idx + 1
        block = [line]
        idx += 1
        while idx < len(lines):
            stripped = lines[idx].strip()
            if stripped.startswith("### ") or stripped.startswith("#### "):
                break
            block.append(lines[idx])
            idx += 1

        raw = "\n".join(block).rstrip()
        category = field_value(block, "类别")
        rating = field_value(block, "评价")
        tags_text = field_value(block, "标签")
        event_text = field_value(block, "事件")
        related_event = field_value(block, "关联事件")
        source_file = rel_path(path, data_dir)
        events.append(
            {
                "event_key": event_key(source_file, event_id),
                "event_id": event_id,
                "event_type": "member",
                "member_id": member_id,
                "member_name": member.name,
                "member_alias": member.alias,
                "member_role": member.role,
                "member_level": member.level,
                "member_team": member.team,
                "stakeholder_id": "",
                "stakeholder_name": "",
                "stakeholder_department": "",
                "feedback_type": "",
                "evidence_level": "",
                "verification_status": "",
                "source_party": "",
                "related_members": "",
                "related_project": "",
                "related_event": related_event,
                "date": current_date,
                "title": title,
                "category": category,
                "rating": rating,
                "tags": parse_tags(tags_text),
                "event": event_text,
                "summary": compact(event_text or title),
                "source_file": source_file,
                "source_line": start_line,
                "raw_markdown": raw,
            }
        )
    return events


def parse_stakeholder_timeline(
    path: Path,
    stakeholder_id: str,
    stakeholder: Stakeholder,
    data_dir: Path,
) -> list[dict[str, object]]:
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    events: list[dict[str, object]] = []
    current_date = ""
    idx = 0

    while idx < len(lines):
        line = lines[idx]
        date_match = re.match(r"^###\s+(\d{4}-\d{2}-\d{2})", line.strip())
        if date_match:
            current_date = date_match.group(1)
            idx += 1
            continue

        event_match = re.match(r"^####\s+(.+?)\s+\[(FBK-[A-Z0-9-]+)\]\s*$", line.strip())
        if not event_match:
            idx += 1
            continue

        title = event_match.group(1).strip()
        event_id = event_match.group(2).strip()
        start_line = idx + 1
        block = [line]
        idx += 1
        while idx < len(lines):
            stripped = lines[idx].strip()
            if stripped.startswith("### ") or stripped.startswith("#### "):
                break
            block.append(lines[idx])
            idx += 1

        raw = "\n".join(block).rstrip()
        tags_text = field_value(block, "标签")
        feedback_type = field_value(block, "反馈类型")
        evidence_level = field_value(block, "证据等级")
        verification_status = field_value(block, "核实状态")
        source_party = field_value(block, "来源方")
        related_members = field_value(block, "涉及成员")
        related_project = field_value(block, "涉及项目")
        fact_text = field_section(block, "事实描述")
        judgement = field_section(block, "当前判断")
        next_actions = field_section(block, "后续动作")
        related_event = field_value(block, "关联事件")
        summary_source = fact_text or judgement or title
        source_file = rel_path(path, data_dir)

        events.append(
            {
                "event_key": event_key(source_file, event_id),
                "event_id": event_id,
                "event_type": "stakeholder_feedback",
                "member_id": "",
                "member_name": "",
                "member_alias": "",
                "member_role": "",
                "member_level": "",
                "member_team": "",
                "stakeholder_id": stakeholder_id,
                "stakeholder_name": stakeholder.name,
                "stakeholder_department": stakeholder.department,
                "feedback_type": feedback_type,
                "evidence_level": evidence_level,
                "verification_status": verification_status,
                "source_party": source_party,
                "related_members": related_members,
                "related_project": related_project,
                "related_event": related_event,
                "date": current_date,
                "title": title,
                "category": "相关方反馈",
                "rating": "",
                "tags": parse_tags(tags_text),
                "event": fact_text,
                "summary": compact(summary_source),
                "current_judgement": judgement,
                "next_actions": next_actions,
                "source_file": source_file,
                "source_line": start_line,
                "raw_markdown": raw,
            }
        )
    return events


def collect_events(data_dir: Path, members: dict[str, Member]) -> list[dict[str, object]]:
    members_dir = data_dir / "members"
    events: list[dict[str, object]] = []

    if members_dir.exists():
        for child in sorted(members_dir.iterdir()):
            if child.is_dir() and child.name.startswith("member-"):
                member_id = child.name
                member = members.get(member_id, Member(member_id=member_id))
                events.extend(parse_timeline(child / "timeline.md", member_id, member, data_dir))
            elif child.is_file() and child.name.endswith("-时间轴.md"):
                name = child.name.removesuffix("-时间轴.md")
                member = next((item for item in members.values() if item.name == name), Member(member_id=name, name=name))
                events.extend(parse_timeline(child, member.member_id, member, data_dir))

    stakeholders_dir = data_dir / "stakeholders"
    if stakeholders_dir.exists():
        for child in sorted(stakeholders_dir.iterdir()):
            if not child.is_dir() or not child.name.startswith("stakeholder-"):
                continue
            stakeholder = parse_stakeholder_profile(child / "profile.md", child.name)
            events.extend(parse_stakeholder_timeline(child / "timeline.md", child.name, stakeholder, data_dir))

    events.sort(
        key=lambda item: (
            str(item.get("date", "")),
            str(item.get("member_id", "")),
            str(item.get("stakeholder_id", "")),
            str(item.get("event_id", "")),
        )
    )
    return events


def write_jsonl(path: Path, events: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for event in events:
            handle.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")


def duplicate_event_key_groups(events: list[dict[str, object]]) -> dict[str, list[dict[str, object]]]:
    groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for event in events:
        groups[str(event.get("event_key", ""))].append(event)
    return {event_key: group for event_key, group in groups.items() if event_key and len(group) > 1}


def write_sqlite(path: Path, members: dict[str, Member], events: list[dict[str, object]], tasks: list[object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        path.unlink()
    conn = sqlite3.connect(path)
    try:
        conn.execute(
            """
            CREATE TABLE members (
                member_id TEXT PRIMARY KEY,
                name TEXT,
                alias TEXT,
                role TEXT,
                level TEXT,
                team TEXT
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE events (
                event_key TEXT PRIMARY KEY,
                event_id TEXT,
                event_type TEXT,
                member_id TEXT,
                member_name TEXT,
                stakeholder_id TEXT,
                stakeholder_name TEXT,
                stakeholder_department TEXT,
                feedback_type TEXT,
                evidence_level TEXT,
                verification_status TEXT,
                source_party TEXT,
                related_members TEXT,
                related_project TEXT,
                related_event TEXT,
                date TEXT,
                title TEXT,
                category TEXT,
                rating TEXT,
                tags TEXT,
                event TEXT,
                summary TEXT,
                current_judgement TEXT,
                next_actions TEXT,
                source_file TEXT,
                source_line INTEGER,
                raw_markdown TEXT
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE tasks (
                task_id TEXT PRIMARY KEY,
                title TEXT,
                status TEXT,
                priority TEXT,
                object_type TEXT,
                object_id TEXT,
                object_name TEXT,
                member_id TEXT,
                member_name TEXT,
                fingerprint TEXT,
                source_events TEXT,
                source_files TEXT,
                created_date TEXT,
                updated_date TEXT,
                due_date TEXT,
                next_check TEXT,
                tags TEXT,
                body TEXT,
                history TEXT
            )
            """
        )
        conn.execute("CREATE INDEX idx_events_event_id ON events(event_id)")
        conn.execute("CREATE INDEX idx_events_member_date ON events(member_id, date)")
        conn.execute("CREATE INDEX idx_events_stakeholder_date ON events(stakeholder_id, date)")
        conn.execute("CREATE INDEX idx_events_feedback_status ON events(feedback_type, evidence_level, verification_status)")
        conn.execute("CREATE INDEX idx_events_date ON events(date)")
        conn.execute("CREATE INDEX idx_tasks_status_check ON tasks(status, next_check)")
        conn.execute("CREATE INDEX idx_tasks_member_status ON tasks(member_id, status)")

        for member in members.values():
            conn.execute(
                "INSERT OR REPLACE INTO members VALUES (?, ?, ?, ?, ?, ?)",
                (member.member_id, member.name, member.alias, member.role, member.level, member.team),
            )

        for event in events:
            conn.execute(
                """
                INSERT INTO events VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    event["event_key"],
                    event["event_id"],
                    event.get("event_type", ""),
                    event["member_id"],
                    event["member_name"],
                    event.get("stakeholder_id", ""),
                    event.get("stakeholder_name", ""),
                    event.get("stakeholder_department", ""),
                    event.get("feedback_type", ""),
                    event.get("evidence_level", ""),
                    event.get("verification_status", ""),
                    event.get("source_party", ""),
                    event.get("related_members", ""),
                    event.get("related_project", ""),
                    event.get("related_event", ""),
                    event["date"],
                    event["title"],
                    event["category"],
                    event["rating"],
                    " ".join(event.get("tags", [])),
                    event["event"],
                    event["summary"],
                    event.get("current_judgement", ""),
                    event.get("next_actions", ""),
                    event["source_file"],
                    event["source_line"],
                    event["raw_markdown"],
                ),
            )
        for task in tasks:
            conn.execute(
                """
                INSERT OR REPLACE INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    task.task_id,
                    task.title,
                    task.status,
                    task.priority,
                    task.object_type,
                    task.object_id,
                    task.object_name,
                    task.member_id,
                    task.member_name,
                    task.fingerprint,
                    " ".join(task.source_events),
                    " | ".join(task.source_files),
                    task.created_date,
                    task.updated_date,
                    task.due_date,
                    task.next_check,
                    " ".join(task.tags),
                    task.body,
                    " | ".join(task.history),
                ),
            )
        conn.commit()
    finally:
        conn.close()


def main() -> int:
    parser = argparse.ArgumentParser(description="Rebuild Team Memory JSONL and SQLite indexes from Markdown.")
    parser.add_argument("--skill-dir", default=None, help="team-memory skill directory")
    args = parser.parse_args()

    try:
        paths = resolve_paths(args.skill_dir, require_lock=True)
    except TeamMemoryPathError as exc:
        print(f"ERROR: {exc}")
        return 1

    print_warnings(paths.warnings)
    members = parse_config_members(paths.config_path)
    events = collect_events(paths.data_dir, members)
    tasks = parse_tasks_md(tasks_path(paths.data_dir))
    duplicate_event_keys = duplicate_event_key_groups(events)
    if duplicate_event_keys:
        print("ERROR: 发现同一文件内重复事件 ID，已停止重建索引，避免 SQLite 静默覆盖。")
        for event_key, group in sorted(duplicate_event_keys.items())[:10]:
            locations = ", ".join(f"{event['source_file']}:{event['source_line']}" for event in group)
            print(f"- {event_key}: {locations}")
        if len(duplicate_event_keys) > 10:
            print(f"- 仅显示前 10 个，另有 {len(duplicate_event_keys) - 10} 个。")
        print("请先在对应 timeline.md 中修正重复事件 ID 后再重建索引。")
        return 1
    index_dir = paths.data_dir / ".index"
    jsonl_path = index_dir / "events.jsonl"
    tasks_jsonl_path = index_dir / "tasks.jsonl"
    sqlite_path = index_dir / "team-memory.sqlite"
    manifest_path = index_dir / "manifest.json"

    write_jsonl(jsonl_path, events)
    tasks_to_jsonl(tasks_jsonl_path, tasks)
    write_sqlite(sqlite_path, members, events, tasks)
    manifest = {
        "generated-at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source-of-truth": "markdown",
        "data-dir": str(paths.data_dir),
        "members": len(members),
        "events": len(events),
        "tasks": len(tasks),
        "jsonl": str(jsonl_path),
        "tasks-jsonl": str(tasks_jsonl_path),
        "sqlite": str(sqlite_path),
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"已重建索引: {jsonl_path}")
    print(f"已重建待办索引: {tasks_jsonl_path}")
    print(f"已重建数据库: {sqlite_path}")
    print(f"事件数: {len(events)}")
    print(f"待办数: {len(tasks)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
