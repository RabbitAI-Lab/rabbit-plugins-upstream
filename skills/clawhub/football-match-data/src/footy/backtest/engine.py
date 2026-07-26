"""Walk-forward backtesting engine.

For each test season we refit on all earlier data (no future leakage), then
predict every match in that season, settle bets at Pinnacle (PS) closing odds,
and record metrics. Refitting once per season is a good speed/accuracy
trade-off — within a season team strength moves slowly.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import date

import numpy as np

from ..data.schema import Match
from ..models.dixon_coles import DixonColesModel
from ..models.poisson import PoissonModel
from .metrics import BetRecord, BacktestReport, aggregate, rps

log = logging.getLogger(__name__)

# Settle bets at Pinnacle closing odds — the sharpest book, least likely to
# limit winners, and the standard reference for value betting research.
SETTLE_BOOK = "PS"


@dataclass
class BacktestConfig:
    min_edge: float = 0.02  # only bet when pred prob beats implied prob by >=2%
    half_life_days: float = 180.0
    model: str = "dixon-coles"  # "dixon-coles" or "poisson"


def _season_of(m: Match) -> str:
    """Map a match to its season label (e.g. 2023-24)."""
    d = date.fromisoformat(m.date)
    # European seasons cross the calendar year: July-Dec => current year season.
    if d.month >= 7:
        return f"{d.year}-{(d.year + 1) % 100:02d}"
    return f"{d.year - 1}-{d.year % 100:02d}"


def _make_model(cfg: BacktestConfig):
    if cfg.model == "poisson":
        return PoissonModel()
    return DixonColesModel(half_life_days=cfg.half_life_days)


def _best_implied(odds_1x2: dict, outcome: str) -> float | None:
    """Implied probability for an outcome using the settlement book's odds."""
    if SETTLE_BOOK in odds_1x2:
        idx = {"H": 0, "D": 1, "A": 2}[outcome]
        o = odds_1x2[SETTLE_BOOK][idx]
        return 1.0 / o if o > 0 else None
    return None


def _settle_odds(odds_1x2: dict, outcome: str) -> float | None:
    idx = {"H": 0, "D": 1, "A": 2}[outcome]
    if SETTLE_BOOK in odds_1x2:
        o = odds_1x2[SETTLE_BOOK][idx]
        return o if o > 0 else None
    return None


def run_backtest(
    matches: list[Match], cfg: BacktestConfig | None = None
) -> BacktestReport:
    cfg = cfg or BacktestConfig()
    finished = sorted([m for m in matches if m.is_finished], key=lambda m: m.date)
    if len(finished) < 200:
        raise ValueError(f"Need at least 200 finished matches, got {len(finished)}.")

    # Determine which seasons to test: leave out the earliest season(s) as the
    # initial training window so every test match has prior history.
    seasons = sorted({_season_of(m) for m in finished})
    if len(seasons) < 2:
        raise ValueError("Need matches spanning at least 2 seasons.")
    test_seasons = seasons[1:]

    bet_records: list[BetRecord] = []
    rps_values: list[float] = []
    rps_naive_values: list[float] = []
    rps_market_values: list[float] = []
    n_predicted = 0

    for season in test_seasons:
        train = [m for m in finished if _season_of(m) < season]
        test = [m for m in finished if _season_of(m) == season]
        if not train or not test:
            continue

        # Skip matches with no closing odds — can't settle them.
        test = [m for m in test if SETTLE_BOOK in m.odds_1x2]
        if not test:
            continue

        model = _make_model(cfg)
        try:
            model.fit(train)
        except Exception as exc:  # fitting can fail on degenerate slices
            log.warning("Fit failed for season %s: %s", season, exc)
            continue

        for m in test:
            if m.home not in model.params.attack or m.away not in model.params.defence:
                continue  # team not in training set (e.g. promoted) — skip
            pred = model.predict(m.home, m.away)
            p1x2 = pred["probs_1x2"]
            # Skip degenerate predictions (overflow / non-finite) so they don't
            # poison the RPS average or trigger spurious bets.
            if not all(np.isfinite(v) for v in p1x2.values()):
                continue

            # De-vigged market probabilities for the RPS-market baseline.
            mkt = _devig_market(m.odds_1x2[SETTLE_BOOK])

            rps_values.append(rps(p1x2["H"], p1x2["D"], p1x2["A"], m.result))
            rps_naive_values.append(rps(1 / 3, 1 / 3, 1 / 3, m.result))
            if mkt is not None:
                rps_market_values.append(rps(mkt[0], mkt[1], mkt[2], m.result))
            n_predicted += 1

            # Value bet on whichever of H/D/A offers the best positive edge.
            for outcome in ("H", "D", "A"):
                implied = _best_implied(m.odds_1x2, outcome)
                settle_o = _settle_odds(m.odds_1x2, outcome)
                if implied is None or settle_o is None:
                    continue
                edge = p1x2[outcome] - implied
                if edge >= cfg.min_edge:
                    bet_records.append(
                        BetRecord(
                            date=m.date, home=m.home, away=m.away,
                            market=f"1X2-{outcome}", outcome=outcome,
                            pred_prob=p1x2[outcome], odds=settle_o,
                            actual_hit=(m.result == outcome), edge=edge,
                        )
                    )

    log.info("Backtest: predicted %d matches, %d bets placed", n_predicted, len(bet_records))
    rep = aggregate(bet_records, rps_values)
    rep.n_predicted = n_predicted
    rep.rps_naive = float(np.mean(rps_naive_values)) if rps_naive_values else float("nan")
    rep.rps_market = float(np.mean(rps_market_values)) if rps_market_values else float("nan")
    return rep


def _devig_market(odds_1x2: tuple) -> tuple[float, float, float] | None:
    """De-vig a bookmaker's 1X2 odds into fair probabilities."""
    try:
        h, d, a = odds_1x2
        implied = [1.0 / h, 1.0 / d, 1.0 / a]
        overround = sum(implied)
        if overround <= 0:
            return None
        return tuple(p / overround for p in implied)  # type: ignore[return-value]
    except (TypeError, ValueError, ZeroDivisionError):
        return None
