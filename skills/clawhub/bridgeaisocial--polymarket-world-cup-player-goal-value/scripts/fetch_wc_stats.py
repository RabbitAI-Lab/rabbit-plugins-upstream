#!/usr/bin/env python3
"""
fetch_wc_stats.py — refresh WC tournament stats and rebuild filtered player CSV.

Run before each skill execution to keep player data current:
    python scripts/fetch_wc_stats.py
    python player_goal_value.py --venue sim

Sources:
    - Understat base stats:  data/understat_players_recent_top5.csv
    - WC match stats:        ESPN API (all completed WC matches)
    - Custom players:        data/custom_players.json  (non-Understat stars)

Output:
    data/wc_players_filtered.csv  (drop-in for player_data_file config)
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
import time
import unicodedata
from pathlib import Path
from typing import Dict, Optional

BASE = Path(__file__).parent.parent  # skill root
UNDERSTAT_CSV = BASE / "data" / "understat_players_recent_top5.csv"
CUSTOM_JSON = BASE / "data" / "custom_players.json"
OUTPUT_CSV = BASE / "data" / "wc_players_filtered.csv"
MATCH_CACHE = BASE / "data" / ".wc_match_cache.json"

ESPN_SCOREBOARD = (
    "https://site.api.espn.com/apis/site/v2/sports/soccer/fifa.world/"
    "scoreboard?dates=20260611-20261231&limit=200"
)
ESPN_SUMMARY = (
    "https://site.api.espn.com/apis/site/v2/sports/soccer/fifa.world/summary?event={}"
)

# WC squad / role filters
MIN_CLUB_MINUTES = 300
FW_MIN_G90 = 0.20
MF_MIN_G90 = 0.35
STARTER_AVG_MINS = 45
STARTER_MIN_GAMES = 15
SUB_AVG_MINS = 20
SUB_MIN_GAMES = 18

# WC minute estimates (ESPN doesn't expose per-player WC minutes)
WC_STARTER_MINS = 78
WC_SUB_MINS = 28

UNDERSTAT_POSITIONS = {"FW": "F", "MF": "M", "DF": "D", "GK": "G"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _norm(name: str) -> str:
    s = unicodedata.normalize("NFKD", name)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    return " ".join(s.split())


def _token_match(a: str, b: str) -> bool:
    na, nb = _norm(a), _norm(b)
    if na == nb:
        return True
    ta, tb = set(na.split()), set(nb.split())
    # All tokens of the shorter name appear in the longer
    shorter = ta if len(ta) <= len(tb) else tb
    longer = tb if len(ta) <= len(tb) else ta
    return shorter and shorter.issubset(longer)


def _fetch(url: str) -> Optional[dict]:
    result = subprocess.run(
        ["curl", "-s", "--max-time", "12", url],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return None
    try:
        return json.loads(result.stdout)
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Step 1 — fetch WC match IDs (with caching of already-processed matches)
# ---------------------------------------------------------------------------

def fetch_completed_match_ids() -> list[str]:
    data = _fetch(ESPN_SCOREBOARD)
    if not data:
        print("  ERROR: could not reach ESPN scoreboard", file=sys.stderr)
        return []
    return [
        e["id"] for e in data.get("events", [])
        if e.get("status", {}).get("type", {}).get("description") == "Full Time"
    ]


# ---------------------------------------------------------------------------
# Step 2 — aggregate per-player WC stats across all completed matches
# ---------------------------------------------------------------------------

def _stat(stats: list, key: str) -> float:
    for s in stats:
        if s.get("name") == key:
            return float(s.get("value", 0))
    return 0.0


def fetch_wc_player_stats(match_ids: list[str]) -> Dict[str, dict]:
    # Load cache
    cache: dict = {}
    cached_ids: set = set()
    if MATCH_CACHE.exists():
        try:
            blob = json.loads(MATCH_CACHE.read_text())
            cache = blob.get("players", {})
            cached_ids = set(blob.get("processed_ids", []))
        except Exception:
            pass

    new_ids = [mid for mid in match_ids if mid not in cached_ids]
    print(f"  {len(cached_ids)} matches cached, fetching {len(new_ids)} new...")

    for mid in new_ids:
        data = _fetch(ESPN_SUMMARY.format(mid))
        if not data:
            continue
        for team in data.get("rosters", []):
            for player in team.get("roster", []):
                ath = player.get("athlete") or {}
                name = ath.get("displayName") or player.get("displayName", "")
                if not name:
                    continue
                stats = player.get("stats", [])
                starter = bool(player.get("starter"))
                subbed_in = bool(player.get("subbedIn"))
                appeared = starter or subbed_in or _stat(stats, "appearances") > 0

                if name not in cache:
                    cache[name] = {
                        "goals": 0, "assists": 0, "shots_on": 0, "shots": 0,
                        "appearances": 0, "starts": 0, "sub_ins": 0,
                    }
                p = cache[name]
                p["goals"] += _stat(stats, "totalGoals")
                p["assists"] += _stat(stats, "goalAssists")
                p["shots_on"] += _stat(stats, "shotsOnTarget")
                p["shots"] += _stat(stats, "totalShots")
                if appeared:
                    p["appearances"] += 1
                if starter:
                    p["starts"] += 1
                if subbed_in:
                    p["sub_ins"] += 1
        cached_ids.add(mid)
        time.sleep(0.05)

    # Save cache
    MATCH_CACHE.write_text(json.dumps({
        "processed_ids": list(cached_ids),
        "players": cache,
    }, indent=2))
    print(f"  Cache updated: {len(cache)} players across {len(cached_ids)} matches")
    return cache


# ---------------------------------------------------------------------------
# Step 3 — load 2026 WC squads from Wikipedia
# ---------------------------------------------------------------------------

def fetch_wc_squads() -> list[dict]:
    url = (
        "https://en.wikipedia.org/w/api.php"
        "?action=query&titles=2026_FIFA_World_Cup_squads"
        "&prop=revisions&rvprop=content&format=json&rvslots=main"
    )
    data = _fetch(url)
    if not data:
        print("  WARNING: could not fetch WC squads, skipping squad filter", file=sys.stderr)
        return []
    pages = data.get("query", {}).get("pages", {})
    content = ""
    for page in pages.values():
        content = page.get("revisions", [{}])[0].get("slots", {}).get("main", {}).get("*", "")
    players = []
    for m in re.finditer(
        r"\{\{nat fs g player\|no=(\d+)\|pos=(\w+)\|name=\[\[([^\]|]+)"
        r"(?:\|[^\]]+)?\]\]\|sortname=([^|}\n]+)",
        content,
    ):
        pos = m.group(2)
        sortname = m.group(4).strip()
        parts = [p.strip() for p in sortname.split(",", 1)]
        name = (parts[1] + " " + parts[0]) if len(parts) == 2 else parts[0]
        players.append({"pos": pos, "name": name})
    print(f"  {len(players)} WC squad players found")
    return players


# ---------------------------------------------------------------------------
# Step 4 — load and filter Understat base stats
# ---------------------------------------------------------------------------

def load_understat(wc_squad: list[dict]) -> list[dict]:
    wc_names = [p["name"] for p in wc_squad]
    wc_pos = {p["name"]: p["pos"] for p in wc_squad}

    def match_wc(csv_name: str):
        for wn in wc_names:
            if _token_match(csv_name, wn):
                return wn, wc_pos[wn]
        return None, None

    rows = []
    with open(UNDERSTAT_CSV, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                mins = float(r["minutes"] or 0)
                goals = float(r["goals"] or 0)
                games = float(r["games"] or 0)
            except Exception:
                continue
            if mins < MIN_CLUB_MINUTES or games <= 0:
                continue

            wc_name, wc_pos_code = match_wc(r["player_name"])
            if not wc_name:
                continue
            if wc_pos_code not in ("FW", "MF"):
                continue

            g90 = goals / mins * 90
            avg_mins = mins / games
            is_starter = avg_mins >= STARTER_AVG_MINS and games >= STARTER_MIN_GAMES
            is_sub = avg_mins >= SUB_AVG_MINS and games >= SUB_MIN_GAMES
            if not (is_starter or is_sub):
                continue
            if wc_pos_code == "FW" and g90 < FW_MIN_G90:
                continue
            if wc_pos_code == "MF" and g90 < MF_MIN_G90:
                continue

            r["_wc_name"] = wc_name
            r["_wc_pos"] = wc_pos_code
            r["_g90"] = g90
            rows.append(r)

    print(f"  {len(rows)} Understat players matched to WC squad")
    return rows


# ---------------------------------------------------------------------------
# Step 5 — load custom player overrides (non-Understat stars like Messi)
# ---------------------------------------------------------------------------

def load_custom_players() -> list[dict]:
    if not CUSTOM_JSON.exists():
        return []
    try:
        return json.loads(CUSTOM_JSON.read_text())
    except Exception:
        print(f"  WARNING: could not parse {CUSTOM_JSON}", file=sys.stderr)
        return []


# ---------------------------------------------------------------------------
# Step 6 — merge WC stats into Understat rows + custom rows
# ---------------------------------------------------------------------------

def merge_wc_stats(
    understat_rows: list[dict],
    custom_rows: list[dict],
    wc_stats: Dict[str, dict],
) -> list[dict]:

    def find_wc_stat(name: str) -> Optional[dict]:
        for espn_name, stat in wc_stats.items():
            if _token_match(name, espn_name):
                return stat
        return None

    out = []

    # --- Understat players ---
    for r in understat_rows:
        club_mins = float(r["minutes"])
        club_goals = float(r["goals"])
        club_npg = float(r.get("npg") or club_goals)
        club_games = float(r["games"])

        wc = find_wc_stat(r["player_name"]) or find_wc_stat(r["_wc_name"])
        wc_goals = float(wc["goals"]) if wc else 0.0
        wc_apps = int(wc["appearances"]) if wc else 0
        wc_starts = int(wc["starts"]) if wc else 0
        wc_sub_ins = int(wc["sub_ins"]) if wc else 0
        wc_assists = float(wc["assists"]) if wc else 0.0
        wc_shots_on = float(wc["shots_on"]) if wc else 0.0

        wc_mins = wc_starts * WC_STARTER_MINS + wc_sub_ins * WC_SUB_MINS

        aug_mins = club_mins + wc_mins
        aug_goals = club_goals + wc_goals
        aug_npg = club_npg + wc_goals
        aug_games = club_games + wc_apps
        adj_g90 = aug_goals / aug_mins * 90 if aug_mins > 0 else 0

        note = (
            f"wc:{int(wc_goals)}G/{int(wc_assists)}A in {wc_apps}app"
            if wc_apps > 0 else "no_wc_data"
        )

        out.append({
            "player_name": r["player_name"],
            "minutes": round(aug_mins, 1),
            "games": int(aug_games),
            "goals": round(aug_goals, 3),
            "npg": round(aug_npg, 3),
            "position": r.get("position", ""),
            "team_title": r.get("team_title", ""),
            "league": r.get("league", ""),
            "season": r.get("season", ""),
            "source": "understat+espn_wc2026",
            "wc_goals": int(wc_goals),
            "wc_apps": wc_apps,
            "wc_starts": wc_starts,
            "wc_shots_on": int(wc_shots_on),
            "wc_adj_g90": round(adj_g90, 4),
            "wc_note": note,
        })

    # --- Custom players (e.g. Messi — not in Understat) ---
    for c in custom_rows:
        name = c["player_name"]
        wc = find_wc_stat(name)
        wc_goals = float(wc["goals"]) if wc else 0.0
        wc_apps = int(wc["appearances"]) if wc else 0
        wc_starts = int(wc["starts"]) if wc else 0
        wc_sub_ins = int(wc["sub_ins"]) if wc else 0
        wc_assists = float(wc["assists"]) if wc else 0.0
        wc_shots_on = float(wc["shots_on"]) if wc else 0.0

        # Use custom base stats + WC data
        base_mins = float(c.get("base_minutes", 0))
        base_goals = float(c.get("base_goals", 0))
        base_npg = float(c.get("base_npg", base_goals))
        base_games = float(c.get("base_games", 0))

        wc_mins = wc_starts * WC_STARTER_MINS + wc_sub_ins * WC_SUB_MINS
        aug_mins = base_mins + wc_mins
        aug_goals = base_goals + wc_goals
        aug_npg = base_npg + wc_goals
        aug_games = base_games + wc_apps
        adj_g90 = aug_goals / aug_mins * 90 if aug_mins > 0 else 0

        note = (
            f"custom+wc:{int(wc_goals)}G/{int(wc_assists)}A in {wc_apps}app"
            if wc_apps > 0 else "custom_no_wc_data"
        )

        out.append({
            "player_name": name,
            "minutes": round(aug_mins, 1),
            "games": int(aug_games),
            "goals": round(aug_goals, 3),
            "npg": round(aug_npg, 3),
            "position": c.get("position", "F S"),
            "team_title": c.get("team_title", ""),
            "league": c.get("league", "custom"),
            "season": c.get("season", "2026"),
            "source": "custom+espn_wc2026",
            "wc_goals": int(wc_goals),
            "wc_apps": wc_apps,
            "wc_starts": wc_starts,
            "wc_shots_on": int(wc_shots_on),
            "wc_adj_g90": round(adj_g90, 4),
            "wc_note": note,
        })

    out.sort(key=lambda x: -x["wc_adj_g90"])
    return out


# ---------------------------------------------------------------------------
# Step 7 — write output CSV
# ---------------------------------------------------------------------------

FIELDNAMES = [
    "player_name", "minutes", "games", "goals", "npg",
    "position", "team_title", "league", "season", "source",
    "wc_goals", "wc_apps", "wc_starts", "wc_shots_on",
    "wc_adj_g90", "wc_note",
]


def write_csv(rows: list[dict]) -> None:
    OUTPUT_CSV.parent.mkdir(exist_ok=True)
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    print(f"  Written {len(rows)} players → {OUTPUT_CSV}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-cache", action="store_true",
                        help="Ignore match cache and re-fetch all matches")
    args = parser.parse_args()

    if args.no_cache and MATCH_CACHE.exists():
        MATCH_CACHE.unlink()
        print("Cache cleared.")

    print("1/5  Fetching completed WC match IDs from ESPN...")
    match_ids = fetch_completed_match_ids()
    print(f"     {len(match_ids)} completed matches found")

    print("2/5  Fetching per-player WC stats...")
    wc_stats = fetch_wc_player_stats(match_ids)

    print("3/5  Loading 2026 WC squad lists from Wikipedia...")
    wc_squad = fetch_wc_squads()

    print("4/5  Loading and filtering Understat base stats...")
    if not UNDERSTAT_CSV.exists():
        print(f"  ERROR: {UNDERSTAT_CSV} not found.", file=sys.stderr)
        print("  Run: python scripts/fetch_understat_players.py --seasons 2026,2025,2024 --min-minutes 300")
        sys.exit(1)
    understat_rows = load_understat(wc_squad)

    custom_rows = load_custom_players()
    print(f"  {len(custom_rows)} custom player(s) loaded from {CUSTOM_JSON.name}")

    print("5/5  Merging WC stats and writing output...")
    merged = merge_wc_stats(understat_rows, custom_rows, wc_stats)
    write_csv(merged)

    # Summary
    with_wc = [r for r in merged if r["wc_apps"] > 0]
    scorers = [r for r in merged if r["wc_goals"] > 0]
    print()
    print(f"Done. {len(merged)} players total, {len(with_wc)} with WC appearances, "
          f"{len(scorers)} WC scorers.")
    print()
    print("Top 10 by WC-adjusted g/90:")
    fmt = "  %-26s  ClbG90=%-6s  WcG=%-3s  WcApp=%-3s  AdjG90=%s"
    for r in merged[:10]:
        club_g90 = (
            (r["goals"] - r["wc_goals"]) / (r["minutes"] - r["wc_starts"] * WC_STARTER_MINS
            - (r["wc_apps"] - r["wc_starts"]) * WC_SUB_MINS) * 90
        ) if r["minutes"] > 0 else 0
        print(fmt % (
            r["player_name"][:26],
            f"{club_g90:.3f}",
            r["wc_goals"],
            r["wc_apps"],
            f"{r['wc_adj_g90']:.3f}",
        ))


if __name__ == "__main__":
    main()
