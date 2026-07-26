#!/usr/bin/env python3
"""Adaptive game-window runner for World Cup Player Goal Value.

Hermes cron invokes this every 5 minutes. It is silent outside live/pregame
World Cup windows. During game windows it refreshes WC player stats and runs the
skill in dry-run/paper-preview mode unless a future persisted non-SIM paper venue
is explicitly added.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
SCOREBOARD_URL = "https://site.api.espn.com/apis/site/v2/sports/soccer/fifa.world/scoreboard"
GAMMA_EVENTS_URL = "https://gamma-api.polymarket.com/events/keyset"
PREP_WINDOW_SECONDS = 30 * 60
LIVE_STATES = {"in"}
PREP_STATES = {"pre"}


@dataclass
class GameContext:
    mode: str
    name: str
    start_ts: float | None
    detail: str
    score: str


def parse_iso(raw: str | None) -> float | None:
    if not raw:
        return None
    try:
        if raw.endswith("Z"):
            raw = raw[:-1] + "+00:00"
        return datetime.fromisoformat(raw).timestamp()
    except Exception:
        return None


def fetch_scoreboard() -> list[dict[str, Any]]:
    req = urllib.request.Request(SCOREBOARD_URL, headers={"User-Agent": "Hermes/WCPlayerGoalValue"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        return (json.loads(resp.read().decode("utf-8")).get("events") or [])


def score_line(event: dict[str, Any]) -> str:
    comps = ((event.get("competitions") or [{}])[0].get("competitors") or [])
    parts = []
    for comp in comps:
        team = comp.get("team") or {}
        short = team.get("shortDisplayName") or team.get("displayName") or team.get("name") or "Team"
        score = comp.get("score")
        parts.append(f"{short} {score if score is not None else '0'}")
    return " - ".join(parts)


def active_game_contexts(now_ts: float | None = None) -> list[GameContext]:
    now_ts = now_ts or datetime.now(timezone.utc).timestamp()
    contexts: list[GameContext] = []
    for event in fetch_scoreboard():
        status = ((event.get("status") or {}).get("type") or {})
        state = (status.get("state") or "").lower()
        detail = status.get("detail") or status.get("shortDetail") or ""
        start_ts = parse_iso(event.get("date"))
        name = event.get("name") or event.get("shortName") or "World Cup match"
        score = score_line(event)
        if state in LIVE_STATES:
            contexts.append(GameContext("live", name, start_ts, detail, score))
        elif state in PREP_STATES and start_ts is not None and 0 <= start_ts - now_ts <= PREP_WINDOW_SECONDS:
            start = datetime.fromtimestamp(start_ts, timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
            contexts.append(GameContext("prep", name, start_ts, f"starts {start}", score))
    contexts.sort(key=lambda g: (0 if g.mode == "live" else 1, g.start_ts or 0))
    return contexts


def normalize_title(text: str) -> str:
    return " ".join((text or "").replace("–", "-").split()).lower()


def active_polymarket_event_slugs(contexts: list[GameContext], max_pages: int = 3) -> list[str]:
    wanted = {normalize_title(ctx.name) for ctx in contexts if ctx.name}
    if not wanted:
        return []
    slugs: list[str] = []
    cursor = None
    for _ in range(max_pages):
        params = {
            "tag_id": "102232",
            "related_tags": "true",
            "closed": "false",
            "limit": "100",
            "include_best_lines": "true",
        }
        if cursor:
            params["after_cursor"] = cursor
        query = urllib.parse.urlencode(params)
        req = urllib.request.Request(f"{GAMMA_EVENTS_URL}?{query}", headers={"User-Agent": "Hermes/WCPlayerGoalValue"})
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except Exception:
            break
        for event in data.get("events") or []:
            title = normalize_title(str(event.get("title") or ""))
            slug = str(event.get("slug") or "").strip()
            if slug and title in wanted:
                slugs.append(slug)
        cursor = data.get("next_cursor")
        if not cursor:
            break
    return list(dict.fromkeys(slugs))


def filtered(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if line.startswith("venue='sim' — PAPER trading with virtual $SIM"):
            continue
        if line.startswith("venue='polymarket' — LIVE trading with real funds."):
            # The SDK banner is venue-based and misleading here: this runner
            # deliberately omits --live, so the child strategy is a dry-run.
            continue
        if line.startswith("$SIM paper mode active"):
            continue
        lines.append(line)
    return "\n".join(lines) + ("\n" if lines else "")


def player_data_is_fresh(env: dict[str, str], max_age_minutes: float) -> bool:
    raw_path = env.get("SIMMER_WCPGV_PLAYER_DATA_FILE") or "data/wc_players_filtered.csv"
    data_path = Path(raw_path)
    if not data_path.is_absolute():
        data_path = ROOT / data_path
    if not data_path.exists():
        return False
    age_seconds = datetime.now(timezone.utc).timestamp() - data_path.stat().st_mtime
    return age_seconds <= max_age_minutes * 60


def should_refresh_player_data(args: argparse.Namespace, env: dict[str, str]) -> bool:
    if args.skip_refresh:
        return False
    try:
        max_age_minutes = float(env.get("SIMMER_WCPGV_REFRESH_MAX_AGE_MIN", "360"))
    except ValueError:
        max_age_minutes = 360.0
    if max_age_minutes <= 0:
        return True
    return not player_data_is_fresh(env, max_age_minutes)


def run_strategy(args: argparse.Namespace, contexts: list[GameContext]) -> int:
    print("World Cup player-goal game window active:")
    for ctx in contexts:
        label = "LIVE" if ctx.mode == "live" else "PREP"
        print(f"- {label}: {ctx.name} — {ctx.detail} — score {ctx.score}")
    print()

    env = os.environ.copy()
    env["TRADING_VENUE"] = args.venue
    env.setdefault("SIMMER_WCPGV_PLAYER_DATA_FILE", "data/wc_players_filtered.csv")
    env.setdefault("SIMMER_WCPGV_MIN_PLAYER_MINUTES", "300")
    env.setdefault("SIMMER_WCPGV_MAX_POSITION", "12")
    env.setdefault("SIMMER_WCPGV_DAILY_BUDGET", "40")
    env.setdefault("SIMMER_WCPGV_MAX_TRADES", "3")
    active_slugs = active_polymarket_event_slugs(contexts)
    if active_slugs:
        env["SIMMER_WCPGV_COMBO_EVENT_SLUGS"] = ",".join(active_slugs)
        print(f"Polymarket event filter: {env['SIMMER_WCPGV_COMBO_EVENT_SLUGS']}")

    if should_refresh_player_data(args, env):
        refresh = subprocess.run([sys.executable, str(ROOT / "scripts" / "fetch_wc_stats.py")], cwd=str(ROOT), env=env, text=True, capture_output=True)
        if refresh.returncode != 0:
            if refresh.stdout:
                print(refresh.stdout, end="")
            if refresh.stderr:
                print(refresh.stderr, end="", file=sys.stderr)
            return refresh.returncode

    cmd = [sys.executable, str(ROOT / "player_goal_value.py"), "--venue", args.venue, "--quiet"]
    proc = subprocess.run(cmd, cwd=str(ROOT), env=env, text=True, capture_output=True)
    out = filtered(proc.stdout)
    err = filtered(proc.stderr)
    if out:
        print(out, end="")
    if err:
        print(err, end="", file=sys.stderr)
    return proc.returncode


def main() -> int:
    ap = argparse.ArgumentParser(description="Run Player Goal Value only during World Cup game windows")
    ap.add_argument("--venue", default=os.getenv("TRADING_VENUE", "sim"))
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--skip-refresh", action="store_true")
    args = ap.parse_args()

    try:
        contexts = active_game_contexts()
    except Exception as exc:
        if args.status:
            print(f"scoreboard unavailable: {type(exc).__name__}: {exc}")
        return 0

    if args.status:
        if not contexts:
            print("No active World Cup prep/live game window. Player Goal Value would stay silent.")
        else:
            print(f"{len(contexts)} active game window(s):")
            for ctx in contexts:
                print(f"- {ctx.mode}: {ctx.name} — {ctx.detail} — score {ctx.score}")
        return 0

    if not contexts and not args.force:
        return 0
    if not contexts and args.force:
        contexts = [GameContext("force", "forced run", None, "manual force", "n/a")]
    return run_strategy(args, contexts)


if __name__ == "__main__":
    raise SystemExit(main())
