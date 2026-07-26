#!/usr/bin/env python3
"""Read-only portfolio/status viewer for MLB Live Trader.

This command is deliberately inert: it never places, cancels, or redeems an
order, and it never runs a preflight. It reads Simmer positions/portfolio plus
the skill's local idempotency state and prints them as JSON.

Identity constants and the state-file location are imported from the
``mlb_live_trader`` monofile rather than re-declared here. A divergent
``TRADE_SOURCE`` would silently filter out real positions and under-report
exposure, so there is exactly one definition of it.

Credentials are read by the Simmer SDK from the environment; this script never
reads, stores, or prints them.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any, Mapping

from simmer_sdk import SimmerClient

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from mlb_live_trader import (  # noqa: E402  (path set up immediately above)
    SKILL_SLUG,
    TRADE_SOURCE,
    VENUE,
    _STATE_PATH,
)

STATE_PATH = _STATE_PATH


def _json_default(value: Any) -> Any:
    return asdict(value) if is_dataclass(value) else str(value)


def _local_state() -> Mapping[str, Any]:
    try:
        value = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def main() -> int:
    parser = argparse.ArgumentParser(description="Show MLB Live Trader status")
    parser.add_argument("--live", action="store_true", help="inspect real Polymarket mode")
    parser.add_argument("--starting-balance", type=float, default=1000.0)
    args = parser.parse_args()
    client = SimmerClient.from_env(
        venue=VENUE,
        live=args.live,
        starting_balance=args.starting_balance,
    )
    positions = []
    for position in client.get_positions(venue=VENUE, source=TRADE_SOURCE):
        if is_dataclass(position):
            positions.append(asdict(position))
        elif isinstance(position, Mapping):
            positions.append(dict(position))
    payload = {
        "skill": SKILL_SLUG,
        "source": TRADE_SOURCE,
        "mode": "live" if args.live else "dry/paper",
        "positions": positions,
        "local_state": _local_state(),
        "portfolio": client.get_portfolio(venue=VENUE) if args.live else None,
        "paper_summary": client.get_paper_summary() if not args.live else None,
    }
    print(json.dumps(payload, indent=2, default=_json_default))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
