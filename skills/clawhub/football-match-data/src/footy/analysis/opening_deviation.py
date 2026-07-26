"""初盘偏差信号 — the bookmaker's first word is often their truest.

When the opening handicap DEVIATES significantly from the theoretical line
derived from European odds, this is a deliberate choice by the bookmaker.

Key insight from 操盘手分析:
  - 初盘浅开 (>0.5球) → 庄家开盘就在说不看好热门 → 强烈冷门预警
  - 初盘深开 (>0.5球) → 庄家开盘就在保护热门 → 真实看好信号
  - 初盘吻合 (±0.25球内) → 庄家无明确态度 → 正常

After the initial opening, subsequent line movement is the "second sentence".
When the first and second sentences CONFLICT, the first is more trustworthy.
"""
from __future__ import annotations

from dataclasses import dataclass

from .euro_ah import euro_to_ah, AH_NAMES


@dataclass
class OpeningDeviation:
    """Analysis of opening handicap deviation."""

    euro_odds: float           # the favorite's European odds
    theoretical_ah: float      # what the AH SHOULD be
    actual_open_ah: float      # what the AH ACTUALLY opened at
    deviation: float           # |actual| - |theoretical|, positive = deep, negative = shallow
    signal: str                # "浅开预警" / "深开看好" / "吻合"
    severity: str              # "high" / "medium" / "low"
    interpretation: str


def analyze_opening(
    home_odds: float,
    draw_odds: float,
    away_odds: float,
    open_ah: float,  # negative = home favored
) -> OpeningDeviation:
    """Analyze the opening handicap vs theoretical from European odds.

    This is the bookmaker's FIRST word — deliberately chosen before any
    market pressure. Often more honest than subsequent movements.

    open_ah: the actual opening Asian handicap line.
    """
    # Determine favorite
    fav_odds = min(home_odds, away_odds)
    fav_is_home = home_odds < away_odds

    # Theoretical AH from odds
    theoretical = euro_to_ah(fav_odds)
    theo_abs = abs(theoretical)
    open_abs = abs(open_ah)

    # Deviation: positive = deeper, negative = shallower
    deviation = open_abs - theo_abs

    # Classify
    if abs(deviation) < 0.12:
        signal = "吻合"
        severity = "low"
        interpretation = (
            f"初盘{AH_NAMES.get(open_ah, open_ah)}与理论{AH_NAMES.get(theoretical, theoretical)}一致。"
            f"庄家开盘无明确偏向。"
        )
    elif deviation > 0.25:
        signal = "深开看好"
        severity = "high" if deviation > 0.50 else "medium"
        interpretation = (
            f"🔴 初盘深开{deviation:.2f}球: 理论{AH_NAMES.get(theoretical,theoretical)},"
            f"实开{AH_NAMES.get(open_ah, open_ah)}。"
            f"庄家第一句话就在保护{'上盘' if fav_is_home else '下盘'}。"
            f"真实看好信号——开盘就设高门槛阻挡资金。"
        )
    elif deviation < -0.25:
        signal = "浅开预警"
        severity = "high" if deviation < -0.50 else "medium"
        interpretation = (
            f"🔴 初盘浅开{abs(deviation):.2f}球: 理论{AH_NAMES.get(theoretical,theoretical)},"
            f"实开{AH_NAMES.get(open_ah, open_ah)}。"
            f"庄家第一句话就在说'不看好{'上盘' if fav_is_home else '下盘'}'。"
            f"强烈冷门预警——韩国同款信号(浅开0.5球→输球)。"
        )
    else:
        signal = "轻微偏差"
        severity = "low"
        interpretation = f"初盘偏差{deviation:+.2f}球，在合理范围内，无明确信号。"

    return OpeningDeviation(
        euro_odds=fav_odds,
        theoretical_ah=theoretical,
        actual_open_ah=open_ah,
        deviation=deviation,
        signal=signal,
        severity=severity,
        interpretation=interpretation,
    )
