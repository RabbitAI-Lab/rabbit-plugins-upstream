"""Team form analysis — opposition-adjusted recent performance.

Encodes the professional insight that "form isn't just W/D/L — you need
to adjust for WHO they played and WHERE." A team losing to top sides is
very different from losing to relegation candidates.

This module computes form features from historical match data, which can
then be used as bias adjustments in the Poisson model.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Sequence

import numpy as np

from ..data.schema import Match


@dataclass
class TeamForm:
    """Recent performance snapshot for one team."""

    team: str
    # Weighted average goals scored / conceded over the lookback window,
    # with exponential decay (newer = more important).
    avg_gf: float  # goals for
    avg_ga: float  # goals against
    # Points per game (3/1/0) weighted.
    ppg: float
    # Recent trend: positive = improving, negative = declining.
    trend: float
    # Split by venue.
    home_gf: float
    home_ga: float
    away_gf: float
    away_ga: float


def _exp_weights(n: int, half_life: int = 5) -> np.ndarray:
    """Exponential decay weights, newest first."""
    xi = np.log(2) / half_life
    w = np.exp(-xi * np.arange(n)[::-1])
    return w / w.sum()


def _match_weight(m: Match, base_attack: dict[str, float], base_defence: dict[str, float]) -> float:
    """Opponent strength multiplier: beating a strong team is worth more."""
    opp_att = base_attack.get(m.away if m.home else m.home, 0)
    opp_def = base_defence.get(m.home if m.away else m.away, 0)
    # Higher opponent attack+defence = tougher opponent → weight up.
    strength = np.exp(opp_att - opp_def)  # ~1.0 for average team
    return float(np.clip(strength, 0.5, 2.0))


def compute_form(
    matches: Sequence[Match],
    team: str,
    as_of_date: str,
    window: int = 6,
    base_attack: dict[str, float] | None = None,
    base_defence: dict[str, float] | None = None,
) -> TeamForm:
    """Compute recent form for `team` on or before `as_of_date`.

    window: number of recent matches to look back.
    base_attack/defence: model parameters for opponent-strength adjustment.
    """
    att = base_attack or {}
    defe = base_defence or {}

    # Collect team's recent matches (on or before as_of_date).
    recent = sorted(
        [m for m in matches
         if m.is_finished and m.date <= as_of_date
         and (m.home == team or m.away == team)],
        key=lambda m: m.date,
    )[-window:]

    if not recent:
        return TeamForm(team=team, avg_gf=0, avg_ga=0, ppg=0, trend=0,
                        home_gf=0, home_ga=0, away_gf=0, away_ga=0)

    weights = _exp_weights(len(recent), half_life=5)

    gf_vals: list[float] = []
    ga_vals: list[float] = []
    pts_vals: list[float] = []
    home_gf: list[float] = []
    home_ga: list[float] = []
    away_gf: list[float] = []
    away_ga: list[float] = []

    for i, m in enumerate(recent):
        w = weights[i] * _match_weight(m, att, defe)
        if m.home == team:
            gf_vals.append(m.home_goals * w)
            ga_vals.append(m.away_goals * w)
            home_gf.append(m.home_goals)
            home_ga.append(m.away_goals)
            if m.home_goals > m.away_goals:
                pts_vals.append(3.0 * w)
            elif m.home_goals == m.away_goals:
                pts_vals.append(1.0 * w)
            else:
                pts_vals.append(0.0)
        else:
            gf_vals.append(m.away_goals * w)
            ga_vals.append(m.home_goals * w)
            away_gf.append(m.away_goals)
            away_ga.append(m.home_goals)
            if m.away_goals > m.home_goals:
                pts_vals.append(3.0 * w)
            elif m.away_goals == m.home_goals:
                pts_vals.append(1.0 * w)
            else:
                pts_vals.append(0.0)

    # Trend: slope of goals-for over time (positive = improving).
    n = len(recent)
    trend = 0.0
    gf_raw = []
    for m in recent:
        gf_raw.append(float(m.home_goals if m.home == team else m.away_goals))
    if n >= 3:
        x = np.arange(n)
        y = np.array(gf_raw)
        if np.std(y) > 0:
            trend = float(np.polyfit(x, y, 1)[0])  # slope

    return TeamForm(
        team=team,
        avg_gf=float(np.mean(gf_vals)) if gf_vals else 0,
        avg_ga=float(np.mean(ga_vals)) if ga_vals else 0,
        ppg=float(np.mean(pts_vals)) if pts_vals else 0,
        trend=trend,
        home_gf=float(np.mean(home_gf)) if home_gf else 0,
        home_ga=float(np.mean(home_ga)) if home_ga else 0,
        away_gf=float(np.mean(away_gf)) if away_gf else 0,
        away_ga=float(np.mean(away_ga)) if away_ga else 0,
    )


def form_adjustment(form: TeamForm, is_home: bool) -> dict[str, float]:
    """Convert TeamForm into λ bias factors for the Poisson model.

    Returns {attack_bias, defence_bias} where > 0 boosts scoring,
    < 0 reduces it. These are additive adjustments on the log-rate scale.
    """
    if form.ppg == 0:  # insufficient data
        return {"attack_bias": 0.0, "defence_bias": 0.0}

    gf = form.home_gf if is_home else form.away_gf
    ga = form.home_ga if is_home else form.away_ga

    # Baseline: average team scores ~1.4 goals per game.
    # If team is scoring 2.0 recently → log(2.0/1.4) ≈ +0.36 attack boost.
    baseline_gf = 1.4
    baseline_ga = 1.4

    att_bias = np.log(max(gf, 0.3) / baseline_gf) if gf > 0 else 0.0
    def_bias = -np.log(max(ga, 0.3) / baseline_ga) if ga > 0 else 0.0

    # Scale down: form should nudge, not dominate.
    scale = 0.3
    # Trend bonus: improving team gets a small extra boost.
    trend_bonus = np.clip(form.trend * 0.05, -0.10, 0.10)

    return {
        "attack_bias": float(np.clip(att_bias * scale + trend_bonus, -0.3, 0.3)),
        "defence_bias": float(np.clip(def_bias * scale, -0.3, 0.3)),
    }
