"""Odds-market signal engine — encode analyst know-how as structured signals.

Four pillars of Chinese football betting analysis (from earlier web research):
  1. Kelly variance  — dispersion across bookmakers (low = consensus)
  2. Odds dispersion — standard deviation of implied probs (high + skew = upset)
  3. Asian handicap interpretation (line+water movement patterns)
  4. Market direction — which side the market is tilting toward

These signals are supplementary, not deterministic. They are shown alongside
the statistical model output for the user's holistic judgment.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Sequence


# ---------------------------------------------------------------------------
# 1. Kelly variance — industry-standard "how much do bookies agree?"
# ---------------------------------------------------------------------------

def kelly_index(odds: float, fair_prob: float) -> float:
    """Kelly index for one bookmaker on one outcome = odds × fair_prob - 1."""
    return odds * fair_prob - 1.0


def kelly_variance(odds_list: Sequence[float], fair_prob: float) -> dict:
    """Compute Kelly index for each bookmaker, then return variance stats.

    Low variance = bookmakers are in agreement on this outcome (strong signal).
    High variance = disagreement, possibly a volatile match.

    fair_prob should be the de-vigged probability from a reference book (e.g. PS).
    """
    kellys = [kelly_index(o, fair_prob) for o in odds_list if o and o > 0]
    if len(kellys) < 2:
        return {"mean_kelly": None, "variance": None, "signal": "insufficient_data"}
    mean_k = sum(kellys) / len(kellys)
    var_k = sum((k - mean_k) ** 2 for k in kellys) / len(kellys)
    if var_k < 0.005:
        signal = "high_consensus"
    elif var_k < 0.02:
        signal = "moderate_agreement"
    else:
        signal = "divergent — potential upset alert"
    return {"mean_kelly": round(mean_k, 4), "variance": round(var_k, 6), "signal": signal}


# ---------------------------------------------------------------------------
# 2. Implied-probability dispersion — "赔率离散度"
# ---------------------------------------------------------------------------

def odds_dispersion(
    odds_1x2: dict[str, tuple[float, float, float]],
    outcome_idx: int,
) -> dict:
    """Standard deviation of implied probabilities across bookmakers for one outcome.

    High dispersion + skew toward the favourite = classic cold-warning pattern:
    "高离散+正偏态 = 冷门预警" (from research results).
    """
    probs = []
    for bm, odds in odds_1x2.items():
        o = odds[outcome_idx]
        if o and o > 0:
            probs.append(1.0 / o)
    if len(probs) < 2:
        return {"std": None, "signal": "insufficient_data"}
    mean_p = sum(probs) / len(probs)
    std_p = math.sqrt(sum((p - mean_p) ** 2 for p in probs) / len(probs))
    cv = std_p / mean_p if mean_p > 0 else 0  # coefficient of variation

    if std_p < 0.01:
        signal = "tight — bookmakers in lockstep"
    elif std_p < 0.03:
        signal = "normal spread"
    else:
        signal = "wide dispersion — cold upset risk elevated"
    return {
        "std_dev": round(std_p, 4),
        "mean_prob": round(mean_p, 4),
        "cv": round(cv, 4),
        "signal": signal,
    }


# ---------------------------------------------------------------------------
# 3. Asian handicap pattern interpretation — "盘口分析口诀"
# ---------------------------------------------------------------------------

@dataclass
class AsianHandicapSignal:
    """Result of analysing a handicap line + water level movement."""

    pattern: str  # e.g. "升盘降水", "降盘升水"
    direction: str  # "favors_upper" | "favors_lower" | "uncertain"
    interpretation: str  # human-readable analysis
    confidence: str  # "high" | "medium" | "low"


# The classic four combinations from the research:
#   升盘降水看时间  → if early → genuine favour; if late → trap
#   降盘降水观走势  → watch fund flow direction
#   升盘升水走水位  → likely baiting public money
#   降盘升水多开上  → upper side (home/favourite) has value
_HANDICAP_RULES = {
    "line_up_water_down": AsianHandicapSignal(
        pattern="升盘降水 (line up, water down)",
        direction="favors_upper",
        interpretation=(
            "门槛提高+水位降低=双重看强信号。若发生在受注早期(开盘后1-2小时)则"
            "为真实看好；若临近开赛则需警惕诱盘。判断标准: 看时间窗口。"
        ),
        confidence="high",
    ),
    "line_down_water_down": AsianHandicapSignal(
        pattern="降盘降水 (line down, water down)",
        direction="uncertain",
        interpretation=(
            "盘口降低+水位降低=反常组合(低盘口+低价暗示热门)。需结合资金流向判断:"
            "若下盘有大资金涌入则庄家被动降盘=下盘机会；若无资金异常则为诱下。"
        ),
        confidence="medium",
    ),
    "line_up_water_up": AsianHandicapSignal(
        pattern="升盘升水 (line up, water up)",
        direction="favors_lower",
        interpretation=(
            "盘口提高+水位提高=高门槛+高价=庄家给上盘高回报吸引资金。"
            "常见诱盘手法，意图制造'上盘很强'的假象吸引投注。"
            "口诀: 升盘升水走水位 → 跟水位方向走。"
        ),
        confidence="medium",
    ),
    "line_down_water_up": AsianHandicapSignal(
        pattern="降盘升水 (line down, water up)",
        direction="favors_upper",
        interpretation=(
            "盘口降低+水位升高=浅盘高水，经典阻上诱下格局。"
            "庄家制造'上盘不稳'假象，真实意图是保护上盘打出。"
            "口诀: 降盘升水多开上 → 上盘打出概率较高。"
        ),
        confidence="high",
    ),
}


def classify_handicap_movement(
    line_change: float,  # positive = line went up (harder for upper to cover)
    water_change: float,  # positive = water/payout went up
) -> AsianHandicapSignal | None:
    """Classify a handicap line+water movement into one of the four classic patterns."""
    threshold = 0.0  # any move counts; set > 0 for noise filter
    if abs(line_change) < 0.05 and abs(water_change) < 0.01:
        return None  # no material movement

    if line_change > threshold and water_change < -threshold:
        return _HANDICAP_RULES["line_up_water_down"]
    if line_change < -threshold and water_change < -threshold:
        return _HANDICAP_RULES["line_down_water_down"]
    if line_change > threshold and water_change > threshold:
        return _HANDICAP_RULES["line_up_water_up"]
    if line_change < -threshold and water_change > threshold:
        return _HANDICAP_RULES["line_down_water_up"]
    return None


# ---------------------------------------------------------------------------
# 3.5. Line movement — opening→closing odds shift (初盘→终盘变化)
# ---------------------------------------------------------------------------

@dataclass
class LineMovementSignal:
    bookmarker: str
    direction: str  # "steam_home" | "steam_draw" | "steam_away" | "stable"
    magnitude: str  # "strong" (>0.10) | "moderate" (>0.03) | "none"
    confidence_boost: bool  # does this signal INCREASE prediction confidence?
    interpretation: str


def analyze_line_movement(
    odds_open: tuple[float, float, float] | None,
    odds_close: tuple[float, float, float] | None,
    book: str = "PS",
    actual_result: str | None = None,
) -> LineMovementSignal | None:
    """Analyze open-to-close line movement for one bookmaker.

    When odds DROP on a side and that side WINS, it's market confirmation
    (steam = sharp money knew). This is the strongest accuracy booster.

    When odds RISE on a side and it wins, it's a reverse move (market was wrong)
    — great for value, not great for pure accuracy.
    """
    if not odds_open or not odds_close:
        return None
    moves = [odds_close[i] - odds_open[i] for i in range(3)]
    max_drop = min(moves)
    max_rise = max(moves)

    if abs(max_drop) < 0.03 and abs(max_rise) < 0.03:
        return LineMovementSignal(
            bookmarker=book, direction="stable", magnitude="none",
            confidence_boost=False,
            interpretation="盘口稳定，无资金方向信号",
        )

    steam_idx = moves.index(max_drop) if abs(max_drop) > abs(max_rise) else moves.index(max_rise)
    steam_side = ["home", "draw", "away"][steam_idx]
    is_drop = moves[steam_idx] < 0
    mag = "strong" if abs(moves[steam_idx]) > 0.10 else "moderate"

    direction = f"{'steam' if is_drop else 'drift'}_{steam_side}"

    # Confidence boost: only when steam direction matches actual winner
    outcomes = ["H", "D", "A"]
    boost = (
        is_drop
        and actual_result is not None
        and steam_side == {"H": "home", "D": "draw", "A": "away"}[actual_result]
    )

    side_cn = {"home": "主队(上盘)", "draw": "平局", "away": "客队(下盘)"}[steam_side]
    if is_drop:
        interp = (
            f"资金涌向{side_cn}（赔率下降{abs(moves[steam_idx]):.2f}），"
            f"市场真金白银看好{'✅ 与实际赛果一致' if boost else ''}"
        )
    else:
        interp = (
            f"{side_cn}赔率上升{moves[steam_idx]:.2f}，"
            f"资金远离该方向{'⚠️ 逆向变动' if boost else ''}"
        )

    return LineMovementSignal(
        bookmarker=book, direction=direction, magnitude=mag,
        confidence_boost=boost, interpretation=interp,
    )


# ---------------------------------------------------------------------------
# 4. Market direction — which side is getting sharper?
# ---------------------------------------------------------------------------

@dataclass
class MarketAnalysis:
    """Full market analysis for a single match."""

    home: str
    away: str
    # Kelly variance per outcome
    kelly_var_h: dict = field(default_factory=dict)
    kelly_var_d: dict = field(default_factory=dict)
    kelly_var_a: dict = field(default_factory=dict)
    # Dispersion per outcome
    dispersion_h: dict = field(default_factory=dict)
    dispersion_d: dict = field(default_factory=dict)
    dispersion_a: dict = field(default_factory=dict)
    # Overall market verdict
    verdict: str = ""
    warnings: list[str] = field(default_factory=list)


def analyze_market(
    odds_1x2: dict[str, tuple[float, float, float]],
    fair_probs: tuple[float, float, float] | None = None,
) -> MarketAnalysis:
    """Run the full signal suite on a match's closing odds.

    odds_1x2: {bookmaker_prefix: (home_odds, draw_odds, away_odds)}
    fair_probs: de-vigged Pinnacle probabilities (if None, de-vig from PS or Avg).
    """
    bookmakers = list(odds_1x2)
    if len(bookmakers) < 2:
        return MarketAnalysis(
            home="?", away="?", verdict="insufficient bookmakers for cross-validation",
        )

    # De-vig a reference baseline: prefer PS, fallback to Avg or Max.
    ref_key = "PS" if "PS" in odds_1x2 else ("Avg" if "Avg" in odds_1x2 else bookmakers[0])
    ref_odds = odds_1x2[ref_key]
    if fair_probs is None:
        from .value import devig as _devig
        fair_probs = _devig(ref_odds)

    warnings: list[str] = []

    # Kelly variance for each outcome
    kv_h = kelly_variance(
        [odds_1x2[b][0] for b in bookmakers if b in odds_1x2],
        fair_probs[0],
    )
    kv_d = kelly_variance(
        [odds_1x2[b][1] for b in bookmakers if b in odds_1x2],
        fair_probs[1],
    )
    kv_a = kelly_variance(
        [odds_1x2[b][2] for b in bookmakers if b in odds_1x2],
        fair_probs[2],
    )
    if kv_h.get("signal", "").startswith("divergent"):
        warnings.append(f"Home Kelly divergent: {kv_h['variance']:.6f}")
    if kv_d.get("signal", "").startswith("divergent"):
        warnings.append(f"Draw Kelly divergent: {kv_d['variance']:.6f}")
    if kv_a.get("signal", "").startswith("divergent"):
        warnings.append(f"Away Kelly divergent: {kv_a['variance']:.6f}")

    # Dispersion for each outcome
    disp_h = odds_dispersion(odds_1x2, 0)
    disp_d = odds_dispersion(odds_1x2, 1)
    disp_a = odds_dispersion(odds_1x2, 2)

    # Cold upset check: high dispersion + skew (disproportionately high prob on outsider)
    if (
        disp_a.get("signal", "").startswith("wide dispersion")
        and fair_probs[2] > fair_probs[0] * 0.7
    ):
        warnings.append(
            "COLD UPSET ALERT: away-side wide dispersion with elevated probability"
        )

    verdict = "normal" if not warnings else "⚠️ anomalous — see warnings"

    return MarketAnalysis(
        home="", away="",
        kelly_var_h=kv_h, kelly_var_d=kv_d, kelly_var_a=kv_a,
        dispersion_h=disp_h, dispersion_d=disp_d, dispersion_a=disp_a,
        verdict=verdict, warnings=warnings,
    )


# ---------------------------------------------------------------------------
# 5. "阻、控、诱" — professional Asian handicap intent detection
# ---------------------------------------------------------------------------

@dataclass
class HandicapIntent:
    """Bookmaker intent behind the handicap line + water level."""

    intent: str  # "阻" | "控" | "诱"
    target_side: str  # "上盘" | "下盘" | "均衡"
    interpretation: str
    confidence: str  # "high" | "medium" | "low"


def detect_handicap_intent(
    handicap_line: float,           # e.g. -0.5, -1.0
    model_goal_diff: float,         # model predicted (home - away) goals
    home_water: float | None = None,# payout for upper side
    away_water: float | None = None,# payout for lower side
) -> HandicapIntent | None:
    """Classify bookmaker intent using the professional '阻/控/诱' framework.

    阻 (Block):   line is deeper than justified → blocking upper → upper has value
    控 (Control): line close to fair, water tight → balanced, no signal
    诱 (Lure):    line is shallower + high water → luring money → opposite side

    handicap_line is from the upper-side perspective (negative = upper favored).
    model_goal_diff is (home_goals - away_goals) from the model.
    """
    if model_goal_diff is None or handicap_line is None:
        return None

    fair_line = -model_goal_diff  # upper favoured by X goals
    gap = handicap_line - fair_line  # positive = line deeper than fair

    water_spread = None
    if home_water is not None and away_water is not None and home_water > 0 and away_water > 0:
        water_spread = home_water - away_water

    # High confidence signals
    if gap > 0.5 and water_spread is not None and water_spread < -0.05:
        # Deep line + upper water low = classic 阻上
        return HandicapIntent(
            intent="阻",
            target_side="上盘",
            interpretation=(
                f"盘口深开{gap:+.2f}球+上盘低水({home_water:.2f})，典型的阻上格局。"
                "庄家真实意图：保护上盘打出。口诀：深盘低水阻上。"
            ),
            confidence="high",
        )
    if gap < -0.3 and water_spread is not None and water_spread > 0.05:
        # Shallow line + upper water high = classic 诱上
        return HandicapIntent(
            intent="诱",
            target_side="下盘",
            interpretation=(
                f"盘口浅开{gap:+.2f}球+上盘高水({home_water:.2f})，典型的诱上格局。"
                "庄家真实意图：驱赶资金到下盘。口诀：浅盘高水诱上。"
            ),
            confidence="high",
        )

    # Medium confidence
    if abs(gap) < 0.3 and water_spread is not None and abs(water_spread) < 0.03:
        return HandicapIntent(
            intent="控",
            target_side="均衡",
            interpretation=(
                "盘口接近合理价位，水位紧贴，庄家控盘均衡。"
                "无明显阻诱信号，需结合基本面判断。"
            ),
            confidence="medium",
        )

    # Lower confidence
    if gap > 0.3:
        return HandicapIntent(
            intent="阻",
            target_side="上盘",
            interpretation=(
                f"盘口偏深{gap:+.2f}球，庄家设高门槛阻挡上盘资金。"
                "上盘阻力大但真实看好。需结合水位确认。"
            ),
            confidence="medium",
        )
    if gap < -0.3:
        return HandicapIntent(
            intent="诱",
            target_side="下盘",
            interpretation=(
                f"盘口偏浅{gap:+.2f}球，庄家降低门槛吸引上盘资金。"
                "小心诱盘陷阱，下盘更有价值。"
            ),
            confidence="medium",
        )

    return HandicapIntent(
        intent="控",
        target_side="均衡",
        interpretation="盘口无明显异常，按基本面模型判断。",
        confidence="low",
    )


# ---------------------------------------------------------------------------
# 6. Kelly direction — which side do bookmakers collectively favor?
# ---------------------------------------------------------------------------

def kelly_direction(
    odds_1x2: dict[str, tuple[float, float, float]],
    fair_probs: tuple[float, float, float],
) -> dict:
    """Which outcome has the lowest (most favorable) average Kelly index?

    Lower Kelly = bookmaker more willing to take risk on that outcome.
    This is the professional insight: "凯利指数越低=庄家越看好".
    """
    avg_k = {"H": 0.0, "D": 0.0, "A": 0.0}
    counts = {"H": 0, "D": 0, "A": 0}
    for book, odds in odds_1x2.items():
        for idx, outcome in enumerate(("H", "D", "A")):
            if odds[idx] > 0 and fair_probs[idx] > 0:
                k = odds[idx] * fair_probs[idx] - 1.0
                avg_k[outcome] += k
                counts[outcome] += 1

    for o in avg_k:
        if counts[o] > 0:
            avg_k[o] /= counts[o]

    best = min(avg_k, key=lambda o: avg_k[o])
    worst = max(avg_k, key=lambda o: avg_k[o])

    interpretation = (
        f"庄家最看好: {best} (凯利 {avg_k[best]:.4f})，"
        f"最不看好: {worst} (凯利 {avg_k[worst]:.4f})。"
        f"凯利指数越低=庄家承担赔付风险意愿越高=越看好该结果。"
    )

    return {
        "avg_kelly": avg_k,
        "best_outcome": best,
        "worst_outcome": worst,
        "interpretation": interpretation,
    }
