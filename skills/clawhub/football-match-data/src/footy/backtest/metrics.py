"""Evaluation metrics for probabilistic football predictions.

These metrics let us judge a model honestly — none of them is "accuracy",
because beating 80% accuracy in football betting is impossible and
misleading. Instead we measure calibration (RPS), value (ROI/CLV), and
skill (vs a naive baseline).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence

import numpy as np


def rps(prob_h: float, prob_d: float, prob_a: float, actual: str) -> float:
    """Ranked Probability Score for a 1X2 prediction.

    Lower is better. Penalises predictions that put mass far from the true
    outcome while respecting the ordinal structure (H > D > A). A model that
    always predicts 1/3 each scores ~0.222 on average; a perfect model scores 0.
    """
    cum_pred = np.cumsum([prob_h, prob_d, prob_a])
    cum_actual = np.cumsum([1.0 if actual == o else 0.0 for o in ("H", "D", "A")])
    return float(np.sum((cum_pred - cum_actual) ** 2) / (3 - 1))


@dataclass
class BetRecord:
    """One settled flat-stake (1 unit) bet."""

    date: str
    home: str
    away: str
    market: str  # e.g. "1X2-H", "OU2.5-over"
    outcome: str  # the side we backed
    pred_prob: float
    odds: float
    actual_hit: bool
    edge: float  # pred_prob - implied_prob

    @property
    def pnl(self) -> float:
        return (self.odds - 1.0) if self.actual_hit else -1.0


@dataclass
class BacktestReport:
    n_bets: int = 0
    n_hits: int = 0
    total_pnl: float = 0.0
    stake: float = 0.0
    avg_rps: float = 0.0
    avg_clv: float = 0.0
    by_edge_bucket: dict[str, dict] = field(default_factory=dict)
    # Reference RPS values for honest skill comparison.
    rps_naive: float = 0.0  # always predict 1/3 each
    rps_market: float = float("nan")  # Pinnacle implied probabilities
    n_predicted: int = 0

    @property
    def roi(self) -> float:
        return self.total_pnl / self.stake if self.stake else 0.0

    @property
    def hit_rate(self) -> float:
        return self.n_hits / self.n_bets if self.n_bets else 0.0

    def summary_lines(self) -> list[str]:
        clv = "n/a (needs open odds)" if np.isnan(self.avg_clv) else f"{self.avg_clv:+.2%}"
        mkt = "n/a" if np.isnan(self.rps_market) else f"{self.rps_market:.4f}"
        # Skill score: how much of the gap between naive and market the model closes.
        return [
            f"Matches predicted: {self.n_predicted}",
            f"Bets placed      : {self.n_bets}",
            f"Hit rate         : {self.hit_rate:.1%}",
            f"Total PnL        : {self.total_pnl:+.2f} units (flat 1u)",
            f"ROI              : {self.roi:+.2%}",
            f"RPS (model)      : {self.avg_rps:.4f}",
            f"RPS (market)     : {mkt}",
            f"RPS (naive 1/3)  : {self.rps_naive:.4f}",
            f"Avg CLV          : {clv}  (positive = beat closing line)",
        ]


def aggregate(records: Sequence[BetRecord], rps_values: Sequence[float]) -> BacktestReport:
    """Build a BacktestReport from settled bets and per-match RPS values."""
    rep = BacktestReport()
    rep.n_bets = len(records)
    rep.n_hits = sum(1 for r in records if r.actual_hit)
    rep.total_pnl = sum(r.pnl for r in records)
    rep.stake = float(rep.n_bets)
    rep.avg_rps = float(np.mean(rps_values)) if rps_values else 0.0
    # CLV placeholder: without open odds we approximate CLV as edge persistence;
    # a real CLV needs open vs close odds. Set to NaN if unavailable.
    rep.avg_clv = float("nan")
    rep.by_edge_bucket = _bucket_by_edge(records)
    return rep


def _bucket_by_edge(records: Sequence[BetRecord]) -> dict[str, dict]:
    buckets = {"0-2%": [], "2-5%": [], "5-10%": [], ">10%": []}
    for r in records:
        e = r.edge
        key = ">10%" if e > 0.10 else "5-10%" if e > 0.05 else "2-5%" if e > 0.02 else "0-2%"
        buckets[key].append(r)
    out = {}
    for key, recs in buckets.items():
        if not recs:
            continue
        pnl = sum(r.pnl for r in recs)
        out[key] = {
            "n": len(recs),
            "roi": pnl / len(recs),
            "hit_rate": sum(1 for r in recs if r.actual_hit) / len(recs),
        }
    return out
