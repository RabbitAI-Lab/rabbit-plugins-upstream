#!/usr/bin/env python3
"""Fetch and print Coil's free daily market board (public, no key, no account).

Source: https://coil.trade/api/board/free — the free tier of the Coil Scanner board.
Standard library only. Read-only: this fetches and prints, it never trades.

Impersonal research publication, decision support only — not investment advice.

    python3 scripts/coil_board.py            # today's board
    python3 scripts/coil_board.py --record   # also print the engine's published record
"""
import json
import sys
import urllib.error
import urllib.request

BASE = "https://coil.trade"
UA = "coil-board-skill/1.1 (+https://github.com/joeyfife/coil-board-skill)"
BOOK_ORDER = ["spx", "qqq", "macro", "crypto"]
BOOK_LABEL = {"spx": "S&P 500", "qqq": "Nasdaq-100", "macro": "Macro", "crypto": "Crypto"}


def get(path):
    req = urllib.request.Request(BASE + path, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read())
    except urllib.error.URLError as e:
        print(f"could not reach {BASE}{path}: {getattr(e, 'reason', e)}")
        sys.exit(1)


def print_board():
    d = get("/api/board/free")
    asof = d.get("asof") or d.get("asof_daily") or "?"
    print(f"COIL BOARD — as published {asof}"
          + (" (free tier: one market day delayed)" if d.get("delayed") else ""))
    for key in BOOK_ORDER:
        bk = (d.get("books") or {}).get(key)
        if not bk:
            continue
        print(f"\n{BOOK_LABEL.get(key, key).upper()}  [{bk.get('regime_mode', '?')}]")
        verdict = bk.get("regime_verdict") or ""
        if verdict:
            # regime verdicts are prose; wrap them so a terminal read stays legible
            words, line = verdict.split(), ""
            for w in words:
                if len(line) + len(w) + 1 > 88:
                    print(f"  {line}")
                    line = w
                else:
                    line = f"{line} {w}".strip()
            if line:
                print(f"  {line}")
        for n in (bk.get("top3") or []):
            opp = n.get("opp", n.get("opp_pct", "?"))
            print(f"    {n.get('sym', '?'):9s} opp {str(opp):>3s}  {n.get('state', '?'):8s}"
                  f"  {(n.get('sector') or '')[:28]}")
    print("\nScores and states only — never stop or target prices, never individualized advice.")
    print("Markets can lose money. Past scores do not predict future results.")


def print_record():
    """The publisher's own record, free and unauthenticated. Read it before trusting scores."""
    p = get("/api/perf")
    h = (p.get("perf") or {}).get("headline")
    print("\nENGINE RECORD (free, /api/perf)")
    if not h:
        print("  not published right now — omitted rather than estimated")
        return
    print(f"  since inception: engine {h.get('engine_return_pct'):+.2f}%"
          f" · SPY {h.get('spy_return_pct'):+.2f}%"
          f" · QQQ {h.get('qqq_return_pct'):+.2f}%")
    note = (p.get("perf") or {}).get("note")
    if note:
        print(f"  {note}")
    print("  commitments (tamper-evidence): https://coil.trade/api/board/proof")


if __name__ == "__main__":
    print_board()
    if "--record" in sys.argv[1:]:
        print_record()
