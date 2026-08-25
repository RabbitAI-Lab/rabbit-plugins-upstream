#!/usr/bin/env python3
"""coding-2: lightweight convention checker for the live-dashboard pattern.

This skill builds dynamic HTML dashboards backed by a data API where each chart
must independently call the API and poll every 60s. This linter checks an
HTML/JS file for those specific conventions. Advisory only; no network, no writes.

Usage:
    python3 style_lint.py dashboard.html
    python3 style_lint.py app.js
    python3 style_lint.py dashboard.html --require-poll 60000

Checks:
  - presence of a fetch/XHR call
  - each chart uses its own fetch (heuristic: >=1 fetch per chart block)
  - a 60s (60000ms) polling interval (setInterval / setTimeout)
  - guards for code !== 0 before rendering
  - no hardcoded '$SESSION_GROUP_ID$' / '${...}' placeholder strings
"""
import argparse
import re
import sys


def lint(text, require_poll_ms=60000):
    issues = []
    # network call present
    if not re.search(r"fetch\s*\(|XMLHttpRequest|\.open\s*\(\s*[\"']POST", text):
        issues.append("no fetch/XHR/POST call detected")
    # independent fetch per chart (heuristic: more than one fetch)
    fetches = len(re.findall(r"fetch\s*\(", text))
    if fetches < 2:
        issues.append(f"only {fetches} fetch() found (each chart should fetch independently)")
    # polling interval
    intervals = [int(m) for m in re.findall(r"set(?:Interval|Timeout)\s*\([^,]+,\s*(\d+)", text)]
    if not intervals:
        issues.append("no setInterval/setTimeout polling found")
    elif require_poll_ms not in intervals:
        issues.append(f"poll interval {require_poll_ms}ms not found (found: {intervals})")
    # code guard
    if not re.search(r"code\s*!==?\s*0|result\s*\.?\s*data", text):
        issues.append("no guard for code !== 0 / result.data before render")
    # leftover placeholders (should be substituted before deploy)
    for ph in [r"<SESSION_GROUP_ID>", r"<nama_tabel>", r"API_BASE_URL"]:
        if re.search(re.escape(ph), text):
            issues.append(f"placeholder not substituted before deploy: {ph}")
    return issues


def main():
    p = argparse.ArgumentParser(description="coding-2 dashboard convention checker")
    p.add_argument("path", help="html or js file to lint")
    p.add_argument("--require-poll", type=int, default=60000, help="expected poll ms (default 60000)")
    args = p.parse_args()
    try:
        with open(args.path, encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        print(f"[style_lint] cannot read {args.path}: {e}", file=sys.stderr)
        return 2
    issues = lint(text, args.require_poll)
    if not issues:
        print(f"[style_lint] {args.path}: OK (dashboard conventions satisfied)")
        return 0
    print(f"[style_lint] {args.path}: {len(issues)} issue(s)")
    for it in issues:
        print(f"  - {it}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
