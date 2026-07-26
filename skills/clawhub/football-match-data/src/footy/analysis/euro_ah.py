"""欧赔→亚盘 标准换算 + 深开/浅开 偏差检测。

Standard European-to-Asian handicap conversion table (Chinese professional source).
Detects when actual handicap deviates from theoretical → trap/block/lure signal.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional

# Standard conversion: European home odds → Asian handicap line
# Based on Chinese professional analysis standards (1.85 water baseline)
EURO_TO_AH = [
    (1.10, 1.14, -2.50),  # 两球半
    (1.14, 1.18, -2.00),  # 两球
    (1.18, 1.22, -1.75),  # 球半/两球
    (1.22, 1.28, -1.50),  # 球半
    (1.28, 1.35, -1.25),  # 一球/球半
    (1.35, 1.45, -1.00),  # 一球
    (1.45, 1.60, -0.75),  # 半球/一球
    (1.60, 1.70, -0.50),  # 半球
    (1.70, 1.90, -0.25),  # 平手/半球
    (1.90, 2.30, 0.00),   # 平手
    (2.30, 2.60, 0.00),   # 平手(高水)
]

# Reverse: for away-team-favored matches (home odds > 2.60, away < 1.90)
# Use the away odds to compute the handicap from the away perspective,
# then flip the sign.

AH_NAMES = {
    -2.50: "两球半",
    -2.00: "两球",
    -1.75: "球半/两球",
    -1.50: "球半",
    -1.25: "一球/球半",
    -1.00: "一球",
    -0.75: "半球/一球",
    -0.50: "半球",
    -0.25: "平手/半球",
    0.00: "平手",
    0.25: "受平手/半球",
    0.50: "受半球",
    0.75: "受半球/一球",
    1.00: "受一球",
    1.25: "受一球/球半",
    1.50: "受球半",
    1.75: "受球半/两球",
    2.00: "受两球",
    2.50: "受两球半",
}


@dataclass
class EuroAhDeviation:
    """Result of comparing European odds → theoretical AH vs actual AH."""

    euro_odds: float  # the European odds used (home or away, whichever is favored)
    theoretical_ah: float  # what the AH should be
    actual_ah: float  # what the AH actually is
    deviation: float  # actual - theoretical: positive=深开, negative=浅开
    signal: str  # "深开" | "浅开" | "吻合"
    interpretation: str
    severity: str  # "high" | "medium" | "low"


def euro_to_ah(euro_odds: float) -> float:
    """Convert a single European odds value to its standard Asian handicap line.

    Returns negative values = favored side gives goals.
    euro_odds should be the odds for the FAVORED side (lower number).
    """
    if euro_odds <= 1.0:
        return 0.0
    if euro_odds > 2.60:
        # Underdog is very weak, favorite at ~1.30-1.40
        # Reciprocal: 1/(1/euro_odds) — use the favorite's odds
        fav_odds = 1.0 / (1.0 - 1.0 / euro_odds + 0.01) if euro_odds < 10 else 2.0
        return euro_to_ah(fav_odds)

    for lo, hi, line in EURO_TO_AH:
        if lo <= euro_odds < hi:
            return line

    # Extrapolate
    if euro_odds < 1.10:
        return -3.00
    return 0.00


def detect_deviation(
    euro_home: float,
    euro_draw: float,
    euro_away: float,
    actual_ah_line: float,  # negative = home gives goals
) -> Optional[EuroAhDeviation]:
    """Compare theoretical AH from European odds vs actual AH.

    actual_ah_line: the real Asian handicap line (negative = home favored).
    Returns deviation analysis.
    """
    # Determine which side is favored
    if euro_home < euro_away:
        # Home is favored
        euro_favored = euro_home
        theoretical = euro_to_ah(euro_favored)
        actual = actual_ah_line
        fav_side = "上盘(主)"
    elif euro_away < euro_home:
        # Away is favored → flip perspective
        euro_favored = euro_away
        theoretical_away = euro_to_ah(euro_favored)
        theoretical = theoretical_away  # away side gives goals → positive
        actual = actual_ah_line
        fav_side = "下盘(客)"
    else:
        theoretical = 0.0
        actual = actual_ah_line
        fav_side = "均衡"

    deviation = actual - theoretical

    # For negative handicaps (favored side giving goals):
    # More negative = deeper handicap, less negative = shallower.
    # Use absolute values to determine deep vs shallow.
    abs_actual = abs(actual) if actual != 0 else 0
    abs_theo = abs(theoretical) if theoretical != 0 else 0
    deep_shallow = abs_actual - abs_theo  # positive = deeper, negative = shallower

    # Interpretation
    if abs(deep_shallow) < 0.12:
        signal = "吻合"
        severity = "low"
        interp = f"实盘{AH_NAMES.get(actual, actual)}与欧赔折算{AH_NAMES.get(theoretical, theoretical)}一致，正常开盘"
    elif deep_shallow > 0:
        signal = "深开"
        levels = abs(deep_shallow)
        severity = "high" if levels >= 0.50 else "medium"
        interp = (
            f"⚠️ 深开{levels:.2f}球: 实盘{AH_NAMES.get(actual, actual)} > 折算{AH_NAMES.get(theoretical, theoretical)}。"
            f"门槛高于欧赔标准。若{fav_side}基本面热 → 诱上({fav_side}难打出)；"
            f"若始终高水阻挡 → 阻上({fav_side}仍有机会)。需结合必发成交量判断。"
        )
    else:
        signal = "浅开"
        levels = abs(deep_shallow)
        severity = "high" if levels >= 0.50 else "medium" if levels >= 0.25 else "low"
        interp = (
            f"⚠️ 浅开{levels:.2f}球: 实盘{AH_NAMES.get(actual, actual)} < 折算{AH_NAMES.get(theoretical, theoretical)}。"
            f"门槛低于欧赔标准→便宜盘→庄家不看好{fav_side}。"
            f"\"便宜莫贪\"——庄家不会无故送钱。{fav_side}大胜概率降低，防冷平/冷负。"
        )

    return EuroAhDeviation(
        euro_odds=euro_favored,
        theoretical_ah=theoretical,
        actual_ah=actual,
        deviation=deviation,
        signal=signal,
        interpretation=interp,
        severity=severity,
    )
