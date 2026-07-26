#!/usr/bin/env python3
"""
每日效率规划师 — 时间块日程生成脚本

根据任务列表、可用时间段和优先级，自动生成时间块日程。
使用番茄钟工作法：25分钟工作 + 5分钟休息，每4组15分钟长休息。

用法:
    python generate_schedule.py --tasks '{"tasks": [...], "start": "09:00", "end": "22:00"}'
    python generate_schedule.py --interactive

示例:
    python generate_schedule.py --tasks '{"tasks": [{"name": "写报告", "priority": "high", "duration": 90, "deadline": "14:00"}], "start": "09:00", "end": "22:00"}'
"""

import argparse
import json
import sys
from datetime import datetime, timedelta


POMODORO_WORK = 25  # 分钟
POMODORO_BREAK = 5  # 分钟
POMODORO_LONG_BREAK = 15  # 分钟
POMODORO_BEFORE_LONG = 4  # 每完成4个番茄钟后长休息
BUFFER = 5  # 任务间缓冲时间（分钟）
LUNCH_START = (12, 0)
LUNCH_END = (13, 30)

PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}
PRIORITY_LABEL = {"high": "🔴 紧急重要", "medium": "🟡 重要", "low": "🟢 常规"}


def parse_time(time_str):
    """解析 HH:MM 格式的时间字符串为分钟数。"""
    parts = time_str.strip().split(":")
    return int(parts[0]) * 60 + int(parts[1])


def format_time(minutes):
    """将分钟数格式化为 HH:MM。"""
    h = minutes // 60
    m = minutes % 60
    return f"{h:02d}:{m:02d}"


def sort_tasks(tasks):
    """按优先级和截止时间排序任务。"""
    def sort_key(task):
        priority = PRIORITY_ORDER.get(task.get("priority", "medium"), 1)
        deadline = task.get("deadline")
        if deadline:
            deadline_val = parse_time(deadline)
        else:
            deadline_val = 9999  # 无截止时间的排后面
        return (priority, deadline_val)

    return sorted(tasks, key=sort_key)


def is_lunch_time(time_min):
    """检查给定时间是否在午休时段内。"""
    lunch_start = LUNCH_START[0] * 60 + LUNCH_START[1]
    lunch_end = LUNCH_END[0] * 60 + LUNCH_END[1]
    return lunch_start <= time_min < lunch_end


def generate_schedule(tasks, start_time, end_time):
    """
    生成时间块日程。

    Args:
        tasks: 任务列表，每个任务包含 name, priority, duration, deadline(可选)
        start_time: 开始时间 HH:MM
        end_time: 结束时间 HH:MM

    Returns:
        list: 时间块列表，每个块包含 time, task, type, pomodoro_count
    """
    start_min = parse_time(start_time)
    end_min = parse_time(end_time)
    sorted_tasks = sort_tasks(tasks)

    schedule = []
    current_time = start_min
    pomodoro_count = 0
    lunch_scheduled = False

    for task in sorted_tasks:
        remaining_duration = task.get("duration", 60)

        # 检查是否到了午休时间
        if not lunch_scheduled and is_lunch_time(current_time):
            schedule.append({
                "time": format_time(current_time),
                "end": format_time(LUNCH_START[0] * 60 + LUNCH_END[1]),
                "task": "🍽️ 午餐 + 休息",
                "type": "lunch",
                "pomodoro": "—",
                "status": "⬜",
            })
            current_time = LUNCH_END[0] * 60 + LUNCH_END[1]
            lunch_scheduled = True

        # 如果任务有截止时间，检查是否需要提前
        deadline = task.get("deadline")
        if deadline:
            deadline_min = parse_time(deadline)
            if current_time + remaining_duration > deadline_min:
                # 尽早安排
                pass  # 已通过排序处理

        # 将任务分解为番茄钟
        while remaining_duration > 0 and current_time < end_min:
            # 跳过午休时间
            if is_lunch_time(current_time):
                if not lunch_scheduled:
                    schedule.append({
                        "time": format_time(current_time),
                        "end": format_time(LUNCH_END[0] * 60 + LUNCH_END[1]),
                        "task": "🍽️ 午餐 + 休息",
                        "type": "lunch",
                        "pomodoro": "—",
                        "status": "⬜",
                    })
                    current_time = LUNCH_END[0] * 60 + LUNCH_END[1]
                    lunch_scheduled = True
                else:
                    current_time = LUNCH_END[0] * 60 + LUNCH_END[1]
                    continue

            if current_time >= end_min:
                break

            # 工作时段
            work_duration = min(POMODORO_WORK, remaining_duration)
            pomodoro_count += 1
            schedule.append({
                "time": format_time(current_time),
                "end": format_time(current_time + work_duration),
                "task": task["name"],
                "type": "work",
                "pomodoro": f"🍅 #{pomodoro_count}",
                "status": "⬜",
            })
            current_time += work_duration
            remaining_duration -= work_duration

            # 休息时段
            if remaining_duration > 0 or (pomodoro_count % POMODORO_BEFORE_LONG == 0):
                if pomodoro_count % POMODORO_BEFORE_LONG == 0:
                    break_duration = POMODORO_LONG_BREAK
                    break_label = "☕ 长休息"
                else:
                    break_duration = POMODORO_BREAK
                    break_label = "☕ 休息"

                if current_time + break_duration <= end_min:
                    schedule.append({
                        "time": format_time(current_time),
                        "end": format_time(current_time + break_duration),
                        "task": break_label,
                        "type": "break",
                        "pomodoro": "—",
                        "status": "⬜",
                    })
                    current_time += break_duration

            # 任务间缓冲
            if remaining_duration <= 0:
                current_time += BUFFER

    return schedule


def format_schedule_markdown(schedule, tasks, date_str=None):
    """将日程格式化为 Markdown 表格。"""
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")

    lines = []
    lines.append(f"# 📅 今日效率规划 — {date_str}\n")

    # 今日目标
    lines.append("## 🎯 今日目标\n")
    high_priority = [t for t in tasks if t.get("priority") == "high"]
    if high_priority:
        lines.append(f"完成 {len(high_priority)} 项核心任务：{'、'.join(t['name'] for t in high_priority[:3])}\n")
    else:
        lines.append(f"完成 {len(tasks)} 项任务\n")

    # 优先级矩阵
    lines.append("## 📊 优先级矩阵\n")
    lines.append("| 优先级 | 任务 | 预计时长 | 截止时间 |")
    lines.append("|--------|------|----------|----------|")
    sorted_tasks = sort_tasks(tasks)
    for task in sorted_tasks:
        priority = PRIORITY_LABEL.get(task.get("priority", "medium"), "🟢 常规")
        duration = f"{task.get('duration', 60)}分钟"
        deadline = task.get("deadline", "—")
        lines.append(f"| {priority} | {task['name']} | {duration} | {deadline} |")
    lines.append("")

    # 时间块日程
    lines.append("## ⏰ 时间块日程\n")
    lines.append("| 时间 | 任务 | 番茄钟 | 状态 |")
    lines.append("|------|------|--------|------|")
    for block in schedule:
        time_range = f"{block['time']}-{block['end']}"
        lines.append(f"| {time_range} | {block['task']} | {block['pomodoro']} | {block['status']} |")
    lines.append("")

    # 清单
    lines.append("## ✅ 今日清单\n")
    for task in sorted_tasks:
        lines.append(f"- [ ] {task['name']}")
    lines.append("")

    # 统计
    work_blocks = [b for b in schedule if b["type"] == "work"]
    total_work = sum(POMODORO_WORK for _ in work_blocks)
    lines.append("## 📈 统计\n")
    lines.append(f"- 番茄钟总数：{len(work_blocks)} 🍅")
    lines.append(f"- 预计工作时长：{total_work // 60}小时{total_work % 60}分钟")
    lines.append(f"- 时间块总数：{len(schedule)}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="每日效率规划师 — 生成时间块日程")
    parser.add_argument(
        "--tasks",
        type=str,
        help='任务JSON，格式: {"tasks": [...], "start": "09:00", "end": "22:00"}',
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="交互式模式",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="输出文件路径（可选）",
    )

    args = parser.parse_args()

    if args.interactive:
        print("=" * 50)
        print("  📅 每日效率规划师 — 交互模式")
        print("=" * 50)

        tasks = []
        print("\n请输入今天的任务（输入空行结束）：")
        while True:
            name = input(f"任务 {len(tasks) + 1} 名称（空行结束）: ").strip()
            if not name:
                break
            duration = input("预计时长（分钟，默认60）: ").strip()
            duration = int(duration) if duration else 60
            priority = input("优先级 (high/medium/low，默认medium): ").strip().lower()
            priority = priority if priority in ("high", "medium", "low") else "medium"
            deadline = input("截止时间 (HH:MM，可省略): ").strip()
            task = {"name": name, "duration": duration, "priority": priority}
            if deadline:
                task["deadline"] = deadline
            tasks.append(task)

        start_time = input("\n可用时间起点 (默认 09:00): ").strip()
        start_time = start_time if start_time else "09:00"
        end_time = input("可用时间终点 (默认 22:00): ").strip()
        end_time = end_time if end_time else "22:00"

    elif args.tasks:
        data = json.loads(args.tasks)
        tasks = data.get("tasks", [])
        start_time = data.get("start", "09:00")
        end_time = data.get("end", "22:00")
    else:
        # Demo 模式
        print("未提供任务数据，运行演示模式...\n")
        tasks = [
            {"name": "写项目报告", "priority": "high", "duration": 90, "deadline": "14:00"},
            {"name": "回复邮件", "priority": "medium", "duration": 30},
            {"name": "学习新技术", "priority": "medium", "duration": 60},
            {"name": "整理桌面", "priority": "low", "duration": 15},
        ]
        start_time = "09:00"
        end_time = "22:00"

    schedule = generate_schedule(tasks, start_time, end_time)
    markdown = format_schedule_markdown(schedule, tasks)

    print(markdown)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(markdown)
        print(f"\n✅ 已保存到: {args.output}")


if __name__ == "__main__":
    main()
