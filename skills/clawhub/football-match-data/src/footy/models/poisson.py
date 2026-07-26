"""Poisson goal model — the classic baseline for football prediction.

Models home/away goals as independent Poisson variables parameterised by each
team's attack/defence strengths and a home advantage. Serves as both a usable
predictor and the ablation baseline against Dixon-Coles.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.optimize import minimize
from scipy.stats import poisson

MAX_GOALS = 10  # truncate the scoreline grid here; tail probability is negligible


@dataclass
class PoissonParams:
    """Fitted parameters: attack/defence per team plus home advantage & rho=0."""

    attack: dict[str, float]
    defence: dict[str, float]
    home_adv: float
    intercept: float  # baseline scoring rate (log scale)
    rho: float = 0.0  # unused in plain Poisson; present for a uniform interface

    def goal_rates(self, home: str, away: str) -> tuple[float, float]:
        """Expected goals for (home, away)."""
        lam_h = np.exp(self.intercept + self.attack[home] + self.defence[away] + self.home_adv)
        lam_a = np.exp(self.intercept + self.attack[away] + self.defence[home])
        return float(lam_h), float(lam_a)


def score_grid(lam_h: float, lam_a: float, rho: float = 0.0) -> np.ndarray:
    """Joint probability matrix P(home=i, away=j) for i,j in 0..MAX_GOALS.

    With rho=0 this is the independent-Poisson product. The Dixon-Coles low-score
    correction (rho != 0) is applied here too so both models share this kernel.
    """
    h = poisson.pmf(np.arange(MAX_GOALS + 1), lam_h)
    a = poisson.pmf(np.arange(MAX_GOALS + 1), lam_a)
    grid = np.outer(h, a)  # shape (MAX_GOALS+1, MAX_GOALS+1)

    if rho != 0.0:
        # Dixon-Coles adjustment only touches the four low-score cells.
        tau = np.ones_like(grid)
        tau[0, 0] = 1 - lam_h * lam_a * rho
        tau[0, 1] = 1 + lam_h * rho
        tau[1, 0] = 1 + lam_a * rho
        tau[1, 1] = 1 - rho
        grid = grid * tau
        grid = np.clip(grid, 0, None)

    # Renormalise so probabilities sum to 1 over the truncated grid.
    total = grid.sum()
    if total > 0:
        grid /= total
    return grid


def probs_from_grid(grid: np.ndarray) -> dict[str, float]:
    """Collapse a score-grid into 1X2 probabilities."""
    diag = np.trace(grid)
    home = float(np.tril(grid, -1).sum())
    away = float(np.triu(grid, 1).sum())
    return {"H": home, "D": float(diag), "A": away}


def over_under_probs(grid: np.ndarray, line: float = 2.5) -> dict[str, float]:
    """Over/Under probabilities for a goal line (e.g. 2.5)."""
    total = 0.0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if i + j > line:
                total += grid[i, j]
    return {"over": float(total), "under": 1.0 - float(total)}


class PoissonModel:
    """Independent-Poisson model (no Dixon-Coles rho)."""

    def __init__(self) -> None:
        self.params: PoissonParams | None = None

    @property
    def name(self) -> str:
        return "Poisson"

    def fit(self, matches: list) -> PoissonParams:
        """Fit via maximum likelihood on completed matches.

        `matches` items need: home, away, home_goals, away_goals, date.
        """
        teams = sorted({m.home for m in matches} | {m.away for m in matches})
        idx = {t: i for i, t in enumerate(teams)}
        n = len(teams)

        # Observed (goals_home, goals_away, home_idx, away_idx).
        gh = np.array([m.home_goals for m in matches], dtype=float)
        ga = np.array([m.away_goals for m in matches], dtype=float)
        hi = np.array([idx[m.home] for m in matches])
        ai = np.array([idx[m.away] for m in matches])

        # Parameter vector: [intercept, home_adv, attack_1..n, defence_1..n].
        # We use sum-to-zero constraints via the last team as reference (not
        # strictly identified, but fine for prediction).
        x0 = np.concatenate([
            [np.log(np.mean(gh + ga) / 2 + 1e-3)],  # intercept
            [0.2],  # home advantage
            np.zeros(n),  # attack
            np.zeros(n),  # defence
        ])

        def neg_ll(p: np.ndarray) -> float:
            intercept, hv = p[0], p[1]
            att = p[2 : 2 + n]
            defe = p[2 + n :]
            # Clip the linear predictor to avoid overflow in exp() when the
            # optimiser wanders on small/degenerate training slices.
            lin_h = np.clip(intercept + att[hi] + defe[ai] + hv, -8, 8)
            lin_a = np.clip(intercept + att[ai] + defe[hi], -8, 8)
            lam_h = np.exp(lin_h)
            lam_a = np.exp(lin_a)
            ll = poisson.logpmf(gh, lam_h) + poisson.logpmf(ga, lam_a)
            total = float(np.sum(ll))
            if not np.isfinite(total):
                return 1e9
            return -total

        bounds = (
            [(-2, 2)]       # intercept
            + [(0, 0.6)]    # home advantage
            + [(-1.5, 1.5)] * n  # attack
            + [(-1.5, 1.5)] * n  # defence
        )
        res = minimize(neg_ll, x0, method="L-BFGS-B", bounds=bounds)
        p = res.x
        att_raw = p[2 : 2 + n]
        def_raw = p[2 + n :]
        att_centered = att_raw - att_raw.mean()
        def_centered = def_raw - def_raw.mean()
        params = PoissonParams(
            attack={t: float(att_centered[idx[t]]) for t in teams},
            defence={t: float(def_centered[idx[t]]) for t in teams},
            home_adv=float(p[1]),
            intercept=float(p[0]),
        )
        self.params = params
        return params

    def predict(self, home: str, away: str) -> dict:
        """Return goal rates, score grid, 1X2 and O/U 2.5 probabilities."""
        if self.params is None:
            raise RuntimeError("Model not fitted. Call fit() first.")
        lam_h, lam_a = self.params.goal_rates(home, away)
        grid = score_grid(lam_h, lam_a, rho=0.0)
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
