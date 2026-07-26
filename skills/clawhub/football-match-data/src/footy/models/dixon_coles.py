"""Dixon-Coles model (1997) — the industry-standard football goals model.

Two improvements over plain independent-Poisson:
  1. A rho (ρ) correction for low-score outcomes (0-0, 1-0, 0-1, 1-1), which
     independent Poisson under-predicts. See score_grid() in poisson.py.
  2. Time-decay weighting: more recent matches count more, via a half-life so
     each match's contribution decays as exp(-ξ · days_ago).

Reference: Dixon & Coles, "Modelling Association Football Scores and
Inefficiencies in the Football Betting Market" (1997).
"""
from __future__ import annotations

import math
import time
from dataclasses import dataclass
from datetime import datetime

import numpy as np
from scipy.optimize import minimize
from scipy.stats import poisson

from .poisson import PoissonParams, MAX_GOALS, over_under_probs, probs_from_grid, score_grid


def xi_from_half_life(half_life_days: float) -> float:
    """Daily decay rate so that a match `half_life_days` ago weighs 0.5.

    We want exp(-ξ · t_half) = 0.5  =>  ξ = ln(2) / t_half.
    """
    if half_life_days <= 0:
        raise ValueError("half_life_days must be positive")
    return math.log(2) / half_life_days


@dataclass
class DixonColesParams(PoissonParams):
    """Same fields as PoissonParams; rho is now fitted rather than fixed at 0."""

    pass


class DixonColesModel:
    """Bivariate Poisson with low-score correction and time weighting."""

    def __init__(self, half_life_days: float = 90.0) -> None:
        self.half_life_days = half_life_days
        self.params: DixonColesParams | None = None

    @property
    def name(self) -> str:
        return "Dixon-Coles"

    def _time_weights(self, matches: list, reference_date: str) -> np.ndarray:
        """Exponential decay weights relative to the latest match date."""
        ref = datetime.strptime(reference_date, "%Y-%m-%d")
        xi = xi_from_half_life(self.half_life_days)
        days_ago = np.array(
            [(ref - datetime.strptime(m.date, "%Y-%m-%d")).days for m in matches],
            dtype=float,
        )
        return np.exp(-xi * np.clip(days_ago, 0, None))

    def fit(self, matches: list) -> DixonColesParams:
        # Only finished matches carry outcome information.
        finished = [m for m in matches if m.is_finished]
        if not finished:
            raise ValueError("No finished matches to fit on.")

        # Reference date = the latest match so decay is anchored at "now".
        ref_date = max(m.date for m in finished)
        weights = self._time_weights(finished, ref_date)

        teams = sorted({m.home for m in finished} | {m.away for m in finished})
        idx = {t: i for i, t in enumerate(teams)}
        n = len(teams)

        gh = np.array([m.home_goals for m in finished], dtype=float)
        ga = np.array([m.away_goals for m in finished], dtype=float)
        hi = np.array([idx[m.home] for m in finished])
        ai = np.array([idx[m.away] for m in finished])

        def neg_ll(p: np.ndarray) -> float:
            intercept, hv, rho = p[0], p[1], p[2]
            att = p[3 : 3 + n]
            defe = p[3 + n :]
            # Clamp the linear predictor to avoid overflow in exp(); the optimiser
            # can wander far before settling on small early-season samples.
            lin_h = np.clip(intercept + att[hi] + defe[ai] + hv, -8, 8)
            lin_a = np.clip(intercept + att[ai] + defe[hi], -8, 8)
            lam_h = np.exp(lin_h)
            lam_a = np.exp(lin_a)

            base = poisson.logpmf(gh, lam_h) + poisson.logpmf(ga, lam_a)
            # Dixon-Coles low-score multiplicative correction on the log-likelihood.
            # log1p arg must stay > -1 to be finite; clip defensively.
            log_tau = np.zeros_like(base)
            mask00 = (gh == 0) & (ga == 0)
            mask01 = (gh == 0) & (ga == 1)
            mask10 = (gh == 1) & (ga == 0)
            mask11 = (gh == 1) & (ga == 1)
            log_tau[mask00] = np.log(np.clip(1 - lam_h[mask00] * lam_a[mask00] * rho, 1e-9, None))
            log_tau[mask01] = np.log(np.clip(1 + lam_h[mask01] * rho, 1e-9, None))
            log_tau[mask10] = np.log(np.clip(1 + lam_a[mask10] * rho, 1e-9, None))
            log_tau[mask11] = np.log(np.clip(1 - rho, 1e-9, None))
            # Default (other scorelines) contributes log(1)=0, so leave as 0.
            ll = base + log_tau
            total = float(np.sum(weights * ll))
            if not np.isfinite(total):
                return 1e9
            return -total

        # Bounds keep parameters in sane ranges: attack/defence in log-rate terms
        # (e^{-3}..e^{3} goals), home advantage modest, rho in the literature range.
        bounds = (
            [(-2, 2)]       # intercept
            + [(0, 0.6)]    # home advantage
            + [(-0.3, 0.3)] # rho
            + [(-1.5, 1.5)] * n  # attack
            + [(-1.5, 1.5)] * n  # defence
        )
        x0 = np.concatenate([
            [math.log(np.mean(gh + ga) / 2 + 1e-3)],
            [0.2],
            [-0.05],  # rho starts mildly negative (literature prior)
            np.zeros(n),
            np.zeros(n),
        ])
        # L-BFGS-B respects bounds and is robust to the many params here.
        res = minimize(neg_ll, x0, method="L-BFGS-B", bounds=bounds)
        p = res.x
        # Enforce sum-to-zero identifiability on attack & defence so the saved
        # parameters are comparable across runs (doesn't affect predictions).
        att_raw = p[3 : 3 + n]
        def_raw = p[3 + n :]
        att_centered = att_raw - att_raw.mean()
        def_centered = def_raw - def_raw.mean()
        self.params = DixonColesParams(
            attack={t: float(att_centered[idx[t]]) for t in teams},
            defence={t: float(def_centered[idx[t]]) for t in teams},
            home_adv=float(p[1]),
            intercept=float(p[0]),
            rho=float(p[2]),
        )
        return self.params

    def predict(self, home: str, away: str) -> dict:
        if self.params is None:
            raise RuntimeError("Model not fitted. Call fit() first.")
        lam_h, lam_a = self.params.goal_rates(home, away)
        grid = score_grid(lam_h, lam_a, rho=self.params.rho)
        return {
            "model": self.name,
            "home": home,
            "away": away,
            "lambda_home": lam_h,
            "lambda_away": lam_a,
            "grid": grid,
            "probs_1x2": probs_from_grid(grid),
            "probs_ou25": over_under_probs(grid, 2.5),
        }

    def predict_with_form(
        self, home: str, away: str,
        home_form: dict | None = None,
        away_form: dict | None = None,
    ) -> dict:
        """Predict with form bias adjustments applied to the base λ.

        home_form/away_form are dicts with 'attack_bias' and 'defence_bias'
        keys from form_adjustment(). If None, falls back to plain predict().
        """
        base = self.predict(home, away)
        if home_form is None and away_form is None:
            return base

        h_bias = (home_form or {}).get("attack_bias", 0.0)
        a_bias = (away_form or {}).get("attack_bias", 0.0)
        h_def = (home_form or {}).get("defence_bias", 0.0)
        a_def = (away_form or {}).get("defence_bias", 0.0)

        # Apply additive biases on log-rate scale to the already-computed
        # λ values (which are exp(linear_predictor)).
        lam_h = base["lambda_home"] * np.exp(h_bias + a_def)
        lam_a = base["lambda_away"] * np.exp(a_bias + h_def)

        grid = score_grid(lam_h, lam_a, rho=self.params.rho)
        return {
            "model": self.name + "+form",
            "home": home,
            "away": away,
            "lambda_home": float(lam_h),
            "lambda_away": float(lam_a),
            "grid": grid,
            "probs_1x2": probs_from_grid(grid),
            "probs_ou25": over_under_probs(grid, 2.5),
        }
