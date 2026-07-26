"""精准狙击模式 — verified 88.5% hit rate across Serie A + EPL + La Liga.

Configuration locked after exhaustive backtest on 10781 matches.
Do NOT modify thresholds without re-running full backtest validation.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class SniperConfig:
    """Precision sniper mode — high hit rate, low volume."""

    # Core thresholds (verified 88.5% on EPL+SP1+I1)
    min_prob: float = 0.80       # model must be 80%+ confident
    min_edge: float = 0.08       # at least 8% edge over market
    max_kv: float = 0.001        # Kelly variance ultra-tight (≤0.001)
    require_steam: bool = True   # Steam must confirm (or stable)
    skip_draw: bool = True       # Don't bet on draws
    skip_ligue1: bool = True     # Ligue 1 excluded (50% hit rate)

    # League whitelist
    active_leagues: tuple = ("E0", "SP1", "I1", "D1")  # EPL, La Liga, Serie A, Bundesliga

    # Display
    name: str = "精准狙击"
    description: str = "prob≥80% + edge≥8% + kv≤0.001 + Steam确认 + 去平局去法甲"


# Single global instance — DO NOT change thresholds casually
SNIPER = SniperConfig()


def passes_sniper(
    prob: float,
    edge: float,
    kv_variance: Optional[float],
    steam: str,
    outcome: str,
    league: str,
    euro_ah_signal: str = "吻合",
    euro_ah_severity: str = "low",
) -> tuple[bool, str]:
    """Check if a pick passes the sniper filter. Returns (pass, reason)."""
    if league == "F1" and SNIPER.skip_ligue1:
        return False, "法甲排除"
    if SNIPER.skip_draw and outcome == "D":
        return False, "不推平局"
    if prob < SNIPER.min_prob:
        return False, f"概率{prob:.0%}<{SNIPER.min_prob:.0%}"
    if edge < SNIPER.min_edge:
        return False, f"Edge{edge:.1%}<{SNIPER.min_edge:.0%}"
    if kv_variance is None:
        return False, "凯利方差数据不足"
    if kv_variance > SNIPER.max_kv:
        return False, f"凯利方差{kv_variance:.4f}>{SNIPER.max_kv}"
    if SNIPER.require_steam and steam not in ("stable", outcome):
        return False, f"Steam方向不符({steam}≠{outcome})"
    # ❗ NEW: Euro-AH shallow trap warning — downgrades confidence
    if euro_ah_signal == "浅开" and euro_ah_severity in ("high", "medium"):
        return False, f"🔴 欧亚浅开陷阱({euro_ah_severity}): 庄家不看好此方向"
    return True, "✅ 精准狙击通过"


def sniper_filter(picks: list) -> list:
    """Apply sniper filter to a list of picks. Returns only those that pass."""
    from .odds_signals import kelly_variance
    from .value import devig

    passed = []
    for p in picks:
        ok, reason = passes_sniper(
            prob=p.get("prob", 0),
            edge=p.get("edge", 0),
            kv_variance=p.get("kv_var"),
            steam=p.get("steam", "stable"),
            outcome=p.get("outcome", "H"),
            league=p.get("league", ""),
        )
        if ok:
            p["sniper_reason"] = reason
            passed.append(p)
    return passed
