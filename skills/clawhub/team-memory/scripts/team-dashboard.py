#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import importlib.util
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from task_utils import ACTIVE_STATUS, classify_task, parse_date, parse_tasks_md, tasks_path
from team_memory_paths import TeamMemoryPathError, print_warnings, rel_path, resolve_paths


def load_rebuild_index_module() -> Any:
    path = SCRIPT_DIR / "rebuild-index.py"
    spec = importlib.util.spec_from_file_location("team_memory_rebuild_index", path)
    if not spec or not spec.loader:
        raise RuntimeError(f"无法加载索引解析脚本: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


REBUILD_INDEX = load_rebuild_index_module()

POSITIVE_MARKERS = ("优秀", "良好", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐", "认可", "亮点")
CONCERN_MARKERS = ("需关注", "严重", "⚠", "投诉", "延期", "下滑", "冲突", "失误")
VERIFIED_STATUSES = {"已确认", "已闭环", "部分确认"}
STRONG_EVIDENCE_LEVELS = {"事实", "结论"}
RISK_FEEDBACK_TYPES = {"投诉", "风险"}


@dataclass
class MemberSignal:
    member_id: str
    name: str = ""
    role: str = ""
    level: str = ""
    team: str = ""
    event_count: int = 0
    positive_events: int = 0
    concern_events: int = 0
    stakeholder_feedback: int = 0
    verified_feedback: int = 0
    risky_feedback: int = 0
    active_tasks: int = 0
    high_tasks: int = 0
    overdue_tasks: int = 0
    waiting_tasks: int = 0
    silent_tasks: int = 0
    categories: Counter[str] = field(default_factory=Counter)
    latest_date: str = ""
    latest_title: str = ""
    latest_event_id: str = ""
    latest_source: str = ""
    distill_signals: list[str] = field(default_factory=list)

    @property
    def display_name(self) -> str:
        return self.name or self.member_id

    @property
    def risk_score(self) -> int:
        return (
            self.overdue_tasks * 5
            + self.high_tasks * 3
            + self.waiting_tasks * 2
            + self.silent_tasks * 2
            + self.concern_events * 2
            + self.risky_feedback * 3
        )

    @property
    def opportunity_score(self) -> int:
        return self.positive_events * 2 + self.verified_feedback + self.event_count


def is_positive(text: str) -> bool:
    return any(marker in text for marker in POSITIVE_MARKERS)


def is_concern(text: str) -> bool:
    return any(marker in text for marker in CONCERN_MARKERS)


def compact(raw: str, limit: int = 96) -> str:
    text = re.sub(r"\s+", " ", raw).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def read_signal_lines(path: Path, max_items: int = 4) -> list[str]:
    if not path.exists():
        return []
    signals: list[str] = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith(">"):
            continue
        line = re.sub(r"^[-*]\s+", "", line)
        line = re.sub(r"^\*\*([^*]+)\*\*[:：]?\s*", r"\1: ", line)
        if re.match(r"^[\[\]\s]+$", line):
            continue
        if re.match(r"^[\w\u4e00-\u9fff /-]+[:：]\s*$", line):
            continue
        if len(line) < 3 or line in {"无", "暂无"}:
            continue
        signals.append(compact(line, 90))
        if len(signals) >= max_items:
            break
    return signals


def event_date(event: dict[str, object]) -> date | None:
    return parse_date(str(event.get("date", "")))


def within_window(event: dict[str, object], start: date, end: date) -> bool:
    parsed = event_date(event)
    return bool(parsed and start <= parsed <= end)


def member_matches_feedback(member: MemberSignal, event: dict[str, object]) -> bool:
    haystack = " ".join(
        str(event.get(key, ""))
        for key in ["related_members", "summary", "event", "current_judgement", "title"]
    )
    tokens = [member.member_id, member.name]
    return any(token and token in haystack for token in tokens)


def top_counter(counter: Counter[str], limit: int = 3) -> list[str]:
    return [f"{name} {count}" for name, count in counter.most_common(limit) if name]


def member_status(member: MemberSignal, stale: bool) -> str:
    if member.overdue_tasks or member.risky_feedback or member.concern_events >= 2:
        return "需管理介入"
    if stale:
        return "证据不足"
    if member.positive_events >= 2 and member.risk_score == 0:
        return "高能稳定"
    if member.high_tasks or member.waiting_tasks:
        return "跟进中"
    return "正常观察"


def build_packet(data_dir: Path, config_path: Path, as_of: date, window_days: int, max_members: int) -> dict[str, Any]:
    members = REBUILD_INDEX.parse_config_members(config_path)
    events = REBUILD_INDEX.collect_events(data_dir, members)
    tasks = parse_tasks_md(tasks_path(data_dir))
    start = as_of - timedelta(days=window_days - 1)
    recent_events = [event for event in events if within_window(event, start, as_of)]

    member_signals: dict[str, MemberSignal] = {}
    for member_id, member in members.items():
        member_dir = data_dir / "members" / member_id
        member_signals[member_id] = MemberSignal(
            member_id=member_id,
            name=member.name,
            role=member.role,
            level=member.level,
            team=member.team,
            distill_signals=read_signal_lines(member_dir / "distill.md", 3),
        )

    for event in events:
        member_id = str(event.get("member_id", ""))
        if not member_id or member_id not in member_signals:
            continue
        parsed = event_date(event)
        if parsed and (not member_signals[member_id].latest_date or parsed.isoformat() > member_signals[member_id].latest_date):
            member_signals[member_id].latest_date = parsed.isoformat()
            member_signals[member_id].latest_title = str(event.get("title", ""))
            member_signals[member_id].latest_event_id = str(event.get("event_id", ""))
            source = str(event.get("source_file", ""))
            line = str(event.get("source_line", ""))
            member_signals[member_id].latest_source = f"{source}:{line}" if source and line else source

    category_counts: Counter[str] = Counter()
    rating_counts: Counter[str] = Counter()
    stakeholder_counts: Counter[str] = Counter()
    for event in recent_events:
        if str(event.get("event_type", "")) == "member":
            member_id = str(event.get("member_id", ""))
            signal = member_signals.get(member_id)
            if not signal:
                continue
            category = str(event.get("category", "")).strip()
            rating = str(event.get("rating", "")).strip()
            signal.event_count += 1
            signal.categories[category] += 1
            category_counts[category] += 1
            if rating:
                rating_counts[rating] += 1
            joined = " ".join(str(event.get(key, "")) for key in ["rating", "title", "summary", "tags"])
            if is_positive(joined):
                signal.positive_events += 1
            if is_concern(joined):
                signal.concern_events += 1
        elif str(event.get("event_type", "")) == "stakeholder_feedback":
            feedback_type = str(event.get("feedback_type", "")).strip()
            evidence_level = str(event.get("evidence_level", "")).strip()
            verification_status = str(event.get("verification_status", "")).strip()
            if feedback_type:
                stakeholder_counts[feedback_type] += 1
            for signal in member_signals.values():
                if not member_matches_feedback(signal, event):
                    continue
                signal.stakeholder_feedback += 1
                if evidence_level in STRONG_EVIDENCE_LEVELS and verification_status in VERIFIED_STATUSES:
                    signal.verified_feedback += 1
                if feedback_type in RISK_FEEDBACK_TYPES:
                    signal.risky_feedback += 1

    classified_tasks = [(task, classify_task(task, as_of)) for task in tasks]
    for task, info in classified_tasks:
        if task.status not in ACTIVE_STATUS:
            continue
        object_type = task.object_type or "member"
        object_id = task.object_id or task.member_id
        if object_type != "member" or object_id not in member_signals:
            continue
        signal = member_signals[object_id]
        signal.active_tasks += 1
        if task.priority == "高":
            signal.high_tasks += 1
        if info["overdue"]:
            signal.overdue_tasks += 1
        if info["waiting"]:
            signal.waiting_tasks += 1
        if info["silent"]:
            signal.silent_tasks += 1

    total_members = len(member_signals)
    members_with_recent_events = sum(1 for item in member_signals.values() if item.event_count)
    stale_members = [item for item in member_signals.values() if item.event_count == 0]
    active_tasks = [task for task, _ in classified_tasks if task.status in ACTIVE_STATUS]
    overdue_tasks = [task for task, info in classified_tasks if info["overdue"]]
    high_tasks = [task for task, _ in classified_tasks if task.status in ACTIVE_STATUS and task.priority == "高"]
    waiting_tasks = [task for task, info in classified_tasks if info["waiting"]]
    silent_tasks = [task for task, info in classified_tasks if info["silent"]]
    concern_events = sum(item.concern_events for item in member_signals.values())
    positive_events = sum(item.positive_events for item in member_signals.values())
    risky_feedback = sum(item.risky_feedback for item in member_signals.values())

    health_score = 82
    health_score -= min(28, len(overdue_tasks) * 7 + len(high_tasks) * 3)
    health_score -= min(18, concern_events * 3 + risky_feedback * 4)
    health_score -= min(16, len(stale_members) * 4)
    health_score += min(10, positive_events * 2)
    health_score = max(0, min(100, health_score))
    coverage = round((members_with_recent_events / total_members) * 100) if total_members else 0
    control_pressure = len(overdue_tasks) * 3 + len(high_tasks) * 2 + len(waiting_tasks) + len(silent_tasks)
    momentum = positive_events - concern_events - risky_feedback

    if health_score >= 85 and control_pressure <= 2:
        judgement = "整体稳定，可以把管理重心放在提效、授权和标杆复制。"
    elif health_score >= 70:
        judgement = "整体可控，但需要先处理局部风险、沉默待办和证据盲区。"
    else:
        judgement = "控制压力偏高，建议先收敛风险、明确责任边界，再推进发展型动作。"

    strengths: list[str] = []
    if positive_events:
        strengths.append(f"近期正向信号 {positive_events} 条，集中在 {', '.join(top_counter(category_counts)) or '若干维度'}。")
    if stakeholder_counts:
        strengths.append(f"相关方反馈覆盖 {sum(stakeholder_counts.values())} 条，类型为 {', '.join(top_counter(stakeholder_counts))}。")
    top_opportunities = sorted(member_signals.values(), key=lambda item: (-item.opportunity_score, item.member_id))[:3]
    if top_opportunities:
        names = "、".join(item.display_name for item in top_opportunities if item.opportunity_score > 0)
        if names:
            strengths.append(f"可考虑放大贡献或授权的成员：{names}。")

    risks: list[str] = []
    if overdue_tasks or high_tasks:
        risks.append(f"活跃待办 {len(active_tasks)} 项，其中高优先 {len(high_tasks)} 项、逾期 {len(overdue_tasks)} 项。")
    if concern_events or risky_feedback:
        risks.append(f"需关注成员信号 {concern_events} 条，相关方风险/投诉关联 {risky_feedback} 条。")
    if stale_members:
        risks.append(f"{len(stale_members)} 名成员在近 {window_days} 天缺少记录，团队判断可能存在证据盲区。")
    if not risks:
        risks.append("未发现明显集中风险，仍建议保持每周待办复盘和关键事件记录。")

    attention_members = sorted(
        member_signals.values(),
        key=lambda item: (-item.risk_score, item.event_count, item.member_id),
    )
    attention_members = [item for item in attention_members if item.risk_score or item.event_count == 0][:max_members]

    member_rows: list[dict[str, Any]] = []
    for item in sorted(member_signals.values(), key=lambda member: (-member.risk_score, -member.opportunity_score, member.member_id)):
        stale = item.event_count == 0
        next_action = next_action_for_member(item, stale)
        member_rows.append(
            {
                "id": item.member_id,
                "name": item.display_name,
                "role": " ".join(part for part in [item.role, item.level] if part),
                "team": item.team,
                "status": member_status(item, stale),
                "recent_events": item.event_count,
                "positive_events": item.positive_events,
                "concern_events": item.concern_events,
                "active_tasks": item.active_tasks,
                "latest": compact(" / ".join(part for part in [item.latest_date, item.latest_title] if part), 80),
                "source": item.latest_event_id or item.latest_source,
                "signals": item.distill_signals[:2],
                "next_action": next_action,
            }
        )

    next_7_days = action_list_7_days(overdue_tasks, high_tasks, waiting_tasks, attention_members, risks)
    next_30_days = action_list_30_days(stale_members, top_opportunities, category_counts)
    context_files = {
        "team_overview": read_signal_lines(data_dir / "team-memory-overview.md", 3),
        "upward_expectations": read_signal_lines(data_dir / "upward" / "expectations.md", 3),
        "company_strategy": read_signal_lines(data_dir / "company" / "strategy.md", 3),
    }
    evidence_events = latest_evidence_rows(recent_events, limit=8)

    return {
        "meta": {
            "title": "团队一图流",
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "as_of": as_of.isoformat(),
            "window_days": window_days,
            "window_start": start.isoformat(),
            "data_dir": str(data_dir),
        },
        "kpis": [
            {"label": "团队健康", "value": f"{health_score}/100", "hint": health_label(health_score)},
            {"label": "证据覆盖", "value": f"{coverage}%", "hint": f"{members_with_recent_events}/{total_members} 人有近况"},
            {"label": "控制压力", "value": str(control_pressure), "hint": f"高优先 {len(high_tasks)} / 逾期 {len(overdue_tasks)}"},
            {"label": "势能差", "value": str(momentum), "hint": f"正向 {positive_events} - 风险 {concern_events + risky_feedback}"},
        ],
        "summary": {
            "judgement": judgement,
            "strengths": strengths[:4],
            "risks": risks[:5],
            "attention_members": [item.display_name for item in attention_members[:5]],
        },
        "coverage": {
            "members": total_members,
            "recent_members": members_with_recent_events,
            "recent_events": len(recent_events),
            "member_events": sum(1 for event in recent_events if str(event.get("event_type", "")) == "member"),
            "stakeholder_feedback": sum(1 for event in recent_events if str(event.get("event_type", "")) == "stakeholder_feedback"),
            "active_tasks": len(active_tasks),
            "high_tasks": len(high_tasks),
            "overdue_tasks": len(overdue_tasks),
            "waiting_tasks": len(waiting_tasks),
            "silent_tasks": len(silent_tasks),
            "top_categories": top_counter(category_counts, 5),
            "top_ratings": top_counter(rating_counts, 5),
            "stakeholder_types": top_counter(stakeholder_counts, 5),
        },
        "members": member_rows,
        "actions": {
            "next_7_days": next_7_days,
            "next_30_days": next_30_days,
        },
        "context": context_files,
        "evidence": evidence_events,
        "fallback_note": "SVG、Markdown 和 JSON 均来自同一个数据包；如果不能生成图片，直接使用本 Markdown 结构输出。",
    }


def next_action_for_member(member: MemberSignal, stale: bool) -> str:
    if member.overdue_tasks:
        return "先关闭逾期事项，确认责任人和日期。"
    if member.risky_feedback:
        return "核实相关方风险，区分事实、反馈和结论。"
    if member.concern_events:
        return "安排一次短沟通，确认原因和下一步改善动作。"
    if member.high_tasks or member.waiting_tasks:
        return "推进高优先/等待反馈事项，避免沉默。"
    if member.active_tasks:
        return "检查活跃待办，确认交付标准和关闭时间。"
    if stale:
        return "补一次近况记录，避免管理判断失真。"
    if member.positive_events >= 2:
        return "考虑授权更高挑战或沉淀方法给团队复用。"
    return "保持观察，下一次记录补充成果和协作证据。"


def action_list_7_days(overdue_tasks: list[Any], high_tasks: list[Any], waiting_tasks: list[Any], attention: list[MemberSignal], risks: list[str]) -> list[str]:
    actions: list[str] = []
    if overdue_tasks:
        actions.append(f"逐条处理 {len(overdue_tasks)} 个逾期待办，写清继续、延期或关闭原因。")
    if high_tasks:
        actions.append(f"本周固定检查 {len(high_tasks)} 个高优先待办，避免只记录不闭环。")
    if waiting_tasks:
        actions.append(f"追问 {len(waiting_tasks)} 个 waiting 事项，补齐外部反馈或下一步动作。")
    for member in attention[:3]:
        actions.append(f"和 {member.display_name} 对齐当前状态：{next_action_for_member(member, member.event_count == 0)}")
    if not actions and risks:
        actions.append("保持每周复盘节奏，并把新的风险或认可及时写入时间轴。")
    return actions[:6]


def action_list_30_days(stale_members: list[MemberSignal], opportunities: list[MemberSignal], category_counts: Counter[str]) -> list[str]:
    actions: list[str] = []
    if stale_members:
        actions.append(f"为 {len(stale_members)} 名记录不足成员补齐近况、目标和风险判断。")
    names = "、".join(member.display_name for member in opportunities if member.opportunity_score > 0)
    if names:
        actions.append(f"围绕 {names} 设计授权、分享或项目节点，放大正向贡献。")
    top = category_counts.most_common(1)
    if top:
        actions.append(f"把高频维度「{top[0][0]}」沉淀成可复制标准或检查清单。")
    actions.append("月底复盘团队看板：证据覆盖、关键风险、相关方反馈和待办闭环率。")
    return actions[:5]


def latest_evidence_rows(events: list[dict[str, object]], limit: int = 8) -> list[dict[str, str]]:
    ordered = sorted(events, key=lambda event: (str(event.get("date", "")), str(event.get("event_id", ""))), reverse=True)
    rows: list[dict[str, str]] = []
    for event in ordered[:limit]:
        source = str(event.get("source_file", ""))
        line = str(event.get("source_line", ""))
        rows.append(
            {
                "date": str(event.get("date", "")),
                "id": str(event.get("event_id", "")),
                "object": str(event.get("member_name") or event.get("stakeholder_name") or ""),
                "summary": compact(str(event.get("summary") or event.get("title") or ""), 86),
                "source": f"{source}:{line}" if source and line else source,
            }
        )
    return rows


def health_label(score: int) -> str:
    if score >= 85:
        return "稳定进攻"
    if score >= 70:
        return "可控需跟进"
    if score >= 55:
        return "压力偏高"
    return "优先止血"


def render_markdown(packet: dict[str, Any]) -> str:
    meta = packet["meta"]
    lines = [
        f"# {meta['title']}（{meta['as_of']}）",
        "",
        f"> 窗口: {meta['window_start']} 至 {meta['as_of']}；生成时间: {meta['generated_at']}；文字版与 A4 图版共用同一数据包。",
        "",
        "## 1. 管理结论",
        "",
        f"- 当前判断: {packet['summary']['judgement']}",
    ]
    lines.extend(f"- 亮点/机会: {item}" for item in packet["summary"]["strengths"] or ["暂无明显正向集中信号。"])
    lines.extend(f"- 关键注意: {item}" for item in packet["summary"]["risks"])

    lines.extend(["", "## 2. 关键数据", "", "| 指标 | 数值 | 解读 |", "| --- | ---: | --- |"])
    for item in packet["kpis"]:
        lines.append(f"| {item['label']} | {item['value']} | {item['hint']} |")
    coverage = packet["coverage"]
    lines.extend(
        [
            f"| 近窗事件 | {coverage['recent_events']} | 成员事件 {coverage['member_events']} / 相关方反馈 {coverage['stakeholder_feedback']} |",
            f"| 活跃待办 | {coverage['active_tasks']} | 高优先 {coverage['high_tasks']} / 逾期 {coverage['overdue_tasks']} / 等待 {coverage['waiting_tasks']} / 沉默 {coverage['silent_tasks']} |",
        ]
    )

    lines.extend(
        [
            "",
            "## 3. 人员雷达",
            "",
            "| 成员 | 状态 | 近期信号 | 下步管理动作 | 证据 |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for member in packet["members"]:
        signal = f"事件 {member['recent_events']}，正向 {member['positive_events']}，关注 {member['concern_events']}，待办 {member['active_tasks']}"
        if member["signals"]:
            signal += "；" + "；".join(member["signals"])
        lines.append(
            f"| {member['name']} | {member['status']} | {signal} | {member['next_action']} | {member['source'] or member['latest'] or '无近期证据'} |"
        )

    lines.extend(["", "## 4. 7 天动作", ""])
    lines.extend(f"- {item}" for item in packet["actions"]["next_7_days"])
    lines.extend(["", "## 5. 30 天动作", ""])
    lines.extend(f"- {item}" for item in packet["actions"]["next_30_days"])

    context_rows = [
        ("团队概况", packet["context"]["team_overview"]),
        ("向上期望", packet["context"]["upward_expectations"]),
        ("公司战略", packet["context"]["company_strategy"]),
    ]
    if any(items for _, items in context_rows):
        lines.extend(["", "## 6. 背景摘录", ""])
        for title, items in context_rows:
            if items:
                lines.append(f"- {title}: {'；'.join(items)}")

    lines.extend(["", "## 7. 证据索引", ""])
    if packet["evidence"]:
        for item in packet["evidence"]:
            lines.append(f"- {item['date']} `{item['id']}` {item['object']} - {item['summary']}（{item['source']}）")
    else:
        lines.append("- 当前窗口内没有可引用事件。")
    lines.extend(["", f"> {packet['fallback_note']}"])
    return "\n".join(lines) + "\n"


def display_width(text: str) -> int:
    width = 0
    for char in text:
        width += 2 if "\u4e00" <= char <= "\u9fff" else 1
    return width


def wrap_text(text: str, max_units: int) -> list[str]:
    if not text:
        return []
    result: list[str] = []
    current = ""
    for char in text:
        if char in "\n\r":
            if current:
                result.append(current)
                current = ""
            continue
        next_text = current + char
        if current and display_width(next_text) > max_units:
            result.append(current)
            current = char
        else:
            current = next_text
    if current:
        result.append(current)
    return result


class Svg:
    def __init__(self, width: int = 1240, height: int = 1754) -> None:
        self.width = width
        self.height = height
        self.parts: list[str] = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
            "<defs>",
            "<style>",
            "text{font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',Arial,sans-serif;letter-spacing:0}",
            ".small{font-size:20px}.body{font-size:24px}.h2{font-size:30px;font-weight:700}.h1{font-size:44px;font-weight:800}",
            "</style>",
            "</defs>",
        ]

    def rect(self, x: int, y: int, w: int, h: int, fill: str, stroke: str = "none", radius: int = 8) -> None:
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>')

    def text(self, x: int, y: int, text: str, size: int = 24, fill: str = "#20242a", weight: int = 400) -> None:
        self.parts.append(
            f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}">{html.escape(text)}</text>'
        )

    def block(self, x: int, y: int, w: int, h: int, title: str, lines: list[str], accent: str = "#0f7a7a", max_lines: int = 9) -> None:
        self.rect(x, y, w, h, "#ffffff", "#dedbd2")
        self.rect(x, y, 8, h, accent, "none", 4)
        self.text(x + 24, y + 42, title, 28, "#20242a", 750)
        cursor = y + 78
        used = 0
        for raw in lines:
            bullet = "• "
            for idx, wrapped in enumerate(wrap_text(raw, max(18, (w - 62) // 13))):
                if used >= max_lines:
                    self.text(x + 24, cursor, "…", 22, "#6b675f", 400)
                    return
                prefix = bullet if idx == 0 else "  "
                self.text(x + 24, cursor, prefix + wrapped, 22, "#34373d", 400)
                cursor += 32
                used += 1

    def close(self) -> str:
        self.parts.append("</svg>")
        return "\n".join(self.parts) + "\n"


def render_svg(packet: dict[str, Any]) -> str:
    svg = Svg()
    meta = packet["meta"]
    svg.rect(0, 0, svg.width, svg.height, "#f6f3ec", "none", 0)
    svg.rect(44, 40, 1152, 112, "#20242a", "none", 8)
    svg.text(72, 94, "团队一图流", 44, "#ffffff", 800)
    svg.text(72, 130, f"{meta['window_start']} 至 {meta['as_of']}  ·  A4 管理看板", 22, "#d8d1c4", 500)
    svg.text(880, 94, meta["generated_at"], 22, "#d8d1c4", 500)
    svg.text(880, 130, "同构输出: SVG / Markdown / JSON", 20, "#d8d1c4", 400)

    card_x = [44, 338, 632, 926]
    accents = ["#0f7a7a", "#6f5f2e", "#b7791f", "#7a2e2e"]
    for idx, item in enumerate(packet["kpis"]):
        x = card_x[idx]
        svg.rect(x, 178, 270, 116, "#ffffff", "#dedbd2")
        svg.rect(x, 178, 270, 8, accents[idx], "none", 4)
        svg.text(x + 22, 222, item["label"], 22, "#6b675f", 650)
        svg.text(x + 22, 266, item["value"], 42, "#20242a", 800)
        svg.text(x + 132, 264, compact(item["hint"], 18), 16, "#6b675f", 400)

    summary = packet["summary"]
    svg.block(
        44,
        322,
        552,
        278,
        "管理结论",
        [summary["judgement"], *summary["strengths"][:3]],
        "#0f7a7a",
        7,
    )
    svg.block(44, 626, 552, 314, "关键注意点", summary["risks"], "#b42318", 8)
    svg.block(44, 966, 552, 286, "未来 7 天动作", packet["actions"]["next_7_days"], "#b7791f", 7)
    context_lines = []
    for title, key in [("团队概况", "team_overview"), ("向上期望", "upward_expectations"), ("公司战略", "company_strategy")]:
        values = packet["context"][key]
        if values:
            context_lines.append(f"{title}: {values[0]}")
    if not context_lines:
        context_lines = ["暂无团队概况、向上期望或公司战略摘录；建议补充以提升大局判断。"]
    svg.block(44, 1278, 552, 362, "背景与证据盲区", context_lines, "#6f5f2e", 8)

    svg.rect(624, 322, 572, 618, "#ffffff", "#dedbd2")
    svg.rect(624, 322, 8, 618, "#0f7a7a", "none", 4)
    svg.text(652, 364, "人员雷达", 28, "#20242a", 750)
    y = 404
    for member in packet["members"][:7]:
        status_color = "#26734d"
        if member["status"] in {"需管理介入", "证据不足"}:
            status_color = "#b42318" if member["status"] == "需管理介入" else "#b7791f"
        svg.rect(652, y, 516, 68, "#f8f7f3", "#ebe7dd", 6)
        svg.text(672, y + 28, member["name"], 22, "#20242a", 700)
        svg.text(672, y + 54, compact(member["role"] or member["team"] or member["id"], 26), 17, "#6b675f", 400)
        svg.text(840, y + 28, member["status"], 20, status_color, 700)
        metric = f"事{member['recent_events']} 正{member['positive_events']} 关{member['concern_events']} 待{member['active_tasks']}"
        svg.text(840, y + 54, metric, 17, "#6b675f", 400)
        action = svg_member_action(member)
        svg.text(1012, y + 42, action, 17, "#34373d", 400)
        y += 78
    if len(packet["members"]) > 7:
        svg.text(652, y + 20, f"另有 {len(packet['members']) - 7} 名成员详见 Markdown 版。", 18, "#6b675f", 400)

    coverage = packet["coverage"]
    data_lines = [
        f"成员 {coverage['recent_members']}/{coverage['members']} 有近窗证据，窗口事件 {coverage['recent_events']} 条。",
        f"待办: 活跃 {coverage['active_tasks']}，高优先 {coverage['high_tasks']}，逾期 {coverage['overdue_tasks']}，等待 {coverage['waiting_tasks']}。",
        f"高频类别: {', '.join(coverage['top_categories']) or '暂无'}。",
        f"相关方类型: {', '.join(coverage['stakeholder_types']) or '暂无'}。",
    ]
    svg.block(624, 966, 572, 286, "数据控制台", data_lines, "#6f5f2e", 7)

    evidence_lines = [
        f"{item['date']} {item['id']} {item['object']} - {item['summary']}"
        for item in packet["evidence"][:6]
    ] or ["当前窗口内没有可引用事件。"]
    svg.block(624, 1278, 572, 362, "证据索引", evidence_lines, "#20242a", 8)
    svg.text(44, 1706, "提示: 图版用于快速判断，绩效/晋升/处罚必须回到事件日期、事件 ID、证据等级和原文。", 20, "#6b675f", 500)
    return svg.close()


def svg_member_action(member: dict[str, Any]) -> str:
    text = str(member.get("next_action", ""))
    if "逾期" in text:
        return "关逾期"
    if "相关方" in text or "核实" in text:
        return "核风险"
    if "沟通" in text:
        return "短沟通"
    if "高优先" in text or "等待" in text:
        return "推待办"
    if "活跃待办" in text or "关闭时间" in text:
        return "推待办"
    if "近况" in text:
        return "补近况"
    if "授权" in text or "沉淀" in text:
        return "授权/沉淀"
    return "观察"


def write_outputs(packet: dict[str, Any], output_dir: Path, fmt: str) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    stamp = packet["meta"]["as_of"].replace("-", "")
    paths: list[Path] = []
    if fmt in {"markdown", "all"}:
        path = output_dir / f"team-dashboard-{stamp}.md"
        path.write_text(render_markdown(packet), encoding="utf-8")
        paths.append(path)
    if fmt in {"svg", "all"}:
        path = output_dir / f"team-dashboard-{stamp}.svg"
        path.write_text(render_svg(packet), encoding="utf-8")
        paths.append(path)
    if fmt in {"json", "all"}:
        path = output_dir / f"team-dashboard-{stamp}.json"
        path.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        paths.append(path)
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate an A4 Team Memory dashboard and matching text fallback.")
    parser.add_argument("--skill-dir", default=None, help="team-memory skill directory")
    parser.add_argument("--as-of", default=None, help="dashboard date, YYYY-MM-DD; defaults to today")
    parser.add_argument("--days", type=int, default=90, help="lookback window in days")
    parser.add_argument("--max-members", type=int, default=12, help="maximum member rows for the dashboard packet")
    parser.add_argument("--format", choices=["markdown", "svg", "json", "all"], default="all")
    parser.add_argument("--output-dir", default=None, help="defaults to data/insights")
    args = parser.parse_args()

    if args.days < 7:
        print("ERROR: --days 至少为 7，避免一图流被偶然事件带偏。")
        return 1
    as_of = parse_date(args.as_of or "") or date.today()
    try:
        paths = resolve_paths(args.skill_dir, require_lock=True)
    except TeamMemoryPathError as exc:
        print(f"ERROR: {exc}")
        return 1

    print_warnings(paths.warnings)
    output_dir = Path(args.output_dir).expanduser().resolve() if args.output_dir else paths.data_dir / "insights"
    packet = build_packet(paths.data_dir, paths.config_path, as_of, args.days, args.max_members)
    outputs = write_outputs(packet, output_dir, args.format)
    for path in outputs:
        print(f"已生成: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
