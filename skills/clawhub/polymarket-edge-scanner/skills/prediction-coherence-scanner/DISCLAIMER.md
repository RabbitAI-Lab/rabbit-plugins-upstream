# Disclaimer

## This is a framework, not a production trading system

This skill is a scanner and a set of safety gates. It is a starting point for
your own research, not a validated money-making system.

## No financial advice

Nothing in this skill constitutes financial, investment, or trading advice. The
default strategy is a starting point, not a tested edge. On the market data
measured while building it (17/07/2026), the scanner found no executable edge at
all, and the executable quote data needed to confirm one was not available
through the API. See [references/METHOD.md](references/METHOD.md).

## Default parameters are not validated

Defaults are calibrated for testing the plumbing, not for live profit. The
caps ($10 per trade, 5 trades per run, dry-run unless `--live`) exist to bound
mistakes, not to size a real position. Run paper mode on the `sim` venue for an
extended period before considering anything else.

## Automated trading carries irreversible risk

When this skill runs with `--live` against `polymarket` or `kalshi`, it places
real on-chain orders with real funds. On-chain trades cannot be recalled.

## The arbitrage guarantee is conditional and fragile

The "guaranteed payout" holds only if the leg set is genuinely complete, every
leg fills, and the resolution criteria are what you believe them to be. Any one
of those failing turns a supposed hedge into an open directional bet. Partial
fills are the normal failure mode. Read the execution risk section of
METHOD.md before running with `--live`.

## Use of this skill is at your own risk

By installing and running this skill you agree that the authors are not liable
for any losses, direct or indirect, that arise from its use.
