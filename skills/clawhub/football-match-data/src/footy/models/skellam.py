"""Skellam distribution — direct goal-difference modeling for Asian Handicap.

The Skellam distribution is the difference of two independent Poisson variables.
If GH ~ Poisson(λh) and GA ~ Poisson(λa), then GD = GH - GA ~ Skellam(λh, λa).

Key advantage over grid-based Poisson: directly answers "probability of winning
by X+ goals" without summing a 2D grid. More accurate tail probabilities for AH.

Formula: P(GD = k) = e^{-(λh+λa)} * (λh/λa)^{k/2} * I_{|k|}(2√(λh·λa))
where I_k is the modified Bessel function of the first kind.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from scipy.special import iv  # modified Bessel function


@dataclass
class SkellamAH:
    """Asian Handicap analysis via Skellam goal-difference distribution."""

    lam_home: float
    lam_away: float
    home_cover_prob: float = 0.0  # P(GD > |ah_line|) for home side
    away_cover_prob: float = 0.0  # P(-GD > |ah_line|) for away side
    most_likely_gd: int = 0       # most likely goal difference

    # Detailed probabilities
    prob_gd: dict[int, float] = None  # {gd: probability}

    def __post_init__(self):
        if self.prob_gd is None:
            self.prob_gd = {}


def skellam_pmf(k: int, lam_h: float, lam_a: float) -> float:
    """Probability mass function of Skellam(λh, λa) at point k.

    P(GD = k) where GD = HomeGoals - AwayGoals.
    k > 0: home wins by k goals. k < 0: away wins by |k| goals.
    """
    if lam_h <= 0 or lam_a <= 0:
        return 0.0

    # P(GD = k) = e^{-(λh+λa)} * (λh/λa)^{k/2} * I_{|k|}(2√(λh·λa))
    rate_sum = lam_h + lam_a
    sqrt_prod = 2.0 * math.sqrt(lam_h * lam_a)
    ratio = lam_h / lam_a

    try:
        bessel = iv(abs(k), sqrt_prod)  # I_{|k|}(z)
        prob = math.exp(-rate_sum) * (ratio ** (k / 2.0)) * bessel
        return max(0.0, float(prob))
    except (OverflowError, ValueError):
        # Fall back to grid-based approximation for extreme values
        return _grid_approx(k, lam_h, lam_a)


def _grid_approx(k: int, lam_h: float, lam_a: float, max_goals: int = 15) -> float:
    """Grid-based fallback for extreme lambda values."""
    from scipy.stats import poisson
    prob = 0.0
    for i in range(max_goals + 1):
        j = i - k
        if 0 <= j <= max_goals:
            prob += poisson.pmf(i, lam_h) * poisson.pmf(j, lam_a)
    return prob


def skellam_cdf_gt(k: float, lam_h: float, lam_a: float, max_gd: int = 20) -> float:
    """P(GD > k) — probability goal difference EXCEEDS k.

    For AH analysis: home covering -X handicap requires GD > X.
    k can be non-integer (e.g., -0.75 for half-ball handicaps).
    """
    # For non-integer k, treat as P(GD >= ceil(k))
    # E.g., P(GD > 1.5) = P(GD >= 2)
    k_int = math.ceil(k) if k != int(k) else int(k) + 1
    k_int = max(k_int, -max_gd)

    prob = 0.0
    for gd in range(k_int, max_gd + 1):
        prob += skellam_pmf(gd, lam_h, lam_a)
    return min(1.0, max(0.0, prob))


def skellam_cdf_lt(k: float, lam_h: float, lam_a: float, max_gd: int = 20) -> float:
    """P(GD < k) — probability goal difference is LESS than k.

    For away team covering: P(-GD > X) = P(GD < -X).
    """
    k_int = math.floor(k) if k != int(k) else int(k) - 1
    k_int = min(k_int, max_gd)

    prob = 0.0
    for gd in range(-max_gd, k_int + 1):
        prob += skellam_pmf(gd, lam_h, lam_a)
    return min(1.0, max(0.0, prob))


def analyze_ah(
    lam_home: float,
    lam_away: float,
    ah_line: float,          # negative = home gives goals, positive = home receives
    max_gd: int = 20,
) -> SkellamAH:
    """Full AH analysis for a match using Skellam distribution.

    ah_line: Asian handicap from home perspective.
      -0.5 = home gives 0.5 (home favored by half ball)
      0.5 = home gets 0.5 (away favored by half ball)

    Returns home/away cover probabilities.
    """
    ah_abs = abs(ah_line)

    if ah_line <= 0:
        # Home gives goals: home must win by > |ah_line|
        home_cover = skellam_cdf_gt(ah_abs, lam_home, lam_away, max_gd)
        away_cover = skellam_cdf_lt(-ah_abs, lam_home, lam_away, max_gd)
    else:
        # Home receives goals: away must win by > |ah_line|
        away_cover = skellam_cdf_lt(-ah_abs, lam_home, lam_away, max_gd)
        home_cover = skellam_cdf_gt(ah_abs, lam_home, lam_away, max_gd)

    # Most likely goal difference
    probs = {}
    for gd in range(-max_gd, max_gd + 1):
        p = skellam_pmf(gd, lam_home, lam_away)
        if p > 0.001:
            probs[gd] = p
    most_likely = max(probs, key=probs.get) if probs else 0

    return SkellamAH(
        lam_home=lam_home,
        lam_away=lam_away,
        home_cover_prob=home_cover,
        away_cover_prob=away_cover,
        most_likely_gd=most_likely,
        prob_gd=probs,
    )


def cover_signal(home_cover: float, away_cover: float, threshold: float = 0.60) -> dict:
    """Convert cover probabilities into actionable signals."""
    signals = {}

    if home_cover > threshold:
        signals["home"] = {
            "direction": "上盘(主)穿盘",
            "prob": home_cover,
            "strength": "strong" if home_cover > 0.70 else "moderate",
        }
    elif home_cover > 0.50:
        signals["home"] = {
            "direction": "上盘(主)有空间",
            "prob": home_cover,
            "strength": "weak",
        }

    if away_cover > threshold:
        signals["away"] = {
            "direction": "下盘(客)穿盘",
            "prob": away_cover,
            "strength": "strong" if away_cover > 0.70 else "moderate",
        }
    elif away_cover > 0.50:
        signals["away"] = {
            "direction": "下盘(客)有空间",
            "prob": away_cover,
            "strength": "weak",
        }

    if not signals:
        signals["info"] = {"direction": "盘口均衡", "prob": max(home_cover, away_cover)}

    return signals
