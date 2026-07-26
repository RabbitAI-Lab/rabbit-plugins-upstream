"""公司异常检测 — conservative bookmakers offering high odds = red flag.

Conservative companies (10Bet 88.5%, Pinnacle 89.3%, 马会 89.5%, 澳门 89.8%)
operate on thin margins. When they offer HIGHER odds than the market average
on a specific outcome, it means they're NOT afraid of that outcome happening.

This is a strong contrarian signal.
"""
from __future__ import annotations

from typing import Optional

# Conservative bookmakers with their known payout rates
CONSERVATIVE = {
    "竞彩官方": 0.86,    # 中国竞彩官方,返还率最低
    "Pinnacle": 0.893,   # 最锋利
    "皇冠": 0.893,
    "香港马会": 0.895,
    "澳门": 0.898,
    "Bwin": 0.897,
    "1xBet": 0.891,
    "盈禾": 0.891,
}


def detect_anomaly(
    odds_data: dict[str, tuple[float, float, float]],
    outcome_idx: int,  # 0=home, 1=draw, 2=away
    threshold: float = 0.03,
) -> Optional[str]:
    """Check if conservative companies are offering unusually high odds.

    Returns a warning message if anomaly found, None otherwise.
    """
    if not odds_data:
        return None

    # Average odds for this outcome across all companies
    all_vals = [o[outcome_idx] for o in odds_data.values() if o[outcome_idx] > 0]
    if not all_vals:
        return None
    avg_odds = sum(all_vals) / len(all_vals)

    warnings = []
    for name in CONSERVATIVE:
        if name not in odds_data:
            continue
        odds_val = odds_data[name][outcome_idx]
        if odds_val <= 0:
            continue
        # Conservative company offering HIGHER odds than average
        gap = odds_val - avg_odds
        if gap > threshold:
            warnings.append(
                f"{name}(返还{CONSERVATIVE[name]:.1%})给{odds_val:.2f} > 均值{avg_odds:.2f}"
            )

    if warnings:
        return "🔴 公司异常: " + ", ".join(warnings) + " — 保守公司不怕该结果"

    # Also check: conservative company offering LOWER odds than avg
    # This means they're protecting against this outcome
    protects = []
    for name in CONSERVATIVE:
        if name not in odds_data:
            continue
        odds_val = odds_data[name][outcome_idx]
        if odds_val <= 0:
            continue
        gap = odds_val - avg_odds
        if gap < -threshold:
            protects.append(
                f"{name}(返还{CONSERVATIVE[name]:.1%})给{odds_val:.2f} < 均值{avg_odds:.2f}"
            )

    if protects:
        return "🟢 公司保护: " + ", ".join(protects) + " — 保守公司在压低赔付"

    return None


def confidence_adjustment(
    odds_data: dict[str, tuple[float, float, float]],
    outcome_idx: int,
    current_stars: int,
) -> tuple[int, str]:
    """Adjust star rating based on company anomaly detection.

    Returns (adjusted_stars, reason).
    """
    warning = detect_anomaly(odds_data, outcome_idx)
    if warning is None:
        return current_stars, ""

    if "🔴" in warning:
        # Conservative companies don't fear this outcome → downgrade
        new_stars = max(1, current_stars - 1)
        return new_stars, warning
    elif "🟢" in warning:
        # Conservative companies protecting this outcome → maintain or upgrade
        return current_stars, warning

    return current_stars, warning
