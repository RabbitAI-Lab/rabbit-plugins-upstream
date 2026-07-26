#!/usr/bin/env python3
"""
Price alert checker for the tracked portfolio names.
Alerts when current price moves >= 5% in either direction from the previous
day's close.
Only runs during NYSE trading hours (Mon-Fri 09:30-16:00 America/New_York).
"""
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

SYMBOLS = ["CPNG", "INFQ", "NFLX", "NB", "SPCX"]
THRESHOLD = 5.0
# Deliberately NOT stock-alerts-state.json — the market-watch cron owns that
# file and stores a different schema (prices/previousClose). Sharing it made
# the two clobber each other.
STATE_FILE = "/root/.openclaw/workspace/stock-alert-fired.json"


def now_in_ny():
    return datetime.now(timezone.utc).astimezone(
        timezone(datetime.strptime("2024-01-01", "%Y-%m-%d")
                 .astimezone()
                 .tzinfo.utcoffset(None) if False else None)
    )


def is_nyse_open():
    ny = datetime.now(timezone.utc).astimezone(__import__('zoneinfo').ZoneInfo('America/New_York'))
    weekday = ny.weekday()  # 0=Mon, 6=Sun
    if weekday >= 5:
        return False
    time_str = ny.strftime("%H:%M")
    return "09:30" <= time_str <= "16:00"


def fetch_yahoo(symbol):
    # range=1d is load-bearing: chartPreviousClose is the close *before* the
    # requested window, so range=5d yields a week-old baseline, not yesterday.
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1d&range=1d"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    result = subprocess.run(
        ["curl", "-s", "-A", headers["User-Agent"], url],
        capture_output=True, text=True, timeout=30
    )
    if result.returncode != 0:
        return None
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return None


def main():
    if not is_nyse_open():
        return

    today = datetime.now(timezone.utc).astimezone(
        __import__('zoneinfo').ZoneInfo('America/New_York')
    ).strftime("%Y-%m-%d")

    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                state = json.load(f)
        except (json.JSONDecodeError, OSError):
            state = {}
    else:
        state = {}

    alerts = []
    for symbol in SYMBOLS:
        data = fetch_yahoo(symbol)
        if not data:
            continue
        try:
            meta = data["chart"]["result"][0]["meta"]
            prev_close = float(meta["chartPreviousClose"])
            current = float(meta["regularMarketPrice"])
        except (KeyError, IndexError, ValueError, TypeError):
            continue

        if prev_close == 0:
            continue

        pct = ((current - prev_close) / prev_close) * 100
        if abs(pct) < THRESHOLD:
            continue

        direction = "up" if pct > 0 else "down"
        # Fire once per symbol per direction per day, so a name that keeps
        # sliding doesn't re-alert, but a reversal still gets through.
        fired = state.get(symbol) or {}
        if fired.get("date") == today and direction in fired.get("dirs", []):
            continue

        icon = "🚨" if direction == "down" else "🚀"
        alerts.append(
            f"{icon} {symbol} is {direction} {abs(pct):.2f}% today "
            f"(now ${current:.2f}, prev close ${prev_close:.2f})."
        )
        dirs = fired.get("dirs", []) if fired.get("date") == today else []
        state[symbol] = {"date": today, "dirs": dirs + [direction]}

    if state:
        with open(STATE_FILE, "w") as f:
            json.dump(state, f)

    if alerts:
        print("\n".join(alerts))


if __name__ == "__main__":
    main()
