#!/usr/bin/env python3
"""Regenerate data.js for the football hub from TheSportsDB.

Usage: python3 fetch_league.py epl

Pulls teams, fixtures, results and squads for a league, computes punter
stats, and writes a self-contained data.js (window.HUB_DATA = {...}).
"""
import json
import hashlib
import os
import sys
import time
import urllib.request
import urllib.parse

BASE = "https://www.thesportsdb.com/api/v1/json/3"
SLEEP = 1.0  # free demo key rate limit (long backoff kicks in on HTTP 429)
CACHE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".api_cache")

LEAGUES = {
    "epl": {
        "league_id": "4328",
        "name": "Premier League",
        "full_name": "English Premier League",
        "country": "England",
        "brand_color": "#00ff87",  # default hero accent before a club is picked
        # Demo key truncates list/search endpoints, so we discover teams by
        # name. Extra names are fine: only teams whose idLeague matches are kept.
        "team_names": [
            "Arsenal", "Aston Villa", "Bournemouth", "Brentford",
            "Brighton and Hove Albion", "Burnley", "Chelsea", "Coventry City",
            "Crystal Palace", "Everton", "Fulham", "Leeds United",
            "Liverpool", "Manchester City", "Manchester United",
            "Newcastle United", "Nottingham Forest", "Sunderland",
            "Tottenham Hotspur", "West Ham United", "Wolverhampton Wanderers",
            "Sheffield United", "Middlesbrough", "Ipswich Town",
            "Leicester City", "Southampton", "West Bromwich Albion",
            "Stoke City", "Norwich City", "Hull City", "Watford",
        ],
    },
}

OUT_FILE = "data.js"


def get(path):
    # Successful responses are cached on disk, so re-runs only fetch gaps.
    os.makedirs(CACHE_DIR, exist_ok=True)
    cf = os.path.join(CACHE_DIR, hashlib.md5(path.encode()).hexdigest() + ".json")
    if os.path.exists(cf):
        with open(cf) as f:
            return json.load(f)
    url = BASE + "/" + path
    for attempt in range(5):
        time.sleep(SLEEP)
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                data = json.loads(r.read().decode("utf-8"))
            with open(cf, "w") as f:
                json.dump(data, f)
            return data
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 4:
                wait = 15 * (attempt + 1)
                print("  ! 429 rate limit, retrying in %ds: %s" % (wait, path), flush=True)
                time.sleep(wait)
                continue
            print("  ! failed: %s (%s)" % (path, e), flush=True)
            return {}
        except Exception as e:
            print("  ! failed: %s (%s)" % (path, e), flush=True)
            return {}
    return {}


def clean(s):
    if s is None:
        return None
    if isinstance(s, str):
        return (s.replace("—", "-").replace("–", "-")
                 .replace("\u2019", "'").replace("\u2018", "'")
                 .replace("\u201c", '"').replace("\u201d", '"')
                 .replace("\r", " ").strip())
    return s


def clean_event(e):
    return {
        "id": e.get("idEvent"),
        "event": clean(e.get("strEvent")),
        "timestamp": e.get("strTimestamp"),  # naive UTC
        "home": clean(e.get("strHomeTeam")),
        "away": clean(e.get("strAwayTeam")),
        "homeScore": e.get("intHomeScore"),
        "awayScore": e.get("intAwayScore"),
        "venue": clean(e.get("strVenue")),
        "homeGoals": clean(e.get("strHomeGoalDetails")),
        "awayGoals": clean(e.get("strAwayGoalDetails")),
        "season": e.get("strSeason"),
    }


def discover_teams(cfg):
    lid = cfg["league_id"]
    found = {}

    d = get("lookup_all_teams.php?id=%s" % lid)
    for t in d.get("teams") or []:
        if t.get("idLeague") == lid:
            found[t["idTeam"]] = t
    print("lookup_all_teams: %d match" % len(found))

    d = get("search_all_teams.php?l=%s" % urllib.parse.quote(cfg["full_name"]))
    n0 = len(found)
    for t in d.get("teams") or []:
        if t.get("idLeague") == lid:
            found[t["idTeam"]] = t
    print("search_all_teams: +%d" % (len(found) - n0))

    for name in cfg.get("team_names", []):
        if any(t.get("strTeam") == name for t in found.values()):
            continue
        d = get("searchteams.php?t=%s" % urllib.parse.quote(name))
        for t in d.get("teams") or []:
            if t.get("idLeague") == lid:
                found[t["idTeam"]] = t

    teams = sorted(found.values(), key=lambda t: t.get("strTeam", ""))
    print("discovered %d teams" % len(teams))
    return teams


def build_team(t):
    return {
        "id": t["idTeam"],
        "name": clean(t.get("strTeam")),
        "short": clean(t.get("strTeamShort")) or "",
        "badge": t.get("strBadge") or "",
        "colors": [clean(t.get("strColour1")) or "",
                   clean(t.get("strColour2")) or "",
                   clean(t.get("strColour3")) or ""],
        "stadium": clean(t.get("strStadium")) or "",
        "formed": t.get("intFormedYear") or "",
    }


def build_player(p):
    return {
        "name": clean(p.get("strPlayer")),
        "position": clean(p.get("strPosition")) or "",
        "nationality": clean(p.get("strNationality")) or "",
        "number": clean(p.get("strNumber")) or "",
        "thumb": p.get("strThumb") or "",
    }


def make_writeup(team, ev):
    """2-3 plain sentences about the club's most recent match."""
    hs, as_ = ev.get("homeScore"), ev.get("awayScore")
    if hs is None or as_ is None:
        return ""
    hs, as_ = int(hs), int(as_)
    home = team == ev["home"]
    opp = ev["away"] if home else ev["home"]
    venue = ev.get("venue") or "the ground"
    score = "%d-%d" % (hs, as_)
    gf, ga = (hs, as_) if home else (as_, hs)

    if gf > ga:
        s1 = "%s beat %s %s at %s." % (team, opp, score, venue)
    elif gf == ga:
        s1 = "%s drew %s with %s at %s." % (team, score, opp, venue)
    else:
        s1 = "%s lost %s to %s at %s." % (team, score, opp, venue)

    scorers = []
    for det in (ev.get("homeGoals") or "").split(";"):
        det = det.strip()
        if det:
            scorers.append(det)
    for det in (ev.get("awayGoals") or "").split(";"):
        det = det.strip()
        if det:
            scorers.append(det)
    if scorers:
        s2 = "On the scoresheet: " + ", ".join(scorers[:6]) + "."
    elif hs + as_ == 0:
        s2 = "Neither side could find a way through in a tight contest."
    elif hs + as_ >= 4:
        s2 = "The goals flowed and the fans got their money's worth."
    elif gf > ga:
        s2 = "It stayed close, but the lads saw it out to the final whistle."
    elif gf == ga:
        s2 = "A point apiece felt about right on the day."
    else:
        s2 = "It was tight all the way, and one moment settled it."

    s3 = "Attention now turns to the next fixture."
    return " ".join([s1, s2, s3])


def compute_stats(results):
    played = [r for r in results
              if r.get("homeScore") is not None and r.get("awayScore") is not None]
    if not played:
        return {"games": 0, "avgGoals": 0, "homeWinPct": 0,
                "bttsPct": 0, "topScoringTeam": None}
    total = hw = btts = 0
    goals_by_team = {}
    for r in played:
        hs, as_ = int(r["homeScore"]), int(r["awayScore"])
        total += hs + as_
        if hs > as_:
            hw += 1
        if hs > 0 and as_ > 0:
            btts += 1
        goals_by_team[r["home"]] = goals_by_team.get(r["home"], 0) + hs
        goals_by_team[r["away"]] = goals_by_team.get(r["away"], 0) + as_
    n = len(played)
    top = max(goals_by_team.items(), key=lambda kv: kv[1]) if goals_by_team else (None, 0)
    return {
        "games": n,
        "avgGoals": round(total / n, 2),
        "homeWinPct": round(100 * hw / n),
        "bttsPct": round(100 * btts / n),
        "topScoringTeam": {"name": top[0], "goals": top[1]} if top[0] else None,
    }


def dedup_sort(events, cap, reverse=False):
    seen, out = set(), []
    for e in events:
        if e["id"] and e["id"] not in seen:
            seen.add(e["id"])
            out.append(e)
    out.sort(key=lambda e: e.get("timestamp") or "", reverse=reverse)
    return out[:cap]


def main():
    key = sys.argv[1] if len(sys.argv) > 1 else "epl"
    if key not in LEAGUES:
        print("unknown league '%s'. Options: %s" % (key, ", ".join(LEAGUES)))
        sys.exit(1)
    cfg = LEAGUES[key]
    lid = cfg["league_id"]

    raw_teams = discover_teams(cfg)
    teams = [build_team(t) for t in raw_teams]

    print("fetching league events...")
    league_next = [clean_event(e)
                   for e in (get("eventsnextleague.php?id=%s" % lid).get("events") or [])]
    league_past = [clean_event(e)
                   for e in (get("eventspastleague.php?id=%s" % lid).get("events") or [])]

    team_fixtures, squads, writeups = {}, {}, {}
    for i, t in enumerate(teams, 1):
        print("[%d/%d] %s" % (i, len(teams), t["name"]))
        nxt = [clean_event(e) for e in (get("eventsnext.php?id=%s" % t["id"]).get("events") or [])]
        past = [clean_event(e) for e in (get("eventslast.php?id=%s" % t["id"]).get("results") or [])]
        team_fixtures[t["id"]] = {"next": nxt[:5], "past": past[:5]}
        league_next.extend(nxt)
        league_past.extend(past)
        players = [build_player(p)
                   for p in (get("lookup_all_players.php?id=%s" % t["id"]).get("player") or [])]
        players = [p for p in players if p["position"] in
                   ("Goalkeeper", "Defender", "Midfielder", "Forward")]
        squads[t["id"]] = players
        writeups[t["id"]] = make_writeup(t["name"], past[0]) if past else ""

    data = {
        "league": {"key": key, "id": lid, "name": cfg["name"],
                   "fullName": cfg["full_name"], "country": cfg["country"],
                   "brandColor": cfg["brand_color"]},
        "generatedAt": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()),
        "teams": teams,
        "leagueFixtures": dedup_sort(league_next, 10),
        "leagueResults": dedup_sort(league_past, 10, reverse=True),
        "teamFixtures": team_fixtures,
        "squads": squads,
        "writeups": writeups,
        "stats": compute_stats(league_past),
    }

    blob = json.dumps(data, ensure_ascii=True, indent=1)
    blob = blob.replace("\\u2014", "-").replace("\\u2013", "-")
    with open(OUT_FILE, "w") as f:
        f.write("// Generated by fetch_league.py (%s). Do not edit by hand.\n" % key)
        f.write("window.HUB_DATA = " + blob + ";\n")
    print("wrote %s: %d teams, %d league fixtures, %d league results, stats from %d games"
          % (OUT_FILE, len(teams), len(data["leagueFixtures"]),
             len(data["leagueResults"]), data["stats"]["games"]))


if __name__ == "__main__":
    main()
