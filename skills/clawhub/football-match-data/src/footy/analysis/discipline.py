"""Signal discipline — probability ranges, not binary.

Three iron rules from Switzerland-Canada复盘:
  1. Every signal must output a probability RANGE, never absolute
  2. Multiple signals stack → upgrade confidence level
  3. Fundamental gap acts as a reverse check on technical signals
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

# Historical steam magnitude → favorite win rate (from 8955-match backtest)
STEAM_WIN_RATES = {
    (0.01, 0.05): 0.58,
    (0.05, 0.10): 0.55,
    (0.10, 0.15): 0.49,
    (0.15, 0.20): 0.46,
    (0.20, 0.25): 0.43,
    (0.25, 0.30): 0.41,
    (0.30, 0.40): 0.40,
    (0.40, 1.00): 0.35,
}


@dataclass
class SignalResult:
    """A single signal with probability range, never absolute."""

    name: str
    direction: str  # which side this favors
    probability: float  # 0-1, the historical hit rate of this signal
    interpretation: str  # NEVER say "X will happen"


@dataclass
class FinalVerdict:
    """Aggregated verdict from all signals."""

    signals: list[SignalResult] = field(default_factory=list)
    confidence: str = "low"
    recommendation: str = ""
    caveat: str = ""


def steam_to_probability(steam_magnitude: float, fav_odds: float) -> SignalResult:
    """Convert steam magnitude to a probability range.

    Returns SignalResult with historical win rate for this steam level.
    """
    for (lo, hi), win_rate in STEAM_WIN_RATES.items():
        if lo <= abs(steam_magnitude) < hi:
            fail_rate = 1.0 - win_rate
            direction = "热门方向" if steam_magnitude < 0 else "冷门方向"
            if fail_rate > 0.55:
                interp = (
                    f"Steam {abs(steam_magnitude):.3f}→历史同档热门胜率仅{win_rate:.0%}。"
                    f"冷门概率{fail_rate:.0%}——高但非确定。"
                )
            elif fail_rate > 0.45:
                interp = (
                    f"Steam {abs(steam_magnitude):.3f}→历史同档热门胜率{win_rate:.0%}。"
                    f"方向有参考价值但非决定性。"
                )
            else:
                interp = (
                    f"Steam {abs(steam_magnitude):.3f}→历史同档热门胜率{win_rate:.0%}。"
                    f"信号偏弱，不单独使用。"
                )
            return SignalResult(
                name="Steam方向",
                direction=direction,
                probability=win_rate if steam_magnitude < 0 else fail_rate,
                interpretation=interp,
            )
    return SignalResult(name="Steam方向", direction="无信号", probability=0.5,
                        interpretation="Steam幅度不足，无信号。")


def combine_signals(signals: list[SignalResult], fundamental_gap: str = "") -> FinalVerdict:
    """Combine multiple signals into a calibrated verdict.

    fundamental_gap: 'large' | 'moderate' | 'small' — the real strength gap
    """
    v = FinalVerdict(signals=signals)

    if not signals:
        v.confidence = "low"
        v.recommendation = "信号不足，不推荐"
        return v

    # Count signals per direction
    fav_signals = [s for s in signals if s.direction == "热门方向"]
    dog_signals = [s for s in signals if s.direction == "冷门方向"]
    strong_signals = [s for s in signals if s.probability > 0.55]

    # Confidence upgrade rules
    if len(strong_signals) >= 3:
        v.confidence = "high"
    elif len(strong_signals) >= 2:
        v.confidence = "medium"
    elif len(strong_signals) >= 1:
        v.confidence = "low"
    else:
        v.confidence = "low"

    # Fundamental gap reverse check
    if fundamental_gap == "large" and len(dog_signals) > len(fav_signals):
        v.caveat = (
            "⚠️ 技术信号指向冷门，但基本面差距大。"
            "信号仅降温非反转——热门胜率打折但不会归零。"
        )
        v.confidence = "low"  # downgrade due to fundamental conflict
        v.recommendation = "冷门概率升高但非确定，不宜重注冷门方向"
    elif fundamental_gap == "large":
        v.recommendation = "基本面差距大，热门方向可信。技术信号参考但不推翻。"
    elif len(dog_signals) > len(fav_signals) and len(strong_signals) >= 2:
        v.recommendation = "多信号指向冷门，可考虑冷门方向"
    else:
        v.recommendation = "信号混杂，轻仓或不碰"

    return v
