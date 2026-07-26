"""Tests for value-betting math (devig, edge, EV, Kelly)."""
from __future__ import annotations

import math

from footy.analysis.value import devig, evaluate, kelly_fraction


def test_devig_removes_overround():
    # A -110/-110 style market: implied 52.4% + 52.4% = 104.8%.
    # For 1X2 use (2.0, 3.5, 4.0): implied sums to >1.
    fair = devig((2.0, 3.5, 4.0))
    assert abs(sum(fair) - 1.0) < 1e-9
    # Favourite (lowest odds) should carry the highest fair probability.
    assert fair[0] > fair[1] > fair[2]


def test_devig_symmetric_market_is_50_50():
    fair = devig((1.90, 1.90, 0.0001))  # degenerate; test the 2-way intuition instead
    # Two-way even money at 1.90 each de-vigs to exactly 0.5/0.5.
    two_way = devig((1.90, 1.90))
    assert abs(two_way[0] - 0.5) < 1e-9
    assert abs(two_way[1] - 0.5) < 1e-9


def test_evaluate_zero_edge_for_fair_odds():
    # If model prob equals implied prob, edge and EV should be ~0.
    odds = 2.0
    pred = 1.0 / odds
    vb = evaluate("1X2-H", "Home", pred, odds)
    assert abs(vb.edge) < 1e-9
    assert abs(vb.ev) < 1e-9


def test_evaluate_positive_ev_when_edge_positive():
    # Model thinks 60%, market offers 2.0 (implied 50%) -> strong +EV.
    vb = evaluate("1X2-H", "Home", 0.60, 2.0)
    assert vb.edge == math.isclose(vb.edge, 0.10, abs_tol=1e-9) or vb.edge > 0.09
    assert vb.ev > 0.19  # 0.6*2 - 1 = 0.2


def test_kelly_formula_matches_skill_reference():
    # Betting skill: f* = (fair_prob - market_prob) / (1 - market_prob).
    # fair=0.58, implied=0.52 => f* = 0.06/0.48 = 0.125.
    full = kelly_fraction(0.06, 0.52, fraction=1.0)
    assert abs(full - 0.125) < 1e-9


def test_half_kelly_halves_full():
    full = kelly_fraction(0.06, 0.52, fraction=1.0)
    half = kelly_fraction(0.06, 0.52, fraction=0.5)
    assert abs(half - full / 2) < 1e-9


def test_kelly_zero_when_no_edge():
    assert kelly_fraction(0.0, 0.5) == 0.0
    assert kelly_fraction(-0.1, 0.5) == 0.0  # negative edge -> no bet
