#!/usr/bin/env python3
"""Fetch fresh job-board data into job-boards-cache/."""

import json
import urllib.request
from pathlib import Path

WORKSPACE = Path("/root/.openclaw/workspace")
CACHE_DIR = WORKSPACE / "job-boards-cache"
CREDS_PATH = Path("/root/.openwork/credentials.json")


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def fetch_dealwork():
    if not CREDS_PATH.exists():
        return {"error": "credentials not found"}
    creds = json.loads(CREDS_PATH.read_text(encoding="utf-8"))
    api_key = creds.get("apiKey")
    if not api_key:
        return {"error": "apiKey missing"}

    url = "https://dealwork.ai/api/v1/jobs?page=1&per_page=100"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {api_key}"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}", "body": e.read().decode("utf-8", errors="ignore")}
    except Exception as e:
        return {"error": str(e)}


def fetch_moltcities():
    url = "https://moltcities.org/api/jobs"
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}", "body": e.read().decode("utf-8", errors="ignore")}
    except Exception as e:
        return {"error": str(e)}


def fetch_simmer():
    creds_path = Path("/root/.simmer/credentials.json")
    if not creds_path.exists():
        return {"error": "credentials not found"}
    creds = json.loads(creds_path.read_text(encoding="utf-8"))
    api_key = creds.get("api_key")
    if not api_key:
        return {"error": "api_key missing"}

    headers = {"Authorization": f"Bearer {api_key}"}
    base = "https://www.simmer.markets/api/sdk"
    try:
        req_events = urllib.request.Request(f"{base}/events", headers=headers)
        req_markets = urllib.request.Request(f"{base}/markets", headers=headers)
        with urllib.request.urlopen(req_events, timeout=30) as r:
            events = json.loads(r.read().decode("utf-8"))
        with urllib.request.urlopen(req_markets, timeout=30) as r:
            markets = json.loads(r.read().decode("utf-8"))
        return {"events": events, "markets": markets}
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}", "body": e.read().decode("utf-8", errors="ignore")}
    except Exception as e:
        return {"error": str(e)}


def main():
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    save_json(CACHE_DIR / "dealwork.json", fetch_dealwork())
    save_json(CACHE_DIR / "moltcities.json", fetch_moltcities())
    simmer = fetch_simmer()
    if "events" in simmer and "markets" in simmer:
        save_json(CACHE_DIR / "simmer_events.json", {"events": simmer["events"]})
        save_json(CACHE_DIR / "simmer.json", simmer["markets"])
    else:
        save_json(CACHE_DIR / "simmer_fetched.json", simmer)


if __name__ == "__main__":
    main()
