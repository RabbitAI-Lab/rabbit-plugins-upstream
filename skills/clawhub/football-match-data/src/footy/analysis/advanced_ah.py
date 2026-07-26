"""Advanced Asian Handicap Analysis — 4 manipulation models + 9 line-change paths.

From 足球财富 + professional trader methodology.

Four Core Models:
  浅阻盘: Weak block — favorite barely favored, underdog looks safer. Favorite covers.
  深阻盘: Deep block — favorite must win big, psychological barrier. Favorite often covers.
  浅诱盘: Shallow lure — cheap handicap, easy to cover. COLD UPSET HIGH RISK.
  深诱盘: Deep lure — very deep + continued rise. Favorite wins but doesn't cover.

9 Line-Change Paths (变盘九种):
  Before: 深 / 合理 / 浅 × After: 更深 / 合理 / 更浅
  Key rules: 深盘降盘=利空 / 浅盘降盘=阻盘 / 临场升盘+高水=诱盘
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class ManipulationType(Enum):
    SHALLOW_BLOCK = "浅阻盘"      # 平半盘: weak block, favorite covers
    DEEP_BLOCK = "深阻盘"         # 一球+: psychological barrier, favorite covers
    SHALLOW_LURE = "浅诱盘"       # 半一盘: cheap lure, cold upset risk HIGH
    DEEP_LURE = "深诱盘"          # 球半+: deep lure, favorite wins but doesn't cover
    NEUTRAL = "均衡盘"            # No clear manipulation


class LineDirection(Enum):
    DEEPENED = "更深"             # Line moved deeper (favorite gives more)
    STABLE = "合理"               # Line unchanged
    SHALLOWER = "更浅"            # Line moved shallower (favorite gives less)


@dataclass
class AdvancedAH:
    """Complete Asian Handicap analysis report."""

    # Input
    home_odds: float
    draw_odds: float
    away_odds: float
    open_line: float      # opening handicap (negative = home favored)
    close_line: float     # closing handicap
    open_water_fav: float # opening payout for favorite side
    close_water_fav: float# closing payout for favorite side

    # Computed
    manipulation: ManipulationType = ManipulationType.NEUTRAL
    line_change: LineDirection = LineDirection.STABLE
    water_change: str = ""  # "升水" / "降水" / "稳定"
    signal: str = ""
    confidence: str = "low"
    risk_level: str = ""   # "高风险" / "中风险" / "低风险"
    bet_suggestion: str = ""


def _water_level(water: float) -> str:
    if water <= 0.85: return "低水"
    if water <= 1.00: return "中水"
    return "高水"


def analyze_advanced_ah(
    home_odds: float, draw_odds: float, away_odds: float,
    open_line: float, close_line: float,
    open_water_fav: float = 0.90, close_water_fav: float = 0.90,
) -> AdvancedAH:
    """Full advanced Asian handicap analysis.

    open_line/close_line: handicap from home perspective.
      Negative = home favored (gives goals).
      Positive = away favored (home receives goals).
    """
    report = AdvancedAH(
        home_odds=home_odds, draw_odds=draw_odds, away_odds=away_odds,
        open_line=open_line, close_line=close_line,
        open_water_fav=open_water_fav, close_water_fav=close_water_fav,
    )

    # ---- Determine which side is favored ----
    if home_odds < away_odds:
        fav_side = "上盘(主)"
        fav_odds = home_odds
        line_is_deeper = close_line < open_line  # more negative = deeper
        line_diff = open_line - close_line       # positive = deepened
    else:
        fav_side = "下盘(客)"
        fav_odds = away_odds
        line_is_deeper = close_line > open_line  # more positive = deeper
        line_diff = close_line - open_line       # positive = deepened

    # ---- Line change direction ----
    if abs(line_diff) < 0.12:
        report.line_change = LineDirection.STABLE
    elif line_diff > 0:
        report.line_change = LineDirection.DEEPENED
    else:
        report.line_change = LineDirection.SHALLOWER

    # ---- Water change ----
    water_diff = close_water_fav - open_water_fav
    if abs(water_diff) < 0.03:
        report.water_change = "稳定"
    elif water_diff > 0:
        report.water_change = "升水"
    else:
        report.water_change = "降水"

    # ---- Classify manipulation type ----
    abs_line = abs(close_line)

    # Determine manipulation based on handicap depth + line/water movement
    if abs_line <= 0.25:  # 平手/平半
        if report.line_change == LineDirection.DEEPENED:
            report.manipulation = ManipulationType.SHALLOW_LURE
        else:
            report.manipulation = ManipulationType.SHALLOW_BLOCK
    elif abs_line <= 0.75:  # 半球/半一
        if report.line_change == LineDirection.SHALLOWER and report.water_change == "升水":
            report.manipulation = ManipulationType.SHALLOW_BLOCK  # 退盘升水=阻
        elif report.line_change == LineDirection.DEEPENED and report.water_change == "降水":
            report.manipulation = ManipulationType.SHALLOW_LURE   # 升盘降水=诱
        else:
            report.manipulation = ManipulationType.NEUTRAL
    elif abs_line <= 1.50:  # 一球到球半
        if report.line_change == LineDirection.DEEPENED and report.water_change == "升水":
            report.manipulation = ManipulationType.DEEP_LURE     # 深盘再升+高水=诱
        elif report.line_change == LineDirection.SHALLOWER:
            report.manipulation = ManipulationType.DEEP_BLOCK    # 退盘=阻
        else:
            report.manipulation = ManipulationType.DEEP_BLOCK
    else:  # 球半+
        if report.line_change == LineDirection.DEEPENED:
            report.manipulation = ManipulationType.DEEP_LURE
        else:
            report.manipulation = ManipulationType.DEEP_BLOCK

    # ---- Risk & Signal ----
    if report.manipulation == ManipulationType.SHALLOW_LURE:
        report.risk_level = "高风险"
        report.confidence = "high"
        report.signal = (
            f"浅诱盘: {fav_side}只让{abs_line:.2f}球，赢球即赢盘→便宜盘。"
            f"庄家制造\"稳赢\"假象吸引资金。此盘型冷门高发区，"
            f"尤其是{report.line_change.value}配合{report.water_change}时。"
        )
        report.bet_suggestion = f"⚠️ 避开{fav_side}，考虑反向或放弃"
    elif report.manipulation == ManipulationType.DEEP_LURE:
        report.risk_level = "中风险"
        report.confidence = "medium"
        report.signal = (
            f"深诱盘: {fav_side}让{abs_line:.2f}球(深盘)，且{report.line_change.value}"
            f"+{report.water_change}。庄家强化大胜信心→诱盘。"
            f"大概率赢球输盘——{fav_side}能赢但穿不了{abs_line:.2f}球。"
        )
        report.bet_suggestion = f"{fav_side}可能小胜，不追穿盘"
    elif report.manipulation == ManipulationType.SHALLOW_BLOCK:
        report.risk_level = "中风险"
        report.confidence = "low"
        report.signal = (
            f"浅阻盘: {fav_side}浅开{abs_line:.2f}球，"
            f"配合{report.line_change.value}+{report.water_change}。"
            f"[7230场回测: 赢球率47%→无统计优势，不做方向推荐]"
        )
        report.bet_suggestion = f"无明确信号，建议跳过或结合基本面"
    elif report.manipulation == ManipulationType.DEEP_BLOCK:
        report.risk_level = "低风险"
        report.confidence = "high" if report.line_change == LineDirection.SHALLOWER else "medium"
        report.signal = (
            f"深阻盘: {fav_side}让{abs_line:.2f}球(深盘)，"
            f"高门槛阻挡。{fav_side}赢球率73%但穿盘率仅47%。"
            f"[7230场回测: 赢球73.4%, 穿盘46.7%→1X2可信,AH慎追]"
        )
        report.bet_suggestion = f"{fav_side}1X2方向，不追穿盘"
    elif report.manipulation == ManipulationType.DEEP_LURE:
        report.risk_level = "中风险"
        report.confidence = "high"
        report.signal = (
            f"深诱盘: {fav_side}让{abs_line:.2f}球(深盘)，"
            f"且{report.line_change.value}+{report.water_change}。"
            f"[7230场回测: 赢球67.7%, 穿盘仅38.7%→经典赢球输盘]"
        )
        report.bet_suggestion = f"{fav_side}能赢但穿不了{abs_line:.2f}球"
    else:
        report.risk_level = "中风险"
        report.signal = (
            f"均衡盘: 无明显阻诱信号。"
            f"[7230场回测: 穿盘54.3%→正常水平，按基本面判断]"
        )
        report.bet_suggestion = "参考1X2方向"

    return report


def calibrate(report: AdvancedAH, underdog_odds: float, injuries_fav: int = 0,
              injuries_dog: int = 0, form_edge: str = "") -> AdvancedAH:
    """Calibrate manipulation type using fundamental factors.

    Key calibrations:
    1. Massive underdog (odds > 10.0): deep handicap = genuine, not lure
    2. Stable line + stable water: market consensus, less manipulation
    3. Significant injuries to favorite: downgrade bullish signals
    """
    # ---- Rule 1: Massive gap = genuine strength, not manipulation ----
    if underdog_odds > 10.0 and report.manipulation in (
        ManipulationType.DEEP_LURE, ManipulationType.DEEP_BLOCK
    ):
        old = report.manipulation.value
        report.manipulation = ManipulationType.NEUTRAL
        report.confidence = "high"
        report.signal = (
            f"[校准] 原判{old}，但弱旅赔率>{underdog_odds:.0f}→实力差距真实。"
            f"深盘是实力体现，非庄家操纵。按实力盘处理。"
        )
        report.bet_suggestion = "实力差距确认，热门方向可信"

    # ---- Rule 2: Stable line = market consensus ----
    if (report.line_change == LineDirection.STABLE 
        and report.water_change == "稳定"
        and report.manipulation in (ManipulationType.DEEP_BLOCK, ManipulationType.NEUTRAL)):
        report.signal += (
            " 盘口水位双稳定→市场共识强，无操纵迹象。结合基本面正常判断。"
        )

    # ---- Rule 3: Trapped between deep lure and genuine ----
    if (report.manipulation == ManipulationType.DEEP_LURE 
        and report.line_change == LineDirection.DEEPENED
        and report.water_change == "降水"):
        # This pattern is ambiguous — could be lure OR genuine steam
        report.signal += (
            " ⚠️ 升盘+降水=经典诱盘信号，但如果基本面碾压"
            "（弱旅赔率>10或伤停严重），则是真实资金涌入。需交叉验证必发成交量。"
        )

    # ---- Rule 4: Injuries downgrade ----
    if injuries_fav >= 2:
        report.confidence = "low"
        report.signal += f" ⚠️ 热门方{injuries_fav}人伤停→实力打折，降级处理。"

    # ---- Rule 5: Non-elite favorite + deep handicap = over-aggressive ----
    # Use odds RATIO (fav/underdog) instead of absolute odds.
    # Ratio < 0.2 = massive gap = genuine. Ratio > 0.25 = narrower = questionable.
    fav_odds = report.home_odds if report.home_odds < report.away_odds else report.away_odds
    abs_line = abs(report.close_line)
    odds_ratio = fav_odds / underdog_odds if underdog_odds > 0 else 1.0

    if abs_line >= 1.0 and odds_ratio > 0.20:  # not a massive gap
        if odds_ratio > 0.30 or (fav_odds >= 1.30 and abs_line >= 1.0):
            report.manipulation = ManipulationType.DEEP_LURE
            report.risk_level = "中风险"
            report.signal += (
                f" ⚠️ 赔率比{fav_odds:.2f}/{underdog_odds:.0f}={odds_ratio:.2f}(>0.20)"
                f"+深盘{abs_line:.2f}球→盘口偏深，非碾压局。大概率赢球输盘。"
            )
            report.bet_suggestion = "1X2可考虑，但AH穿盘概率低"

    # ---- Rule 6: Ultra-deep handicap (>2.0) + massive gap = genuine ----
    if abs_line >= 2.0 and odds_ratio < 0.10:
        report.manipulation = ManipulationType.NEUTRAL
        report.confidence = "high"
        report.signal += (
            f" 超深盘{abs_line:.2f}+赔率比{odds_ratio:.2f}→碾压局，穿盘可信。"
        )

    return report
