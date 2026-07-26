---
name: "mlb-live-trader"
description: "Paper-first live MLB moneyline evaluation and bounded Simmer execution."
metadata:
  author: "kvzsolt"
  version: "1.0.0"
  displayName: "MLB Live Trader"
  difficulty: "intermediate"
---

# MLB Live Trader

MLB Live Trader evaluates in-progress MLB full-game moneylines by comparing ESPN's live win probability with the executable Simmer/Polymarket price.

> 🚨 **Framework, not a production trading system.** Read [DISCLAIMER.md](DISCLAIMER.md) before connecting real funds. Paper mode is the default; real orders require `--live`. Default hard bounds include **2% of bankroll and $25 maximum per trade**, **3 trades per run**, **$35 per game**, and **$100 daily/portfolio exposure**.

> **This is a template.** The signal and execution plumbing are deterministic, but the defaults are not a validated trading edge. Measure calibration, latency, fills, and drawdown out of sample before changing limits.

The monofile entrypoint performs:

`scan → identify → score → EV gate → Kelly size → safeguards → execute`

It rejects pregame/final games, props, stale or incomplete quotes, ambiguous market wording, suspended games, missing play-by-play, uncertain doubleheaders, duplicate signals, existing game positions, and orders below the venue minimum. It never imports a CLOB client or sends orders directly to Polymarket.

## Method

1. Read ESPN live MLB status, inning, score, count, outs, bases, pitcher, batter, last play, and home win probability. If the current scoreboard play lacks probability, use only a bounded summary fallback tied to its own play ID.
2. Resolve the matching active full-game moneyline through Simmer and verify teams, date, venue, outcome mapping, and executable order-book quotes.
3. Shrink the ESPN estimate toward 50%, with confidence increasing as the game progresses.
4. Require the adjusted probability to exceed the executable outcome price plus the fee buffer and minimum EV.
5. Use `simmer_sdk.sizing.size_position()` for fractional-Kelly sizing, then enforce hard bankroll, order, game, daily, portfolio, spread, slippage, liquidity, and trade-count caps.
6. Submit a bounded FAK limit buy tagged with `source=sdk:mlb-live-trader` and `skill_slug=mlb-live-trader`.
7. Enter at most once per game and hold to resolution. Never martingale or average down.

## Setup

```bash
python -m venv .venv
. .venv/bin/activate
pip install 'simmer-sdk>=0.22.2,<0.23'
export SIMMER_API_KEY='sk_live_...'
```

Install the published skill:

```bash
npx clawhub@latest install mlb-live-trader
```

## Run safely

```bash
# Validate configuration without an API request
python mlb_live_trader.py --config

# One paper cycle using real market data; cannot place a real order
python mlb_live_trader.py

# Continuous paper loop
python mlb_live_trader.py --loop

# Read-only status output
python scripts/status.py
python scripts/status.py --live

# Explicit real-money opt-in
python mlb_live_trader.py --live
```

Use `--set KEY=VALUE` to persist safe tuning changes in `config.json`. Never place credentials in that file. For example:

```bash
python mlb_live_trader.py --set min_ev=0.07 --set max_position_usd=15
```

`--no-safeguards` disables only Simmer context/discipline checks. Hard EV, price, minimum-share, spread, exposure, idempotency, and SDK preflight controls remain active.

## Important defaults

- Fractional Kelly: `0.25`
- Minimum fee-adjusted EV: `0.05`
- Probability haircut: `0.90`
- Per-trade bankroll cap: `0.02`
- Per-order cap: `$25`
- Per-game cap: `$35`
- Daily spend cap: `$100`
- Portfolio exposure cap: `$100`
- Maximum trades per run: `3`
- Quote age limit: `90 seconds`
- Maximum spread: `0.08`
- Maximum slippage: `0.03`
- Minimum shares: `5`

The complete set of managed settings is declared under `tunables` in `clawhub.json`.

## Status command

`scripts/status.py` is read-only. It reports the execution mode, strategy-tagged positions, paper summary or live portfolio, and local idempotency state. It must never place, cancel, redeem, or modify orders and never prints credentials.

Run it first when a live order is blocked:

```bash
python scripts/status.py --live
```

## Local state

The strategy writes `.mlb-live-trader-state.json` beside the entrypoint with mode `0600`. It contains signal IDs, market/order IDs, reserved spend, and timestamps—not secrets. A process lock prevents overlapping runs. Delete the state only when deliberately resetting idempotency and daily-spend history.

## Fail-closed behavior

- No in-progress ESPN game: skip.
- Unvalidated or missing probability: skip.
- No unambiguous active full-game moneyline: skip.
- Stale quote, excessive spread/slippage, insufficient depth, or weak EV: skip.
- Existing position, cooldown, duplicate signal, or exposure cap: skip.
- ESPN/API parsing failure: skip and report the reason.
- Real wallet/preflight failure: skip and inspect with `scripts/status.py --live`.

ESPN's public site feed is undocumented and can change, lag, omit fields, or correct plays. Never replace missing feed values with guessed probabilities.

## Publish and verify

```bash
npx clawhub@latest publish . --slug mlb-live-trader --version 1.0.0
npx clawhub@latest inspect mlb-live-trader
```

Verify that ClawHub reports `Moderation: CLEAN` and test a fresh install before enabling managed execution.
