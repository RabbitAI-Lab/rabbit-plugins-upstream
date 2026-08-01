from __future__ import annotations

import difflib
import json
import re
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path

from team_memory_paths import rel_path


TASK_STATUS = {"open", "waiting", "done", "deferred", "dropped"}
ACTIVE_STATUS = {"open", "waiting", "deferred"}
PRIORITY_ORDER = {"高": 3, "中": 2, "低": 1}
TASK_SECTION_LABELS = {"追踪项", "我的承诺", "后续动作"}


@dataclass
class Member:
    member_id: str
    name: str = ""
    alias: str = ""
    role: str = ""
    level: str = ""
    team: str = ""


@dataclass
class SourceTask:
    title: str
    body: str
    priority: str
    object_type: str
    object_id: str
    object_name: str
    member_id: str
    member_name: str
    date: str
    source_event: str
    source_file: str
    source_line: int
    tags: list[str] = field(default_factory=list)

    @property
    def fingerprint(self) -> str:
        return task_fingerprint(self.object_key, self.body)

    @property
    def object_key(self) -> str:
        return f"{self.object_type}:{self.object_id}"


@dataclass
class Task:
    task_id: str
    title: str
    status: str = "open"
    priority: str = "中"
    object_type: str = "member"
    object_id: str = ""
    object_name: str = ""
    member_id: str = ""
    member_name: str = ""
    fingerprint: str = ""
    source_events: list[str] = field(default_factory=list)
    source_files: list[str] = field(default_factory=list)
    created_date: str = ""
    updated_date: str = ""
    due_date: str = ""
    next_check: str = ""
    tags: list[str] = field(default_factory=list)
    body: str = ""
    history: list[str] = field(default_factory=list)

    def to_json(self) -> dict[str, object]:
        return {
            "task_id": self.task_id,
            "title": self.title,
            "status": self.status,
            "priority": self.priority,
            "object_type": self.object_type,
            "object_id": self.object_id,
            "object_name": self.object_name,
            "member_id": self.member_id,
            "member_name": self.member_name,
            "fingerprint": self.fingerprint,
            "source_events": self.source_events,
            "source_files": self.source_files,
            "created_date": self.created_date,
            "updated_date": self.updated_date,
            "due_date": self.due_date,
            "next_check": self.next_check,
            "tags": self.tags,
            "body": self.body,
            "history": self.history,
        }


def today_text() -> str:
    return date.today().isoformat()


def clean_value(raw: str) -> str:
    raw = raw.split("#", 1)[0].strip()
    if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
        return raw[1:-1]
    return raw


def parse_config_members(config_path: Path) -> dict[str, Member]:
    if not config_path.exists():
        return {}
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

    for line in config_path.read_text(encoding="utf-8").splitlines():
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


def ensure_task_layout(data_dir: Path) -> None:
    (data_dir / "tasks" / "reviews").mkdir(parents=True, exist_ok=True)
    (data_dir / "tasks" / ".gitkeep").touch(exist_ok=True)


def tasks_path(data_dir: Path) -> Path:
    ensure_task_layout(data_dir)
    return data_dir / "tasks" / "tasks.md"


def reviews_dir(data_dir: Path) -> Path:
    ensure_task_layout(data_dir)
    return data_dir / "tasks" / "reviews"


def normalize_text(text: str) -> str:
    text = re.sub(r"\(来源:[^)]+\)", "", text)
    text = re.sub(r"（来源：[^）]+）", "", text)
    text = re.sub(r"[`*_#>\[\]()（）:：,，.。;；!！?？/\\|｜-]+", "", text)
    text = re.sub(r"\s+", "", text)
    return text.lower()


def task_fingerprint(object_key: str, text: str) -> str:
    normalized = normalize_text(text)
    # Keep the fingerprint readable; exact matching compares the full normalized body.
    return f"{object_key}:{normalized[:48]}"


def text_similarity(left: str, right: str) -> float:
    left_norm = normalize_text(left)
    right_norm = normalize_text(right)
    if not left_norm or not right_norm:
        return 0.0
    ratio = difflib.SequenceMatcher(None, left_norm, right_norm).ratio()
    left_chars = set(left_norm)
    right_chars = set(right_norm)
    jaccard = len(left_chars & right_chars) / max(1, len(left_chars | right_chars))
    return max(ratio, jaccard)


def same_task_body(left: str, right: str) -> bool:
    left_norm = normalize_text(left)
    right_norm = normalize_text(right)
    return bool(left_norm and right_norm and left_norm == right_norm)


def split_list(raw: str) -> list[str]:
    raw = raw.strip()
    if not raw or raw == "无":
        return []
    return [item.strip() for item in re.split(r"[;,，；]\s*", raw) if item.strip()]


def parse_tags(raw: str) -> list[str]:
    tags = re.findall(r"#[\w\u4e00-\u9fff-]+", raw)
    if tags:
        return tags
    return split_list(raw)


def field_value(lines: list[str], label: str) -> str:
    pattern = re.compile(rf"^\*\*{re.escape(label)}\*\*:\s*(.*)$")
    for line in lines:
        match = pattern.match(line.strip())
        if match:
            return match.group(1).strip()
    return ""


def parse_tasks_md(path: Path) -> list[Task]:
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    tasks: list[Task] = []
    idx = 0
    while idx < len(lines):
        heading = re.match(r"^###\s+(TASK-\d{8}-\d{3})\s+-\s+(.+)$", lines[idx].strip())
        if not heading:
            idx += 1
            continue
        task_id, title = heading.groups()
        block: list[str] = []
        idx += 1
        while idx < len(lines) and not lines[idx].startswith("### "):
            block.append(lines[idx])
            idx += 1

        object_type = field_value(block, "对象类型")
        object_raw = field_value(block, "对象")
        member_raw = field_value(block, "成员")
        if not object_raw and member_raw:
            object_raw = member_raw
            object_type = object_type or "member"
        if not object_type:
            object_type = "member" if member_raw else ""
        object_parts = object_raw.split(" ", 1)
        member_parts = member_raw.split(" ", 1)
        object_id = object_parts[0].strip() if object_parts else ""
        object_name = object_parts[1].strip() if len(object_parts) > 1 else ""
        member_id = member_parts[0].strip() if member_parts else ""
        member_name = member_parts[1].strip() if len(member_parts) > 1 else ""
        if object_type == "member" and object_id and not member_id:
            member_id = object_id
            member_name = object_name
        task = Task(
            task_id=task_id,
            title=title.strip(),
            status=field_value(block, "状态") or "open",
            priority=field_value(block, "优先级") or "中",
            object_type=object_type,
            object_id=object_id or member_id,
            object_name=object_name or member_name,
            member_id=member_id,
            member_name=member_name,
            fingerprint=field_value(block, "主题指纹"),
            source_events=split_list(field_value(block, "来源事件")),
            source_files=split_list(field_value(block, "来源文件")),
            created_date=field_value(block, "创建日期"),
            updated_date=field_value(block, "更新日期"),
            due_date=field_value(block, "截止日期"),
            next_check=field_value(block, "下次检查"),
            tags=parse_tags(field_value(block, "标签")),
        )

        section = ""
        body_lines: list[str] = []
        history_lines: list[str] = []
        for line in block:
            stripped = line.strip()
            if stripped == "**任务内容**:":
                section = "body"
                continue
            if stripped == "**历史记录**:":
                section = "history"
                continue
            if stripped.startswith("**") and stripped.endswith(":"):
                section = ""
                continue
            if section == "body" and stripped.startswith("- "):
                body_lines.append(stripped[2:].strip())
            elif section == "history" and stripped.startswith("- "):
                history_lines.append(stripped[2:].strip())
        task.body = "\n".join(body_lines).strip()
        task.history = history_lines
        tasks.append(task)
    return tasks


def next_task_id(tasks: list[Task], created_date: str) -> str:
    prefix = f"TASK-{created_date.replace('-', '')}-"
    max_number = 0
    for task in tasks:
        if not task.task_id.startswith(prefix):
            continue
        try:
            max_number = max(max_number, int(task.task_id.rsplit("-", 1)[1]))
        except ValueError:
            continue
    return f"{prefix}{max_number + 1:03d}"


def render_tasks_md(tasks: list[Task]) -> str:
    ordered = sorted(
        tasks,
        key=lambda item: (
            item.status not in ACTIVE_STATUS,
            -PRIORITY_ORDER.get(item.priority, 0),
            item.next_check or "9999-12-31",
            item.created_date or "9999-12-31",
            item.task_id,
        ),
    )
    lines = [
        "# Team Memory 待办台账",
        "",
        "> Markdown 是任务状态源；成员时间轴是事实证据源。使用 scripts/sync-tasks.py、review-tasks.py、resolve-task.py 管理。",
        "",
        "## 任务列表",
        "",
    ]
    if not ordered:
        lines.append("暂无任务。")
        lines.append("")
        return "\n".join(lines)

    for task in ordered:
        object_type = task.object_type or "member"
        object_id = task.object_id or task.member_id
        object_name = task.object_name or task.member_name
        lines.extend(
            [
                f"### {task.task_id} - {task.title}",
                f"**状态**: {task.status}",
                f"**优先级**: {task.priority}",
                f"**对象类型**: {object_type}",
                f"**对象**: {object_id} {object_name}".rstrip(),
            ]
        )
        if object_type == "member":
            lines.append(f"**成员**: {task.member_id or object_id} {task.member_name or object_name}".rstrip())
        lines.extend(
            [
                f"**主题指纹**: {task.fingerprint}",
                f"**来源事件**: {', '.join(task.source_events) if task.source_events else '无'}",
                f"**来源文件**: {', '.join(task.source_files) if task.source_files else '无'}",
                f"**创建日期**: {task.created_date}",
                f"**更新日期**: {task.updated_date}",
                f"**截止日期**: {task.due_date}",
                f"**下次检查**: {task.next_check}",
                f"**标签**: {' '.join(task.tags)}",
                "",
                "**任务内容**:",
            ]
        )
        for item in (task.body.splitlines() if task.body else [task.title]):
            lines.append(f"- {item}")
        lines.extend(["", "**历史记录**:"])
        for item in task.history:
            lines.append(f"- {item}")
        lines.append("")
    return "\n".join(lines)


def write_tasks_md(path: Path, tasks: list[Task]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_tasks_md(tasks), encoding="utf-8")


def parse_task_line(raw: str) -> tuple[bool, str, str, list[str]]:
    match = re.match(r"^[-*]\s+\[(?P<mark>[ xX])\]\s*(?P<body>.+)$", raw.strip())
    if not match:
        return False, "", "", []
    checked = match.group("mark").lower() == "x"
    body = match.group("body").strip()
    source_events = re.findall(r"(?:来源|source)[:：]\s*((?:OBS|DLG|FBK)-[A-Z0-9-]+)", body, flags=re.IGNORECASE)
    body = re.sub(r"[（(]\s*来源[:：]\s*(?:OBS|DLG|FBK)-[A-Z0-9-]+\s*[）)]", "", body).strip()
    priority = "中"
    priority_match = re.match(r"^(高|中|低)\s*[-:：]\s*(.+)$", body)
    if priority_match:
        priority, body = priority_match.groups()
        body = body.strip()
    return checked, priority, body, source_events


def infer_next_check(priority: str, base_date: str) -> str:
    parsed = parse_date(base_date) or date.today()
    days = {"高": 3, "中": 7, "低": 30}.get(priority, 7)
    return (parsed + timedelta(days=days)).isoformat()


def parse_date(raw: str) -> date | None:
    if not raw:
        return None
    try:
        return datetime.strptime(raw[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


@dataclass
class TaskOwner:
    object_type: str
    object_id: str
    object_name: str
    member_id: str = ""
    member_name: str = ""


def stakeholder_name_from_profile(path: Path, fallback: str) -> str:
    if not path.exists():
        return fallback
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    return field_value(lines, "名称") or field_value(lines, "姓名") or fallback


def extract_source_tasks(data_dir: Path, members: dict[str, Member]) -> list[SourceTask]:
    members_dir = data_dir / "members"
    sources: list[SourceTask] = []
    if members_dir.exists():
        for child in sorted(members_dir.iterdir()):
            if child.is_dir() and child.name.startswith("member-"):
                member_id = child.name
                member = members.get(member_id, Member(member_id=member_id))
                owner = TaskOwner("member", member_id, member.name, member_id, member.name)
                for file_name in ["timeline.md", "distill.md"]:
                    path = child / file_name
                    sources.extend(extract_source_tasks_from_file(path, owner, data_dir))
            elif child.is_file() and child.name.endswith("-时间轴.md"):
                name = child.name.removesuffix("-时间轴.md")
                member = next((item for item in members.values() if item.name == name), Member(member_id=name, name=name))
                owner = TaskOwner("member", member.member_id, member.name, member.member_id, member.name)
                sources.extend(extract_source_tasks_from_file(child, owner, data_dir))
    stakeholders_dir = data_dir / "stakeholders"
    if stakeholders_dir.exists():
        for child in sorted(stakeholders_dir.iterdir()):
            if not child.is_dir() or not child.name.startswith("stakeholder-"):
                continue
            stakeholder_name = stakeholder_name_from_profile(child / "profile.md", child.name)
            owner = TaskOwner("stakeholder", child.name, stakeholder_name)
            for file_name in ["timeline.md", "distill.md"]:
                path = child / file_name
                sources.extend(extract_source_tasks_from_file(path, owner, data_dir))
    return sources


def extract_source_tasks_from_file(path: Path, owner: TaskOwner, data_dir: Path) -> list[SourceTask]:
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    current_date = ""
    current_event = ""
    current_tags: list[str] = []
    section = ""
    results: list[SourceTask] = []

    for line_no, line in enumerate(lines, start=1):
        stripped = line.strip()
        date_match = re.match(r"^###\s+(\d{4}-\d{2}-\d{2})", stripped)
        if date_match:
            current_date = date_match.group(1)
            current_event = ""
            current_tags = []
            section = ""
            continue
        event_match = re.match(r"^####\s+.+\[((?:OBS|DLG|FBK)-[A-Z0-9-]+)\]\s*$", stripped)
        if event_match:
            current_event = event_match.group(1)
            current_tags = []
            section = ""
            continue
        if stripped.startswith("**标签**:"):
            current_tags = parse_tags(stripped.split(":", 1)[1])
            continue
        bold_section = re.match(r"^\*\*(追踪项|我的承诺|后续动作)\*\*\s*[:：]\s*$", stripped)
        if bold_section:
            section = bold_section.group(1)
            continue
        heading_section = re.match(r"^#{1,6}\s+(.+?)\s*$", stripped)
        if heading_section:
            heading = heading_section.group(1).strip().rstrip(":：")
            section = heading if heading in TASK_SECTION_LABELS else ""
            continue
        if stripped.startswith("**") and stripped.endswith((":","：")):
            section = ""
            continue
        if section not in TASK_SECTION_LABELS:
            continue
        checked, priority, body, explicit_events = parse_task_line(stripped)
        if checked or not body:
            continue
        source_events = explicit_events or ([current_event] if current_event else [])
        event_id = source_events[0] if source_events else ""
        task_date = current_date or today_text()
        results.append(
            SourceTask(
                title=body[:48],
                body=body,
                priority=priority,
                object_type=owner.object_type,
                object_id=owner.object_id,
                object_name=owner.object_name,
                member_id=owner.member_id,
                member_name=owner.member_name,
                date=task_date,
                source_event=event_id,
                source_file=f"{rel_path(path, data_dir)}:{line_no}",
                source_line=line_no,
                tags=current_tags,
            )
        )
    return results


def find_matching_task(tasks: list[Task], source: SourceTask) -> Task | None:
    active = [
        task
        for task in tasks
        if task.status in ACTIVE_STATUS
        and (task.object_type or "member") == source.object_type
        and (task.object_id or task.member_id) == source.object_id
    ]
    for task in active:
        if source.source_file in task.source_files:
            return task
    for task in active:
        if same_task_body(task.body or task.title, source.body):
            return task
    return None


def similar_task_candidates(tasks: list[Task], source: SourceTask, threshold: float = 0.92) -> list[tuple[Task, float]]:
    candidates: list[tuple[Task, float]] = []
    for task in tasks:
        if task.status not in ACTIVE_STATUS:
            continue
        if (task.object_type or "member") != source.object_type:
            continue
        if (task.object_id or task.member_id) != source.object_id:
            continue
        if source.source_file in task.source_files:
            continue
        if same_task_body(task.body or task.title, source.body):
            continue
        score = text_similarity(task.body or task.title, source.body)
        if score >= threshold:
            candidates.append((task, score))
    candidates.sort(key=lambda item: (-item[1], item[0].task_id))
    return candidates


def merge_source_into_task(task: Task, source: SourceTask, run_date: str) -> bool:
    changed = False
    if PRIORITY_ORDER.get(source.priority, 0) > PRIORITY_ORDER.get(task.priority, 0):
        task.priority = source.priority
        changed = True
    if source.source_event and source.source_event not in task.source_events:
        task.source_events.append(source.source_event)
        changed = True
    if source.source_file and source.source_file not in task.source_files:
        task.source_files.append(source.source_file)
        changed = True
    for tag in source.tags:
        if tag not in task.tags:
            task.tags.append(tag)
            changed = True
    if not task.next_check:
        task.next_check = infer_next_check(task.priority, run_date)
        changed = True
    if changed:
        task.updated_date = run_date
        task.history.append(f"{run_date} sync: 合并来源 {source.source_event or source.source_file}")
    return changed


def create_task_from_source(task_id: str, source: SourceTask, run_date: str) -> Task:
    return Task(
        task_id=task_id,
        title=source.title,
        status="open",
        priority=source.priority,
        object_type=source.object_type,
        object_id=source.object_id,
        object_name=source.object_name,
        member_id=source.member_id,
        member_name=source.member_name,
        fingerprint=source.fingerprint,
        source_events=[source.source_event] if source.source_event else [],
        source_files=[source.source_file] if source.source_file else [],
        created_date=run_date,
        updated_date=run_date,
        due_date="",
        next_check=infer_next_check(source.priority, run_date),
        tags=list(dict.fromkeys(source.tags)),
        body=source.body,
        history=[f"{run_date} sync: 创建自 {source.source_event or source.source_file}"],
    )


def tasks_to_jsonl(path: Path, tasks: list[Task]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for task in tasks:
            handle.write(json.dumps(task.to_json(), ensure_ascii=False, sort_keys=True) + "\n")


def classify_task(task: Task, as_of: date) -> dict[str, bool]:
    updated = parse_date(task.updated_date) or parse_date(task.created_date) or as_of
    due = parse_date(task.due_date)
    next_check = parse_date(task.next_check)
    silent_days = (as_of - updated).days
    return {
        "active": task.status in ACTIVE_STATUS,
        "overdue": bool(due and due < as_of and task.status in ACTIVE_STATUS),
        "due_for_check": bool(next_check and next_check <= as_of and task.status in ACTIVE_STATUS),
        "silent": silent_days >= 14 and task.status in ACTIVE_STATUS,
        "high_priority": task.priority == "高" and task.status in ACTIVE_STATUS,
        "waiting": task.status == "waiting",
    }


def task_summary_line(task: Task) -> str:
    object_type = task.object_type or "member"
    object_id = task.object_id or task.member_id
    object_name = task.object_name or task.member_name
    owner = f"{object_type}:{object_id} {object_name}".strip()
    return f"- `{task.task_id}` [{task.status}/{task.priority}] {owner} - {task.title}"
