#!/usr/bin/env python3
"""MoltCities heartbeat.

Checks notifications, inbox, open jobs, town square, and governance proposals.
Logs a summary to workspace/logs/moltcities-heartbeat.log.
"""

import json
import os
import datetime
from pathlib import Path

import requests

ROOT = Path("/root/.openclaw/workspace")
LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "moltcities-heartbeat.log"
STATE_FILE = LOG_DIR / "moltcities-heartbeat.state.json"

BASE = "https://moltcities.org/api"
CREDS_PATH = os.path.expanduser("~/.moltcities/credentials.json")


def now_utc():
    return datetime.datetime.now(datetime.timezone.utc)


def log(msg):
    ts = now_utc().isoformat()
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def load_state():
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception as e:
            log(f"state load error: {e}")
    return {}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2, default=str))


def api_get(path, params=None, auth=True):
    headers = {}
    if auth and os.path.exists(CREDS_PATH):
        creds = json.load(open(CREDS_PATH))
        headers["Authorization"] = f"Bearer {creds['api_key']}"
    try:
        r = requests.get(BASE + path, headers=headers, params=params, timeout=30)
    except Exception as e:
        log(f"request error {path}: {e}")
        return None
    if r.status_code >= 400:
        log(f"API error {r.status_code} on {path}: {r.text[:200]}")
        return None
    return r.json() if r.text else {}


def main():
    log("=== moltcities heartbeat ===")
    state = load_state()

    if not os.path.exists(CREDS_PATH):
        log("no credentials found; exiting")
        return

    creds = json.load(open(CREDS_PATH))
    log(f"agent: {creds.get('agent_name')} ({creds.get('site_url')}) wallet_verified={creds.get('wallet_verified')}")

    me = api_get("/me")
    trust_tier = me.get("agent", {}).get("trust_tier") if me else None

    notifications = api_get("/notifications", params={"limit": 20}) or {}
    unread = notifications.get("unread_count", 0)
    notif_list = notifications.get("notifications", [])

    inbox = api_get("/inbox", params={"unread": "true"}) or {}
    unread_messages = inbox.get("messages", [])

    jobs = api_get("/jobs", params={"status": "open", "limit": 10}, auth=False) or {}
    open_jobs = jobs.get("jobs", [])

    town = api_get("/town-square", params={"limit": 5}) or {}
    messages = town.get("messages", [])

    gov = api_get("/governance/proposals", params={"status": "open"}) or {}
    proposals = gov.get("proposals", [])

    log(
        f"trust_tier={trust_tier} unread_notifications={unread} unread_messages={len(unread_messages)} "
        f"open_jobs={len(open_jobs)} town_messages={len(messages)} open_proposals={len(proposals)}"
    )

    for n in notif_list[:5]:
        log(f"notification: {n.get('type')} - {n.get('content','')[:100]}")

    for j in open_jobs[:5]:
        reward = j.get("reward", {})
        log(
            f"job: {j.get('title')} | reward={reward.get('sol')} SOL | "
            f"template={j.get('verification_template')} | id={j.get('id')}"
        )

    for m in messages[:3]:
        author = m.get("agent", {}).get("name", "?")
        log(f"town: {author}: {m.get('message','')[:120]}")

    for prop in proposals[:3]:
        log(f"proposal: {prop.get('title')} | support={prop.get('votes_support')} oppose={prop.get('votes_oppose')}")

    state["last_check"] = now_utc().isoformat()
    state["unread_notifications"] = unread
    state["unread_messages"] = len(unread_messages)
    state["open_jobs"] = len(open_jobs)
    state["open_proposals"] = len(proposals)
    save_state(state)
    log("=== moltcities heartbeat complete ===\n")


if __name__ == "__main__":
    main()
