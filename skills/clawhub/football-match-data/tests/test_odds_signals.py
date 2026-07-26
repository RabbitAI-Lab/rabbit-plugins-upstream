"""Tests for odds-signal engine."""
from footy.analysis.odds_signals import (
    analyze_market,
    classify_handicap_movement,
    kelly_variance,
    odds_dispersion,
)


def test_kelly_variance_low_on_consensus():
    """When all bookmakers quote similar odds, Kelly variance is low."""
    # All around 2.0 → implied ~0.5 each.
    result = kelly_variance([2.0, 1.98, 2.02, 1.95], fair_prob=0.50)
    assert result["variance"] is not None
    assert result["variance"] < 0.001  # tight
    assert result["signal"] == "high_consensus"


def test_kelly_variance_high_on_divergence():
    result = kelly_variance([2.0, 2.5, 3.0, 1.8], fair_prob=0.50)
    assert result["variance"] is not None
    assert result["variance"] > 0.01
    assert "divergent" in result["signal"]


def test_odds_dispersion_tight():
    odds_map = {
        "B365": (2.0, 3.5, 4.0),
        "PS": (2.02, 3.48, 3.95),
        "WH": (1.98, 3.52, 4.05),
    }
    result = odds_dispersion(odds_map, outcome_idx=0)
    assert result["std_dev"] is not None
    assert result["std_dev"] < 0.02  # tight


def test_odds_dispersion_wide():
    odds_map = {
        "B365": (2.0, 3.5, 4.0),
        "PS": (2.5, 3.0, 3.8),
        "WH": (1.6, 4.5, 5.0),
    }
    result = odds_dispersion(odds_map, outcome_idx=0)
    assert result["std_dev"] is not None
    assert result["std_dev"] > 0.03  # wide


def test_analyze_market_returns_all_fields():
    odds_map = {
        "B365": (2.1, 3.4, 3.6),
        "BW": (2.15, 3.35, 3.55),
        "PS": (2.08, 3.42, 3.62),
        "WH": (2.12, 3.38, 3.58),
    }
    analysis = analyze_market(odds_map)
    assert analysis.verdict in ("normal",)
    assert analysis.kelly_var_h.get("signal") is not None
    assert analysis.dispersion_h.get("signal") is not None


def test_handicap_line_up_water_down():
    sig = classify_handicap_movement(line_change=0.5, water_change=-0.10)
    assert sig is not None
    assert "升盘降水" in sig.pattern
    assert sig.direction == "favors_upper"


def test_handicap_line_down_water_up():
    sig = classify_handicap_movement(line_change=-0.25, water_change=0.08)
    assert sig is not None
    assert "降盘升水" in sig.pattern
    assert sig.direction == "favors_upper"


def test_no_movement_returns_none():
    assert classify_handicap_movement(0.0, 0.0) is None
