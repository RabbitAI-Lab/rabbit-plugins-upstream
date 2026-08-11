#!/usr/bin/env python3
"""
Agent Cognitive States — Self-Check Script

Analyzes conversation/session state and reports cognitive load.
Designed to be called by the agent or by a guardian cron job.

Usage:
    python3 self_check.py --context-tokens 94000 --window 128000
    python3 self_check.py --session-dir /path/to/session
    python3 self_check.py --interactive

Output: JSON report of cognitive states + severity levels.
"""

import argparse
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


# ─── Data Models ──────────────────────────────────────────────────────────────

@dataclass
class CognitiveState:
    name: str
    score: int
    severity: str  # none, low, medium, high
    signal: str
    impact: str = ""
    action: str = ""


@dataclass
class CognitiveReport:
    timestamp: str
    states: list[CognitiveState] = field(default_factory=list)
    cli: int = 0  # Cognitive Load Index (0-100)
    status: str = "🟢 Healthy"
    
    def add(self, state: CognitiveState):
        self.states.append(state)
    
    def compute_cli(self):
        if not self.states:
            self.cli = 0
            self.status = "🟢 Healthy"
            return
        self.cli = sum(s.score for s in self.states) // len(self.states)
        if self.cli < 30:
            self.status = "🟢 Healthy"
        elif self.cli < 50:
            self.status = "🟡 Degraded"
        elif self.cli < 70:
            self.status = "🟠 Strained"
        else:
            self.status = "🔴 Critical"
    
    def active_states(self) -> list[CognitiveState]:
        return [s for s in self.states if s.severity in ("medium", "high")]
    
    def to_dict(self) -> dict:
        return {
            "timestamp": self.timestamp,
            "status": self.status,
            "cli": self.cli,
            "states": [asdict(s) for s in self.states],
            "active_issues": [s.name for s in self.active_states()],
        }


# ─── Severity Helper ──────────────────────────────────────────────────────────

def severity_from_score(score: int) -> str:
    if score < 30: return "none"
    if score < 60: return "low"
    if score < 80: return "medium"
    return "high"


# ─── State Detectors ──────────────────────────────────────────────────────────

def check_fatigue(context_tokens: int, window_size: int) -> CognitiveState:
    """Context Fatigue — context window filling up."""
    utilization = context_tokens / window_size if window_size > 0 else 0
    score = int(utilization * 100)
    
    signal = f"{context_tokens:,}/{window_size:,} tokens ({utilization:.0%})"
    impact = "Early conversation details may be truncated; risk of forgetting original requirements"
    action = "Persist critical facts to memory; suggest session split for remaining work"
    
    return CognitiveState(
        name="Context Fatigue",
        score=score,
        severity=severity_from_score(score),
        signal=signal,
        impact=impact,
        action=action,
    )


def check_drift(turns_since_user: int, goal_keywords: list[str] = None) -> CognitiveState:
    """Attention Drift — wandered from original task."""
    score = min(turns_since_user * 7, 70)
    signal = f"{turns_since_user} agent turns since last user message"
    impact = "May be doing work the user didn't ask for"
    action = "Re-anchor to original goal; pause for user confirmation if >15 turns"
    
    return CognitiveState(
        name="Attention Drift",
        score=score,
        severity=severity_from_score(score),
        signal=signal,
        impact=impact,
        action=action,
    )


def check_memory_debt(unsaved_facts: int, last_save_turns_ago: int) -> CognitiveState:
    """Memory Debt — important facts not persisted."""
    score = min(unsaved_facts * 20, 100)
    if last_save_turns_ago > 5:
        score += 10
    
    signal = f"{unsaved_facts} unsaved critical facts (last save {last_save_turns_ago} turns ago)"
    impact = "Important preferences/decisions will be lost when session ends"
    action = "Batch-write all unsaved facts to memory now"
    
    return CognitiveState(
        name="Memory Debt",
        score=score,
        severity=severity_from_score(score),
        signal=signal,
        impact=impact,
        action=action,
    )


def check_confidence_errosion(consecutive_failures: int, same_tool: bool = False) -> CognitiveState:
    """Confidence Erosion — repeated failures degrading output."""
    score = min(consecutive_failures * 22, 100)
    if same_tool:
        score += 10
    
    signal = f"{consecutive_failures} consecutive failed tool calls" + (" (same tool type)" if same_tool else "")
    impact = "Output quality degrading; risk of infinite retry loops"
    action = "Try fundamentally different approach; if that fails, report blocker honestly"
    
    return CognitiveState(
        name="Confidence Erosion",
        score=score,
        severity=severity_from_score(score),
        signal=signal,
        impact=impact,
        action=action,
    )


def check_fragmentation(active_topics: int, interleaved: bool = False) -> CognitiveState:
    """Context Fragmentation — too many topics in one session."""
    score = min(active_topics * 18, 100)
    if interleaved:
        score += 10
    
    signal = f"{active_topics} active topics" + (" (interleaved)" if interleaved else "")
    impact = "Cross-topic noise degrades reasoning on each individual task"
    action = "Use delegate_task for isolation; suggest /new for next topic"
    
    return CognitiveState(
        name="Context Fragmentation",
        score=score,
        severity=severity_from_score(score),
        signal=signal,
        impact=impact,
        action=action,
    )


def check_skill_staleness(
    skill_command_failed: bool = False,
    skill_path_missing: bool = False,
    skill_age_days: int = 0,
) -> CognitiveState:
    """Skill Staleness — loaded skill is outdated."""
    score = 0
    signal_parts = []
    
    if skill_command_failed:
        score += 60
        signal_parts.append("primary command failed")
    if skill_path_missing:
        score += 70
        signal_parts.append("file path doesn't exist")
    if skill_age_days > 90:
        score += 15
        signal_parts.append(f"skill is {skill_age_days} days old")
    
    if not signal_parts:
        signal_parts.append("no issues detected")
    
    signal = "; ".join(signal_parts)
    impact = "Following outdated instructions produces errors and wasted effort"
    action = "Patch skill with corrected commands/paths before continuing"
    
    return CognitiveState(
        name="Skill Staleness",
        score=score,
        severity=severity_from_score(score),
        signal=signal,
        impact=impact,
        action=action,
    )


# ─── Report Formatting ────────────────────────────────────────────────────────

def format_report_human(report: CognitiveReport) -> str:
    """Format report as human-readable text."""
    lines = [
        f"\n🧠 Cognitive State Report — {report.timestamp}",
        f"   Overall: {report.status} (CLI: {report.cli}/100)",
        "",
    ]
    
    active = report.active_states()
    if not active:
        lines.append("   All systems nominal. No cognitive states requiring attention.")
        return "\n".join(lines)
    
    lines.append(f"   ⚠️  {len(active)} active state(s) requiring attention:\n")
    
    for state in report.states:
        if state.severity == "none":
            continue
        
        icon = {
            "Context Fatigue": "🥱",
            "Attention Drift": "🧠",
            "Memory Debt": "📝",
            "Confidence Erosion": "😤",
            "Context Fragmentation": "🧩",
            "Skill Staleness": "🔧",
        }.get(state.name, "⚠️")
        
        sev_icon = {"low": "🟡", "medium": "🟠", "high": "🔴"}.get(state.severity, "⚪")
        
        lines.append(f"   {icon} {state.name} [{sev_icon} {state.severity}, score {state.score}]")
        lines.append(f"      ├─ Signal: {state.signal}")
        if state.severity in ("medium", "high"):
            lines.append(f"      ├─ Impact: {state.impact}")
            lines.append(f"      └─ Action: {state.action}")
        else:
            lines.append(f"      └─ (monitoring)")
        lines.append("")
    
    return "\n".join(lines)


def format_report_markdown(report: CognitiveReport) -> str:
    """Format report as markdown."""
    lines = [
        f"## 🧠 Cognitive State Report",
        f"**{report.timestamp}** | Overall: **{report.status}** (CLI: {report.cli}/100)",
        "",
    ]
    
    active = report.active_states()
    if not active:
        lines.append("All systems nominal. ✅")
        return "\n".join(lines)
    
    lines.append("| State | Severity | Score | Signal |")
    lines.append("|-------|----------|-------|--------|")
    
    for s in report.states:
        if s.severity == "none":
            continue
        lines.append(f"| {s.name} | {s.severity} | {s.score} | {s.signal} |")
    
    lines.append("")
    lines.append("### Recommended Actions")
    for s in active:
        lines.append(f"- **{s.name}**: {s.action}")
    
    return "\n".join(lines)


# ─── Main ─────────────────────────────────────────────────────────────────────

def run_full_check(
    context_tokens: int = 0,
    window_size: int = 128000,
    turns_since_user: int = 0,
    unsaved_facts: int = 0,
    last_save_turns_ago: int = 0,
    consecutive_failures: int = 0,
    same_tool_failures: bool = False,
    active_topics: int = 1,
    interleaved: bool = False,
    skill_command_failed: bool = False,
    skill_path_missing: bool = False,
    skill_age_days: int = 0,
) -> CognitiveReport:
    """Run all cognitive state checks and return composite report."""
    report = CognitiveReport(timestamp=datetime.now(timezone.utc).isoformat())
    
    report.add(check_fatigue(context_tokens, window_size))
    report.add(check_drift(turns_since_user))
    report.add(check_memory_debt(unsaved_facts, last_save_turns_ago))
    report.add(check_confidence_errosion(consecutive_failures, same_tool_failures))
    report.add(check_fragmentation(active_topics, interleaved))
    report.add(check_skill_staleness(skill_command_failed, skill_path_missing, skill_age_days))
    
    report.compute_cli()
    return report


def main():
    parser = argparse.ArgumentParser(description="Agent Cognitive States Self-Check")
    parser.add_argument("--context-tokens", type=int, default=0, help="Estimated tokens used")
    parser.add_argument("--window", type=int, default=128000, help="Context window size")
    parser.add_argument("--turns-since-user", type=int, default=0, help="Agent turns since last user msg")
    parser.add_argument("--unsaved-facts", type=int, default=0, help="Critical facts not in memory")
    parser.add_argument("--last-save", type=int, default=0, help="Turns since last memory save")
    parser.add_argument("--failures", type=int, default=0, help="Consecutive failed tool calls")
    parser.add_argument("--same-tool", action="store_true", help="Failures are same tool type")
    parser.add_argument("--topics", type=int, default=1, help="Active topics in session")
    parser.add_argument("--interleaved", action="store_true", help="Topics are interleaved")
    parser.add_argument("--skill-failed", action="store_true", help="Skill command failed")
    parser.add_argument("--skill-path-missing", action="store_true", help="Skill path missing")
    parser.add_argument("--skill-age", type=int, default=0, help="Skill age in days")
    parser.add_argument("--format", choices=["human", "markdown", "json"], default="human")
    parser.add_argument("--interactive", action="store_true", help="Interactive mode: prompt for inputs")
    args = parser.parse_args()
    
    if args.interactive:
        def ask(prompt, default=0):
            try:
                return int(input(f"{prompt} [{default}]: ") or default)
            except (ValueError, EOFError):
                return default
        
        def ask_bool(prompt, default=False):
            try:
                return (input(f"{prompt} [{'y/N' if not default else 'Y/n'}]: ") or ('n' if not default else 'y')).lower().startswith('y')
            except EOFError:
                return default
        
        args.context_tokens = ask("Estimated tokens used", 0)
        args.window = ask("Context window size", 128000)
        args.turns_since_user = ask("Agent turns since last user message", 0)
        args.unsaved_facts = ask("Unsaved critical facts", 0)
        args.last_save = ask("Turns since last memory save", 0)
        args.failures = ask("Consecutive failed tool calls", 0)
        args.topics = ask("Active topics in session", 1)
        args.skill_age = ask("Skill age (days)", 0)
        args.same_tool = ask_bool("Same tool repeated?")
        args.interleaved = ask_bool("Topics interleaved?")
        args.skill_failed = ask_bool("Skill command failed?")
        args.skill_path_missing = ask_bool("Skill path missing?")
    
    report = run_full_check(
        context_tokens=args.context_tokens,
        window_size=args.window,
        turns_since_user=args.turns_since_user,
        unsaved_facts=args.unsaved_facts,
        last_save_turns_ago=args.last_save,
        consecutive_failures=args.failures,
        same_tool_failures=args.same_tool,
        active_topics=args.topics,
        interleaved=args.interleaved,
        skill_command_failed=args.skill_failed,
        skill_path_missing=args.skill_path_missing,
        skill_age_days=args.skill_age,
    )
    
    if args.format == "json":
        print(json.dumps(report.to_dict(), indent=2))
    elif args.format == "markdown":
        print(format_report_markdown(report))
    else:
        print(format_report_human(report))
    
    # Exit code: non-zero if any high-severity state
    if any(s.severity == "high" for s in report.states):
        sys.exit(2)
    elif any(s.severity == "medium" for s in report.states):
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
