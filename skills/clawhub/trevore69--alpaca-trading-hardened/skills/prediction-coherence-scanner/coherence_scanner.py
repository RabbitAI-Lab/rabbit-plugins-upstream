#!/usr/bin/env python3
"""
Coherence scanner for mutually exclusive prediction market outcome groups.

Method
------
In a set of outcomes that is mutually exclusive and exhaustive (exactly one
resolves YES), the executable YES prices must sum to 1.00 at resolution. When
they sum to less than 1.00 net of costs, buying every leg pays 1.00 for less
than 1.00. That is a structural relationship, not a forecast.

The hard part is not the arithmetic. It is proving the leg set is complete.
An incomplete leg set looks exactly like a large arbitrage and is the single
most expensive mistake this strategy can make. See references/METHOD.md for
the measurements behind every gate in this file.

Defaults are conservative: dry-run unless --live, $10 per trade, 5 trades per
run. This is a template. The default signal is price coherence within an
event; remix the grouping and gating for your own venue and market family.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

SKILL_SLUG = "prediction-coherence-scanner"
TRADE_SOURCE = f"sdk:{SKILL_SLUG}"

# ---------------------------------------------------------------------------
# Gates. Every number here is justified in references/METHOD.md.
# ---------------------------------------------------------------------------

# A complete partition prices near 1.00. Observed complete groups sat in
# [0.9950, 1.0195]. A sum far BELOW 1.0 is overwhelmingly evidence of missing
# legs rather than free money, so we refuse to trade below this floor. This
# inversion (deeper apparent edge means more likely broken) is the core rule.
MIN_PLAUSIBLE_SUM = 0.90

# Above this, the group is almost certainly not a partition (unrelated props
# bundled under one event id summed to 5.44 in live data).
MAX_PLAUSIBLE_SUM = 1.25

# Required margin after costs before acting.
MIN_MARGIN = 0.01

# Risk bounds.
MAX_TRADE_USD = 10.0
MAX_TRADES_PER_RUN = 5
MIN_LEGS = 2
MAX_QUOTE_AGE_SECONDS = 120.0


@dataclass
class Decision:
    """Outcome of assessing one candidate outcome group."""

    event_id: Optional[str]
    event_name: Optional[str]
    action: str  # "BUY_ALL_LEGS" or "ABSTAIN"
    reason: str
    leg_count: int
    family: Optional[str] = None
    midpoint_sum: Optional[float] = None
    executable_sum: Optional[float] = None
    margin: Optional[float] = None
    legs: List[Dict[str, Any]] = field(default_factory=list)

    @property
    def tradeable(self) -> bool:
        return self.action == "BUY_ALL_LEGS"


# ---------------------------------------------------------------------------
# Pure logic. No network, no credentials, unit tested in tests/.
# ---------------------------------------------------------------------------


def group_by_event(markets: Iterable[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Bucket markets by event_id.

    An event id is a grouping hint only. It does NOT imply the legs are
    mutually exclusive, which is why detect_partition_family gates every
    group before any arithmetic is trusted.
    """
    groups: Dict[str, List[Dict[str, Any]]] = {}
    for m in markets:
        eid = m.get("event_id")
        if not eid:
            continue
        groups.setdefault(eid, []).append(m)
    return groups


def detect_partition_family(legs: Sequence[Dict[str, Any]]) -> Tuple[Optional[str], str]:
    """Identify structural evidence that legs form a real partition.

    Evidence must be STRUCTURAL, never derived from the price sum. Using the
    sum to decide a group is a partition and then trading the same sum as a
    signal is circular, and it is exactly how a broken group gets traded.

    Returns (family, evidence) where family is None when there is no evidence.
    """
    if len(legs) < MIN_LEGS:
        return None, "fewer than two legs"

    names = [str(l.get("event_name") or "") for l in legs]
    event_name = names[0] if names else ""
    lowered = event_name.lower()

    # Polymarket's negative-risk adapter enforces that exactly one outcome in
    # the event resolves YES. That is a venue-level guarantee, not a guess.
    if all(l.get("polymarket_neg_risk") for l in legs):
        return "neg_risk", "all legs carry polymarket_neg_risk=true"

    # Exact-score ladders enumerate disjoint scorelines.
    if "exact score" in lowered:
        return "exact_score", f"event_name indicates an exact-score ladder: {event_name!r}"

    # Explicit rejection of known non-partition bundles. "More Markets" mixes
    # over/unders, spreads and both-teams-to-score under one event id.
    if "more markets" in lowered:
        return None, f"event bundles unrelated props: {event_name!r}"

    return None, "no structural evidence that these legs are mutually exclusive"


def executable_price(leg: Dict[str, Any]) -> Optional[float]:
    """Price actually payable to buy one YES share.

    Midpoints are not tradeable. If the venue does not publish an ask, this
    returns None and the caller must abstain rather than substitute a
    midpoint, which would systematically understate cost.
    """
    ask = leg.get("best_ask")
    if ask is None:
        return None
    try:
        ask = float(ask)
    except (TypeError, ValueError):
        return None
    if not (0.0 < ask <= 1.0):
        return None
    return ask


def _quotes_are_fresh(legs: Sequence[Dict[str, Any]], max_age: float) -> Tuple[bool, str]:
    for l in legs:
        age = l.get("quote_age_seconds")
        if age is None:
            continue
        try:
            if float(age) > max_age:
                return False, f"stale quote: {float(age):.0f}s old (limit {max_age:.0f}s)"
        except (TypeError, ValueError):
            continue
    return True, ""


def fee_adjusted_cost(exec_sum: float, legs: Sequence[Dict[str, Any]]) -> float:
    """Add per-leg taker fees to the raw executable sum."""
    total = exec_sum
    for l in legs:
        bps = l.get("fee_rate_bps") or 0
        try:
            bps = float(bps)
        except (TypeError, ValueError):
            bps = 0.0
        price = executable_price(l) or 0.0
        total += price * (bps / 10_000.0)
    return total


def assess_group(
    legs: Sequence[Dict[str, Any]],
    *,
    window_truncated: bool = False,
    min_margin: float = MIN_MARGIN,
    min_plausible_sum: float = MIN_PLAUSIBLE_SUM,
    max_plausible_sum: float = MAX_PLAUSIBLE_SUM,
    max_quote_age: float = MAX_QUOTE_AGE_SECONDS,
) -> Decision:
    """Decide whether one outcome group is a coherent, tradeable dutch book.

    The order of gates matters. Completeness is checked before edge, because
    a group that fails completeness produces a large and entirely fake edge.
    """
    legs = list(legs)
    eid = legs[0].get("event_id") if legs else None
    ename = legs[0].get("event_name") if legs else None

    def abstain(reason: str, **kw: Any) -> Decision:
        return Decision(
            event_id=eid,
            event_name=ename,
            action="ABSTAIN",
            reason=reason,
            leg_count=len(legs),
            legs=legs,
            **kw,
        )

    if len(legs) < MIN_LEGS:
        return abstain("group has fewer than two legs")

    # Gate 1: structural proof of mutual exclusivity.
    family, evidence = detect_partition_family(legs)
    if family is None:
        return abstain(f"not a proven partition: {evidence}")

    # Gate 2: the discovery window must not have been capped. A truncated
    # window silently drops legs, and dropped legs manufacture fake edge.
    if window_truncated:
        return abstain(
            "discovery window was truncated, so the leg set cannot be proven complete",
            family=family,
        )

    midpoint_sum = 0.0
    for l in legs:
        try:
            midpoint_sum += float(l.get("current_probability") or 0.0)
        except (TypeError, ValueError):
            return abstain("leg has an unreadable probability", family=family)

    # Gate 3: completeness. This is the gate that matters most.
    if midpoint_sum < min_plausible_sum:
        return abstain(
            f"suspected missing legs: midpoint sum {midpoint_sum:.4f} is below "
            f"{min_plausible_sum:.2f}. A complete partition prices near 1.00, so this "
            f"is far more likely an incomplete leg set than a {1 - midpoint_sum:.0%} arbitrage",
            family=family,
            midpoint_sum=midpoint_sum,
        )
    if midpoint_sum > max_plausible_sum:
        return abstain(
            f"legs are not mutually exclusive: midpoint sum {midpoint_sum:.4f} exceeds "
            f"{max_plausible_sum:.2f}",
            family=family,
            midpoint_sum=midpoint_sum,
        )

    # Gate 4: quotes must be real, complete and fresh.
    prices = [executable_price(l) for l in legs]
    if any(p is None for p in prices):
        missing = sum(1 for p in prices if p is None)
        return abstain(
            f"no executable quote on {missing}/{len(legs)} legs; midpoints are not "
            "tradeable so cost cannot be established",
            family=family,
            midpoint_sum=midpoint_sum,
        )
    fresh, why = _quotes_are_fresh(legs, max_quote_age)
    if not fresh:
        return abstain(why, family=family, midpoint_sum=midpoint_sum)

    # Gate 5: edge must survive real execution cost.
    exec_sum = fee_adjusted_cost(sum(p for p in prices if p is not None), legs)
    margin = 1.0 - exec_sum
    if margin < min_margin:
        return abstain(
            f"no edge after costs: buying all legs costs {exec_sum:.4f} for a 1.00 "
            f"payout, margin {margin:+.4f} is below the {min_margin:.4f} minimum",
            family=family,
            midpoint_sum=midpoint_sum,
            executable_sum=exec_sum,
            margin=margin,
        )

    return Decision(
        event_id=eid,
        event_name=ename,
        action="BUY_ALL_LEGS",
        reason=(
            f"{family} partition of {len(legs)} legs costs {exec_sum:.4f} at the ask "
            f"for a guaranteed 1.00 payout, locking {margin:+.4f} per set ({evidence})"
        ),
        leg_count=len(legs),
        family=family,
        midpoint_sum=midpoint_sum,
        executable_sum=exec_sum,
        margin=margin,
        legs=legs,
    )


def scan(
    markets: Iterable[Dict[str, Any]],
    *,
    window_truncated: bool = False,
    **kw: Any,
) -> List[Decision]:
    """Assess every event group found in markets, best margin first."""
    margin_floor = kw.get("min_margin", MIN_MARGIN)
    if margin_floor < 0:
        raise ValueError(
            f"min_margin={margin_floor:+.4f} is negative, which would buy sets that cost "
            f"more than their 1.00 payout. That is a guaranteed {-margin_floor:.2%} loss "
            "per set, not an edge. The floor must be >= 0."
        )
    out = [
        assess_group(legs, window_truncated=window_truncated, **kw)
        for legs in group_by_event(markets).values()
    ]
    out.sort(key=lambda d: (not d.tradeable, -(d.margin or -1)))
    return out


# ---------------------------------------------------------------------------
# Network layer.
# ---------------------------------------------------------------------------


def get_client(live: bool = False, venue: str = "sim"):
    from simmer_sdk import SimmerClient  # imported lazily so tests need no SDK

    key = os.environ.get("SIMMER_API_KEY")
    if not key:
        raise SystemExit("SIMMER_API_KEY is not set. Get one at simmer.markets/dashboard")
    return SimmerClient(api_key=key, venue=venue, live=live)


def fetch_event_legs(client, query: str, limit: int = 200) -> Tuple[List[Dict[str, Any]], bool]:
    """Fetch candidate legs with a filtered query.

    Filtered queries are applied server side before the result cap, so they
    reach the whole catalogue. An unfiltered browse is capped and will drop
    legs, which is why this function requires a query.
    """
    if not query or not query.strip():
        raise ValueError("a query is required; unfiltered discovery is capped and drops legs")

    raw = client._request("GET", "/api/sdk/markets", params={"q": query, "limit": limit})
    markets = raw.get("markets", [])
    truncated = bool(raw.get("truncated") or raw.get("capped_at_limit"))
    return markets, truncated


def execute(client, decision: Decision, *, live: bool, stake: float) -> List[Dict[str, Any]]:
    """Buy every leg of a confirmed coherent set.

    Partial fills break the guarantee: owning some legs of a dutch book is an
    open directional bet, not an arbitrage. Any leg failure is reported so the
    operator can unwind deliberately.
    """
    results: List[Dict[str, Any]] = []
    per_leg = min(stake, MAX_TRADE_USD) / max(len(decision.legs), 1)

    for leg in decision.legs:
        if not live:
            results.append(
                {"market_id": leg["id"], "simulated": True, "amount": round(per_leg, 4)}
            )
            continue
        res = client.trade(
            market_id=leg["id"],
            side="yes",
            amount=round(per_leg, 4),
            order_type="limit",
            price=executable_price(leg),
            source=TRADE_SOURCE,
            skill_slug=SKILL_SLUG,
            reasoning=decision.reason[:280],
        )
        results.append(
            {
                "market_id": leg["id"],
                "success": res.success,
                "fill_status": res.fill_status,
                "cost": res.cost,
                "error": res.error,
            }
        )
        if not res.success:
            results.append(
                {
                    "warning": "leg failed; the set is no longer a complete dutch book. "
                    "Review open exposure before rerunning."
                }
            )
            break
    return results


def non_negative_margin(raw: str) -> float:
    """Reject a negative margin floor before it can arm a known-losing buy."""
    try:
        v = float(raw)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{raw!r} is not a number")
    if v < 0:
        raise argparse.ArgumentTypeError(
            f"{v:+.4f} is negative. A set costing more than 1.00 pays back exactly 1.00, "
            f"so this would lock in a {-v:.2%} loss per set on purpose. Use 0 to act on "
            "any non-negative edge, or omit the flag for the 0.01 default."
        )
    return v


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Scan for coherent dutch books in outcome groups")
    p.add_argument("--query", required=True, help="Market search query, for example 'Golden Boot'")
    p.add_argument("--live", action="store_true", help="Place real orders (default: dry run)")
    p.add_argument("--venue", default="sim", choices=["sim", "polymarket", "kalshi"])
    p.add_argument("--stake", type=float, default=MAX_TRADE_USD, help=f"Total per set (cap {MAX_TRADE_USD})")
    p.add_argument("--min-margin", type=non_negative_margin, default=MIN_MARGIN,
                   help=f"Minimum edge after costs before acting (default {MIN_MARGIN}). "
                        "Must be >= 0; a negative floor buys guaranteed losses.")
    p.add_argument("--json", action="store_true", help="Emit JSON")
    p.add_argument("--show-abstains", action="store_true", help="Print groups that were rejected")
    args = p.parse_args(argv)

    client = get_client(live=args.live, venue=args.venue)
    markets, truncated = fetch_event_legs(client, args.query)
    decisions = scan(markets, window_truncated=truncated, min_margin=args.min_margin)

    tradeable = [d for d in decisions if d.tradeable][:MAX_TRADES_PER_RUN]

    if args.json:
        print(json.dumps({
            "query": args.query,
            "window_truncated": truncated,
            "groups_examined": len(decisions),
            "tradeable": [asdict(d) for d in tradeable],
            "abstained": [asdict(d) for d in decisions if not d.tradeable],
        }, indent=2, default=str))
    else:
        mode = "LIVE" if args.live else "DRY RUN"
        print(f"[{mode}] query={args.query!r} venue={args.venue}")
        print(f"groups examined: {len(decisions)}  truncated_window: {truncated}")
        if truncated:
            print("  ! window truncated: leg sets cannot be proven complete, all groups abstain")
        for d in decisions:
            if d.tradeable:
                print(f"\n  TRADE  {d.event_name} [{d.family}, {d.leg_count} legs]")
                print(f"         {d.reason}")
            elif args.show_abstains:
                print(f"\n  abstain  {d.event_name or d.event_id} [{d.leg_count} legs]")
                print(f"           {d.reason}")
        if not tradeable:
            print("\nNo coherent dutch book found. Abstaining is the expected outcome.")

    for d in tradeable:
        for r in execute(client, d, live=args.live, stake=args.stake):
            print(f"    {r}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
