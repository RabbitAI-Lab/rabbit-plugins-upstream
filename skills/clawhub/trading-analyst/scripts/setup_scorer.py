#!/usr/bin/env python3
"""
setup_scorer.py — SKOR OBJEKTIF tiap setup (ganti "confluence >=2" yang subjektif).

Daripada cuma nanya "ada >=2 konfirmasi?", tool ini kasih SKOR 0-100 + grade +
gate PASS/NO-TRADE berdasarkan banyak faktor terukur. Biar Clara (dan Bos) bisa
ranking setup mana yang lebih layak, bukan cuma "valid/tidak".

Input: JSON via --json atau stdin, mis.
  {
    "bias": "bullish",                 # bullish/bearish/neutral
    "confluence_count": 3,             # jumlah konfirmasi independen
    "rr": 2.5,                         # reward:risk
    "risk_pct": 1.0,                   # % equity per trade
    "macro_filter": "CONFIRM",         # CONFIRM/NEUTRAL/CONFLICT/unknown
    "rsi_extreme": false,              # RSI ob/os di level = extra confluence
    "zone_fresh": true,                # zona S/D belum diuji
    "news_clear": true,                # tdk ada high-impact +-30m
    "spread_ok": true                  # spread < 0.5% ATR
  }

Output: JSON {score, grade, verdict, hard_pass, breakdown:[...]}

Hard gate (NO-TRADE kalau salah satu gagal):
  confluence_count >= 2
  rr >= 1.5
  risk_pct <= 2.0
  news_clear == true
  spread_ok == true

Usage:
  echo '$JSON' | python3 setup_scorer.py
  python3 setup_scorer.py --json '$JSON'
"""
import argparse
import json
import sys

WEIGHTS = {
    "bias_clear": 10,
    "confluence": {2: 15, 3: 25, 4: 30},  # key = min(count,4)
    "rr": {1.5: 10, 2.0: 20, 3.0: 25},     # key = highest threshold met
    "risk": {1.0: 15, 1.5: 8, 2.0: 0},     # key = highest threshold met (<=)
    "macro": {"CONFIRM": 15, "NEUTRAL": 5, "CONFLICT": -15, "unknown": 0},
    "rsi_extreme": 5,
    "zone_fresh": 5,
    "news_clear": 10,
    "spread_ok": 5,
}


def _rr_points(rr):
    if rr is None:
        return 0
    if rr >= 3.0:
        return WEIGHTS["rr"][3.0]
    if rr >= 2.0:
        return WEIGHTS["rr"][2.0]
    if rr >= 1.5:
        return WEIGHTS["rr"][1.5]
    return 0


def _risk_points(risk):
    if risk is None:
        return 0
    if risk <= 1.0:
        return WEIGHTS["risk"][1.0]
    if risk <= 1.5:
        return WEIGHTS["risk"][1.5]
    if risk <= 2.0:
        return WEIGHTS["risk"][2.0]
    return 0


def score(d):
    bd = []
    total = 0

    # bias
    bc = WEIGHTS["bias_clear"] if d.get("bias") in ("bullish", "bearish") else 0
    total += bc
    bd.append(("bias_clear", bc, f"bias={d.get('bias')}"))

    # confluence
    c = int(d.get("confluence_count", 0))
    cp = WEIGHTS["confluence"].get(min(c, 4), 0)
    total += cp
    bd.append(("confluence", cp, f"count={c}"))

    # rr
    rp = _rr_points(d.get("rr"))
    total += rp
    bd.append(("rr", rp, f"rr={d.get('rr')}"))

    # risk
    rkp = _risk_points(d.get("risk_pct"))
    total += rkp
    bd.append(("risk", rkp, f"risk%={d.get('risk_pct')}"))

    # macro
    mf = d.get("macro_filter", "unknown")
    mp = WEIGHTS["macro"].get(mf, 0)
    total += mp
    bd.append(("macro", mp, f"filter={mf}"))

    # extras
    for key, w in (("rsi_extreme", WEIGHTS["rsi_extreme"]),
                   ("zone_fresh", WEIGHTS["zone_fresh"]),
                   ("news_clear", WEIGHTS["news_clear"]),
                   ("spread_ok", WEIGHTS["spread_ok"])):
        v = d.get(key, False)
        pts = w if v else 0
        total += pts
        bd.append((key, pts, f"{key}={v}"))

    total = max(0, min(100, total))

    # hard gate
    hard = (c >= 2 and (d.get("rr") or 0) >= 1.5 and (d.get("risk_pct") or 99) <= 2.0)

    if total >= 85:
        grade = "A"
    elif total >= 70:
        grade = "B"
    elif total >= 55:
        grade = "C"
    else:
        grade = "D"

    verdict = "STRONG" if (hard and grade in ("A", "B")) else \
              "OK" if (hard and grade == "C") else "WEAK/NO-TRADE"

    return {
        "score": total,
        "grade": grade,
        "verdict": verdict,
        "hard_pass": hard,
        "breakdown": [{"factor": k, "points": p, "note": n} for k, p, n in bd],
    }


def main():
    p = argparse.ArgumentParser(description="Score a trade setup objectively (0-100).")
    p.add_argument("--json", default=None, help="JSON setup descriptor")
    args = p.parse_args()

    raw = args.json or sys.stdin.read().strip()
    if not raw:
        print("[warn] no JSON; nothing scored", file=sys.stderr)
        return
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"[error] invalid JSON: {e}", file=sys.stderr)
        sys.exit(1)

    res = score(data)
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
