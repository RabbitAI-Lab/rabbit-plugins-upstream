"""赔率骨架分类器 — from《足彩投资：赔率核心思维》纳兰老九.

Classifies odds into three types based on their position within the standard
European-to-Asian handicap interval:

  实盘 (Real):  odds align with fundamentals → market is honest
  韬盘 (Hidden): odds deviate to hide true intent → trap signal
  中庸盘 (Neutral): odds at equilibrium → no edge either way

Also: 分布理论 — identifies market force direction:
  顺分布: public money follows fundamentals
  逆分布: public money goes against fundamentals → contrarian signal
  中庸分布: balanced forces
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


# Standard odds skeleton intervals (from《赔率核心思维》)
# Each interval has: (lo, hi, center, standard_AH)
# The "center" is the equilibrium point within the interval.
SKELETON_INTERVALS = [
    # (odds_lo, odds_hi, center_odds, description)
    (1.10, 1.15, 1.125, "深盘区"),
    (1.15, 1.22, 1.185, "球半/两球区"),
    (1.22, 1.30, 1.260, "球半区"),
    (1.30, 1.40, 1.350, "一球/球半区"),
    (1.40, 1.53, 1.465, "一球区"),
    (1.53, 1.70, 1.615, "半一区"),
    (1.70, 1.90, 1.800, "半球区"),
    (1.90, 2.10, 2.000, "平半区"),
    (2.10, 2.40, 2.250, "平手区"),
    (2.40, 2.80, 2.600, "平手高水区"),
    (2.80, 3.50, 3.150, "受让区"),
]


@dataclass
class OddsSkeleton:
    """Analysis of odds position within the skeleton framework."""

    odds: float              # the analyzed odds value
    interval_name: str = "" # which skeleton interval
    center_odds: float = 0.0 # equilibrium point
    deviation_pct: float = 0.0  # % deviation from center
    
    # Classification
    skeleton_type: str = ""  # 实盘 / 韬盘 / 中庸盘
    
    # Distribution (market forces)
    distribution: str = ""   # 顺分布 / 逆分布 / 中庸分布
    
    # Interpretation
    signal: str = ""
    confidence: str = ""  # high / medium / low
    
    # Raw data
    multi_book_avg: float = 0.0  # average across bookmakers
    multi_book_std: float = 0.0  # std dev across bookmakers


def classify_skeleton(
    odds: float,
    multi_book_data: Optional[dict] = None,  # {book_name: (h, d, a)}
    steam_direction: str = "stable",
    steam_magnitude: float = 0.0,
) -> OddsSkeleton:
    """Analyze an odds value within the skeleton framework.
    
    odds: the reference odds (e.g., Pinnacle or Bet365)
    multi_book_data: if provided, compute consensus metrics
    steam_direction: 'H'/'D'/'A'/'stable' — which way odds moved
    steam_magnitude: size of odds movement
    """
    sk = OddsSkeleton(odds=odds)
    
    # ---- Step 1: Identify skeleton interval ----
    for lo, hi, center, name in SKELETON_INTERVALS:
        if lo <= odds < hi:
            sk.interval_name = name
            sk.center_odds = center
            break
    
    if not sk.interval_name:
        # Extrapolate for extreme odds
        if odds < 1.10:
            sk.interval_name = "超深盘区"
            sk.center_odds = 1.08
        else:
            sk.interval_name = "超受让区"
            sk.center_odds = 4.0
    
    # ---- Step 2: Deviation from center ----
    if sk.center_odds > 0:
        sk.deviation_pct = (odds - sk.center_odds) / sk.center_odds
    
    # ---- Step 3: Multi-book consensus (only the analyzed side) ----
    if multi_book_data:
        values = [tup[0] if tup[0] < tup[2] else tup[2] 
                  for tup in multi_book_data.values() 
                  if tup[0] > 0 and tup[2] > 0]
        if len(values) >= 3:
            import statistics
            sk.multi_book_avg = statistics.mean(values)
            sk.multi_book_std = statistics.stdev(values)
    else:
        sk.multi_book_std = 0.0
    
    # ---- Step 4: Classify skeleton type ----
    # 实盘: near center + tight consensus + stable steam
    # 韬盘: far from center OR wide consensus OR significant steam
    
    near_center = abs(sk.deviation_pct) < 0.03
    tight_consensus = sk.multi_book_std > 0 and sk.multi_book_std < 0.08
    no_steam = steam_magnitude < 0.04
    
    if near_center and (tight_consensus or sk.multi_book_std == 0) and no_steam:
        sk.skeleton_type = "实盘"
        sk.confidence = "high"
        sk.signal = "赔率在骨架中心，庄家诚实开盘。按基本面正常判断。"
    elif abs(sk.deviation_pct) > 0.08 or (sk.multi_book_std > 0.12) or steam_magnitude > 0.10:
        sk.skeleton_type = "韬盘"
        sk.confidence = "high" if steam_magnitude > 0.10 else "medium"
        # Sub-classify: 韬高 or 韬低
        if sk.deviation_pct > 0.05:
            sk.signal = (
                f"赔率偏高({sk.deviation_pct:+.1%})偏离骨架中心{sk.center_odds:.2f}。"
                f"韬高——庄家抬高赔率制造不稳。需结合盘口判断真实意图。"
            )
        elif sk.deviation_pct < -0.05:
            sk.signal = (
                f"赔率偏低({sk.deviation_pct:+.1%})偏离骨架中心{sk.center_odds:.2f}。"
                f"韬低——庄家压低赔率吸筹。警惕诱盘。"
            )
        else:
            sk.signal = (
                f"多公司分歧大(σ={sk.multi_book_std:.3f})或Steam显著。"
                f"庄家控盘意图明显。结合必发+盘口综合判断。"
            )
    else:
        sk.skeleton_type = "中庸盘"
        sk.confidence = "low"
        sk.signal = "赔率在中庸区间，无明显韬实偏斜。需其他维度辅助判断。"

    # ---- Step 5: Distribution (market forces) ----
    if steam_magnitude > 0.05:
        if sk.deviation_pct > 0 and steam_direction not in ("stable",):
            # Odds rising + steam going opposite = 逆分布
            sk.distribution = "逆分布"
        elif sk.deviation_pct < 0 and steam_direction not in ("stable",):
            # Odds dropping + steam confirming = 顺分布
            sk.distribution = "顺分布"
        else:
            sk.distribution = "中庸分布"
    else:
        sk.distribution = "中庸分布"

    return sk


def skeleton_summary(sk: OddsSkeleton) -> str:
    """One-line summary for display."""
    return (
        f"[{sk.interval_name}] {sk.skeleton_type} "
        f"({sk.deviation_pct:+.1%} off center) | "
        f"{sk.distribution} | {sk.confidence}"
    )
