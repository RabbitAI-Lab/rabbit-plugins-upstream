#!/usr/bin/env python3
"""HealthOS read-only API client (allow-listed, no writes).

Reads HEALTHOS_API_TOKEN (and optional HEALTHOS_API_URL) from the environment.
Every request is a GET to an allow-listed path; there is no write surface.
Prints JSON to stdout. The token is never logged or echoed.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request

API_URL = os.environ.get("HEALTHOS_API_URL", "https://api.healthosx.com/api")
TOKEN = os.environ.get("HEALTHOS_API_TOKEN", "")

# Browser User-Agent: the API is behind Cloudflare, which rejects unknown
# clients with error 1010.
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json",
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    ),
}

ALLOWED_METRICS = {
    "steps", "active_energy", "heart_rate", "resting_heart_rate",
    "hrv_sdnn", "respiratory_rate", "body_weight",
    "blood_pressure_systolic", "blood_pressure_diastolic",
}


def get(path: str, params: dict) -> dict:
    if not TOKEN:
        raise SystemExit("HEALTHOS_API_TOKEN is not set")
    query = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    url = f"{API_URL}{path}" + (f"?{query}" if query else "")
    request = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as exc:
        body = exc.read().decode()
        raise SystemExit(f"API error {exc.code}: {body}") from None
    except urllib.error.URLError as exc:
        raise SystemExit(f"request failed: {exc.reason}") from None


def iso_date(value: str, name: str) -> str:
    # Accept YYYY-MM-DD and normalise to an instant-friendly range boundary.
    import datetime
    try:
        datetime.date.fromisoformat(value)
    except ValueError:
        raise SystemExit(f"invalid {name} date: {value!r} (use YYYY-MM-DD)") from None
    return value


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="HealthOS read-only API")
    sub = parser.add_subparsers(dest="command", required=True)

    p_summary = sub.add_parser("summary")
    p_summary.add_argument("--date", help="YYYY-MM-DD")
    p_summary.add_argument("--tz", default="UTC")

    p_metrics = sub.add_parser("metrics")
    p_metrics.add_argument("--type", required=True, help="metric type (allow-listed)")
    p_metrics.add_argument("--from", dest="from_", help="start date YYYY-MM-DD")
    p_metrics.add_argument("--to", help="end date YYYY-MM-DD")
    p_metrics.add_argument("--limit", type=int, default=500)

    p_sleep = sub.add_parser("sleep")
    p_sleep.add_argument("--from", dest="from_", help="start date YYYY-MM-DD")
    p_sleep.add_argument("--to", help="end date YYYY-MM-DD")

    p_workouts = sub.add_parser("workouts")
    p_workouts.add_argument("--from", dest="from_", help="start date YYYY-MM-DD")
    p_workouts.add_argument("--to", help="end date YYYY-MM-DD")

    args = parser.parse_args(argv)

    if args.command == "summary":
        data = get("/v1/health/summary", {"date": args.date, "tz": args.tz})
    elif args.command == "metrics":
        if args.type not in ALLOWED_METRICS:
            raise SystemExit(f"metric type not allowed: {args.type!r}")
        data = get("/v1/health/metrics", {
            "metric_type": args.type,
            "from": iso_date(args.from_, "from") if args.from_ else None,
            "to": iso_date(args.to, "to") if args.to else None,
            "limit": args.limit,
        })
    elif args.command == "sleep":
        data = get("/v1/health/sleep", {
            "from": iso_date(args.from_, "from") if args.from_ else None,
            "to": iso_date(args.to, "to") if args.to else None,
        })
    else:  # workouts
        data = get("/v1/health/workouts", {
            "from": iso_date(args.from_, "from") if args.from_ else None,
            "to": iso_date(args.to, "to") if args.to else None,
        })

    print(json.dumps(data, indent=2, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
