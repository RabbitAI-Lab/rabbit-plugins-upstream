#!/usr/bin/env python3
"""Validate completeness of a structured research claim ledger.

This checks that evidence provenance and incentive fields exist. It does not
judge whether a claim is true or whether a source is trustworthy.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED = {
    "claim",
    "type",
    "evidence",
    "source_date",
    "source_class",
    "incentive",
    "independence",
    "optimization_risk",
    "verification_path",
    "confidence",
    "status",
}

ALLOWED_TYPES = {"fact", "interpretation", "inference", "forecast"}
ALLOWED_RISKS = {"low", "medium", "high"}
ALLOWED_STATUSES = {"supported", "qualified", "rejected", "unresolved"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path, help="JSON file containing a list of claim objects")
    args = parser.parse_args()

    try:
        data = json.loads(args.ledger.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    if not isinstance(data, list) or not data:
        print("ERROR: ledger must be a non-empty JSON list")
        return 1

    failures = 0
    for index, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            print(f"ERROR: claim {index} is not an object")
            failures += 1
            continue

        missing = sorted(key for key in REQUIRED if key not in item or item[key] in (None, "", []))
        if missing:
            print(f"ERROR: claim {index} missing: {', '.join(missing)}")
            failures += 1

        if item.get("type") not in ALLOWED_TYPES:
            print(f"ERROR: claim {index} has invalid type: {item.get('type')!r}")
            failures += 1
        if item.get("optimization_risk") not in ALLOWED_RISKS:
            print(f"ERROR: claim {index} has invalid optimization_risk: {item.get('optimization_risk')!r}")
            failures += 1
        if item.get("status") not in ALLOWED_STATUSES:
            print(f"ERROR: claim {index} has invalid status: {item.get('status')!r}")
            failures += 1

    if failures:
        print(f"FAILED: {failures} ledger issue(s)")
        return 1

    print(f"PASS: {len(data)} claim(s) include provenance and incentive fields")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
