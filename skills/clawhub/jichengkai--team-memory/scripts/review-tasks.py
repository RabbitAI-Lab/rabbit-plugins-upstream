#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime

from task_utils import (
    ACTIVE_STATUS,
    classify_task,
    ensure_task_layout,
    parse_date,
    parse_tasks_md,
    reviews_dir,
    task_summary_line,
    tasks_path,
)
from team_memory_paths import TeamMemoryPathError, print_warnings, resolve_paths


def lines_for(title: str, rows: list[str]) -> list[str]:
    return ["", f"## {title}", "", *(rows if rows else ["无。"])]


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate weekly or monthly Team Memory task review.")
    parser.add_argument("--skill-dir", default=None, help="team-memory skill directory")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--weekly", action="store_true", help="weekly active task scan")
    mode.add_argument("--monthly", action="store_true", help="monthly full task review")
    parser.add_argument("--as-of", default=None, help="review date, YYYY-MM-DD; defaults to today")
    args = parser.parse_args()

    try:
        paths = resolve_paths(args.skill_dir, require_lock=True)
    except TeamMemoryPathError as exc:
        print(f"ERROR: {exc}")
        return 1
    print_warnings(paths.warnings)
    ensure_task_layout(paths.data_dir)

    as_of = parse_date(args.as_of or "") or datetime.now().date()
    review_type = "monthly" if args.monthly else "weekly"
    tasks = parse_tasks_md(tasks_path(paths.data_dir))
    classified = [(task, classify_task(task, as_of)) for task in tasks]

    active = [task_summary_line(task) for task, info in classified if info["active"]]
    overdue = [task_summary_line(task) for task, info in classified if info["overdue"]]
    due_for_check = [task_summary_line(task) for task, info in classified if info["due_for_check"]]
    silent = [task_summary_line(task) for task, info in classified if info["silent"]]
    high = [task_summary_line(task) for task, info in classified if info["high_priority"]]
    waiting = [task_summary_line(task) for task, info in classified if info["waiting"]]

    lines = [
        f"# Team Memory {'月度' if args.monthly else '每周'}待办复盘",
        "",
        f"- 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- 复盘日期: {as_of.isoformat()}",
        f"- 总任务数: {len(tasks)}",
        f"- 活跃任务数: {len(active)}",
    ]
    lines += lines_for("需要立即处理", overdue + high)
    lines += lines_for("本周建议追问", due_for_check + waiting)
    lines += lines_for("沉默超过 14 天", silent)

    if args.monthly:
        month_prefix = as_of.strftime("%Y-%m")
        created = [task_summary_line(task) for task in tasks if task.created_date.startswith(month_prefix)]
        updated = [task_summary_line(task) for task in tasks if task.updated_date.startswith(month_prefix)]
        closed = [
            task_summary_line(task)
            for task in tasks
            if task.status in {"done", "dropped"} and task.updated_date.startswith(month_prefix)
        ]
        deferred = [
            task_summary_line(task)
            for task in tasks
            if task.status == "deferred" and task.updated_date.startswith(month_prefix)
        ]
        status_counts = Counter(task.status for task in tasks)
        lines += [
            "",
            "## 状态统计",
            "",
            *(f"- {status}: {count}" for status, count in sorted(status_counts.items())),
        ]
        lines += lines_for("本月新增", created)
        lines += lines_for("本月关闭", closed)
        lines += lines_for("本月延期", deferred)
        lines += lines_for("本月有动作", updated)
        lines += lines_for(
            "下月重点建议",
            [
                "- 优先关闭逾期和高优先任务。",
                "- 对 waiting 任务逐条追问处理结果。",
                "- 对沉默任务决定继续跟进、延期或丢弃。",
            ],
        )
    else:
        lines += lines_for(
            "处理建议",
            [
                "- 先处理逾期和高优先任务。",
                "- 对 waiting 任务追问对方反馈或自己的下一步动作。",
                "- 对沉默任务补一次状态；没有价值时转 dropped 并写原因。",
            ],
        )

    output = reviews_dir(paths.data_dir) / f"{review_type}-review-{as_of.strftime('%Y%m%d')}.md"
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"已生成待办复盘: {output}")
    print(f"活跃 {len(active)}，逾期 {len(overdue)}，沉默 {len(silent)}，等待反馈 {len(waiting)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
