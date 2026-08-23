#!/usr/bin/env python3
"""
log_titik.py — Clara's AUTO-JOURNAL for XAU/USD analysis with concrete levels.

When an analysis produces "titik" (entry/SL/TP points), Clara logs it WITHOUT
being asked. This keeps a persistent, queryable history across sessions.

Appends one JSON line per call to memory/trading/analysis_log.jsonl and keeps a
human-readable memory/trading/analysis_log.md in sync.

Input: a JSON blob via --json or stdin, e.g.
  {
    "price": 4520.20,
    "bias": "Bullish di resistance",
    "note": "analisa harian no-screenshot",
    "levels": [
      {"type":"BUY_STOP","entry":4550,"sl":4500,"tp":4730,"rr":3.6,"note":"breakout >4545"},
      {"type":"BUY_LIMIT","entry":4400,"sl":4345,"tp":4545,"rr":2.6,"note":"pullback support"}
    ]
  }

Usage:
  echo '$JSON' | python3 log_titik.py
  python3 log_titik.py --json '$JSON'

No network, no destructive ops. Only appends to the log.
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone

LOG_DIR = os.path.join(
    os.path.dirname(  # workspace/memory/trading  (from skills/<name>/scripts/)
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )
        )
    ),
    "memory", "trading"
)
JSONL = os.path.join(LOG_DIR, "analysis_log.jsonl")
MD = os.path.join(LOG_DIR, "analysis_log.md")


def main():
    p = argparse.ArgumentParser(description="Auto-journal XAU analysis levels (titik).")
    p.add_argument("--json", default=None, help="JSON string with price/bias/levels")
    args = p.parse_args()

    raw = args.json
    if raw is None:
        raw = sys.stdin.read().strip()
    if not raw:
        print("[warn] no JSON input; nothing logged", file=sys.stderr)
        return

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"[error] invalid JSON: {e}", file=sys.stderr)
        sys.exit(1)

    levels = data.get("levels", [])
    if not levels:
        print("[info] no levels (titik) — not logging. Analysis had no concrete points.",
              file=sys.stderr)
        return

    entry = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "price": data.get("price"),
        "bias": data.get("bias", ""),
        "note": data.get("note", ""),
        "levels": levels,
    }

    os.makedirs(LOG_DIR, exist_ok=True)
    with open(JSONL, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

    # append human-readable
    with open(MD, "a", encoding="utf-8") as f:
        f.write(f"\n## {entry['ts']}  (price {entry['price']})\n")
        f.write(f"Bias: {entry['bias']}\n")
        if entry["note"]:
            f.write(f"Note: {entry['note']}\n")
        for lv in levels:
            f.write(
                f"- {lv.get('type','?')} @ {lv.get('entry')} | SL {lv.get('sl')} | "
                f"TP {lv.get('tp')} | R:R {lv.get('rr')} | {lv.get('note','')}\n"
            )

    print(f"[ok] logged {len(levels)} titik to {JSONL}", file=sys.stderr)


if __name__ == "__main__":
    main()
