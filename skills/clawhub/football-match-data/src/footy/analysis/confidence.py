"""High-confidence bet filter — quality over quantity.

Combines model probability, bookmaker consensus, and line movement to score
each potential bet. Only those above threshold are shown.

Design principle: the user wants FEW high-accuracy picks, not MANY noisy ones.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from ..data.schema import Match


@dataclass
class ConfidentPick:
    """A bet that passes the multi-dimensional confidence filter."""

    match: Match
    outcome: str  # "H", "D", or "A"
    side_label: str  # e.g. "Arsenal (上盘)" or "Fulham (下盘)"
    model_prob: float
    odds: float
    edge: float
    ev: float
    kelly_stake: float  # full-Kelly units for 100u bankroll
    pick_type: str = ""  # "稳胆" | "博胆"

    # Confidence components (0-100 each)
    prob_score: float = 0.0
    steam_score: float = 0.0
    consensus_score: float = 0.0
    edge_score: float = 0.0
    total_score: float = 0.0

    # Signal details for display
    steam_direction: str = ""
    kelly_variance_signal: str = ""
    dispersion_signal: str = ""


def _safe_book(m: Match, book: str = "PS") -> tuple | None:
    """Get closing odds for a book, falling back to any available."""
    if book in m.odds_1x2:
        return m.odds_1x2[book]
    for b in m.odds_1x2:
        return m.odds_1x2[b]
    return None


def score_picks(
    matches: list[Match],
    model_predictions: dict[str, dict],
    min_prob: float = 0.50,
    min_edge: float = 0.03,
    min_total_score: float = 60.0,
    max_picks: int = 5,
) -> list[ConfidentPick]:
    """Score and filter all potential bets, returning only the best.

    model_predictions: {(home, away): model_1x2_probs} mapping.
    """
    from .odds_signals import analyze_line_movement

    picks: list[ConfidentPick] = []

    for m in matches:
        key = (m.home, m.away)
        if key not in model_predictions:
            continue
        probs = model_predictions[key]
        close = _safe_book(m)
        if not close:
            continue

        open_odds = m.odds_open_1x2.get("PS") or m.odds_open_1x2.get(list(m.odds_open_1x2)[0]) if m.odds_open_1x2 else None

        # ---- Line movement signal ----
        lm = analyze_line_movement(open_odds, close, book="PS", actual_result=m.result)

        # ---- Kelly variance (consensus) ----
        from .odds_signals import kelly_variance as _kv
        kv = {0: None, 1: None, 2: None}
        for idx in range(3):
            odds_list = [o[idx] for o in m.odds_1x2.values() if o[idx] and o[idx] > 0]
            if len(odds_list) >= 2:
                kv[idx] = _kv(odds_list, 1.0 / close[idx])  # rough fair prob

        # ---- Dispersion ----
        from .odds_signals import odds_dispersion as _od
        disp = {
            0: _od(m.odds_1x2, 0) if len(m.odds_1x2) >= 2 else None,
            1: _od(m.odds_1x2, 1) if len(m.odds_1x2) >= 2 else None,
            2: _od(m.odds_1x2, 2) if len(m.odds_1x2) >= 2 else None,
        }

        # ---- Score each outcome ----
        for outcome_idx, outcome in enumerate(("H", "D", "A")):
            prob = probs.get(outcome, 0)
            if prob < min_prob:
                continue
            implied = 1.0 / close[outcome_idx] if close[outcome_idx] > 0 else 1.0
            edge = prob - implied
            if edge < min_edge:
                continue

            # --- Confidence scoring (0-100 each) ---
            # 1. Probability score: model confidence in this outcome
            prob_score = min(100, prob * 100)  # 0.5 → 50, 0.85 → 85

            # 2. Steam score: line movement confirms this side
            steam_score = 0.0
            steam_dir = ""
            if lm:
                side_map = {"H": "home", "D": "draw", "A": "away"}
                if lm.direction == f"steam_{side_map[outcome]}":
                    steam_score = 30.0 if lm.magnitude == "strong" else 15.0
                    steam_dir = lm.interpretation
                elif lm.direction == "stable":
                    steam_score = 5.0
                    steam_dir = "stable"

            # 3. Consensus score: bookmakers agree on this outcome
            consensus_score = 0.0
            kv_sig = ""
            if kv[outcome_idx]:
                var = kv[outcome_idx].get("variance")
                if var is not None and var < 0.005:
                    consensus_score = 25.0
                    kv_sig = "high_consensus"
                elif var is not None and var < 0.02:
                    consensus_score = 10.0
                    kv_sig = "moderate"

            # 4. Edge score: higher edge = market more wrong
            edge_score = min(20, edge * 100)  # 0.05 → 5, 0.20 → 20

            # 5. Dispersion penalty: wide dispersion hurts confidence
            disp_penalty = 0.0
            disp_sig = ""
            if disp[outcome_idx]:
                std = disp[outcome_idx].get("std_dev") or 0
                if std > 0.03:
                    disp_penalty = 15.0
                    disp_sig = "wide dispersion"
                elif std < 0.01:
                    disp_sig = "tight"

            total = prob_score + steam_score + consensus_score + edge_score - disp_penalty

            if total < min_total_score:
                continue

            # Side label
            if outcome == "H":
                side = f"{m.home} (上盘)"
            elif outcome == "A":
                side = f"{m.away} (下盘)"
            else:
                side = "平局"

            ev = prob * close[outcome_idx] - 1.0
            kelly = (prob - implied) / (1 - implied) if implied < 1 else 0

            picks.append(
                ConfidentPick(
                    match=m, outcome=outcome, side_label=side,
                    model_prob=prob, odds=close[outcome_idx],
                    edge=edge, ev=ev, kelly_stake=kelly * 100,
                    prob_score=prob_score, steam_score=steam_score,
                    consensus_score=consensus_score, edge_score=edge_score,
                    total_score=total,
                    steam_direction=steam_dir,
                    kelly_variance_signal=kv_sig,
                    dispersion_signal=disp_sig,
                )
            )

    picks.sort(key=lambda p: p.total_score, reverse=True)
    return picks[:max_picks]


def score_picks_dual(
    matches: list[Match],
    model_predictions: dict[str, dict],
    max_each: int = 5,
) -> dict[str, list[ConfidentPick]]:
    """Run both accuracy (稳胆) and value (博胆) filters, return both lists.

    稳胆 = high hit-rate picks: model confident AND market agrees AND steam confirms.
    博胆 = high profit picks: significant edge vs market, higher risk/reward.
    """
    # ---- 稳胆: accuracy-first —— 不要求 edge，要求共识 ----
    steady = score_picks(
        matches, model_predictions,
        min_prob=0.60,      # model sure
        min_edge=-0.99,     # allow ANY edge (including negative = market more confident)
        min_total_score=50,
        max_picks=999,      # get all, then filter
    )
    # Filter for accuracy: market must ALSO be confident, steam must confirm
    steady = [
        p for p in steady
        if p.odds < 3.0                     # market implied > 33%
        and p.prob_score >= 60              # model confidence
        and p.steam_score >= 10             # steam confirms direction
    ]
    for p in steady:
        p.pick_type = "稳胆"

    # Sort by model probability (most confident first) for steady picks
    steady.sort(key=lambda p: p.model_prob, reverse=True)

    # ---- 博胆: value-first ----
    bold = score_picks(
        matches, model_predictions,
        min_prob=0.50,
        min_edge=0.05,           # significant edge required
        min_total_score=45,
        max_picks=max_each,
    )
    for p in bold:
        p.pick_type = "博胆"

    # Deduplicate
    steady_keys = {(p.match.date, p.match.home, p.match.away, p.outcome) for p in steady}
    bold = [p for p in bold if (p.match.date, p.match.home, p.match.away, p.outcome) not in steady_keys]

    return {"稳胆": steady[:max_each], "博胆": bold[:max_each]}
