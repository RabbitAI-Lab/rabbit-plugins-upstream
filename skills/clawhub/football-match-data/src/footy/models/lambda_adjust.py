"""泊松系数修正 — 战意/伤病/天气调整预期进球λ.

Based on professional analysis framework:
  - 战意: 德比/保级/争冠 → λ ± 5-15%
  - 伤病: 头号射手缺阵 → λ -15-20%
  - 天气: 大雨/雪 → λ × 0.85
  - 赛程: 一周双赛 → 下半场防守减弱

Apply these as multipliers to the base Poisson lambda for more accurate
O/U and score predictions.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class MatchContext:
    """Contextual factors that affect goal expectations."""

    # Motivation (战意)
    is_derby: bool = False          # 德比战 → +10% goals
    is_relegation_fight: bool = False  # 保级战 → +10% intensity
    is_title_decider: bool = False    # 争冠关键 → +5% attacking
    is_dead_rubber: bool = False      # 无欲无求 → -10% intensity
    must_win_home: bool = False       # 主队必须赢 → +5% attacking
    must_win_away: bool = False       # 客队必须赢 → +5% attacking

    # Injuries (伤病)
    home_key_attacker_out: bool = False  # 主队核心射手缺阵
    away_key_attacker_out: bool = False  # 客队核心射手缺阵
    home_key_defender_out: bool = False  # 主队核心后卫缺阵
    away_key_defender_out: bool = False  # 客队核心后卫缺阵

    # Conditions (环境)
    heavy_rain: bool = False         # 大雨 → 球速慢, 失误多
    extreme_heat: bool = False       # 高温 → 体能消耗大
    fixture_congestion_home: bool = False  # 主队一周双赛
    fixture_congestion_away: bool = False  # 客队一周双赛

    # Match type
    cup_knockout: bool = False       # 杯赛淘汰赛 → 谨慎保守
    early_season: bool = False       # 赛季初 → 防守未磨合
    late_season: bool = False        # 赛季末 → 体能下降


def adjust_lambda(
    base_lam_home: float,
    base_lam_away: float,
    ctx: MatchContext,
) -> tuple[float, float, dict]:
    """Adjust Poisson lambda based on match context.

    Returns (adjusted_lam_home, adjusted_lam_away, adjustments_log).
    """
    adj_home = 1.0
    adj_away = 1.0
    log = []

    # ---- Motivation adjustments ----
    if ctx.is_derby:
        adj_home += 0.10
        adj_away += 0.10
        log.append("德比战: λ+10%")
    if ctx.is_relegation_fight:
        adj_home += 0.10
        adj_away += 0.10
        log.append("保级战: λ+10%")
    if ctx.is_title_decider:
        adj_home += 0.05
        adj_away += 0.05
        log.append("争冠战: λ+5%")
    if ctx.is_dead_rubber:
        adj_home -= 0.10
        adj_away -= 0.10
        log.append("无欲无求: λ-10%")
    if ctx.must_win_home:
        adj_home += 0.05
        log.append("主队必须赢: 主场λ+5%")
    if ctx.must_win_away:
        adj_away += 0.05
        log.append("客队必须赢: 客场λ+5%")

    # ---- Injury adjustments ----
    if ctx.home_key_attacker_out:
        adj_home -= 0.18
        log.append("主队射手缺阵: 主场λ-18%")
    if ctx.away_key_attacker_out:
        adj_away -= 0.18
        log.append("客队射手缺阵: 客场λ-18%")
    if ctx.home_key_defender_out:
        adj_away += 0.10  # opponent scores more
        log.append("主队后卫缺阵: 客场λ+10%")
    if ctx.away_key_defender_out:
        adj_home += 0.10
        log.append("客队后卫缺阵: 主场λ+10%")

    # ---- Weather conditions ----
    if ctx.heavy_rain:
        adj_home *= 0.85
        adj_away *= 0.85
        log.append("大雨: λ×0.85")
    if ctx.extreme_heat:
        adj_home *= 0.90
        adj_away *= 0.90
        log.append("高温: λ×0.90")

    # ---- Fixture congestion ----
    if ctx.fixture_congestion_home:
        adj_home *= 0.92
        log.append("主队一周双赛: 主场λ×0.92")
    if ctx.fixture_congestion_away:
        adj_away *= 0.92
        log.append("客队一周双赛: 客场λ×0.92")

    # ---- Match type ----
    if ctx.cup_knockout:
        adj_home *= 0.90
        adj_away *= 0.90
        log.append("杯赛淘汰赛: λ×0.90")
    if ctx.early_season:
        adj_home += 0.05
        adj_away += 0.05
        log.append("赛季初: λ+5%")
    if ctx.late_season:
        adj_home *= 0.93
        adj_away *= 0.93
        log.append("赛季末: λ×0.93")

    # Apply adjustments
    lam_home = base_lam_home * max(0.5, adj_home)
    lam_away = base_lam_away * max(0.5, adj_away)

    return lam_home, lam_away, log
