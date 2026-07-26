#!/usr/bin/env python3
"""Check dealwork, moltcities, and simmer caches against previous state and summarize matches."""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path("/root/.openclaw/workspace")
CACHE_DIR = WORKSPACE / "job-boards-cache"
STATE_PATH = WORKSPACE / "job-boards-state.json"
PROFILE_PATH = WORKSPACE / "job-boards-profile.json"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def parse_ts(ts):
    if not ts:
        return None
    if ts.endswith("Z"):
        ts = ts[:-1] + "+00:00"
    return datetime.fromisoformat(ts)


def format_deadline(ts):
    dt = parse_ts(ts)
    if not dt:
        return "no deadline"
    now = datetime.now(timezone.utc)
    days = (dt - now).total_seconds() / 86400
    if days < 0:
        return f"overdue ({dt.strftime('%Y-%m-%d')})"
    if days < 1:
        return f"today ({dt.strftime('%Y-%m-%d %H:%M UTC')})"
    if days < 2:
        return f"tomorrow ({dt.strftime('%Y-%m-%d %H:%M UTC')})"
    return f"{dt.strftime('%Y-%m-%d')} ({int(days)} days)"


def price(job):
    mn = job.get("budgetMin")
    mx = job.get("budgetMax")
    fx = job.get("fixedPrice")
    if fx:
        return f"${float(fx):.0f}"
    if mn and mx:
        return f"${float(mn):.0f}-${float(mx):.0f}"
    if mx:
        return f"up to ${float(mx):.0f}"
    if mn:
        return f"from ${float(mn):.0f}"
    return "open budget"


def job_matches_profile(job, profile):
    tags = {t.lower() for t in job.get("tags", [])}
    skills = {s.lower() for s in profile.get("skills", [])}
    categories = {c.lower() for c in profile.get("categories", [])}
    title = job.get("title", "").lower()
    desc = job.get("description", "").lower()
    category = (job.get("category") or "").lower()

    if tags & skills:
        return True
    if category in categories:
        return True
    for kw in profile.get("titleKeywords", []):
        if kw.lower() in title or kw.lower() in desc:
            return True
    return False


def analyze_dealwork(state, profile):
    cache = load_json(CACHE_DIR / "dealwork.json")
    jobs = cache.get("data", [])
    previous_ids = set(state.get("dealwork", {}).get("jobIds", []))
    current_ids = set()
    matches = []
    new_matches = []

    for job in jobs:
        jid = job.get("id")
        if not jid:
            continue
        current_ids.add(jid)
        if job_matches_profile(job, profile):
            info = {
                "id": jid,
                "title": job.get("title", "Untitled"),
                "price": price(job),
                "deadline": format_deadline(job.get("deadline")),
                "biddingDeadline": format_deadline(job.get("biddingDeadline")),
                "mode": job.get("jobMode"),
                "status": job.get("status"),
                "bidCount": job.get("bidCount"),
                "poster": job.get("posterDisplayName", "Unknown"),
            }
            matches.append(info)
            if jid not in previous_ids:
                new_matches.append(info)

    return {
        "total": len(jobs),
        "matched": len(matches),
        "new": new_matches,
        "all_matches": matches,
        "current_ids": list(current_ids),
    }


def moltcities_reward(job):
    reward = job.get("reward") or {}
    sol = reward.get("sol")
    if sol:
        return f"{float(sol):g} SOL"
    lamports = reward.get("lamports")
    if lamports:
        return f"{float(lamports) / 1e9:g} SOL"
    return "no reward listed"


def analyze_moltcities(state, profile):
    path = CACHE_DIR / "moltcities.json"
    if not path.exists():
        return {"error": "no cache file"}
    cache = load_json(path)
    if cache.get("error"):
        return {"error": cache.get("body", "unknown error").strip()}
    jobs = cache.get("jobs", cache.get("data", []))
    previous_ids = set(state.get("moltcities", {}).get("jobIds", []))
    current_ids = set()
    matches = []
    new_matches = []

    for job in jobs:
        jid = job.get("id")
        if not jid:
            continue
        current_ids.add(jid)
        if job.get("status") and job.get("status") != "open":
            continue
        if job_matches_profile(job, profile):
            poster = job.get("poster") or {}
            info = {
                "id": jid,
                "title": job.get("title", "Untitled"),
                "reward": moltcities_reward(job),
                "deadline": format_deadline(job.get("expires_at")),
                "poster": poster.get("name", "Unknown"),
                "created_at": job.get("created_at"),
            }
            matches.append(info)
            if jid not in previous_ids:
                new_matches.append(info)

    return {
        "error": None,
        "total": len(jobs),
        "matched": len(matches),
        "new": new_matches,
        "current_ids": list(current_ids),
    }


def analyze_simmer(state):
    events_cache = load_json(CACHE_DIR / "simmer_events.json")
    markets_cache = load_json(CACHE_DIR / "simmer.json")
    previous_ids = set(state.get("simmer", {}).get("eventIds", []))
    current_ids = set()
    new_events = []

    for event in events_cache.get("events", []):
        eid = event.get("id")
        if not eid:
            continue
        current_ids.add(eid)
        if eid not in previous_ids:
            new_events.append({
                "id": eid,
                "name": event.get("name", "Unnamed"),
                "platform": event.get("platform"),
                "resolves_at": event.get("resolves_at") or "today",
            })

    # Keep only first ~10 new events in summary to avoid noise
    return {
        "total_events": len(events_cache.get("events", [])),
        "total_markets": len(markets_cache.get("markets", [])),
        "new": new_events[:15],
        "new_count": len(new_events),
        "current_ids": list(current_ids),
    }


def main():
    state = load_json(STATE_PATH) if STATE_PATH.exists() else {}
    profile = load_json(PROFILE_PATH) if PROFILE_PATH.exists() else {"skills": []}

    dealwork = analyze_dealwork(state, profile)
    moltcities = analyze_moltcities(state, profile)
    simmer = analyze_simmer(state)

    lines = []
    lines.append(f"Job-boards check — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append("")

    # Dealwork
    lines.append(f"**dealwork.ai** — {dealwork['matched']} matching your profile out of {dealwork['total']} listings")
    if dealwork["new"]:
        lines.append(f"New since last check: {len(dealwork['new'])}")
        lines.append("")
        for job in dealwork["new"]:
            dl = job["deadline"]
            bdl = job["biddingDeadline"]
            deadline = f"deadline {dl}"
            if bdl and "no deadline" not in bdl:
                deadline += f", bid by {bdl}"
            lines.append(f"- **{job['title']}** — {job['price']} — {deadline}")
    else:
        lines.append("No new matching postings since last check.")
    lines.append("")

    # Moltcities
    if moltcities.get("error"):
        lines.append(f"**moltcities.org** — unable to check ({moltcities['error']})")
    else:
        lines.append(f"**moltcities.org** — {moltcities['matched']} matching your profile out of {moltcities['total']} open listings")
        if moltcities["new"]:
            lines.append(f"New since last check: {len(moltcities['new'])}")
            lines.append("")
            for job in moltcities["new"]:
                lines.append(f"- **{job['title']}** — {job['reward']} — deadline {job['deadline']} — posted by {job['poster']}")
        else:
            lines.append("No new matching postings since last check.")
    lines.append("")

    # Simmer
    lines.append(f"**simmer.markets** — {simmer['new_count']} new events since last check ({simmer['total_events']} total events, {simmer['total_markets']} markets)")
    if simmer["new"]:
        for ev in simmer["new"]:
            lines.append(f"- {ev['name']} — resolves {ev['resolves_at']}")
    else:
        lines.append("No new events since last check.")
    lines.append("")

    # Update state
    new_state = {
        "lastCheck": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "dealwork": {
            "count": len(dealwork["current_ids"]),
            "jobIds": dealwork["current_ids"],
        },
        "moltcities": (
            {
                "count": len(moltcities["current_ids"]),
                "jobIds": moltcities["current_ids"],
            }
            if moltcities.get("current_ids")
            else state.get("moltcities", {"count": 0, "jobIds": []})
        ),
        "simmer": {
            "count": len(simmer["current_ids"]),
            "eventIds": simmer["current_ids"],
        },
    }
    save_json(STATE_PATH, new_state)

    summary = "\n".join(lines)
    print(summary)

    # Also write a summary file for inspection
    (WORKSPACE / "job-boards-summary.txt").write_text(summary, encoding="utf-8")


if __name__ == "__main__":
    main()
