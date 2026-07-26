"""Value-betting core: de-vig, edge, EV, Kelly.

These implement the formulas documented in the `betting` skill's
api-reference.md, self-contained (no external dependency) so they are fully
testable and auditable.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass
class ValueBet:
    """A single bet with a positive edge vs the market."""

    market: str  # e.g. "1X2-H", "OU2.5-over"
    outcome: str  # human label of the side backed
    pred_prob: float  # model's estimated true probability
    odds: float  # decimal odds available
    implied_prob: float  # 1 / odds, the break-even probability
    edge: float  # pred_prob - implied_prob
    ev: float  # expected value per unit staked
    kelly: float  # full-Kelly fraction of bankroll

    def __post_init__(self) -> None:
        # Kelly f* = (p - q/b) where b = odds-1, q = 1-p.
        # Equivalent form used by the betting skill:
        #   f* = (pred_prob - implied_prob) / (1 - implied_prob)
        if self.implied_prob >= 1:
            object.__setattr__(self, "kelly", 0.0)
        else:
            object.__setattr__(self, "kelly", (self.pred_prob - self.implied_prob) / (1 - self.implied_prob))


def devig(odds_1x2: Sequence[float]) -> tuple[float, float, float]:
    """Remove the bookmaker margin from 1X2 decimal odds → fair probabilities.

    Example: (2.1, 3.4, 3.6) → implied (0.476, 0.294, 0.278) summing to 1.048
    (4.8% vig); de-vigged to (0.454, 0.280, 0.265).
    """
    implied = [1.0 / o for o in odds_1x2]
    overround = sum(implied)
    return tuple(p / overround for p in implied)  # type: ignore[return-value]


def evaluate(
    market: str, outcome: str, pred_prob: float, odds: float
) -> ValueBet:
    """Edge, EV, and Kelly for backing `outcome` at `odds` with belief `pred_prob`.

    EV = pred_prob * (odds - 1) - (1 - pred_prob) = pred_prob * odds - 1.
    """
    if odds <= 1.0:
        raise ValueError(f"odds must be > 1.0, got {odds}")
    implied = 1.0 / odds
    edge = pred_prob - implied
    ev = pred_prob * odds - 1.0
    return ValueBet(
        market=market,
        outcome=outcome,
        pred_prob=pred_prob,
        odds=odds,
        implied_prob=implied,
        edge=edge,
        ev=ev,
        kelly=0.0,  # filled by __post_init__
    )


def kelly_fraction(edge: float, implied_prob: float, fraction: float = 0.25) -> float:
    """Stake as a fraction of bankroll, using a fractional Kelly (default quarter).

    Academic consensus: Full Kelly = 100% ruin. 25% Kelly is conservative,
    50% for higher risk tolerance. Default 25%.
    """
    full = edge / (1 - implied_prob) if implied_prob < 1 else 0.0
    return max(0.0, full * fraction)
