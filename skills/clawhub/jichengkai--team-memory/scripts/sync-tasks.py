#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from datetime import datetime

from task_utils import (
    create_task_from_source,
    ensure_task_layout,
    extract_source_tasks,
    find_matching_task,
    merge_source_into_task,
    next_task_id,
    parse_config_members,
    parse_tasks_md,
    reviews_dir,
    similar_task_candidates,
    tasks_path,
    write_tasks_md,
)
from team_memory_paths import TeamMemoryPathError, print_warnings, resolve_paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Team Memory follow-up items into data/tasks/tasks.md.")
    parser.add_argument("--skill-dir", default=None, help="team-memory skill directory")
    parser.add_argument("--dry-run", action="store_true", help="generate report without writing tasks.md")
    args = parser.parse_args()

    try:
        paths = resolve_paths(args.skill_dir, require_lock=True)
    except TeamMemoryPathError as exc:
        print(f"ERROR: {exc}")
        return 1
    print_warnings(paths.warnings)

    ensure_task_layout(paths.data_dir)
    run_date = datetime.now().date().isoformat()
    run_stamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    members = parse_config_members(paths.config_path)
    path = tasks_path(paths.data_dir)
    tasks = parse_tasks_md(path)
    sources = extract_source_tasks(paths.data_dir, members)

    created = 0
    merged = 0
    ignored = 0
    actions: list[str] = []
    similar_hints: list[str] = []
    similar_seen: set[tuple[str, str]] = set()

    for source in sources:
        match = find_matching_task(tasks, source)
        if match:
            if merge_source_into_task(match, source, run_date):
                merged += 1
                actions.append(f"- 合并到 `{match.task_id}`: {source.body} ({source.source_event or source.source_file})")
            else:
                ignored += 1
            continue
        for candidate, score in similar_task_candidates(tasks, source)[:3]:
            hint_key = (candidate.task_id, source.source_file)
            if hint_key in similar_seen:
                continue
            similar_seen.add(hint_key)
            similar_hints.append(
                f"- `{candidate.task_id}` 与 `{source.source_file}` 相似度 {score:.2f}，未自动合并: {source.body}"
            )
        task = create_task_from_source(next_task_id(tasks, run_date), source, run_date)
        tasks.append(task)
        created += 1
        actions.append(f"- 新建 `{task.task_id}`: {task.body} ({source.source_event or source.source_file})")

    report_lines = [
        "# Team Memory 待办同步报告",
        "",
        f"- 模式: {'dry-run' if args.dry_run else 'apply'}",
        f"- 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- 扫描追踪项: {len(sources)}",
        f"- 新建任务: {created}",
        f"- 合并来源: {merged}",
        f"- 已存在且无变化: {ignored}",
        f"- 相似但未自动合并: {len(similar_hints)}",
        "",
        "## 变更明细",
        "",
    ]
    report_lines.extend(actions if actions else ["无。"])
    report_lines.extend(["", "## 相似但未自动合并", ""])
    if similar_hints:
        report_lines.extend(similar_hints[:100])
        if len(similar_hints) > 100:
            report_lines.append(f"- 仅显示前 100 条，另有 {len(similar_hints) - 100} 条。")
    else:
        report_lines.append("无。")

    report_path = reviews_dir(paths.data_dir) / f"sync-report-{run_stamp}.md"
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    if args.dry_run:
        print(f"已生成同步预览: {report_path}")
        print("当前为 dry-run，未写入 tasks.md。")
        return 0

    if path.exists():
        backup_dir = paths.data_dir / ".backup" / f"tasks-sync-{run_stamp}"
        backup_dir.mkdir(parents=True, exist_ok=False)
        shutil.copy2(path, backup_dir / "tasks.md")
    write_tasks_md(path, tasks)

    print(f"已同步待办台账: {path}")
    print(f"同步报告: {report_path}")
    print(f"新建 {created}，合并 {merged}，无变化 {ignored}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
