"""Tests for the Poisson model math."""
from __future__ import annotations

import numpy as np

from footy.models.poisson import (
    PoissonModel,
    over_under_probs,
    probs_from_grid,
    score_grid,
)


def _make_matches():
    """Deterministic synthetic matches for reproducible fitting tests."""
    from footy.data.schema import Match

    rng = np.random.default_rng(42)
    teams = ["Strong", "Medium", "Weak"]
    matches = []
    for _ in range(600):
        h, a = rng.choice(teams, size=2, replace=False)
        # Strong teams score more; contrived but known structure.
        base = {"Strong": 1.8, "Medium": 1.2, "Weak": 0.6}
        gh = int(rng.poisson(base[h] * 1.25))  # home boost
        ga = int(rng.poisson(base[a] * 0.85))
        matches.append(Match("2023-01-01", "E0", "Test", h, a, gh, ga))
    return matches


def test_score_grid_sums_to_one():
    grid = score_grid(1.5, 1.1, rho=0.0)
    assert abs(grid.sum() - 1.0) < 1e-9


def test_probs_partition_unity():
    grid = score_grid(2.0, 1.0)
    p = probs_from_grid(grid)
    assert abs(sum(p.values()) - 1.0) < 1e-9


def test_over_under_sums_to_one():
    grid = score_grid(1.8, 1.2)
    ou = over_under_probs(grid, 2.5)
    assert abs(ou["over"] + ou["under"] - 1.0) < 1e-9


def test_dixon_coles_correction_keeps_valid_probs():
    """Non-zero rho must still yield a valid (non-negative, ~normalised) grid."""
    grid = score_grid(1.4, 1.1, rho=0.1)
    assert (grid >= 0).all()
    assert abs(grid.sum() - 1.0) < 1e-9


def test_fit_recovers_strength_ordering():
    """The fitted attack params should rank Strong > Medium > Weak."""
    matches = _make_matches()
    mdl = PoissonModel()
    mdl.fit(matches)
    att = mdl.params.attack
    assert att["Strong"] > att["Medium"] > att["Weak"], (
        f"Expected Strong>Medium>Weak, got {att}"
    )


def test_home_advantage_positive():
    matches = _make_matches()
    mdl = PoissonModel()
    mdl.fit(matches)
    # We baked a ~1.25x home boost into synthetic data => log(1.25)~0.22.
    assert mdl.params.home_adv > 0


def test_predict_keys_present():
    matches = _make_matches()
    mdl = PoissonModel()
    mdl.fit(matches)
    pred = mdl.predict("Strong", "Weak")
    assert set(pred["probs_1x2"]) == {"H", "D", "A"}
    assert abs(sum(pred["probs_1x2"].values()) - 1.0) < 1e-9
    # A strong home side vs weak away should be strongly favoured.
    assert pred["probs_1x2"]["H"] > pred["probs_1x2"]["A"]
