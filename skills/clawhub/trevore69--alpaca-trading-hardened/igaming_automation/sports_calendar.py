#!/usr/bin/env python3
"""Sports calendar for igamingreviews social content.

Tracks the leagues Trevor cares about (NBA, WNBA, EPL, F1, plus other major
SA-betting leagues), pulls recent results and upcoming fixtures from
TheSportsDB, and writes a snapshot that social drafting reads from.

Usage:
    python3 sports_calendar.py            # fetch + write snapshot
    python3 sports_calendar.py --resolve  # re-resolve league IDs, then fetch
"""

import json
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).parent
LEAGUES_PATH = ROOT / "sports_leagues.json"
SNAPSHOT_MD_PATH = ROOT / "sports_snapshot.md"
SNAPSHOT_JSON_PATH = ROOT / "sports_snapshot.json"

API_BASE = "https://www.thesportsdb.com/api/v1/json/3"
SAST = timezone(timedelta(hours=2))
REQUEST_GAP = 0.4  # seconds between API calls, be polite to the free tier

# (key, sport, country-or-None, [name patterns], verified league id or None)
# The demo API key truncates search results to 5 entries, so well-known
# leagues carry IDs verified through lookupleague.php instead of search.
LEAGUE_WISHLIST = [
    ("epl", "Soccer", "England", ["english premier league"], "4328"),
    ("ucl", "Soccer", "Europe", ["uefa champions league"], "4480"),
    ("psl", "Soccer", "South Africa", ["premier"], "4802"),
    ("nba", "Basketball", "United States", ["nba"], "4387"),
    ("wnba", "Basketball", "United States", ["wnba"], "4516"),
    ("f1", "Motorsport", None, ["formula 1"], "4370"),
    ("urc", "Rugby", None, ["united rugby championship"], "4446"),
    ("ipl", "Cricket", "India", ["indian premier league"], "4460"),
    ("sa20", "Cricket", "South Africa", ["sa20"], "5532"),
]


def api_get(endpoint: str) -> dict:
    url = f"{API_BASE}/{endpoint}"
    try:
        resp = requests.get(url, timeout=20)
        resp.raise_for_status()
        time.sleep(REQUEST_GAP)
        return resp.json()
    except Exception as exc:
        print(f"API error on {endpoint}: {exc}")
        return {}


def resolve_leagues() -> list:
    """Build the tracked league list, verifying known IDs via lookupleague."""
    resolved = []
    for key, sport, country, patterns, known_id in LEAGUE_WISHLIST:
        match = None
        if known_id:
            data = api_get(f"lookupleague.php?id={known_id}")
            items = data.get("leagues") or []
            if items:
                candidate = items[0]
                name = (candidate.get("strLeague") or "").lower()
                if any(p in name for p in patterns):
                    match = candidate
                else:
                    print(f"ID MISMATCH for {key}: id {known_id} is '{candidate.get('strLeague')}' - skipped")
        else:
            if country:
                data = api_get(f"search_all_leagues.php?c={country.replace(' ', '%20')}&s={sport}")
            else:
                data = api_get(f"search_all_leagues.php?s={sport}")
            candidates = data.get("countries") or data.get("leagues") or []
            for league in candidates:
                name = (league.get("strLeague") or "").lower()
                if any(p in name for p in patterns):
                    match = league
                    break

        if match:
            resolved.append({
                "key": key,
                "name": match["strLeague"],
                "sport": sport,
                "league_id": match["idLeague"],
            })
            print(f"Resolved {key}: {match['strLeague']} (id {match['idLeague']})")
        elif not known_id:
            print(f"NOT FOUND: {key} ({sport}/{country or 'any'}) - skipped")
    return resolved


def load_leagues() -> list:
    if LEAGUES_PATH.exists():
        with open(LEAGUES_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_leagues(leagues: list):
    with open(LEAGUES_PATH, "w", encoding="utf-8") as f:
        json.dump(leagues, f, indent=2)


def fetch_league_events(league: dict) -> dict:
    lid = league["league_id"]
    nxt = api_get(f"eventsnextleague.php?id={lid}").get("events") or []
    past = api_get(f"eventspastleague.php?id={lid}").get("events") or []
    return {"league": league, "upcoming": nxt[:5], "results": past[:5]}


def parse_dt(event: dict):
    ts = event.get("strTimestamp")
    if ts:
        try:
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except ValueError:
            pass
    date = event.get("dateEvent")
    if date:
        try:
            return datetime.fromisoformat(date).replace(tzinfo=timezone.utc)
        except ValueError:
            return None
    return None


def fmt_dt_sast(dt) -> str:
    if not dt:
        return "date TBC"
    sast = dt.astimezone(SAST)
    return sast.strftime("%d/%m/%Y %H:%M SAST")


def event_title(event: dict) -> str:
    return re.sub(r"\s+", " ", (event.get("strEvent") or "unknown")).strip()


def build_snapshot(sections: list) -> tuple:
    now = datetime.now(timezone.utc)
    md_lines = [
        "# Sports snapshot",
        f"Updated: {now.astimezone(SAST).strftime('%d/%m/%Y %H:%M SAST')}",
        "",
    ]
    data = {"updated_utc": now.isoformat(), "leagues": []}

    for section in sections:
        league = section["league"]
        md_lines.append(f"## {league['name']} ({league['sport']})")
        md_lines.append("")
        md_lines.append("Recent results:")
        if section["results"]:
            for ev in section["results"]:
                home, away = ev.get("intHomeScore"), ev.get("intAwayScore")
                score = f"{home}-{away}" if home is not None and away is not None else "result n/a"
                md_lines.append(f"- {fmt_dt_sast(parse_dt(ev))}: {event_title(ev)} -> {score}")
        else:
            md_lines.append("- none in feed (off-season?)")
        md_lines.append("")
        md_lines.append("Upcoming:")
        if section["upcoming"]:
            for ev in section["upcoming"]:
                md_lines.append(f"- {fmt_dt_sast(parse_dt(ev))}: {event_title(ev)}")
        else:
            md_lines.append("- none in feed (off-season?)")
        md_lines.append("")

        data["leagues"].append({
            "key": league["key"],
            "name": league["name"],
            "sport": league["sport"],
            "results": [
                {
                    "event": event_title(ev),
                    "home_score": ev.get("intHomeScore"),
                    "away_score": ev.get("intAwayScore"),
                    "timestamp": ev.get("strTimestamp"),
                }
                for ev in section["results"]
            ],
            "upcoming": [
                {"event": event_title(ev), "timestamp": ev.get("strTimestamp")}
                for ev in section["upcoming"]
            ],
        })

    return "\n".join(md_lines), data


def run():
    if "--resolve" in sys.argv or not LEAGUES_PATH.exists():
        leagues = resolve_leagues()
        if leagues:
            save_leagues(leagues)
    else:
        leagues = load_leagues()

    if not leagues:
        print("No leagues resolved. Run with --resolve.")
        sys.exit(1)

    print(f"Fetching events for {len(leagues)} leagues...")
    sections = [fetch_league_events(lg) for lg in leagues]
    md, data = build_snapshot(sections)

    with open(SNAPSHOT_MD_PATH, "w", encoding="utf-8") as f:
        f.write(md)
    with open(SNAPSHOT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Snapshot written: {SNAPSHOT_MD_PATH} + {SNAPSHOT_JSON_PATH}")
    print(md)


if __name__ == "__main__":
    run()
