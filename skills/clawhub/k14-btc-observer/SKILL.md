---
name: k14-btc-observer
description: Observe Binance BTCUSDT K14 signals and public Polymarket feeds; test managed runtime and checkpoint persistence without trading.
metadata:
  version: "0.1.0"
  displayName: BTC K14 Observer
  difficulty: advanced
---

# BTC K14 Observer

Read [DISCLAIMER.md](DISCLAIMER.md). This package observes public data only, spends zero dollars, and has no order, cancellation, wallet, redemption, or transaction capability. It cannot be enabled for trading with `--live` or an environment variable.

Run `python observer.py`. It fetches exactly 14 completed Binance BTCUSDT 15-minute bars, applies the bundled frozen monthly thresholds, discovers the matching public Polymarket market, and probes both public WebSocket connections for 900 seconds. Output is JSON Lines with a final `AUTOMATON_REPORT` summary.

The K14 result is a directional candidate, not a complete entry decision. Fair-value, liquidity, execution, position accounting, and dynamic exits remain in the original execution program. No fills or profits are simulated here.

## Managed execution

`clawhub.json` declares a managed entrypoint and a 30-minute schedule. This is a requested schedule, not proof that a cloud runner was provisioned. A run is verified only after its actual report is retrieved. No API key or wallet key is read by this program. `simmer-sdk` is a registry discovery dependency; it is deliberately not instantiated because the probe needs only public data.

Environment: `K14_PROBE_SECONDS` defaults to 900 (range 1–1800); `K14_STATE_DIR` optionally identifies a persistent directory. No arbitrary network destinations are configurable. The default state directory is `state/` beside this script. Use `--seconds 20` for a short connectivity check.

## Interpreting evidence

- `signal_snapshot`: Binance server-time anchored window, input bars, K14, frozen thresholds, and signal candidate. Missing/unclosed bars or expired thresholds fail closed.
- `checkpoint`: a local run identifier and monotonically increasing checkpoint count.
- `previous_run`: a previous record was readable in this filesystem. This alone does not prove distributed mutual exclusion or storage survival after host replacement.
- `ws_summary`: message counts, last receive age, and source-time lag estimates for both public feeds. Lag is an estimate using Binance clock, not an independently synchronized one-way network measurement.
- `run_end`: observed duration, feed failures, and `orders_submitted: 0`.

The SQLite lease prevents overlapping runs sharing the same database. It cannot prevent duplicates on isolated runner filesystems. A previous `RUNNING` run can be recovered only after its lease expires; recovery is reported as interrupted.

## Data validity

The bundled thresholds apply only to October 2026 UTC. A later month is blocked until a separately validated threshold file is supplied. Never silently reuse expired thresholds or switch from Binance global spot to a different exchange. Connection failures are reported without treating an old price as fresh.

Tests and local evidence are outside this deployable folder. Only this folder is intended for publication.
