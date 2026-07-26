"""二级联赛亚盘训练日志 — 记录每场AH信号 vs 实际结果，积累安全水位知识。

Usage:
  from footy.analysis.ah_journal import log_match, show_stats
  log_match(league, home, away, ah_open, ah_close, water_open, water_close, signal, result)
  show_stats()
"""
from __future__ import annotations

import csv
import os
from dataclasses import dataclass
from datetime import date
from pathlib import Path

JOURNAL_PATH = Path(__file__).resolve().parent.parent.parent.parent / "data" / "ah_journal.csv"
HEADER = ["date","league","home","away","stars","signal_type","ah_open","ah_close","water_open","water_close","result","notes"]


@dataclass
class AHRecord:
    date: str
    league: str
    home: str
    away: str
    stars: int
    signal_type: str  # "全票反转" "升盘涌入" "全线降水" "降盘冷却" "混杂"
    ah_open: float
    ah_close: float
    water_open: float
    water_close: float
    result: str = ""   # "" = pending, "win", "loss", "push"
    notes: str = ""


def log_match(league: str, home: str, away: str, stars: int,
              signal_type: str, ah_open: float, ah_close: float,
              water_open: float, water_close: float,
              result: str = "", notes: str = "") -> None:
    """Record a match analysis to the AH journal."""
    exists = JOURNAL_PATH.exists()
    with open(JOURNAL_PATH, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if not exists:
            w.writerow(HEADER)
        w.writerow([date.today().isoformat(), league, home, away, stars,
                     signal_type, f"{ah_open:.2f}", f"{ah_close:.2f}",
                     f"{water_open:.2f}", f"{water_close:.2f}", result, notes])


def load_journal() -> list[dict]:
    """Load all AH journal entries."""
    if not JOURNAL_PATH.exists():
        return []
    with open(JOURNAL_PATH, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def settle(league: str, home: str, away: str, result: str) -> None:
    """Update result for a match."""
    if not JOURNAL_PATH.exists():
        return
    rows = []
    with open(JOURNAL_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["league"] == league and row["home"] == home and row["away"] == away:
                row["result"] = result
            rows.append(row)
    with open(JOURNAL_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HEADER)
        w.writeheader()
        w.writerows(rows)


def show_stats() -> str:
    """Print AH journal statistics."""
    all = load_journal()
    if not all:
        return "No records yet."

    settled = [r for r in all if r["result"] in ("win", "loss", "push")]
    by_stars = {}
    for r in settled:
        stars = int(r["stars"])
        by_stars.setdefault(stars, {"total": 0, "wins": 0})
        by_stars[stars]["total"] += 1
        if r["result"] == "win":
            by_stars[stars]["wins"] += 1

    by_signal = {}
    for r in settled:
        sig = r["signal_type"]
        by_signal.setdefault(sig, {"total": 0, "wins": 0})
        by_signal[sig]["total"] += 1
        if r["result"] == "win":
            by_signal[sig]["wins"] += 1

    lines = [f"AH Journal: {len(all)} records, {len(settled)} settled\n"]
    lines.append("By Stars:")
    for s in sorted(by_stars.keys(), reverse=True):
        d = by_stars[s]
        rate = d["wins"] / d["total"] * 100 if d["total"] else 0
        stars_str = "⭐" * s
        lines.append(f"  {stars_str:<10} {d['wins']}/{d['total']} ({rate:.0f}%)")

    lines.append("\nBy Signal Type:")
    for sig, d in sorted(by_signal.items(), key=lambda x: -x[1]["wins"]/max(x[1]["total"],1)):
        rate = d["wins"] / d["total"] * 100 if d["total"] else 0
        lines.append(f"  {sig:<12} {d['wins']}/{d['total']} ({rate:.0f}%)")

    return "\n".join(lines)
