#!/usr/bin/env python3
"""ClawHub skill: live MLB moneyline trading through Simmer SDK only.

The signal comes from ESPN's live MLB scoreboard. The adapter intentionally
fails closed when the game, probability, market identity, or executable quote
cannot be validated. Real orders require ``--live``; the default uses Simmer's
paper execution against real venue prices.

This file is a self-contained monofile. The ESPN feed client, the live-win-
probability/risk mathematics, and the Simmer execution runtime all live here,
so the packaged skill has no local module dependencies at all -- its only
third-party import is the Simmer SDK. The layout is:

    1. Configuration schema and shared primitives
    2. Signal + risk core (ESPN parsing, market identity, EV, Kelly inputs)
    3. ESPN live feed client (stdlib HTTP, fails closed)
    4. Simmer execution runtime (discovery, sizing, safeguards, CLI)

Every ESPN parser below is defensive: ESPN's public site API is undocumented,
so a game is tradeable only when it is explicitly live, both teams are
recognized, and a valid current/fallback win probability exists.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass, is_dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence

from simmer_sdk import SimmerClient
from simmer_sdk.skill import get_config_path, load_config, update_config
from simmer_sdk.sizing import SIZING_CONFIG_SCHEMA, size_position

try:
    sys.stdout.reconfigure(line_buffering=True)
except (AttributeError, OSError):
    pass

SKILL_SLUG = "mlb-live-trader"
TRADE_SOURCE = "sdk:mlb-live-trader"
VERSION = "1.0.0"
VENUE = "polymarket"
_STATE_PATH = Path(__file__).resolve().with_name(".mlb-live-trader-state.json")
_LOCK_PATH = Path(__file__).resolve().with_name(".mlb-live-trader.lock")

# The standard sizing schema is deliberately merged, as required by Simmer's
# skill contract. Skill-specific controls use namespaced environment variables.
CONFIG_SCHEMA: dict[str, dict[str, Any]] = {
    **SIZING_CONFIG_SCHEMA,
    "starting_balance": {
        "env": "SIMMER_MLB_LIVE_TRADER_STARTING_BALANCE",
        "default": 1000.0,
        "type": float,
    },
    "probability_haircut": {
        "env": "SIMMER_MLB_LIVE_TRADER_PROBABILITY_HAIRCUT",
        "default": 0.90,
        "type": float,
    },
    "early_game_confidence": {
        "env": "SIMMER_MLB_LIVE_TRADER_EARLY_GAME_CONFIDENCE",
        "default": 0.75,
        "type": float,
    },
    "fee_buffer": {
        "env": "SIMMER_MLB_LIVE_TRADER_FEE_BUFFER",
        "default": 0.01,
        "type": float,
    },
    "max_bankroll_fraction": {
        "env": "SIMMER_MLB_LIVE_TRADER_MAX_BANKROLL_FRACTION",
        "default": 0.02,
        "type": float,
    },
    "max_position_usd": {
        "env": "SIMMER_MLB_LIVE_TRADER_MAX_POSITION_USD",
        "default": 25.0,
        "type": float,
    },
    "max_game_exposure_usd": {
        "env": "SIMMER_MLB_LIVE_TRADER_MAX_GAME_EXPOSURE_USD",
        "default": 35.0,
        "type": float,
    },
    "portfolio_exposure_cap_usd": {
        "env": "SIMMER_MLB_LIVE_TRADER_PORTFOLIO_EXPOSURE_CAP_USD",
        "default": 100.0,
        "type": float,
    },
    "daily_spend_limit_usd": {
        "env": "SIMMER_MLB_LIVE_TRADER_DAILY_SPEND_LIMIT_USD",
        "default": 100.0,
        "type": float,
    },
    "min_order_shares": {
        "env": "SIMMER_MLB_LIVE_TRADER_MIN_ORDER_SHARES",
        "default": 5.0,
        "type": float,
    },
    "min_market_price": {
        "env": "SIMMER_MLB_LIVE_TRADER_MIN_MARKET_PRICE",
        "default": 0.03,
        "type": float,
    },
    "max_market_price": {
        "env": "SIMMER_MLB_LIVE_TRADER_MAX_MARKET_PRICE",
        "default": 0.97,
        "type": float,
    },
    "max_spread": {
        "env": "SIMMER_MLB_LIVE_TRADER_MAX_SPREAD",
        "default": 0.08,
        "type": float,
    },
    "max_slippage": {
        "env": "SIMMER_MLB_LIVE_TRADER_MAX_SLIPPAGE",
        "default": 0.03,
        "type": float,
    },
    "book_liquidity_fraction": {
        "env": "SIMMER_MLB_LIVE_TRADER_BOOK_LIQUIDITY_FRACTION",
        "default": 0.80,
        "type": float,
    },
    "min_inning": {
        "env": "SIMMER_MLB_LIVE_TRADER_MIN_INNING",
        "default": 1,
        "type": int,
    },
    "max_inning": {
        "env": "SIMMER_MLB_LIVE_TRADER_MAX_INNING",
        "default": 12,
        "type": int,
    },
    "max_quote_age_seconds": {
        "env": "SIMMER_MLB_LIVE_TRADER_MAX_QUOTE_AGE_SECONDS",
        "default": 90.0,
        "type": float,
    },
    "cooldown_seconds": {
        "env": "SIMMER_MLB_LIVE_TRADER_COOLDOWN_SECONDS",
        "default": 300,
        "type": int,
    },
    "poll_seconds": {
        "env": "SIMMER_MLB_LIVE_TRADER_POLL_SECONDS",
        "default": 15,
        "type": int,
    },
    "max_trades_per_run": {
        "env": "SIMMER_MLB_LIVE_TRADER_MAX_TRADES_PER_RUN",
        "default": 3,
        "type": int,
    },
    "market_query_limit": {
        "env": "SIMMER_MLB_LIVE_TRADER_MARKET_QUERY_LIMIT",
        "default": 25,
        "type": int,
    },
    "espn_timeout_seconds": {
        "env": "SIMMER_MLB_LIVE_TRADER_ESPN_TIMEOUT_SECONDS",
        "default": 8.0,
        "type": float,
    },
    "max_summary_requests": {
        "env": "SIMMER_MLB_LIVE_TRADER_MAX_SUMMARY_REQUESTS",
        "default": 15,
        "type": int,
    },
}
# Raise the standard SDK default from any-positive-EV to a meaningful live edge.
CONFIG_SCHEMA["min_ev"] = {
    **SIZING_CONFIG_SCHEMA["min_ev"],
    "default": 0.05,
}

_CLIENTS: dict[bool, SimmerClient] = {}


# ---------------------------------------------------------------------------
# Shared primitives
# ---------------------------------------------------------------------------


def _finite_float(value: Any) -> float | None:
    """Coerce to a finite float, or ``None``. NaN/inf and junk are rejected."""
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if math.isfinite(result) else None


# The signal core historically exposed this identical coercion under a second
# name. Both names stay bound so either import site keeps working.
_safe_float = _finite_float


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _sequence(value: Any) -> Sequence[Any]:
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return value
    return ()


def _safe_int(value: Any, default: int = 0) -> int:
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return default


def _safe_probability(value: Any) -> float | None:
    probability = _safe_float(value)
    if probability is None or not 0.0 <= probability <= 1.0:
        return None
    return probability


# ---------------------------------------------------------------------------
# Signal + risk core
# ---------------------------------------------------------------------------

# Canonical nickname -> (full name, common abbreviations/aliases).
_TEAM_DATA: dict[str, tuple[str, tuple[str, ...]]] = {
    "diamondbacks": ("Arizona Diamondbacks", ("ari", "d-backs", "dbacks")),
    "braves": ("Atlanta Braves", ("atl",)),
    "orioles": ("Baltimore Orioles", ("bal", "o's")),
    "red sox": ("Boston Red Sox", ("bos", "redsox")),
    "cubs": ("Chicago Cubs", ("chc",)),
    "white sox": ("Chicago White Sox", ("cws", "chw", "whitesox")),
    "reds": ("Cincinnati Reds", ("cin",)),
    "guardians": ("Cleveland Guardians", ("cle",)),
    "rockies": ("Colorado Rockies", ("col",)),
    "tigers": ("Detroit Tigers", ("det",)),
    "astros": ("Houston Astros", ("hou",)),
    "royals": ("Kansas City Royals", ("kc", "kcr")),
    "angels": ("Los Angeles Angels", ("laa", "anaheim angels")),
    "dodgers": ("Los Angeles Dodgers", ("lad",)),
    "marlins": ("Miami Marlins", ("mia",)),
    "brewers": ("Milwaukee Brewers", ("mil",)),
    "twins": ("Minnesota Twins", ("min",)),
    "mets": ("New York Mets", ("nym",)),
    "yankees": ("New York Yankees", ("nyy",)),
    "athletics": ("Athletics", ("ath", "oak", "oakland athletics", "a's")),
    "phillies": ("Philadelphia Phillies", ("phi",)),
    "pirates": ("Pittsburgh Pirates", ("pit",)),
    "padres": ("San Diego Padres", ("sd", "sdp")),
    "giants": ("San Francisco Giants", ("sf", "sfg")),
    "mariners": ("Seattle Mariners", ("sea",)),
    "cardinals": ("St. Louis Cardinals", ("stl", "saint louis cardinals")),
    "rays": ("Tampa Bay Rays", ("tb", "tbr")),
    "rangers": ("Texas Rangers", ("tex",)),
    "blue jays": ("Toronto Blue Jays", ("tor", "bluejays")),
    "nationals": ("Washington Nationals", ("wsh", "was")),
}

_CLEAN_RE = re.compile(r"[^a-z0-9]+")
_WS_RE = re.compile(r"\s+")
_GAME_ONE_RE = re.compile(r"(?:game|gm)\s*(?:1|one)\b", re.IGNORECASE)
_GAME_TWO_RE = re.compile(r"(?:game|gm)\s*(?:2|two)\b", re.IGNORECASE)
_DOUBLEHEADER_RE = re.compile(r"\bdouble[ -]?header\b", re.IGNORECASE)
_EXPLICIT_WIN_RE = re.compile(
    r"\b(?:will|does)\s+(.+?)\s+(?:win|beat)\b", re.IGNORECASE
)

# Anything containing these phrases is not a full-game moneyline.
_PROP_TERMS = (
    "spread",
    "run line",
    "handicap",
    "o/u",
    "over/under",
    "total runs",
    "team total",
    "first 5",
    "1st 5",
    "first five",
    "inning",
    "hits",
    "home run",
    "strikeout",
    "rbi",
    "series",
    "championship",
    "world series",
    "make the playoffs",
    "win the division",
    "regular season wins",
    "margin of victory",
)


@dataclass(frozen=True)
class LiveGameState:
    event_id: str
    game_date: str
    game_number: int
    event_start_time: str | None
    away_team: str
    home_team: str
    away_name: str
    home_name: str
    away_abbreviation: str
    home_abbreviation: str
    away_score: int
    home_score: int
    inning: int
    inning_half: str
    status_detail: str
    outs: int
    balls: int
    strikes: int
    on_first: bool
    on_second: bool
    on_third: bool
    pitcher: str | None
    batter: str | None
    last_play_id: str | None
    last_play_text: str | None
    probability_play_id: str | None
    home_win_probability: float
    probability_source: str
    venue_name: str | None
    neutral_site: bool
    play_by_play_available: bool
    was_suspended: bool
    weather_temperature_f: float | None
    weather_condition: str | None
    broadcast: str | None
    fetched_at: int
    is_doubleheader: bool = False

    @property
    def score(self) -> str:
        return (
            f"{self.away_abbreviation} {self.away_score}-"
            f"{self.home_score} {self.home_abbreviation}"
        )

    @property
    def runners(self) -> str:
        occupied = [
            base
            for base, is_on in (
                ("1B", self.on_first),
                ("2B", self.on_second),
                ("3B", self.on_third),
            )
            if is_on
        ]
        return ",".join(occupied) if occupied else "empty"

    @property
    def count(self) -> str:
        return f"{self.balls}-{self.strikes}"

    @property
    def state_key(self) -> str:
        play = self.probability_play_id or self.last_play_id or "no-play-id"
        return f"{self.event_id}:{play}"


@dataclass(frozen=True)
class StrategyConfig:
    min_edge: float = 0.05
    probability_haircut: float = 0.90
    early_game_confidence: float = 0.75
    fee_buffer: float = 0.01
    kelly_multiplier: float = 0.25
    max_bankroll_fraction: float = 0.02
    max_position_usd: float = 25.0
    max_game_exposure_usd: float = 35.0
    min_order_shares: float = 5.0
    min_inning: int = 1
    max_inning: int = 12
    max_quote_age_seconds: float = 90.0
    min_market_price: float = 0.03
    max_market_price: float = 0.97


@dataclass(frozen=True)
class MarketCandidate:
    side: str
    yes_team: str
    raw_yes_probability: float
    adjusted_yes_probability: float
    p_win: float
    quoted_price: float
    execution_price: float
    effective_price: float
    edge: float
    confidence: float
    raw_kelly_fraction: float


@dataclass(frozen=True)
class SizedSignal:
    candidate: MarketCandidate
    amount_usd: float
    shares: float
    skip_reason: str | None = None


@dataclass(frozen=True)
class SummaryProbability:
    home_win_probability: float
    play_id: str | None


def _clean(value: str) -> str:
    return _WS_RE.sub(" ", _CLEAN_RE.sub(" ", (value or "").lower())).strip()


def canonical_team(value: str) -> str:
    """Normalize ESPN/Polymarket/Simmer team labels to a stable nickname."""
    cleaned = _clean(value)
    if not cleaned:
        return ""
    for canonical, (full, aliases) in _TEAM_DATA.items():
        candidates = (canonical, full, *aliases)
        for candidate in candidates:
            normalized = _clean(candidate)
            if cleaned == normalized or cleaned.endswith(f" {normalized}"):
                return canonical
    return cleaned


def full_team_name(canonical: str) -> str:
    entry = _TEAM_DATA.get(canonical)
    return entry[0] if entry else canonical.title()


def team_search_terms(canonical: str) -> tuple[str, ...]:
    entry = _TEAM_DATA.get(canonical)
    if not entry:
        return (canonical,)
    full, aliases = entry
    return tuple(dict.fromkeys((full, canonical, *aliases)))


def _nested_name(container: Mapping[str, Any], key: str) -> str | None:
    block = _mapping(container.get(key))
    athlete = _mapping(block.get("athlete"))
    for field in ("displayName", "fullName", "shortName"):
        value = athlete.get(field)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def _broadcast_name(competition: Mapping[str, Any]) -> str | None:
    direct = competition.get("broadcast")
    if isinstance(direct, str) and direct.strip():
        return direct.strip()
    for item in _sequence(competition.get("broadcasts")):
        names = _sequence(_mapping(item).get("names"))
        for name in names:
            if isinstance(name, str) and name.strip():
                return name.strip()
    return None


def parse_summary_probability(payload: Mapping[str, Any]) -> SummaryProbability | None:
    """Return the newest valid ESPN home-win probability from a summary payload."""
    history = _sequence(payload.get("winprobability"))
    for point in reversed(history):
        item = _mapping(point)
        probability = _safe_probability(item.get("homeWinPercentage"))
        if probability is None:
            continue
        play_id = item.get("playId") or item.get("play_id")
        return SummaryProbability(probability, str(play_id) if play_id else None)
    return None


def _doubleheader_info(competition: Mapping[str, Any]) -> tuple[int, bool]:
    """Return (game number, is doubleheader) from ESPN competition notes.

    An explicit Game 1/Game 2 marker is treated as a doubleheader marker even
    when ESPN omits the word ``doubleheader``. A generic doubleheader note with
    no game number returns ``0`` so downstream market matching fails closed.
    """
    headlines = [
        str(_mapping(note).get("headline") or "")
        for note in _sequence(competition.get("notes"))
    ]
    combined = " ".join(headlines)
    if _GAME_TWO_RE.search(combined):
        return 2, True
    if _GAME_ONE_RE.search(combined):
        return 1, True
    if _DOUBLEHEADER_RE.search(combined):
        return 0, True
    return 1, False


def parse_scoreboard(
    payload: Mapping[str, Any],
    *,
    fetched_at: int | None = None,
    summary_probabilities: Mapping[str, SummaryProbability] | None = None,
    only_live: bool = True,
) -> list[LiveGameState]:
    """Parse ESPN's live scoreboard defensively and fail closed.

    Only games with a valid win probability are returned. If the scoreboard's
    latest play lacks one, callers may provide a per-event probability parsed
    from the summary endpoint's newest ``winprobability`` point.
    """
    now = (
        int(datetime.now(timezone.utc).timestamp())
        if fetched_at is None
        else int(fetched_at)
    )
    root_day = str(_mapping(payload.get("day")).get("date") or "")[:10]
    fallbacks = summary_probabilities or {}
    output: list[LiveGameState] = []

    for raw_event in _sequence(payload.get("events")):
        event = _mapping(raw_event)
        event_id = str(event.get("id") or "")
        competitions = _sequence(event.get("competitions"))
        if not event_id or not competitions:
            continue
        competition = _mapping(competitions[0])
        status = _mapping(competition.get("status"))
        status_type = _mapping(status.get("type"))
        state = str(status_type.get("state") or "").lower()
        status_name = str(status_type.get("name") or "")
        if only_live and state != "in" and status_name != "STATUS_IN_PROGRESS":
            continue

        home: Mapping[str, Any] | None = None
        away: Mapping[str, Any] | None = None
        for raw_competitor in _sequence(competition.get("competitors")):
            competitor = _mapping(raw_competitor)
            if competitor.get("homeAway") == "home":
                home = competitor
            elif competitor.get("homeAway") == "away":
                away = competitor
        if home is None or away is None:
            continue

        home_meta = _mapping(home.get("team"))
        away_meta = _mapping(away.get("team"))
        home_name = str(home_meta.get("displayName") or home_meta.get("name") or "")
        away_name = str(away_meta.get("displayName") or away_meta.get("name") or "")
        home_team = canonical_team(home_name)
        away_team = canonical_team(away_name)
        if (
            home_team not in _TEAM_DATA
            or away_team not in _TEAM_DATA
            or home_team == away_team
        ):
            continue

        situation = _mapping(competition.get("situation"))
        last_play = _mapping(situation.get("lastPlay"))
        probability = _mapping(last_play.get("probability"))
        home_probability = _safe_probability(probability.get("homeWinPercentage"))
        probability_source = "scoreboard"
        probability_play_id = last_play.get("id")
        if home_probability is None:
            fallback = fallbacks.get(event_id)
            # A probability without its own play ID cannot be tied to the live
            # state and may be stale relative to ``lastPlay``. Fail closed.
            if fallback is None or not fallback.play_id:
                continue
            home_probability = fallback.home_win_probability
            probability_play_id = fallback.play_id
            probability_source = "summary"

        event_date = str(event.get("date") or competition.get("date") or "")[:10]
        game_date = root_day or event_date
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", game_date):
            continue
        detail = str(status_type.get("detail") or status_type.get("shortDetail") or "")
        lowered_detail = detail.lower()
        if lowered_detail.startswith("top"):
            half = "top"
        elif lowered_detail.startswith(("bot", "bottom")):
            half = "bottom"
        else:
            half = "unknown"

        venue = _mapping(competition.get("venue"))
        weather = _mapping(event.get("weather")) or _mapping(competition.get("weather"))
        weather_temp = _safe_float(weather.get("temperature"))
        weather_condition = weather.get("conditionId") or weather.get("displayValue")
        if not isinstance(weather_condition, str) or not weather_condition.strip():
            weather_condition = None

        game_number, is_doubleheader = _doubleheader_info(competition)
        output.append(
            LiveGameState(
                event_id=event_id,
                game_date=game_date,
                game_number=game_number,
                event_start_time=(
                    str(event.get("date") or competition.get("date"))
                    if event.get("date") or competition.get("date")
                    else None
                ),
                away_team=away_team,
                home_team=home_team,
                away_name=away_name,
                home_name=home_name,
                away_abbreviation=str(
                    away_meta.get("abbreviation") or away_team[:3]
                ).upper(),
                home_abbreviation=str(
                    home_meta.get("abbreviation") or home_team[:3]
                ).upper(),
                away_score=_safe_int(away.get("score")),
                home_score=_safe_int(home.get("score")),
                inning=max(1, _safe_int(status.get("period"), 1)),
                inning_half=half,
                status_detail=detail or "In Progress",
                outs=min(3, max(0, _safe_int(situation.get("outs")))),
                balls=min(4, max(0, _safe_int(situation.get("balls")))),
                strikes=min(3, max(0, _safe_int(situation.get("strikes")))),
                on_first=bool(situation.get("onFirst", False)),
                on_second=bool(situation.get("onSecond", False)),
                on_third=bool(situation.get("onThird", False)),
                pitcher=_nested_name(situation, "pitcher"),
                batter=_nested_name(situation, "batter"),
                last_play_id=(
                    str(last_play.get("id")) if last_play.get("id") else None
                ),
                last_play_text=(
                    str(last_play.get("text")) if last_play.get("text") else None
                ),
                probability_play_id=(
                    str(probability_play_id) if probability_play_id else None
                ),
                home_win_probability=home_probability,
                probability_source=probability_source,
                venue_name=(
                    str(venue.get("fullName")) if venue.get("fullName") else None
                ),
                neutral_site=bool(competition.get("neutralSite", False)),
                play_by_play_available=bool(
                    competition.get("playByPlayAvailable", False)
                ),
                was_suspended=bool(competition.get("wasSuspended", False)),
                weather_temperature_f=weather_temp,
                weather_condition=weather_condition,
                broadcast=_broadcast_name(competition),
                fetched_at=now,
                is_doubleheader=is_doubleheader,
            )
        )
    return output


def game_progress(game: LiveGameState) -> float:
    """Approximate fraction of regulation completed from inning/half/outs."""
    inning_index = max(0, game.inning - 1)
    completed_halves = float(inning_index * 2)
    if game.inning_half == "bottom":
        completed_halves += 1.0
    completed_halves += max(0.0, min(1.0, game.outs / 3.0))
    return max(0.0, min(1.0, completed_halves / 18.0))


def adjusted_home_probability(
    game: LiveGameState, config: StrategyConfig
) -> tuple[float, float]:
    """Shrink ESPN's live model toward 50% to absorb latency/model error.

    Confidence rises smoothly as the game progresses. The shrinkage is a risk
    control, not a claim that ESPN probabilities are calibrated to Polymarket.
    """
    progress = game_progress(game)
    early = max(0.0, min(1.0, config.early_game_confidence))
    progress_confidence = early + (1.0 - early) * math.sqrt(progress)
    confidence = max(
        0.0, min(1.0, config.probability_haircut * progress_confidence)
    )
    adjusted = 0.5 + (game.home_win_probability - 0.5) * confidence
    return max(0.001, min(0.999, adjusted)), confidence


def probability_for_team(
    game: LiveGameState, team: str, config: StrategyConfig
) -> tuple[float, float, float]:
    adjusted_home, confidence = adjusted_home_probability(game, config)
    canonical = canonical_team(team)
    if canonical == game.home_team:
        return game.home_win_probability, adjusted_home, confidence
    if canonical == game.away_team:
        return 1.0 - game.home_win_probability, 1.0 - adjusted_home, confidence
    raise ValueError(f"team {team!r} is not in ESPN game {game.event_id}")


def _find_team_position(text: str, canonical: str) -> int | None:
    cleaned = _clean(text)
    positions: list[int] = []
    for term in team_search_terms(canonical):
        term_clean = _clean(term)
        if not term_clean:
            continue
        position = cleaned.find(term_clean)
        if position >= 0:
            positions.append(position)
    return min(positions) if positions else None


def is_full_game_moneyline_text(text: str) -> bool:
    lowered = _clean(text)
    return bool(lowered) and not any(_clean(term) in lowered for term in _PROP_TERMS)


def infer_yes_team(
    question: str,
    game: LiveGameState,
    resolution_criteria: str | None = None,
) -> str | None:
    """Infer which team the market's YES/outcome-0 token represents.

    Explicit ``Will TEAM win`` wording wins. For two-team sports questions, the
    first team named is treated as outcome 0. Ambiguous or prop markets fail
    closed rather than guessing.
    """
    combined = " ".join(
        part for part in (question, resolution_criteria or "") if part
    )
    # Resolution rules for a full-game market often mention innings (for
    # postponement/suspension handling). Prop filtering therefore belongs on
    # the user-facing question, not on the legal resolution prose.
    if not is_full_game_moneyline_text(question):
        return None

    explicit = _EXPLICIT_WIN_RE.search(question)
    if explicit:
        explicit_team = canonical_team(explicit.group(1))
        if explicit_team in {game.away_team, game.home_team}:
            return explicit_team

    away_pos = _find_team_position(question, game.away_team)
    home_pos = _find_team_position(question, game.home_team)
    if away_pos is not None and home_pos is not None:
        return game.away_team if away_pos < home_pos else game.home_team

    q_clean = _clean(question)
    if any(word in q_clean.split() for word in ("win", "beat")):
        if away_pos is not None:
            return game.away_team
        if home_pos is not None:
            return game.home_team
    return None


def market_matches_game(
    question: str,
    game: LiveGameState,
    *,
    resolution_criteria: str | None = None,
    resolves_at: str | None = None,
) -> bool:
    combined = " ".join(
        part for part in (question, resolution_criteria or "") if part
    )
    if not is_full_game_moneyline_text(question):
        return False
    # Doubleheaders are an easy way to buy the right teams in the wrong game.
    # Require an explicit matching Game 1/Game 2 marker for every ESPN event
    # identified as a doubleheader; generic/unknown numbering fails closed.
    market_is_game_one = bool(_GAME_ONE_RE.search(combined))
    market_is_game_two = bool(_GAME_TWO_RE.search(combined))
    if market_is_game_one and market_is_game_two:
        return False
    if game.is_doubleheader:
        if game.game_number == 1 and not market_is_game_one:
            return False
        if game.game_number == 2 and not market_is_game_two:
            return False
        if game.game_number not in {1, 2}:
            return False
    elif market_is_game_one or market_is_game_two:
        return False
    if _find_team_position(combined, game.away_team) is None:
        return False
    if _find_team_position(combined, game.home_team) is None:
        return False
    if resolves_at:
        try:
            resolved_date = datetime.fromisoformat(
                resolves_at.replace("Z", "+00:00")
            ).date()
            game_date = datetime.fromisoformat(game.game_date).date()
            if abs((resolved_date - game_date).days) > 1:
                return False
        except (TypeError, ValueError):
            return False
    return True


def _valid_price(value: float | None) -> bool:
    return value is not None and math.isfinite(value) and 0.0 < value < 1.0


def candidate_for_side(
    *,
    game: LiveGameState,
    yes_team: str,
    yes_price: float,
    side: str,
    config: StrategyConfig,
    execution_price: float | None = None,
) -> MarketCandidate | None:
    if side not in {"yes", "no"}:
        raise ValueError(f"unsupported side {side!r}")
    if not _valid_price(yes_price):
        return None
    raw_yes, adjusted_yes, confidence = probability_for_team(game, yes_team, config)
    quoted = yes_price if side == "yes" else 1.0 - yes_price
    execution = quoted if execution_price is None else execution_price
    if not _valid_price(execution):
        return None
    if not config.min_market_price <= execution <= config.max_market_price:
        return None
    p_win = adjusted_yes if side == "yes" else 1.0 - adjusted_yes
    effective = min(0.999, execution + max(0.0, config.fee_buffer))
    edge = p_win - effective
    raw_kelly = (
        0.0
        if effective >= 1.0
        else max(0.0, (p_win - effective) / (1.0 - effective))
    )
    return MarketCandidate(
        side=side,
        yes_team=canonical_team(yes_team),
        raw_yes_probability=raw_yes,
        adjusted_yes_probability=adjusted_yes,
        p_win=p_win,
        quoted_price=quoted,
        execution_price=execution,
        effective_price=effective,
        edge=edge,
        confidence=confidence,
        raw_kelly_fraction=raw_kelly,
    )


def choose_candidate(
    *,
    game: LiveGameState,
    yes_team: str,
    yes_price: float,
    config: StrategyConfig,
    yes_execution_price: float | None = None,
    no_execution_price: float | None = None,
    quote_age_seconds: float | None = None,
) -> MarketCandidate | None:
    if game.inning < config.min_inning or game.inning > config.max_inning:
        return None
    if game.was_suspended or not game.play_by_play_available:
        return None
    if quote_age_seconds is not None and quote_age_seconds > config.max_quote_age_seconds:
        return None
    candidates = [
        candidate_for_side(
            game=game,
            yes_team=yes_team,
            yes_price=yes_price,
            side="yes",
            config=config,
            execution_price=yes_execution_price,
        ),
        candidate_for_side(
            game=game,
            yes_team=yes_team,
            yes_price=yes_price,
            side="no",
            config=config,
            execution_price=no_execution_price,
        ),
    ]
    eligible = [
        candidate
        for candidate in candidates
        if candidate is not None and candidate.edge >= config.min_edge
    ]
    if not eligible:
        return None
    return max(
        eligible,
        key=lambda item: (item.edge, item.raw_kelly_fraction, item.side == "yes"),
    )


def fractional_kelly_size(
    candidate: MarketCandidate,
    *,
    bankroll: float,
    config: StrategyConfig,
    current_game_exposure_usd: float = 0.0,
) -> SizedSignal:
    """Standalone fractional-Kelly sizing with hard USD and share caps."""
    if bankroll <= 0:
        return SizedSignal(candidate, 0.0, 0.0, "insufficient_bankroll")
    if candidate.edge < config.min_edge:
        return SizedSignal(candidate, 0.0, 0.0, "edge_too_small")
    raw_amount = (
        bankroll
        * candidate.raw_kelly_fraction
        * max(0.0, config.kelly_multiplier)
    )
    bankroll_cap = bankroll * max(0.0, config.max_bankroll_fraction)
    game_cap = max(
        0.0,
        config.max_game_exposure_usd - max(0.0, current_game_exposure_usd),
    )
    amount = min(
        raw_amount,
        bankroll_cap,
        config.max_position_usd,
        game_cap,
        bankroll,
    )
    amount = math.floor(max(0.0, amount) * 100.0) / 100.0
    if amount <= 0:
        return SizedSignal(candidate, 0.0, 0.0, "risk_cap")
    shares = amount / candidate.execution_price
    if shares + 1e-9 < config.min_order_shares:
        return SizedSignal(candidate, amount, shares, "below_minimum_shares")
    return SizedSignal(candidate, amount, shares, None)


def build_reasoning(
    game: LiveGameState, candidate: MarketCandidate, amount_usd: float
) -> str:
    team = (
        candidate.yes_team
        if candidate.side == "yes"
        else game.home_team
        if candidate.yes_team == game.away_team
        else game.away_team
    )
    people = ", ".join(
        part
        for part in (
            f"pitcher={game.pitcher}" if game.pitcher else "",
            f"batter={game.batter}" if game.batter else "",
        )
        if part
    )
    play_text = (game.last_play_text or "").replace("\n", " ").strip()
    if len(play_text) > 140:
        play_text = play_text[:137] + "..."
    context = (
        f"count={game.count}, outs={game.outs}, runners={game.runners}"
        + (f", {people}" if people else "")
    )
    return (
        f"ESPN MLB live signal: buy {candidate.side.upper()} "
        f"({full_team_name(team)}); raw_yes={candidate.raw_yes_probability:.1%}, "
        f"adjusted_yes={candidate.adjusted_yes_probability:.1%}, "
        f"p_win={candidate.p_win:.1%}, execution={candidate.execution_price:.3f}, "
        f"fee_adjusted={candidate.effective_price:.3f}, edge={candidate.edge:.1%}, "
        f"confidence={candidate.confidence:.2f}, size=${amount_usd:.2f}. "
        f"Game {game.status_detail}, {game.score}; {context}. "
        f"ESPN event={game.event_id}, play="
        f"{game.probability_play_id or game.last_play_id or 'unknown'}, "
        f"probability_source={game.probability_source}"
        + (f", last_play={play_text!r}" if play_text else "")
        + "."
    )


def game_identity(game: LiveGameState) -> tuple[str, frozenset[str], int]:
    return game.game_date, frozenset((game.away_team, game.home_team)), game.game_number


def find_matching_game(
    games: Iterable[LiveGameState],
    *,
    game_date: str,
    away_team: str,
    home_team: str,
    game_number: int = 1,
) -> LiveGameState | None:
    target_teams = frozenset((canonical_team(away_team), canonical_team(home_team)))
    exact: list[LiveGameState] = []
    pair_only: list[LiveGameState] = []
    for game in games:
        if frozenset((game.away_team, game.home_team)) != target_teams:
            continue
        pair_only.append(game)
        if game.game_date == game_date and game.game_number == game_number:
            exact.append(game)
    if len(exact) == 1:
        return exact[0]
    # Date mismatches near UTC midnight are tolerable only for a unique, normal
    # single game. Never downgrade doubleheader identity to team-pair matching.
    safe_pair_only = [
        game
        for game in pair_only
        if not game.is_doubleheader and game.game_number == 1 and game_number == 1
    ]
    return safe_pair_only[0] if len(safe_pair_only) == 1 else None


# ---------------------------------------------------------------------------
# ESPN live feed client
# ---------------------------------------------------------------------------

ESPN_SITE_BASE = "https://site.api.espn.com"
_SCOREBOARD_PATH = "/apis/site/v2/sports/baseball/mlb/scoreboard"
_SUMMARY_PATH = "/apis/site/v2/sports/baseball/mlb/summary"


class EspnApiError(RuntimeError):
    """Raised when ESPN data cannot be fetched or validated safely."""


@dataclass(frozen=True)
class EspnSnapshot:
    fetched_at: int
    live_games: tuple[LiveGameState, ...]
    live_event_count: int
    summary_fallback_count: int


class EspnLiveClient:
    """Defensive stdlib client for ESPN's public, undocumented MLB JSON feed."""

    def __init__(
        self,
        *,
        base_url: str = ESPN_SITE_BASE,
        timeout_seconds: float = 8.0,
        retries: int = 2,
        max_response_bytes: int = 12_000_000,
        max_summary_requests: int = 15,
        opener: Callable[..., Any] | None = None,
        sleeper: Callable[[float], None] = time.sleep,
    ) -> None:
        parsed = urllib.parse.urlparse(base_url)
        if parsed.scheme != "https" or not parsed.netloc:
            raise ValueError("ESPN base URL must be an absolute HTTPS URL")
        self.base_url = base_url.rstrip("/")
        self.timeout_seconds = max(1.0, float(timeout_seconds))
        self.retries = max(0, int(retries))
        self.max_response_bytes = max(1024, int(max_response_bytes))
        self.max_summary_requests = max(0, int(max_summary_requests))
        self._opener = opener or urllib.request.urlopen
        self._sleep = sleeper

    def _get_json(self, path: str, params: Mapping[str, str] | None = None) -> dict[str, Any]:
        query = urllib.parse.urlencode(dict(params or {}))
        url = f"{self.base_url}{path}" + (f"?{query}" if query else "")
        request = urllib.request.Request(
            url,
            headers={
                "Accept": "application/json",
                "Accept-Encoding": "identity",
                "User-Agent": "MLB-Live-Trader/1.0 (+ClawHub skill; contact via repository)",
            },
            method="GET",
        )
        last_error: BaseException | None = None
        for attempt in range(self.retries + 1):
            try:
                with self._opener(request, timeout=self.timeout_seconds) as response:
                    status = int(getattr(response, "status", 200))
                    if status != 200:
                        raise EspnApiError(f"ESPN returned HTTP {status}")
                    raw = response.read(self.max_response_bytes + 1)
                    if len(raw) > self.max_response_bytes:
                        raise EspnApiError("ESPN response exceeded configured size limit")
                decoded = json.loads(raw.decode("utf-8"))
                if not isinstance(decoded, dict):
                    raise EspnApiError("ESPN response root was not an object")
                return decoded
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, UnicodeDecodeError, OSError, EspnApiError) as exc:
                last_error = exc
                if attempt < self.retries:
                    self._sleep(0.35 * (2**attempt))
        raise EspnApiError(f"ESPN request failed safely: {type(last_error).__name__}") from last_error

    def fetch_scoreboard(self, date_yyyymmdd: str | None = None) -> dict[str, Any]:
        params = {"dates": date_yyyymmdd} if date_yyyymmdd else None
        return self._get_json(_SCOREBOARD_PATH, params)

    def fetch_summary(self, event_id: str) -> dict[str, Any]:
        if not event_id.isdigit():
            raise ValueError("ESPN event ID must be numeric")
        return self._get_json(_SUMMARY_PATH, {"event": event_id})

    @staticmethod
    def _live_events_missing_probability(scoreboard: Mapping[str, Any]) -> list[str]:
        missing: list[str] = []
        events = scoreboard.get("events")
        if not isinstance(events, list):
            return missing
        for raw_event in events:
            if not isinstance(raw_event, dict):
                continue
            event_id = str(raw_event.get("id") or "")
            competitions = raw_event.get("competitions")
            if not event_id or not isinstance(competitions, list) or not competitions:
                continue
            competition = competitions[0] if isinstance(competitions[0], dict) else {}
            status = competition.get("status") if isinstance(competition.get("status"), dict) else {}
            status_type = status.get("type") if isinstance(status.get("type"), dict) else {}
            if status_type.get("state") != "in" and status_type.get("name") != "STATUS_IN_PROGRESS":
                continue
            situation = competition.get("situation") if isinstance(competition.get("situation"), dict) else {}
            last_play = situation.get("lastPlay") if isinstance(situation.get("lastPlay"), dict) else {}
            probability = last_play.get("probability") if isinstance(last_play.get("probability"), dict) else {}
            try:
                value = float(probability.get("homeWinPercentage"))
                valid = 0.0 <= value <= 1.0
            except (TypeError, ValueError):
                valid = False
            if not valid:
                missing.append(event_id)
        return missing

    @staticmethod
    def _live_event_count(scoreboard: Mapping[str, Any]) -> int:
        count = 0
        events = scoreboard.get("events")
        if not isinstance(events, list):
            return 0
        for raw_event in events:
            if not isinstance(raw_event, dict):
                continue
            competitions = raw_event.get("competitions")
            if not isinstance(competitions, list) or not competitions or not isinstance(competitions[0], dict):
                continue
            status = competitions[0].get("status")
            status = status if isinstance(status, dict) else {}
            status_type = status.get("type")
            status_type = status_type if isinstance(status_type, dict) else {}
            if status_type.get("state") == "in" or status_type.get("name") == "STATUS_IN_PROGRESS":
                count += 1
        return count

    def fetch_live_snapshot(self, *, fetched_at: int | None = None) -> EspnSnapshot:
        now = int(time.time()) if fetched_at is None else int(fetched_at)
        scoreboard = self.fetch_scoreboard()
        fallbacks: dict[str, SummaryProbability] = {}
        missing = self._live_events_missing_probability(scoreboard)
        for event_id in missing[: self.max_summary_requests]:
            try:
                fallback = parse_summary_probability(self.fetch_summary(event_id))
            except (EspnApiError, ValueError):
                continue
            if fallback is not None and fallback.play_id:
                fallbacks[event_id] = fallback
        games = parse_scoreboard(
            scoreboard,
            fetched_at=now,
            summary_probabilities=fallbacks,
            only_live=True,
        )
        return EspnSnapshot(
            fetched_at=now,
            live_games=tuple(games),
            live_event_count=self._live_event_count(scoreboard),
            summary_fallback_count=len(fallbacks),
        )


# ---------------------------------------------------------------------------
# Simmer execution runtime
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class MarketEvaluation:
    market: Any
    game: LiveGameState
    candidate: MarketCandidate
    query: str
    yes_team: str
    quote_age_seconds: float
    spread: float
    top_size_shares: float


@dataclass(frozen=True)
class TradePlan:
    evaluation: MarketEvaluation
    amount_usd: float
    shares: float
    limit_price: float
    bankroll: float
    game_exposure_usd: float


@dataclass(frozen=True)
class SafeguardResult:
    ok: bool
    reason: str
    preflight_id: str | None = None
    context: Mapping[str, Any] | None = None


class RunLock:
    """Simple process lock so overlapping cron/automaton runs cannot double-buy."""

    def __init__(self, path: Path, stale_after_seconds: int = 900) -> None:
        self.path = path
        self.stale_after_seconds = stale_after_seconds
        self._owned = False

    def __enter__(self) -> "RunLock":
        try:
            age = time.time() - self.path.stat().st_mtime
            if age > self.stale_after_seconds:
                self.path.unlink(missing_ok=True)
        except FileNotFoundError:
            pass
        try:
            fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError as exc:
            raise RuntimeError("another MLB Live Trader process already holds the run lock") from exc
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(f"pid={os.getpid()} started={int(time.time())}\n")
        self._owned = True
        return self

    def __exit__(self, _exc_type, _exc, _tb) -> None:
        if self._owned:
            self.path.unlink(missing_ok=True)
            self._owned = False


def get_client(*, live: bool, config: Mapping[str, Any]) -> SimmerClient:
    """Return a singleton Simmer client; API keys are read only by the SDK."""
    key = bool(live)
    if key not in _CLIENTS:
        _CLIENTS[key] = SimmerClient.from_env(
            venue=VENUE,
            live=key,
            starting_balance=float(config["starting_balance"]),
        )
    return _CLIENTS[key]


def _emit(quiet: bool, message: str, *, force: bool = False) -> None:
    if force or not quiet:
        print(message, flush=True)


def _json_default(value: Any) -> Any:
    if is_dataclass(value):
        return asdict(value)
    if isinstance(value, Path):
        return str(value)
    return str(value)


def _as_mapping(value: Any) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        return value
    if is_dataclass(value):
        return asdict(value)
    return {}


def _field(value: Any, name: str, default: Any = None) -> Any:
    if isinstance(value, Mapping):
        return value.get(name, default)
    return getattr(value, name, default)


def _is_true(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    return str(value or "").strip().lower() in {"true", "yes", "1", "on"}


def _validate_config(config: Mapping[str, Any]) -> None:
    method = str(config["position_sizing"])
    if method not in {"fractional_kelly", "kelly", "fixed"}:
        raise ValueError("position_sizing must be fractional_kelly, kelly, or fixed")
    unit_interval_open = (
        "probability_haircut",
        "early_game_confidence",
        "max_bankroll_fraction",
        "book_liquidity_fraction",
    )
    for key in unit_interval_open:
        value = float(config[key])
        if not 0.0 < value <= 1.0:
            raise ValueError(f"{key} must be in (0, 1]")
    unit_interval = (
        "kelly_multiplier",
        "min_ev",
        "fee_buffer",
        "min_market_price",
        "max_market_price",
        "max_spread",
        "max_slippage",
    )
    for key in unit_interval:
        value = float(config[key])
        if not 0.0 <= value < 1.0:
            raise ValueError(f"{key} must be in [0, 1)")
    positive = (
        "starting_balance",
        "max_position_usd",
        "max_game_exposure_usd",
        "portfolio_exposure_cap_usd",
        "daily_spend_limit_usd",
        "min_order_shares",
        "max_quote_age_seconds",
        "cooldown_seconds",
        "poll_seconds",
        "max_trades_per_run",
        "market_query_limit",
        "espn_timeout_seconds",
        "max_summary_requests",
        "min_inning",
        "max_inning",
    )
    for key in positive:
        if float(config[key]) <= 0:
            raise ValueError(f"{key} must be positive")
    if float(config["min_market_price"]) < 0.01:
        raise ValueError("min_market_price must be at least $0.01")
    if float(config["min_market_price"]) >= float(config["max_market_price"]):
        raise ValueError("min_market_price must be below max_market_price")
    if int(config["min_inning"]) > int(config["max_inning"]):
        raise ValueError("min_inning cannot exceed max_inning")
    if float(config["max_position_usd"]) > float(config["portfolio_exposure_cap_usd"]):
        raise ValueError("max_position_usd cannot exceed portfolio_exposure_cap_usd")


def _strategy_config(config: Mapping[str, Any]) -> StrategyConfig:
    return StrategyConfig(
        min_edge=float(config["min_ev"]),
        probability_haircut=float(config["probability_haircut"]),
        early_game_confidence=float(config["early_game_confidence"]),
        fee_buffer=float(config["fee_buffer"]),
        kelly_multiplier=float(config["kelly_multiplier"]),
        max_bankroll_fraction=float(config["max_bankroll_fraction"]),
        max_position_usd=float(config["max_position_usd"]),
        max_game_exposure_usd=float(config["max_game_exposure_usd"]),
        min_order_shares=float(config["min_order_shares"]),
        min_inning=int(config["min_inning"]),
        max_inning=int(config["max_inning"]),
        max_quote_age_seconds=float(config["max_quote_age_seconds"]),
        min_market_price=float(config["min_market_price"]),
        max_market_price=float(config["max_market_price"]),
    )


def _empty_state() -> dict[str, Any]:
    return {
        "version": 1,
        "utc_date": datetime.now(timezone.utc).date().isoformat(),
        "daily_spend_usd": 0.0,
        "signals": {},
        "games": {},
    }


def _load_state(path: Path = _STATE_PATH) -> dict[str, Any]:
    state = _empty_state()
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return state
    except (OSError, json.JSONDecodeError):
        return state
    if not isinstance(loaded, dict) or loaded.get("version") != 1:
        return state
    for key in ("signals", "games"):
        if not isinstance(loaded.get(key), dict):
            loaded[key] = {}
    today = datetime.now(timezone.utc).date()
    if loaded.get("utc_date") != today.isoformat():
        loaded["utc_date"] = today.isoformat()
        loaded["daily_spend_usd"] = 0.0
    # Prune stale game/signal records. They are idempotency metadata, not a ledger.
    cutoff = today - timedelta(days=3)
    loaded["games"] = {
        event_id: item
        for event_id, item in loaded["games"].items()
        if isinstance(item, dict)
        and _parse_date(str(item.get("game_date") or ""), date.min) >= cutoff
    }
    cutoff_ts = time.time() - (3 * 86400)
    loaded["signals"] = {
        key: item
        for key, item in loaded["signals"].items()
        if isinstance(item, dict) and float(item.get("timestamp") or 0) >= cutoff_ts
    }
    loaded["daily_spend_usd"] = max(0.0, float(loaded.get("daily_spend_usd") or 0.0))
    return loaded


def _parse_date(value: str, default: date) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError:
        return default


def _save_state(state: Mapping[str, Any], path: Path = _STATE_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    temp.write_text(
        json.dumps(state, indent=2, sort_keys=True, default=_json_default) + "\n",
        encoding="utf-8",
    )
    os.chmod(temp, 0o600)
    temp.replace(path)


def _event_exposure(state: Mapping[str, Any], event_id: str) -> float:
    games = _as_mapping(state.get("games"))
    item = _as_mapping(games.get(event_id))
    return max(0.0, float(item.get("reserved_usd") or 0.0))


def _event_is_blocked(
    state: Mapping[str, Any], game: LiveGameState, cooldown_seconds: int
) -> str | None:
    signals = _as_mapping(state.get("signals"))
    if game.state_key in signals:
        return "duplicate ESPN play/probability signal"
    item = _as_mapping(_as_mapping(state.get("games")).get(game.event_id))
    if item.get("market_id"):
        return "this skill already opened/reserved one position for the game"
    last_attempt = _finite_float(item.get("last_attempt_at"))
    if last_attempt is not None and time.time() - last_attempt < cooldown_seconds:
        return "game cooldown is active"
    return None


def _record_trade(
    state: dict[str, Any],
    *,
    plan: TradePlan,
    result: Any,
    live: bool,
) -> None:
    now = int(time.time())
    game = plan.evaluation.game
    market = plan.evaluation.market
    actual_cost = _finite_float(_field(result, "cost"))
    reserved = plan.amount_usd if actual_cost is None or actual_cost <= 0 else actual_cost
    state["daily_spend_usd"] = round(
        float(state.get("daily_spend_usd") or 0.0) + reserved, 2
    )
    state.setdefault("signals", {})[game.state_key] = {
        "timestamp": now,
        "event_id": game.event_id,
        "market_id": str(_field(market, "id", "")),
        "side": plan.evaluation.candidate.side,
    }
    state.setdefault("games", {})[game.event_id] = {
        "game_date": game.game_date,
        "last_attempt_at": now,
        "market_id": str(_field(market, "id", "")),
        "side": plan.evaluation.candidate.side,
        "reserved_usd": round(reserved, 2),
        "entry_price": plan.evaluation.candidate.execution_price,
        "live": bool(live),
        "trade_id": _field(result, "trade_id"),
        "order_id": _field(result, "order_id"),
        "fill_status": _field(result, "fill_status"),
    }
    _save_state(state)


def _positions_as_dicts(client: SimmerClient) -> list[dict[str, Any]]:
    positions = client.get_positions(venue=VENUE)
    output: list[dict[str, Any]] = []
    for position in positions:
        if is_dataclass(position):
            output.append(asdict(position))
        elif isinstance(position, Mapping):
            output.append(dict(position))
    return output


def _has_game_position(positions: Sequence[Mapping[str, Any]], game: LiveGameState) -> bool:
    for position in positions:
        if str(position.get("status") or "active").lower() not in {"active", "open", "pending"}:
            continue
        question = str(position.get("question") or "")
        if not question:
            continue
        if market_matches_game(question, game):
            shares_yes = float(position.get("shares_yes") or 0.0)
            shares_no = float(position.get("shares_no") or 0.0)
            if shares_yes > 0 or shares_no > 0:
                return True
    return False


def _market_queries(game: LiveGameState) -> tuple[str, ...]:
    options = (
        f"{game.away_name} {game.home_name}",
        f"{game.away_team} {game.home_team}",
    )
    return tuple(dict.fromkeys(query.strip() for query in options if query.strip()))


def _discover_markets(
    client: SimmerClient,
    game: LiveGameState,
    *,
    limit: int,
) -> list[tuple[Any, str]]:
    by_id: dict[str, tuple[Any, str]] = {}
    for query in _market_queries(game):
        markets = client.get_markets(
            status="active",
            limit=limit,
            include="resolution_criteria",
            q=query,
            venue=VENUE,
            sort="volume",
        )
        for market in markets:
            market_id = str(_field(market, "id", ""))
            if market_id:
                by_id.setdefault(market_id, (market, query))
        # Avoid a second API call once the server-side query found a valid match.
        if any(_market_matches(market, game) for market, _ in by_id.values()):
            break
    return list(by_id.values())


def _market_matches(market: Any, game: LiveGameState) -> bool:
    if str(_field(market, "status", "")).lower() != "active":
        return False
    if _field(market, "is_live_now") is False:
        return False
    source = str(_field(market, "import_source", "") or "").lower()
    if source and source != "polymarket":
        return False
    question = str(_field(market, "question", ""))
    criteria = _field(market, "resolution_criteria")
    resolves_at = _field(market, "resolves_at")
    return market_matches_game(
        question,
        game,
        resolution_criteria=str(criteria) if criteria else None,
        resolves_at=str(resolves_at) if resolves_at else None,
    )


def _quote_age(market: Any) -> float | None:
    direct = _finite_float(_field(market, "quote_age_seconds"))
    if direct is not None:
        return max(0.0, direct)
    quote_ts = _finite_float(_field(market, "quote_ts"))
    if quote_ts is None:
        return None
    return max(0.0, time.time() - quote_ts)


def _evaluate_market(
    market: Any,
    game: LiveGameState,
    query: str,
    core_config: StrategyConfig,
    config: Mapping[str, Any],
) -> MarketEvaluation | None:
    if not _market_matches(market, game):
        return None
    question = str(_field(market, "question", ""))
    criteria_raw = _field(market, "resolution_criteria")
    criteria = str(criteria_raw) if criteria_raw else None
    yes_team = infer_yes_team(question, game, criteria)
    if yes_team is None:
        return None

    best_bid = _finite_float(_field(market, "best_bid"))
    best_ask = _finite_float(_field(market, "best_ask"))
    if best_bid is None or best_ask is None or not 0.0 < best_bid < best_ask < 1.0:
        return None
    spread = _finite_float(_field(market, "spread"))
    spread = best_ask - best_bid if spread is None else spread
    if spread < 0 or spread > float(config["max_spread"]):
        return None
    age = _quote_age(market)
    if age is None or age > float(config["max_quote_age_seconds"]):
        return None

    yes_mid = _finite_float(_field(market, "current_probability"))
    if yes_mid is None or not 0.0 < yes_mid < 1.0:
        yes_mid = (best_bid + best_ask) / 2.0
    no_ask = 1.0 - best_bid
    candidate = choose_candidate(
        game=game,
        yes_team=yes_team,
        yes_price=yes_mid,
        config=core_config,
        yes_execution_price=best_ask,
        no_execution_price=no_ask,
        quote_age_seconds=age,
    )
    if candidate is None:
        return None

    top_size = _finite_float(
        _field(market, "best_ask_size")
        if candidate.side == "yes"
        else _field(market, "best_bid_size")
    )
    if top_size is None or top_size < float(config["min_order_shares"]):
        return None
    return MarketEvaluation(
        market=market,
        game=game,
        candidate=candidate,
        query=query,
        yes_team=yes_team,
        quote_age_seconds=age,
        spread=spread,
        top_size_shares=top_size,
    )


def _bankroll_and_safe_size(
    client: SimmerClient,
    *,
    live: bool,
    config: Mapping[str, Any],
) -> tuple[float, float]:
    if live:
        check = client.ensure_can_trade(
            min_usd=max(
                1.0,
                float(config["min_order_shares"]) * float(config["min_market_price"]),
            ),
            venue=VENUE,
            safety_buffer=max(0.02, float(config["fee_buffer"])),
        )
        if not _is_true(check.get("ok")):
            raise RuntimeError(
                "Simmer balance preflight failed: "
                f"{check.get('reason', 'unknown')} (balance={check.get('balance', 0)})"
            )
        bankroll = float(check.get("balance") or 0.0)
        max_safe = float(check.get("max_safe_size") or 0.0)
        return bankroll, max_safe
    summary = client.get_paper_summary() or {}
    bankroll = float(summary.get("balance") or config["starting_balance"])
    return bankroll, bankroll


def _make_plan(
    evaluation: MarketEvaluation,
    *,
    bankroll: float,
    max_safe_size: float,
    state: Mapping[str, Any],
    config: Mapping[str, Any],
) -> TradePlan | None:
    candidate = evaluation.candidate
    amount = size_position(
        p_win=candidate.p_win,
        market_price=candidate.effective_price,
        bankroll=bankroll,
        method=str(config["position_sizing"]),
        kelly_multiplier=float(config["kelly_multiplier"]),
        min_ev=float(config["min_ev"]),
        max_fraction=float(config["max_bankroll_fraction"]),
    )
    event_exposure = _event_exposure(state, evaluation.game.event_id)
    daily_remaining = max(
        0.0,
        float(config["daily_spend_limit_usd"])
        - float(state.get("daily_spend_usd") or 0.0),
    )
    game_remaining = max(0.0, float(config["max_game_exposure_usd"]) - event_exposure)
    book_cap = (
        evaluation.top_size_shares
        * candidate.execution_price
        * float(config["book_liquidity_fraction"])
    )
    amount = min(
        amount,
        float(config["max_position_usd"]),
        bankroll * float(config["max_bankroll_fraction"]),
        max_safe_size,
        daily_remaining,
        game_remaining,
        book_cap,
        bankroll,
    )
    amount = math.floor(max(0.0, amount) * 100.0) / 100.0
    if amount <= 0:
        return None

    # Preserve the configured EV even if the FAK order walks beyond top-of-book.
    max_by_ev = candidate.p_win - float(config["min_ev"]) - float(config["fee_buffer"])
    max_by_slippage = candidate.execution_price * (
        1.0 + float(config["max_slippage"])
    )
    limit_price = min(max_by_ev, max_by_slippage, 0.99)
    # User-provided skill standard requires at least a $0.01 price. The SDK
    # performs market-specific tick rounding; this code intentionally does not.
    if not 0.01 <= candidate.execution_price <= limit_price <= 0.99:
        return None
    # Simmer/Polymarket enforces the minimum after price rounding. Estimate the
    # worst-case share count at the FAK limit rather than at the top-of-book ask.
    shares = amount / limit_price
    if shares + 1e-9 < float(config["min_order_shares"]):
        return None
    return TradePlan(
        evaluation=evaluation,
        amount_usd=amount,
        shares=shares,
        limit_price=limit_price,
        bankroll=bankroll,
        game_exposure_usd=event_exposure,
    )


def _blocking_recommendation(container: Mapping[str, Any]) -> str | None:
    for key in ("recommendation", "recommended_action", "action", "decision"):
        value = str(container.get(key) or "").strip().lower()
        if any(term in value for term in ("hold", "skip", "avoid", "do not trade", "block")):
            return f"{key}={value}"
    return None


def _recommended_side(container: Mapping[str, Any]) -> str | None:
    """Extract an explicit YES/NO recommendation without guessing direction."""
    for key in ("recommended_side", "side", "trade_side", "direction", "recommendation"):
        value = str(container.get(key) or "").strip().lower()
        if not value:
            continue
        tokens = set(value.replace("_", " ").replace("-", " ").split())
        has_yes = "yes" in tokens
        has_no = "no" in tokens
        if has_yes != has_no:
            return "yes" if has_yes else "no"
    return None


def _slippage_fraction(
    container: Mapping[str, Any], planned_amount: float | None = None
) -> float | None:
    ratio_keys = (
        "estimated_slippage",
        "slippage_pct",
        "slippage_fraction",
        "price_impact",
        "price_impact_pct",
    )

    def ratio(item: Mapping[str, Any]) -> float | None:
        for key in ratio_keys:
            value = _finite_float(item.get(key))
            if value is not None:
                return value / 100.0 if value > 1.0 else value
        return None

    direct = ratio(container)
    if direct is not None:
        return direct

    estimates = container.get("estimates")
    candidates: list[tuple[float | None, float]] = []
    if isinstance(estimates, Mapping):
        iterable = []
        for key, value in estimates.items():
            if not isinstance(value, Mapping):
                continue
            amount = _finite_float(value.get("amount") or value.get("size_usd"))
            if amount is None:
                amount = _finite_float(str(key).replace("$", ""))
            iterable.append((amount, value))
    elif isinstance(estimates, Sequence) and not isinstance(estimates, (str, bytes)):
        iterable = [
            (
                _finite_float(item.get("amount") or item.get("size_usd")),
                item,
            )
            for item in estimates
            if isinstance(item, Mapping)
        ]
    else:
        iterable = []
    for amount, item in iterable:
        value = ratio(item)
        if value is not None:
            candidates.append((amount, value))
    if not candidates:
        return None
    if planned_amount is None:
        return max(value for _amount, value in candidates)
    sized = [(amount, value) for amount, value in candidates if amount is not None]
    if not sized:
        return max(value for _amount, value in candidates)
    at_or_above = sorted((item for item in sized if item[0] >= planned_amount), key=lambda x: x[0])
    if at_or_above:
        return at_or_above[0][1]
    return max(sized, key=lambda x: x[0])[1]


def check_context_safeguards(
    *,
    client: SimmerClient,
    plan: TradePlan,
    config: Mapping[str, Any],
    live: bool,
    no_safeguards: bool,
) -> SafeguardResult:
    """Run SDK context/discipline checks plus a non-skippable preflight."""
    context: Mapping[str, Any] | None = None
    market_id = str(_field(plan.evaluation.market, "id", ""))
    if not no_safeguards:
        raw_context = client.get_market_context(
            market_id,
            venue=VENUE,
            # Simmer's context endpoint accepts the market's YES probability,
            # regardless of which token this strategy plans to buy.
            my_probability=plan.evaluation.candidate.adjusted_yes_probability,
        )
        context = _as_mapping(raw_context)
        if not context:
            return SafeguardResult(False, "market context unavailable")
        positions = _as_mapping(context.get("positions"))
        venue_position = _as_mapping(positions.get(VENUE))
        if _is_true(venue_position.get("has_position")):
            return SafeguardResult(False, "existing Polymarket position in this market", context=context)
        legacy_position = _as_mapping(context.get("position"))
        if _is_true(legacy_position.get("has_position")):
            return SafeguardResult(False, "existing position in this market", context=context)

        discipline = _as_mapping(context.get("discipline"))
        for key in ("would_flip_flop", "is_flip_flop", "flip_flop"):
            if _is_true(discipline.get(key)):
                return SafeguardResult(False, f"discipline safeguard: {key}", context=context)
        recommendation = _blocking_recommendation(discipline)
        if recommendation:
            return SafeguardResult(False, f"discipline safeguard: {recommendation}", context=context)

        edge = _as_mapping(context.get("edge"))
        candidate_side = plan.evaluation.candidate.side
        if candidate_side == "yes":
            recommendation = _blocking_recommendation(edge)
            if recommendation:
                return SafeguardResult(False, f"edge safeguard: {recommendation}", context=context)
            sdk_edge = _finite_float(edge.get("user_edge"))
            if sdk_edge is None:
                sdk_edge = _finite_float(edge.get("edge"))
            if sdk_edge is not None and sdk_edge < float(config["min_ev"]):
                return SafeguardResult(
                    False,
                    "SDK context YES edge fell below the configured gate",
                    context=context,
                )
        else:
            # The context API receives a YES probability, so a signed ``edge``
            # is a YES edge and cannot be compared directly with this NO trade's
            # local executable-price edge. Honor only an explicit contrary side.
            recommended_side = _recommended_side(edge)
            if recommended_side is not None and recommended_side != "no":
                return SafeguardResult(
                    False,
                    f"SDK context recommends {recommended_side.upper()}, not NO",
                    context=context,
                )

        slippage = _slippage_fraction(
            _as_mapping(context.get("slippage")), plan.amount_usd
        )
        if slippage is not None and slippage > float(config["max_slippage"]):
            return SafeguardResult(False, f"SDK slippage {slippage:.2%} exceeds cap", context=context)

        warnings = context.get("warnings")
        if isinstance(warnings, Sequence) and not isinstance(warnings, (str, bytes)):
            for warning in warnings:
                lowered = str(warning).lower()
                if any(
                    term in lowered
                    for term in ("conflict", "flip-flop", "already hold", "unsafe", "low liquidity")
                ):
                    return SafeguardResult(False, f"SDK context warning: {warning}", context=context)

    # Readiness/exposure preflight remains mandatory even with --no-safeguards.
    preflight = client.preflight(
        venue=VENUE if live else "sim",
        planned_amount=plan.amount_usd,
        exposure_cap_usd=float(config["portfolio_exposure_cap_usd"]),
    )
    if not _is_true(_field(preflight, "ok_to_trade")):
        blockers = _field(preflight, "blockers", [])
        return SafeguardResult(
            False,
            f"preflight blocked trade: {', '.join(map(str, blockers)) or 'unknown blocker'}",
            preflight_id=str(_field(preflight, "client_preflight_id", "")) or None,
            context=context,
        )
    return SafeguardResult(
        True,
        "ok",
        preflight_id=str(_field(preflight, "client_preflight_id", "")) or None,
        context=context,
    )


def _trade_was_committed(result: Any) -> bool:
    """Interpret Simmer's fill status as the authoritative execution result.

    ``success`` can mean the request was accepted, not that an order/fill now
    exists. FAK no-fill/failed responses must not consume local exposure, while
    submitted/unconfirmed responses are reserved to prevent duplicate orders.
    """
    if result is None:
        return False
    fill_status = str(_field(result, "fill_status", "unknown") or "unknown").strip().lower()
    if fill_status in {"failed", "no_fill", "no-fill", "rejected", "cancelled", "canceled"}:
        return False
    if fill_status in {
        "filled",
        "partially_filled",
        "partially-filled",
        "partial",
        "submitted",
        "unconfirmed",
        "confirmed",
    }:
        return True
    shares = _finite_float(_field(result, "shares_filled")) or 0.0
    cost = _finite_float(_field(result, "cost")) or 0.0
    return shares > 0.0 or cost > 0.0


def execute_trade(
    *,
    client: SimmerClient,
    plan: TradePlan,
    config: Mapping[str, Any],
    state: dict[str, Any],
    live: bool,
    no_safeguards: bool,
    quiet: bool,
) -> Any | None:
    """Apply safeguards and execute a tagged, publicly reasoned Simmer trade."""
    safeguard = check_context_safeguards(
        client=client,
        plan=plan,
        config=config,
        live=live,
        no_safeguards=no_safeguards,
    )
    if not safeguard.ok:
        _emit(quiet, f"  SKIP safeguard: {safeguard.reason}")
        return None

    evaluation = plan.evaluation
    game = evaluation.game
    candidate = evaluation.candidate
    market = evaluation.market
    reasoning = build_reasoning(game, candidate, plan.amount_usd)
    reasoning += (
        f" Simmer market={_field(market, 'id')}, query={evaluation.query!r}, "
        f"spread={evaluation.spread:.3f}, quote_age={evaluation.quote_age_seconds:.1f}s, "
        f"top_size={evaluation.top_size_shares:.2f}, limit={plan.limit_price:.3f}, "
        f"sizing={config['position_sizing']}@{float(config['kelly_multiplier']):.2f}x, "
        f"preflight={safeguard.preflight_id or 'not-returned'}."
    )
    signal_data = {
        "signal_source": "espn_live_mlb",
        "espn_event_id": game.event_id,
        "espn_play_id": game.probability_play_id or game.last_play_id or "unknown",
        "edge": round(candidate.edge, 6),
        "confidence": round(candidate.confidence, 6),
        "raw_probability": round(candidate.raw_yes_probability, 6),
        "adjusted_probability": round(candidate.adjusted_yes_probability, 6),
        "p_win": round(candidate.p_win, 6),
        "execution_price": round(candidate.execution_price, 6),
        "inning": game.inning,
        "outs": game.outs,
        "score": game.score,
    }
    mode = "LIVE" if live else "DRY/PAPER"
    _emit(
        quiet,
        f"  {mode} BUY {candidate.side.upper()} ${plan.amount_usd:.2f} "
        f"(~{plan.shares:.2f} shares) @ limit {plan.limit_price:.3f}\n"
        f"    {reasoning}",
        force=True,
    )
    result = client.trade(
        market_id=str(_field(market, "id")),
        side=candidate.side,
        amount=plan.amount_usd,
        action="buy",
        venue=VENUE,
        order_type="FAK",
        price=plan.limit_price,
        reasoning=reasoning,
        source=TRADE_SOURCE,
        skill_slug=SKILL_SLUG,
        allow_rebuy=False,
        signal_data=signal_data,
    )
    success = _is_true(_field(result, "success"))
    fill_status = str(_field(result, "fill_status", "unknown"))
    committed = _trade_was_committed(result)
    if committed:
        _record_trade(state, plan=plan, result=result, live=live)
        _emit(
            quiet,
            f"  RESULT committed success={success} simulated={_field(result, 'simulated', False)} "
            f"fill={fill_status} shares={_field(result, 'shares_filled', 0)} "
            f"cost=${float(_field(result, 'cost', 0) or 0):.2f}",
            force=True,
        )
    else:
        _emit(
            quiet,
            f"  RESULT not committed: "
            f"{_field(result, 'error') or _field(result, 'skip_reason') or fill_status}",
            force=True,
        )
    return result


def _best_evaluation(
    client: SimmerClient,
    game: LiveGameState,
    *,
    core_config: StrategyConfig,
    config: Mapping[str, Any],
    quiet: bool,
) -> MarketEvaluation | None:
    found = _discover_markets(
        client,
        game,
        limit=int(config["market_query_limit"]),
    )
    evaluations: list[MarketEvaluation] = []
    for market, query in found:
        evaluation = _evaluate_market(market, game, query, core_config, config)
        if evaluation is not None:
            evaluations.append(evaluation)
    if not evaluations:
        _emit(quiet, "    no matching liquid full-game moneyline with a fresh executable quote")
        return None
    return max(
        evaluations,
        key=lambda item: (
            item.candidate.edge,
            item.candidate.raw_kelly_fraction,
            -item.spread,
        ),
    )


def run_strategy_once(
    *,
    client: SimmerClient,
    config: Mapping[str, Any],
    live: bool,
    no_safeguards: bool,
    quiet: bool,
) -> int:
    """One scan → score → gate → size → execute cycle."""
    state = _load_state()
    if live:
        try:
            client.auto_redeem()
        except Exception as exc:  # Keep trading fail-safe if redemption infrastructure is degraded.
            _emit(quiet, f"auto-redeem warning: {type(exc).__name__}", force=True)
    # Official Simmer guidance calls this once per run before discovery so an
    # underfunded wallet does not generate a storm of rejected trade attempts.
    bankroll, max_safe_size = _bankroll_and_safe_size(client, live=live, config=config)
    espn = EspnLiveClient(
        base_url=ESPN_SITE_BASE,
        timeout_seconds=float(config["espn_timeout_seconds"]),
        max_summary_requests=int(config["max_summary_requests"]),
    )
    snapshot = espn.fetch_live_snapshot()
    _emit(
        quiet,
        f"ESPN live snapshot: {snapshot.live_event_count} in-progress event(s), "
        f"{len(snapshot.live_games)} tradeable probability state(s), "
        f"{snapshot.summary_fallback_count} summary fallback(s)",
        force=True,
    )
    if not snapshot.live_games:
        _emit(quiet, "No live MLB game currently has a validated ESPN win probability.", force=True)
        return 0

    positions = _positions_as_dicts(client)
    core_config = _strategy_config(config)
    candidates: list[MarketEvaluation] = []
    for game in snapshot.live_games:
        _emit(
            quiet,
            f"  {game.away_abbreviation} {game.away_score} @ {game.home_abbreviation} "
            f"{game.home_score} — {game.status_detail}; ESPN home WP "
            f"{game.home_win_probability:.1%} ({game.probability_source})",
        )
        blocked = _event_is_blocked(state, game, int(config["cooldown_seconds"]))
        if blocked:
            _emit(quiet, f"    skip: {blocked}")
            continue
        if _has_game_position(positions, game):
            _emit(quiet, "    skip: an existing position already matches this MLB game")
            continue
        evaluation = _best_evaluation(
            client,
            game,
            core_config=core_config,
            config=config,
            quiet=quiet,
        )
        if evaluation is not None:
            _emit(
                quiet,
                f"    candidate {evaluation.candidate.side.upper()} edge "
                f"{evaluation.candidate.edge:.1%} @ {evaluation.candidate.execution_price:.3f}",
            )
            candidates.append(evaluation)

    candidates.sort(
        key=lambda item: (-item.candidate.edge, item.spread, item.quote_age_seconds)
    )
    placed = 0
    remaining_bankroll = bankroll
    remaining_safe_size = max_safe_size
    for evaluation in candidates:
        if placed >= int(config["max_trades_per_run"]):
            break
        plan = _make_plan(
            evaluation,
            bankroll=remaining_bankroll,
            max_safe_size=remaining_safe_size,
            state=state,
            config=config,
        )
        if plan is None:
            _emit(quiet, f"  SKIP {evaluation.game.event_id}: sizing/liquidity/min-share gate")
            continue
        result = execute_trade(
            client=client,
            plan=plan,
            config=config,
            state=state,
            live=live,
            no_safeguards=no_safeguards,
            quiet=quiet,
        )
        if _trade_was_committed(result):
            placed += 1
            remaining_bankroll = max(0.0, remaining_bankroll - plan.amount_usd)
            remaining_safe_size = max(0.0, remaining_safe_size - plan.amount_usd)

    if not candidates:
        _emit(quiet, "No trade passed live-state, identity, quote, EV, and risk gates.", force=True)
    elif placed == 0:
        _emit(quiet, "Candidates existed, but every trade failed sizing or safeguards.", force=True)
    return placed


def _show_positions(client: SimmerClient, *, live: bool) -> None:
    positions = _positions_as_dicts(client)
    payload: dict[str, Any] = {
        "mode": "live" if live else "dry/paper",
        "venue": VENUE,
        "source": TRADE_SOURCE,
        "positions": positions,
        "local_state": _load_state(),
    }
    if not live:
        payload["paper_summary"] = client.get_paper_summary()
    else:
        payload["portfolio"] = client.get_portfolio(venue=VENUE)
    print(json.dumps(payload, indent=2, default=_json_default), flush=True)


def _show_config(config: Mapping[str, Any]) -> None:
    payload = {
        "skill": SKILL_SLUG,
        "version": VERSION,
        "config_path": str(get_config_path(__file__)),
        "values": dict(config),
    }
    print(json.dumps(payload, indent=2, sort_keys=True, default=_json_default), flush=True)


def _parse_set_values(items: Iterable[str]) -> dict[str, Any]:
    updates: dict[str, Any] = {}
    for item in items:
        if "=" not in item:
            raise ValueError(f"--set expects KEY=VALUE, got {item!r}")
        key, raw = item.split("=", 1)
        key = key.strip()
        if key not in CONFIG_SCHEMA:
            raise ValueError(f"unknown config key {key!r}")
        converter = CONFIG_SCHEMA[key].get("type", str)
        if converter is bool:
            normalized = raw.strip().lower()
            if normalized not in {"true", "false", "1", "0", "yes", "no", "on", "off"}:
                raise ValueError(f"invalid boolean value {raw!r}")
            value = normalized in {"true", "1", "yes", "on"}
        else:
            value = converter(raw)
        updates[key] = value
    return updates


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="mlb_live_trader.py",
        description="Trade live MLB full-game moneylines from ESPN win probability via Simmer.",
    )
    parser.add_argument(
        "--live",
        action="store_true",
        help="execute real Polymarket orders; default is Simmer dry/paper execution",
    )
    parser.add_argument("--positions", action="store_true", help="show positions and local state")
    parser.add_argument("--config", action="store_true", help="print resolved config and exit")
    parser.add_argument(
        "--set",
        action="append",
        default=[],
        metavar="KEY=VALUE",
        help="persist a config override; repeatable",
    )
    parser.add_argument(
        "--no-safeguards",
        action="store_true",
        help="skip SDK context/discipline checks; hard risk controls and preflight remain",
    )
    parser.add_argument("--quiet", action="store_true", help="suppress nonessential scan output")
    parser.add_argument("--loop", action="store_true", help="poll continuously instead of one cycle")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    config = load_config(CONFIG_SCHEMA, __file__, slug=SKILL_SLUG)
    try:
        _validate_config(config)
        if args.set:
            updates = _parse_set_values(args.set)
            preview = dict(config)
            preview.update(updates)
            _validate_config(preview)
            saved = update_config(updates, __file__)
            print(
                json.dumps(
                    {
                        "updated": updates,
                        "config_path": str(get_config_path(__file__)),
                        "stored": saved,
                    },
                    indent=2,
                    sort_keys=True,
                ),
                flush=True,
            )
            return 0
        if args.config:
            _show_config(config)
            return 0

        client = get_client(live=args.live, config=config)
        if args.positions:
            _show_positions(client, live=args.live)
            return 0

        mode = "LIVE REAL-MONEY" if args.live else "DRY/PAPER"
        _emit(args.quiet, f"MLB Live Trader {VERSION} — {mode}", force=True)
        if args.no_safeguards:
            _emit(
                args.quiet,
                "WARNING: SDK context safeguards disabled; hard caps/preflight remain active.",
                force=True,
            )
        with RunLock(_LOCK_PATH):
            if not args.loop:
                run_strategy_once(
                    client=client,
                    config=config,
                    live=args.live,
                    no_safeguards=args.no_safeguards,
                    quiet=args.quiet,
                )
                return 0

            while True:
                started = time.monotonic()
                try:
                    run_strategy_once(
                        client=client,
                        config=config,
                        live=args.live,
                        no_safeguards=args.no_safeguards,
                        quiet=args.quiet,
                    )
                except (EspnApiError, RuntimeError, ValueError) as exc:
                    _emit(
                        args.quiet,
                        f"cycle failed closed: {type(exc).__name__}: {exc}",
                        force=True,
                    )
                delay = max(0.0, int(config["poll_seconds"]) - (time.monotonic() - started))
                time.sleep(delay)
    except KeyboardInterrupt:
        print("stopped", flush=True)
        return 130
    except (EspnApiError, RuntimeError, ValueError) as exc:
        print(f"error: {type(exc).__name__}: {exc}", file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
