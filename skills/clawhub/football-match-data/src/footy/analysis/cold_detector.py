"""冷门检测器 — find matches likely to produce upsets.

Instead of predicting winners (low odds, thin margin), identify matches
where the favorite is likely to FAIL. Bet on underdog +AH.

Cold signals (each adds to the cold index):
  1. Injuries: 2+ key players out for favorite (+20)
  2. Shallow AH trap: 欧亚偏差浅开 (+25)
  3. Historical pattern: repeated failures in similar situations (+15)
  4. Motivation gap: favorite doesn't need win, underdog desperate (+20)
  5. Host nation advantage for underdog (+15)
  6. Over-confidence: odds < 1.30 without massive gap (+10)
  7. Form: underdog in better recent form (+10)
  8. Deep AH unjustified: too deep for the odds (+15)
  9. Round/circumstance: early group stage, second match (+5)

Thresholds:
  Cold index >= 40 → 🟡 Warning: consider underdog +AH
  Cold index >= 55 → 🟠 Alert: strong underdog +AH bet
  Cold index >= 70 → 🔴 Critical: heavy cold expected
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ColdSignal:
    """One cold factor detected."""

    name: str
    description: str
    weight: int  # points added to cold index


@dataclass
class ColdReport:
    """Complete cold/upset analysis for a match."""

    home: str
    away: str
    favorite: str  # which side is favored
    underdog: str
    fav_odds: float
    dog_odds: float

    signals: list[ColdSignal] = field(default_factory=list)
    cold_index: int = 0

    recommendation: str = ""
    bet_suggestion: str = ""
    confidence: str = ""  # low / medium / high


def detect_cold(
    home: str, away: str,
    home_odds: float, draw_odds: float, away_odds: float,
    ah_line: float = 0.0,
    # Fundamental signals
    injuries_fav: int = 0,
    injuries_dog: int = 0,
    fav_must_win: bool = False,
    dog_must_win: bool = False,
    fav_already_qualified: bool = False,
    motivation_known: bool = False,  # only trigger motivation signals when known
    host_is_dog: bool = False,
    is_host_nation: bool = False,  # only True if underdog is actual tournament host
    historical_cold_pattern: str = "",
    dog_recent_form_wins: int = 0,
    fav_recent_form_wins: int = 0,
    is_second_group_match: bool = False,
    ha_euro_deviation_signal: str = "",
) -> ColdReport:
    """Run full cold detection on a match.

    Returns a ColdReport with cold_index and betting suggestion.
    """
    # Determine favorite/underdog
    if home_odds < away_odds:
        fav, dog = home, away
        fav_odds, dog_odds = home_odds, away_odds
        fav_is_home = True
    else:
        fav, dog = away, home
        fav_odds, dog_odds = away_odds, home_odds
        fav_is_home = False

    report = ColdReport(
        home=home, away=away, favorite=fav, underdog=dog,
        fav_odds=fav_odds, dog_odds=dog_odds,
    )

    # ---- Signal 1: Injuries to favorite ----
    if injuries_fav >= 2:
        report.signals.append(ColdSignal(
            "伤病打击", f"{fav}{injuries_fav}名主力伤停，实力折损", weight=20))
        report.cold_index += 20
    elif injuries_fav >= 1:
        report.signals.append(ColdSignal(
            "伤病影响", f"{fav}1名主力伤停", weight=10))
        report.cold_index += 10

    # ---- Signal 2: Shallow AH trap ----
    if ha_euro_deviation_signal == "浅开":
        report.signals.append(ColdSignal(
            "欧亚浅开陷阱", "亚盘比欧赔标准浅→便宜盘→庄家不看好热门", weight=25))
        report.cold_index += 25

    # ---- Signal 3: Historical cold pattern ----
    if historical_cold_pattern:
        report.signals.append(ColdSignal(
            "历史魔咒", historical_cold_pattern, weight=15))
        report.cold_index += 15

    # ---- Signal 4: Motivation gap ----
    # Only apply when motivation is actually known (e.g. from group standings)
    if motivation_known:
        if fav_already_qualified and dog_must_win:
            report.signals.append(ColdSignal(
                "战意差距", f"{fav}已出线无压力，{dog}背水一战", weight=20))
            report.cold_index += 20
        elif not fav_must_win and dog_must_win:
            report.signals.append(ColdSignal(
                "战意差距", f"{fav}平局可接受，{dog}必须赢", weight=15))
            report.cold_index += 15
        elif not fav_must_win and not dog_must_win:
            report.signals.append(ColdSignal(
                "战意不足", f"双方都不需要赢→可能消极，平局概率大。热门方胜率打折。", weight=15))
            report.cold_index += 15

    # ---- Signal 5: Host nation for underdog ----
    # ⚠️ Only trigger if the underdog is the actual tournament host nation.
    # "Home" in 500.com listing ≠ host nation (neutral-venue tournaments).
    if host_is_dog and is_host_nation:
        report.signals.append(ColdSignal(
            "东道主加成", f"{dog}是主办国，主场优势", weight=15))
        report.cold_index += 15

    # ---- Signal 6: Over-confidence ----
    if fav_odds < 1.30 and dog_odds > 10.0:
        report.signals.append(ColdSignal(
            "过度热门", f"{fav}赔率{fav_odds:.2f}市场过度追捧，暗藏风险", weight=10))
        report.cold_index += 10

    # ---- Signal 7: Form reversal ----
    if dog_recent_form_wins > fav_recent_form_wins:
        report.signals.append(ColdSignal(
            "状态逆转", f"{dog}近况{2*dog_recent_form_wins}分 > {fav}{2*fav_recent_form_wins}分", weight=10))
        report.cold_index += 10

    # ---- Signal 8: Deep AH unjustified ----
    odds_ratio = fav_odds / dog_odds if dog_odds > 0 else 1.0
    abs_ah = abs(ah_line)
    if abs_ah >= 1.0 and odds_ratio > 0.25:
        report.signals.append(ColdSignal(
            "深盘不合理", f"{fav}让{abs_ah:.1f}球但赔率比{odds_ratio:.2f}→盘口偏深难穿", weight=15))
        report.cold_index += 15

    # ---- Signal 9: Second group match ----
    if is_second_group_match:
        report.signals.append(ColdSignal(
            "第二轮魔咒", "小组赛第二轮常出冷门", weight=5))
        report.cold_index += 5

    # ---- Recommendation ----
    if report.cold_index >= 70:
        report.confidence = "high"
        report.recommendation = f"🔴 极高冷门风险 ({report.cold_index}分)"
        report.bet_suggestion = f"重注{dog}+AH(受让)，或{dog}胜平"
    elif report.cold_index >= 55:
        report.confidence = "high"
        report.recommendation = f"🟠 高冷门风险 ({report.cold_index}分)"
        report.bet_suggestion = f"建议{dog}+AH(受让)"
    elif report.cold_index >= 40:
        report.confidence = "medium"
        report.recommendation = f"🟡 冷门预警 ({report.cold_index}分)"
        report.bet_suggestion = f"考虑{dog}+AH，至少避开{fav}深盘"
    elif report.cold_index >= 25:
        report.confidence = "low"
        report.recommendation = f"🟢 轻微冷门信号 ({report.cold_index}分)"
        report.bet_suggestion = f"关注但不急于下注"
    else:
        report.recommendation = f"✅ 无明显冷门信号 ({report.cold_index}分)"
        report.bet_suggestion = f"正常按1X2分析"

    return report
