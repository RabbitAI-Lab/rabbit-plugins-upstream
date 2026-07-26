#!/usr/bin/env python3
"""Calibration-aware position sizing for prediction markets.

You bring the probability estimate. This decides the stake, after correcting
that estimate for the error it actually carries.

Kelly sizing assumes your probability is exact. It never is. Sizing on a raw
estimate loses money even when the estimate is genuinely better than the
market. See references/METHOD.md for the measurements behind every default.

Library first, CLI second. Import `decide()` from your own skill, or run this
file directly.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from typing import Any, Optional

SKILL_SLUG = "calibration-aware-sizing"

# --- Defaults. Each traces to a measurement in references/METHOD.md. ---

# Typical dispersion of a liquid prediction-market price around the true
# probability. Enters lambda as the market's precision. 0.03 is a deliberately
# tight assumption: a tighter market means less room for you to beat it, so
# this errs toward smaller stakes.
DEFAULT_SIGMA_MKT = 0.03

# Assumed accuracy of YOUR forecast when you have not measured it. 0.10 is
# deliberately pessimistic. An unmeasured forecaster is not a good one.
DEFAULT_SIGMA_EST = 0.10

# Hard ceiling on the weight placed on your own estimate. lambda -> 1 means
# "trust my number completely", which is the setting that produced a 96%
# wipeout rate under overconfidence. Not reachable from the CLI by accident.
MAX_LAMBDA = 0.60

# Fraction of full Kelly. The backstop that survives a wrong lambda.
DEFAULT_KELLY_MULTIPLIER = 0.25
MAX_KELLY_MULTIPLIER = 0.50

# Minimum edge per share, in dollars, AFTER shrinkage. Below this the edge is
# indistinguishable from noise and fees.
DEFAULT_MIN_EV = 0.02

DEFAULT_MAX_TRADE_USD = 10.0
DEFAULT_EXPOSURE_CAP_USD = 100.0

# Below this many resolved forecasts, a measured sigma is not usable. At
# N=1000 the recovered sigma still spans 0.000-0.086 (p10-p90). There is no
# sample size at which a point estimate of lambda is safe, so measurement
# only ever loosens lambda from the pessimistic default, never past MAX_LAMBDA.
MIN_RESOLVED_FOR_SIGMA = 200

VALID_VENUES = ("sim", "polymarket", "kalshi")


def lambda_from_accuracy(sigma_est: float, sigma_mkt: float = DEFAULT_SIGMA_MKT) -> float:
    """Bayes weight to place on your own estimate versus the market price.

    Treat the market price and your forecast as two independent noisy readings
    of the same true probability. With a flat prior the posterior mean is the
    precision-weighted average, which reduces to:

        p_posterior = q + lambda * (p_hat - q)
        lambda      = sigma_mkt^2 / (sigma_mkt^2 + sigma_est^2)

    Validated against simulation: at sigma_est=0.06 the formula predicts
    lambda=0.20 and the empirical optimum is 0.20. See references/METHOD.md.

    As accurate as the market -> lambda 0.5, halve your edge.
    Twice as noisy as the market -> lambda 0.2, keep a fifth of it.
    """
    if sigma_est < 0 or sigma_mkt < 0:
        raise ValueError("sigma values must be non-negative")
    if sigma_est == 0 and sigma_mkt == 0:
        raise ValueError("sigma_est and sigma_mkt cannot both be zero")
    return (sigma_mkt ** 2) / (sigma_mkt ** 2 + sigma_est ** 2)


def shrink_probability(p_hat: float, market_price: float, lam: float) -> float:
    """Pull a raw forecast toward the market price by weight `lam`."""
    if not 0.0 <= lam <= 1.0:
        raise ValueError(f"lambda must be in [0,1], got {lam}")
    return market_price + lam * (p_hat - market_price)


@dataclass
class Decision:
    """The verdict. `stake` is 0 unless every gate passed."""
    stake: float = 0.0
    side: Optional[str] = None
    price: Optional[float] = None
    p_hat: float = 0.0
    p_shrunk: float = 0.0
    lam: float = 0.0
    edge_raw: float = 0.0
    edge_shrunk: float = 0.0
    kelly_multiplier: float = 0.0
    abstained: bool = True
    reasons: list[str] = field(default_factory=list)

    def explain(self) -> str:
        head = (
            f"stake=${self.stake:.2f} side={self.side} price={self.price}\n"
            f"  p_hat={self.p_hat:.4f} -> p_shrunk={self.p_shrunk:.4f} (lambda={self.lam:.2f})\n"
            f"  edge/share: raw={self.edge_raw:+.4f} shrunk={self.edge_shrunk:+.4f}"
        )
        if self.reasons:
            head += "\n  " + "\n  ".join(f"ABSTAIN: {r}" for r in self.reasons)
        return head


def decide(
    p_hat: float,
    market_price: float,
    bankroll: float,
    *,
    sigma_est: float = DEFAULT_SIGMA_EST,
    sigma_mkt: float = DEFAULT_SIGMA_MKT,
    lam: Optional[float] = None,
    kelly_multiplier: float = DEFAULT_KELLY_MULTIPLIER,
    min_ev: float = DEFAULT_MIN_EV,
    max_trade_usd: float = DEFAULT_MAX_TRADE_USD,
    current_exposure_usd: float = 0.0,
    exposure_cap_usd: float = DEFAULT_EXPOSURE_CAP_USD,
) -> Decision:
    """Turn a probability estimate into a stake, or refuse to.

    Gate order matters: the estimate is corrected before any edge is believed,
    and the edge is tested after correction, never before.
    """
    d = Decision(p_hat=p_hat)

    # Input validity. A forecast outside (0,1) is a bug upstream, not an edge.
    if not 0.0 < p_hat < 1.0:
        d.reasons.append(f"p_hat {p_hat} outside (0,1)")
        return d
    if not 0.0 < market_price < 1.0:
        d.reasons.append(f"market_price {market_price} outside (0,1)")
        return d
    if bankroll <= 0:
        d.reasons.append("bankroll is zero or negative")
        return d

    # Kelly multiplier is capped hard. It is the backstop that survives a
    # wrong lambda, so it does not get to be optional.
    if kelly_multiplier > MAX_KELLY_MULTIPLIER:
        d.reasons.append(
            f"kelly_multiplier {kelly_multiplier} exceeds cap {MAX_KELLY_MULTIPLIER}"
        )
        return d
    if kelly_multiplier <= 0:
        d.reasons.append("kelly_multiplier must be positive")
        return d

    lam = lambda_from_accuracy(sigma_est, sigma_mkt) if lam is None else lam
    if lam > MAX_LAMBDA:
        d.reasons.append(
            f"lambda {lam:.2f} exceeds cap {MAX_LAMBDA} "
            f"(claimed accuracy is not measurable at realistic sample sizes)"
        )
        return d
    d.lam = lam

    d.p_shrunk = shrink_probability(p_hat, market_price, lam)
    d.edge_raw = p_hat - market_price

    # Direction is chosen on the SHRUNK estimate. Shrinkage can legitimately
    # flip a marginal call back to the market's side, and that is the point.
    if d.p_shrunk >= market_price:
        side, price, p_win = "yes", market_price, d.p_shrunk
    else:
        side, price, p_win = "no", 1.0 - market_price, 1.0 - d.p_shrunk
    d.side, d.price = side, price
    d.edge_shrunk = p_win - price

    if d.edge_shrunk < min_ev:
        d.reasons.append(
            f"shrunk edge {d.edge_shrunk:+.4f} below min_ev {min_ev} "
            f"(raw edge was {d.edge_raw:+.4f})"
        )
        return d

    if current_exposure_usd >= exposure_cap_usd:
        d.reasons.append(
            f"exposure ${current_exposure_usd:.2f} at or above cap ${exposure_cap_usd:.2f}"
        )
        return d

    stake = _size(p_win, price, bankroll, kelly_multiplier, min_ev)
    if stake <= 0:
        d.reasons.append("sizing returned zero")
        return d

    # Caps apply in order, tightest wins.
    stake = min(stake, max_trade_usd, exposure_cap_usd - current_exposure_usd, bankroll)
    if stake <= 0:
        d.reasons.append("stake clamped to zero by caps")
        return d

    d.stake = round(stake, 2)
    d.kelly_multiplier = kelly_multiplier
    d.abstained = False
    return d


def _size(p_win: float, price: float, bankroll: float, mult: float, min_ev: float) -> float:
    """Fractional Kelly. Uses the Simmer SDK when present, else closed form.

    The SDK's size_position was verified to match (p-q)/(1-q) exactly, so the
    fallback is equivalent rather than an approximation.
    """
    try:
        from simmer_sdk import size_position  # type: ignore
        return size_position(
            p_win, price, bankroll,
            kelly_multiplier=mult, min_ev=min_ev,
        )
    except ImportError:
        if p_win - price < min_ev:
            return 0.0
        kelly = (p_win - price) / (1.0 - price)
        return max(0.0, kelly * mult * bankroll)


def log_forecast(path: str, p_hat: float, market_price: float, market_id: str,
                 lam: float, stake: float, venue: str) -> None:
    """Append a forecast record. Nothing else records p_hat.

    The Simmer trade record has no outcome/resolved/pnl field and stores your
    forecast only if you put it in signal_data. Without this log there is no
    way to score yourself later.
    """
    rec = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "market_id": market_id,
        "p_hat": p_hat,
        "market_price": market_price,
        "lambda": lam,
        "stake": stake,
        "venue": venue,
        "outcome": None,  # fill with 1/0 once resolved; see scripts/calibrate.py
    }
    with open(path, "a") as fh:
        fh.write(json.dumps(rec) + "\n")


def _load_sigma_from_calibration(path: str) -> Optional[float]:
    """Read a conservative sigma_est written by scripts/calibrate.py."""
    try:
        with open(path) as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError):
        return None
    if data.get("n_resolved", 0) < MIN_RESOLVED_FOR_SIGMA:
        return None
    # Deliberately the conservative (high) end of the interval, never the point
    # estimate. A low sigma reading is the dangerous direction.
    return data.get("sigma_est_conservative")


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        description="Size a prediction-market trade from a probability estimate.",
        epilog="Dry run by default. --live places a real order.",
    )
    ap.add_argument("--p-hat", type=float, required=True,
                    help="Your probability that the YES side resolves true.")
    ap.add_argument("--market-id", help="Simmer market id. Required for --live.")
    ap.add_argument("--market-price", type=float,
                    help="YES price. Fetched from Simmer when omitted.")
    ap.add_argument("--bankroll", type=float,
                    help="Bankroll. Fetched from Simmer when omitted.")
    ap.add_argument("--sigma-est", type=float, default=None,
                    help=f"Your forecast error. Default {DEFAULT_SIGMA_EST} (pessimistic).")
    ap.add_argument("--sigma-mkt", type=float, default=DEFAULT_SIGMA_MKT)
    ap.add_argument("--lambda", dest="lam", type=float, default=None,
                    help=f"Override lambda directly. Capped at {MAX_LAMBDA}.")
    ap.add_argument("--calibration", default="calibration.json",
                    help="Output of scripts/calibrate.py. Used only if it has "
                         f">={MIN_RESOLVED_FOR_SIGMA} resolved forecasts.")
    ap.add_argument("--kelly-multiplier", type=float, default=DEFAULT_KELLY_MULTIPLIER)
    ap.add_argument("--min-ev", type=float, default=DEFAULT_MIN_EV)
    ap.add_argument("--max-trade", type=float, default=DEFAULT_MAX_TRADE_USD)
    ap.add_argument("--exposure-cap", type=float, default=DEFAULT_EXPOSURE_CAP_USD)
    ap.add_argument("--venue", default=os.environ.get("TRADING_VENUE", "sim"),
                    choices=VALID_VENUES)
    ap.add_argument("--forecast-log", default="forecasts.jsonl")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--live", action="store_true",
                    help="Place the order. Without this, nothing is sent.")
    args = ap.parse_args(argv)

    sigma_est = args.sigma_est
    sigma_source = "explicit --sigma-est"
    if sigma_est is None:
        measured = _load_sigma_from_calibration(args.calibration)
        if measured is not None:
            sigma_est, sigma_source = measured, f"measured ({args.calibration})"
        else:
            sigma_est, sigma_source = DEFAULT_SIGMA_EST, "pessimistic default (unmeasured)"

    client = None
    market_price, bankroll, exposure = args.market_price, args.bankroll, 0.0

    if market_price is None or bankroll is None or args.live:
        client = _client(args.venue)
        if client is None:
            print("Need SIMMER_API_KEY and simmer-sdk, or pass "
                  "--market-price and --bankroll for an offline dry run.",
                  file=sys.stderr)
            return 2
        if not args.market_id:
            print("--market-id required when fetching price or trading live.",
                  file=sys.stderr)
            return 2
        market_price, bankroll, exposure = _fetch(client, args.market_id,
                                                  args.venue, market_price, bankroll)
        if market_price is None:
            print(f"Could not read a price for {args.market_id}.", file=sys.stderr)
            return 2

    d = decide(
        args.p_hat, market_price, bankroll,
        sigma_est=sigma_est, sigma_mkt=args.sigma_mkt, lam=args.lam,
        kelly_multiplier=args.kelly_multiplier, min_ev=args.min_ev,
        max_trade_usd=args.max_trade, current_exposure_usd=exposure,
        exposure_cap_usd=args.exposure_cap,
    )

    if args.json:
        out = asdict(d)
        out["sigma_est"] = sigma_est
        out["sigma_source"] = sigma_source
        out["live"] = args.live
        print(json.dumps(out, indent=2))
    else:
        print(f"sigma_est={sigma_est} ({sigma_source})")
        print(d.explain())

    if d.abstained:
        return 1
    if not args.live:
        if not args.json:
            print("\nDRY RUN. No order sent. Re-run with --live to place it.")
        return 0

    return _execute(client, args, d)


def _client(venue: str):
    key = os.environ.get("SIMMER_API_KEY")
    if not key:
        return None
    try:
        from simmer_sdk import SimmerClient  # type: ignore
    except ImportError:
        return None
    return SimmerClient(api_key=key, venue=venue)


def _fetch(client, market_id: str, venue: str, price: Optional[float],
           bankroll: Optional[float]) -> tuple[Optional[float], float, float]:
    """Read price, bankroll and current exposure. Explicit args win."""
    if price is None:
        try:
            m = client.get_market_by_id(market_id)
            if m is not None:
                price = _extract(m, ("current_probability", "price", "yes_price",
                                     "probability", "last_price"))
        except Exception as exc:  # noqa: BLE001 - never trade on a failed read
            print(f"price lookup failed: {exc}", file=sys.stderr)

    exposure = 0.0
    try:
        for pos in client.get_positions(venue=venue) or []:
            exposure += float(_extract(pos, ("cost_basis",)) or 0.0)
    except Exception as exc:  # noqa: BLE001
        print(f"exposure lookup failed, assuming 0: {exc}", file=sys.stderr)

    if bankroll is None:
        bankroll = 0.0
        try:
            pf = client.get_portfolio(venue=venue) or {}
            bucket = pf.get(venue, pf) if isinstance(pf, dict) else {}
            bankroll = float(_extract(bucket, ("cash", "balance", "sim_balance",
                                               "available", "cash_balance")) or 0.0)
        except Exception as exc:  # noqa: BLE001
            print(f"bankroll lookup failed: {exc}", file=sys.stderr)
    return price, bankroll, exposure


def _extract(obj: Any, keys: tuple[str, ...]) -> Optional[float]:
    """Pull the first present key from a dict or object. Venue payloads differ."""
    for k in keys:
        v = obj.get(k) if isinstance(obj, dict) else getattr(obj, k, None)
        if v is not None:
            try:
                return float(v)
            except (TypeError, ValueError):
                continue
    return None


def _execute(client, args, d: Decision) -> int:
    reasoning = (
        f"p_hat={d.p_hat:.3f} shrunk to {d.p_shrunk:.3f} toward market "
        f"{d.price:.3f} at lambda={d.lam:.2f}; shrunk edge {d.edge_shrunk:+.3f}/share; "
        f"{d.kelly_multiplier:g}x Kelly."
    )
    try:
        res = client.trade(
            market_id=args.market_id,
            side=d.side,
            amount=d.stake,
            reasoning=reasoning,
            source=f"sdk:{SKILL_SLUG}",
            skill_slug=SKILL_SLUG,
            # The only durable record of the forecast. The trade row has no
            # outcome field, so calibration depends on this surviving.
            signal_data={
                "p_hat": d.p_hat,
                "p_shrunk": d.p_shrunk,
                "lambda": d.lam,
                "sigma_mkt": args.sigma_mkt,
                "edge_shrunk": d.edge_shrunk,
                "kelly_multiplier": d.kelly_multiplier,
            },
        )
    except Exception as exc:  # noqa: BLE001
        print(f"TRADE FAILED: {exc}", file=sys.stderr)
        return 3

    print(f"\nORDER SENT: {d.side} ${d.stake:.2f} on {args.market_id}")
    print(f"  {res}")
    log_forecast(args.forecast_log, d.p_hat, d.price, args.market_id,
                 d.lam, d.stake, args.venue)
    print(f"  forecast logged to {args.forecast_log} (score it later with "
          f"scripts/calibrate.py)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
