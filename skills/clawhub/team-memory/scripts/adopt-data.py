#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from team_memory_paths import (
    TeamMemoryPathError,
    candidate_data_dirs,
    data_stats,
    has_data_content,
    print_warnings,
    read_root_lock,
    resolve_paths,
    resolve_data_path,
    resolve_skill_dir,
    same_path,
    update_config_data_path,
    write_root_lock,
)


DEFAULT_DIRS = [
    "members",
    "stakeholders",
    "upward",
    "company",
    "insights",
    "templates",
    "tasks/reviews",
    "archive",
    "import/incoming",
    "import/reports",
    ".backup",
]


def ensure_data_layout(data_dir: Path) -> None:
    for item in DEFAULT_DIRS:
        (data_dir / item).mkdir(parents=True, exist_ok=True)
    for item in [
        "members/.gitkeep",
        "stakeholders/.gitkeep",
        "upward/.gitkeep",
        "company/.gitkeep",
        "insights/.gitkeep",
        "templates/.gitkeep",
        "tasks/.gitkeep",
        "tasks/reviews/.gitkeep",
        "archive/.gitkeep",
        "import/incoming/.gitkeep",
        "import/reports/.gitkeep",
    ]:
        path = data_dir / item
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)
    tasks = data_dir / "tasks" / "tasks.md"
    if not tasks.exists():
        tasks.write_text(
            "\n".join(
                [
                    "# Team Memory 待办台账",
                    "",
                    "> Markdown 是任务状态源；成员时间轴是事实证据源。使用 scripts/sync-tasks.py、review-tasks.py、resolve-task.py 管理。",
                    "",
                    "## 任务列表",
                    "",
                    "暂无任务。",
                    "",
                ]
            ),
            encoding="utf-8",
        )


def copy_example_config(skill_dir: Path) -> None:
    config_path = skill_dir / "skill-config.yaml"
    example_path = skill_dir / "skill-config.example.yaml"
    if config_path.exists() or not example_path.exists():
        return
    shutil.copy2(example_path, config_path)


def write_default_context_files(data_dir: Path) -> None:
    upward = data_dir / "upward" / "expectations.md"
    if not upward.exists():
        upward.write_text(
            "\n".join(
                [
                    "# 上级期望与向上管理",
                    "",
                    "## 当前期望",
                    "",
                    "### 本季度",
                    "- [ ] ",
                    "",
                    "## 向上沟通记录",
                    "",
                    "### YYYY-MM-DD",
                    "**议题**: ",
                    "**上级反馈**: ",
                    "**我的行动**: ",
                    "**关联成员**: ",
                    "",
                ]
            ),
            encoding="utf-8",
        )

    strategy = data_dir / "company" / "strategy.md"
    if not strategy.exists():
        strategy.write_text(
            "\n".join(
                [
                    "# 公司战略与业务方向",
                    "",
                    "## 年度战略",
                    "",
                    "### YYYY",
                    "**战略主题**: ",
                    "",
                    "## 业务变化",
                    "",
                    "### YYYY-MM",
                    "**变化**: ",
                    "**影响**: ",
                    "**团队应对**: ",
                    "",
                ]
            ),
            encoding="utf-8",
        )



def run_doctor(skill_dir: Path) -> None:
    subprocess.run([sys.executable, str(skill_dir / "scripts" / "doctor.py"), "--skill-dir", str(skill_dir)], check=False)


def run_rebuild_index(skill_dir: Path) -> int:
    return subprocess.run(
        [sys.executable, str(skill_dir / "scripts" / "rebuild-index.py"), "--skill-dir", str(skill_dir)],
        check=False,
    ).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="Adopt an existing Team Memory data directory as the only writable root.")
    parser.add_argument("--skill-dir", default=None, help="team-memory skill directory")
    parser.add_argument("--data-dir", default=None, help="data directory to adopt; defaults to <skill-dir>/data")
    parser.add_argument("--init-empty", action="store_true", help="allow adopting an empty data directory during first init")
    parser.add_argument("--force", action="store_true", help="adopt even when other candidate data directories exist")
    parser.add_argument("--no-index", action="store_true", help="do not rebuild JSONL/SQLite indexes")
    args = parser.parse_args()

    skill_dir = resolve_skill_dir(args.skill_dir)
    data_dir = Path(args.data_dir).expanduser() if args.data_dir else skill_dir / "data"
    if not data_dir.is_absolute():
        data_dir = skill_dir / data_dir
    data_dir = data_dir.resolve()

    existing_lock = read_root_lock(skill_dir)
    if existing_lock:
        locked_raw = existing_lock.get("data-dir")
        if locked_raw:
            locked_data_dir = resolve_data_path(str(locked_raw), skill_dir)
            if not same_path(locked_data_dir, data_dir) and not args.force:
                print("ERROR: 当前 skill 已锁定另一套主库，已停止。")
                print(f"- 已锁定: {locked_data_dir}")
                print(f"- 本次请求: {data_dir}")
                print("确认要改主库时再运行 adopt-data.py --force。")
                return 1

    if not data_dir.exists() and not args.init_empty:
        print(f"ERROR: 待接管数据目录不存在: {data_dir}")
        return 1

    ensure_data_layout(data_dir)
    if args.init_empty:
        copy_example_config(skill_dir)
        write_default_context_files(data_dir)

    members, events, _ = data_stats(data_dir)
    if not args.init_empty and not has_data_content(data_dir):
        print(f"ERROR: 待接管目录看起来不是 Team Memory data: {data_dir}")
        return 1

    other_candidates = [
        candidate
        for candidate in candidate_data_dirs(skill_dir)
        if not same_path(candidate.data_dir, data_dir) and (candidate.members or candidate.events)
    ]
    if other_candidates and not args.force:
        print("ERROR: 检测到另一套已有 Team Memory 数据，已停止，避免覆盖或误写。")
        for candidate in other_candidates:
            print(f"- {candidate.data_dir}: 成员 {candidate.members}, 事件 {candidate.events}")
        print("已生成检查报告；确认主库后可重新运行 adopt-data.py --force。")
        run_doctor(skill_dir)
        return 1

    lock_path = write_root_lock(skill_dir, data_dir, "Team Memory 主库已接管；Markdown 是唯一可信源。")
    updated_config = update_config_data_path(skill_dir / "skill-config.yaml", skill_dir, data_dir)

    try:
        paths = resolve_paths(skill_dir, require_lock=True)
    except TeamMemoryPathError as exc:
        print(f"ERROR: 主库接管后校验失败: {exc}")
        return 1
    print_warnings(paths.warnings)

    print(f"已固定主库: {data_dir}")
    print(f"锁定文件: {lock_path}")
    print(f"成员数: {members}")
    print(f"事件数: {events}")
    if updated_config:
        print("已同步 skill-config.yaml 的 settings.data-path")

    if args.no_index:
        return 0
    return run_rebuild_index(skill_dir)


if __name__ == "__main__":
    raise SystemExit(main())
