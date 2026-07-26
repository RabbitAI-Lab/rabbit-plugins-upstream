#!/usr/bin/env python3
"""Report what this skill has done, per venue. Read only, places no orders."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from coherence_scanner import SKILL_SLUG, TRADE_SOURCE, get_client  # noqa: E402


def main() -> int:
    venue = os.environ.get("TRADING_VENUE", "sim")
    client = get_client(live=False, venue=venue)

    briefing = client.get_briefing()
    print(f"Venue balances (skill: {SKILL_SLUG})")
    for name, v in (briefing.get("venues") or {}).items():
        if not isinstance(v, dict):
            continue
        print(
            f"  {name:12s} balance={v.get('balance')} pnl={v.get('pnl')} "
            f"positions={v.get('positions_count')}"
        )

    # Pass venue explicitly so a stale paper position is not mistaken for real
    # exposure.
    positions = client.get_positions(venue=venue, source=TRADE_SOURCE)
    print(f"\nOpen positions from this skill on {venue}: {len(positions)}")
    for p in positions:
        print(f"  {p.question[:58]:60s} pnl={p.pnl:+.2f}")

    outcomes = client.get_outcomes(skill_slug=SKILL_SLUG)
    if outcomes:
        print(f"\nResolved outcomes: {outcomes}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
