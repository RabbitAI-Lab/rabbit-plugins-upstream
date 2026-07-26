"""Session state — persistent memory across CLI invocations.

Reads/writes data/state.json, tracking:
  - last command results (backtest ROI, fit params, fetch counts)
  - best-performing filter configurations
  - data source health status
  - pending tasks / unresolved issues
  - free-text notes

Every key command auto-updates the state so the next session can pick up
where the last one left off.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_STATE_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "state.json"

DEFAULTS: dict[str, Any] = {
    "version": 1,
    "created": "",
    "last_updated": "",
    "backtest": {},
    "best_filters": {
        "steady": {"min_prob": 0.55, "min_edge": 0.03, "min_score": 55},
        "bold": {"min_prob": 0.50, "min_edge": 0.05, "min_score": 45},
    },
    "model": {},
    "data_sources": {},
    "live_sessions": [],
    "pending": [
        "中英队名映射（澳客中文→模型英文）",
        "德甲/法甲 澳客联赛ID校准",
        "500.com / 竞彩网 / 懂球帝 适配器"
    ],
    "notes": "",
    "ledger_summary": {},
}


def _load() -> dict:
    try:
        with open(_STATE_PATH, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def _save(data: dict) -> None:
    _STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    data["last_updated"] = now
    if not data.get("created"):
        data["created"] = now
    with open(_STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)


def get_state() -> dict:
    """Return current state, merging with defaults for any missing keys."""
    data = _load()
    for key, default in DEFAULTS.items():
        if key not in data:
            data[key] = default
    return data


# ---- update helpers ----

def log_backtest(league: str, model: str, n_bets: int, hit_rate: float,
                 roi: float, rps_model: float, rps_market: float, rps_naive: float) -> None:
    data = get_state()
    entry = {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
        "league": league, "model": model,
        "n_bets": n_bets, "hit_rate": round(hit_rate, 4),
        "roi": round(roi, 4), "rps_model": round(rps_model, 4),
        "rps_market": round(rps_market, 4), "rps_naive": round(rps_naive, 4),
    }
    history = data.setdefault("backtest_history", [])
    history.append(entry)
    data["backtest"] = entry  # latest only
    # Keep last 20
    if len(history) > 20:
        data["backtest_history"] = history[-20:]
    _save(data)


def log_fit(model: str, league: str, n_matches: int, home_adv: float,
            intercept: float, rho: float, half_life: float = 0) -> None:
    data = get_state()
    data["model"] = {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
        "model": model, "league": league, "n_matches": n_matches,
        "home_adv": round(home_adv, 4), "intercept": round(intercept, 4),
        "rho": round(rho, 4), "half_life_days": half_life,
    }
    _save(data)


def log_fetch(source: str, league: str, n_matches: int) -> None:
    data = get_state()
    data["data_sources"][source] = {
        "last_fetch": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
        "league": league, "matches": n_matches,
    }
    # Remove pending item for this league if present
    pending = data.get("pending", [])
    league_names = {"E0": "英超", "SP1": "西甲", "I1": "意甲", "D1": "德甲", "F1": "法甲"}
    lname = league_names.get(league, league)
    match_str = f"{lname}"
    data["pending"] = [t for t in pending if match_str not in t]
    _save(data)


def log_live(source: str, matches: int) -> None:
    data = get_state()
    sessions = data.setdefault("live_sessions", [])
    sessions.append({
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
        "source": source, "matches": matches,
    })
    if len(sessions) > 50:
        data["live_sessions"] = sessions[-50:]
    _save(data)


def log_value(mode: str, n_picks: int, hit_rate: float, avg_prob: float) -> None:
    data = get_state()
    key = f"value_{mode}_latest"
    data[key] = {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
        "n_picks": n_picks, "hit_rate": round(hit_rate, 4),
        "avg_prob": round(avg_prob, 4),
    }
    _save(data)


def update_notes(text: str) -> None:
    data = get_state()
    data["notes"] = text
    _save(data)


def set_pending(tasks: list[str]) -> None:
    data = get_state()
    data["pending"] = tasks
    _save(data)
