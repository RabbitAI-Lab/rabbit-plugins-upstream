#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
from datetime import datetime, timedelta
from pathlib import Path

from task_utils import ensure_task_layout, parse_tasks_md, reviews_dir, tasks_path, write_tasks_md
from team_memory_paths import TeamMemoryPathError, print_warnings, resolve_paths


VALID_STATUS = {"done", "waiting", "dropped", "deferred"}
WEEKDAYS = "一二三四五六日"


def default_next_check(status: str) -> str:
    days = 7 if status == "waiting" else 30
    return (datetime.now().date() + timedelta(days=days)).isoformat()


def timeline_path(data_dir: Path, member_id: str) -> Path:
    return data_dir / "members" / member_id / "timeline.md"


def next_timeline_event_id(text: str, date_text: str) -> str:
    ymd = date_text.replace("-", "")
    prefix = f"DLG-{ymd}-TASK-"
    max_number = 0
    for match in re.finditer(rf"\[{re.escape(prefix)}(\d{{3}})\]", text):
        max_number = max(max_number, int(match.group(1)))
    return f"{prefix}{max_number + 1:03d}"


def append_timeline_note(data_dir: Path, member_id: str, task_id: str, title: str, note: str) -> Path:
    path = timeline_path(data_dir, member_id)
    if not path.exists():
        raise RuntimeError(f"缺少成员 timeline.md，无法追加处理结果: {path}")

    today = datetime.now().date()
    date_text = today.isoformat()
    weekday = WEEKDAYS[today.weekday()]
    text = path.read_text(encoding="utf-8")
    event_id = next_timeline_event_id(text, date_text)
    now_text = datetime.now().strftime("%H:%M")
    block = "\n".join(
        [
            f"#### {now_text} - 待办处理结果：{title} [{event_id}]",
            f"**事件**: 待办 `{task_id}` 处理结果：{note}",
            "**类别**: 协作沟通",
            "**评价**: 未评级（待办闭环）",
            "**标签**: #待办闭环",
            "",
            "**观察笔记**:",
            f"- 该记录来自已确认的待办处理结果，关联任务: {task_id}",
            "",
            "**追踪项**:",
            "- [x] 已记录处理结果",
            "",
        ]
    )

    heading = f"### {date_text}（周{weekday}）"
    if heading in text:
        text = text.replace(heading, heading + "\n" + block, 1)
    else:
        marker = "## 时间轴（从新到旧）"
        if marker not in text:
            raise RuntimeError(f"未找到时间轴标题: {path}")
        text = text.replace(marker, marker + "\n\n" + heading + "\n" + block, 1)
    path.write_text(text, encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Draft or apply a Team Memory task status update.")
    parser.add_argument("task_id", help="task id, e.g. TASK-20260701-001")
    parser.add_argument("--skill-dir", default=None, help="team-memory skill directory")
    parser.add_argument("--status", required=True, choices=sorted(VALID_STATUS), help="new task status")
    parser.add_argument("--note", required=True, help="confirmed handling result or reason")
    parser.add_argument("--next-check", default="", help="required for deferred; optional for waiting")
    parser.add_argument("--apply", action="store_true", help="write tasks.md after generating the draft")
    parser.add_argument("--append-timeline", action="store_true", help="also append a confirmed timeline note")
    args = parser.parse_args()

    if args.status == "deferred" and not args.next_check:
        print("ERROR: deferred 状态必须提供 --next-check YYYY-MM-DD")
        return 1
    if args.status == "dropped" and not args.note.strip():
        print("ERROR: dropped 状态必须提供原因")
        return 1

    try:
        paths = resolve_paths(args.skill_dir, require_lock=True)
    except TeamMemoryPathError as exc:
        print(f"ERROR: {exc}")
        return 1
    print_warnings(paths.warnings)
    ensure_task_layout(paths.data_dir)

    path = tasks_path(paths.data_dir)
    tasks = parse_tasks_md(path)
    task = next((item for item in tasks if item.task_id == args.task_id), None)
    if not task:
        print(f"ERROR: 未找到任务: {args.task_id}")
        return 1

    run_date = datetime.now().date().isoformat()
    run_stamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    old_status = task.status
    next_check = args.next_check
    if args.status == "waiting" and not next_check:
        next_check = default_next_check(args.status)

    draft_lines = [
        "# Team Memory 待办处理草案",
        "",
        f"- 任务: `{task.task_id}` {task.title}",
        f"- 对象: {(task.object_type or 'member')}:{task.object_id or task.member_id} {task.object_name or task.member_name}".rstrip(),
        f"- 原状态: {old_status}",
        f"- 新状态: {args.status}",
        f"- 处理说明: {args.note}",
        f"- 下次检查: {next_check}",
        f"- 是否写入: {'是' if args.apply else '否，当前只是草案'}",
    ]
    draft_path = reviews_dir(paths.data_dir) / f"resolve-draft-{task.task_id}-{run_stamp}.md"
    draft_path.write_text("\n".join(draft_lines) + "\n", encoding="utf-8")
    print(f"已生成处理草案: {draft_path}")

    if not args.apply:
        print("当前未加 --apply，未写入 tasks.md。")
        return 0

    if args.append_timeline and (task.object_type or "member") != "member":
        print("ERROR: 只有成员待办支持 --append-timeline；相关方待办请在相关方 timeline.md 手动记录处理结果。")
        return 1

    backup_dir = paths.data_dir / ".backup" / f"task-resolve-{run_stamp}"
    backup_dir.mkdir(parents=True, exist_ok=False)
    if path.exists():
        shutil.copy2(path, backup_dir / "tasks.md")

    task.status = args.status
    task.updated_date = run_date
    task.next_check = next_check
    if args.status in {"done", "dropped"}:
        task.next_check = ""
    task.history.append(f"{run_date} resolve: {old_status} -> {args.status}; {args.note}")
    write_tasks_md(path, tasks)

    if args.append_timeline:
        timeline = timeline_path(paths.data_dir, task.member_id)
        if timeline.exists():
            shutil.copy2(timeline, backup_dir / f"{task.member_id}-timeline.md")
        append_timeline_note(paths.data_dir, task.member_id, task.task_id, task.title, args.note)

    print(f"已更新待办台账: {path}")
    print(f"备份目录: {backup_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
