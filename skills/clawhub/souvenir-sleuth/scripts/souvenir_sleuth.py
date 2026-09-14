#!/usr/bin/env python3
"""Souvenir Sleuth — find authentic local souvenirs, dodge tourist traps.

Given a destination, produces a dossier of genuinely local specialties with
fair price ranges, where locals buy them, authenticity tells, customs flags,
and what to avoid. Offline knowledge base (13 destinations); the agent layer
enriches with live web research.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

KB_PATH = Path(__file__).parent / "souvenir_kb.json"

ALIASES = {
    "nola": "neworleans", "new orleans": "neworleans",
    "cdmx": "mexicocity", "mexico city": "mexicocity", "df": "mexicocity",
    "fès": "fez", "fes": "fez", "fez, morocco": "fez",
    "marrakesh": "marrakech",
    "kyoto, japan": "kyoto", "kyōto": "kyoto",
    "chiang mai": "chiangmai", "chiangmai, thailand": "chiangmai",
    "cuzco": "cusco", "cusco, peru": "cusco", "machu picchu": "cusco",
    "cape town": "capetown", "kaapstad": "capetown",
    "praha": "prague", "prague, czechia": "prague",
    "firenze": "florence", "istanbul, turkey": "istanbul",
    "lisboa": "lisbon", "lisbon, portugal": "lisbon",
    "oaxaca de juárez": "oaxaca", "oaxaca, mexico": "oaxaca",
    "ha noi": "hanoi", "hà nội": "hanoi",
}

CUSTOMS_LABEL = {
    "green": "🟢 generally fine",
    "yellow": "🟡 declare / check liquids & quantity",
    "orange": "🟠 often restricted",
    "red": "🔴 prohibited / CITES",
}

TRAP_MARKERS = [
    "snow globe", "fridge magnet", "keychain", "key chain", "t-shirt",
    "shot glass", "mug", "miniature", "souvenir spoon", "logo", "statuette",
    "mini tower", "mini building",
]


def normalize(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())


def match_destination(query: str, kb: dict) -> tuple[str, dict] | None:
    q = normalize(query)
    if q in ALIASES:
        q = ALIASES[q]
    q_key = q.replace(" ", "").replace("-", "")
    if q_key in kb:
        return q_key, kb[q_key]
    # city name embedded in the card's display name ("Kyoto" in "Kyoto, Japan")
    for key, card in kb.items():
        city_first = card["name"].split(",")[0].strip().lower()
        if q == city_first or q_key == city_first.replace(" ", ""):
            return key, card
    # fuzzy: token-level match against any name part (word boundaries only)
    words = set(w for w in re.split(r"[^a-zà-ÿ]+", q) if len(w) >= 4)
    for key, card in kb.items():
        tokens = set(re.split(r"[^a-zà-ÿ]+", normalize(card["name"] + " " + key)))
        tokens = {t for t in tokens if len(t) >= 4}
        if words & tokens:
            return key, card
    return None


def trap_probability(item: str) -> tuple[float, str]:
    """Heuristic trap score for an arbitrary souvenir item, 0-1."""
    it = normalize(item)
    score, hits = 0.0, []
    for m in TRAP_MARKERS:
        if m in it:
            score += 0.5
            hits.append(m)
    if "replica" in it or "mini" in it:
        score += 0.2
        hits.append("replica/mini")
    if re.search(r"(big ben|eiffel|colosseum|pisa|sagrada)", it) and score > 0:
        score += 0.1
    return min(score, 1.0), ", ".join(hits)


def render(destination: dict, budget: float | None, item: str | None) -> str:
    out = []
    a = out.append
    cur = destination["currency"]
    hag = destination["haggling_index"]
    a("=" * 64)
    a(f" SOUVENIR DOSSIER — {destination['name']}")
    a("=" * 64)
    a(f" Currency: {cur}   Haggling index: {'●' * hag}{'○' * (5 - hag)} "
      f"({'fixed prices' if hag <= 1 else 'sticker price is theater' if hag >= 4 else 'polite negotiation'})")
    a("")

    if item:
        p, hits = trap_probability(item)
        verdict = ("TOURIST TRAP 🔴" if p >= 0.5 else
                   "borderline 🟡" if p >= 0.25 else "probably fine 🟢")
        a(f" TRAP CHECK: '{item}'")
        a(f"   probability: {p:.0%}  ({hits or 'no trap markers'})")
        a(f"   verdict: {verdict}")
        a("   → compare with the authentic alternatives below")
        a("")

    a(" AUTHENTIC SPECIALTIES")
    for s in destination["specialties"]:
        lo, hi = s["local_price"]
        if budget is not None and lo > budget:
            continue
        price = f"{lo:,.0f}–{hi:,.0f} {cur}"
        if budget is not None:
            price += f"  (filter ≤ {budget:,.0f})"
        a(f"\n  ▸ {s['item']}  [{s['category']}]")
        a(f"     {s['desc']}")
        a(f"     Fair price : {price}")
        a(f"     Buy at     : {'; '.join(s['buy_zones'])}")
        a(f"     Real tell  : {s['authenticity']}")
        a(f"     Customs    : {CUSTOMS_LABEL.get(s['customs'], s['customs'])}"
          f"   |  Weight: {s['weight_note']}")

    a("")
    a(" AVOID")
    for av in destination.get("avoid", []):
        a(f"  ✗ {av['item']} — {av['why']}")

    a("")
    a(" NEXT STEP (agent): enrich top picks with current shop names, hours,")
    a(" and seasonal availability via web search before shopping day.")
    a("=" * 64)
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Authentic local souvenir finder (offline knowledge base).")
    ap.add_argument("--destination", "-d", help="city/region to shop in")
    ap.add_argument("--item", help="check if a specific item is a tourist trap")
    ap.add_argument("--budget", type=float,
                    help="max fair price in local currency")
    ap.add_argument("--list", action="store_true",
                    help="list all destinations in the knowledge base")
    ap.add_argument("--json", type=Path, help="write dossier as JSON")
    args = ap.parse_args()

    kb = json.loads(KB_PATH.read_text(encoding="utf-8"))

    if args.list:
        print("Destinations in knowledge base:")
        for key, card in sorted(kb.items()):
            print(f"  {card['name']:<28} {len(card['specialties'])} specialties")
        return 0

    if not args.destination:
        ap.error("provide --destination (or --list)")
        return 2

    m = match_destination(args.destination, kb)
    if not m:
        print(f"Destination '{args.destination}' not in the offline knowledge "
              "base.\nRun with --list to see coverage, then have the agent "
              "research it live.", file=sys.stderr)
        return 1
    key, card = m

    text = render(card, args.budget, args.item)
    print(text)

    if args.json:
        payload = {"key": key, "name": card["name"], "currency": card["currency"],
                   "haggling_index": card["haggling_index"],
                   "specialties": card["specialties"], "avoid": card.get("avoid", [])}
        if args.item:
            p, hits = trap_probability(args.item)
            payload["trap_check"] = {"item": args.item,
                                     "probability": round(p, 2), "markers": hits}
        if args.budget is not None:
            payload["specialties"] = [
                s for s in payload["specialties"]
                if s["local_price"][0] <= args.budget]
        args.json.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
        print(f"\nJSON dossier → {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
