# Risk and data disclaimer

Read this before connecting real funds. Running MLB Live Trader means you accept everything below.

## Framework, not a production trading system

This is a template: a deterministic reference implementation of a `scan → score → EV gate → size → safeguards → execute` pipeline. It is not a hardened, supervised, or supported trading product, and it offers no guarantee of uptime, correctness, market coverage, or fill quality. You are the operator, and the operator owns the outcome.

## Not financial advice

Nothing here — the code, the defaults, the documentation, or the example output — is financial, investment, legal, tax, or betting advice, nor an offer or solicitation to trade. No profit is promised or implied, and simulated results do not predict live results.

## Live orders are real and irreversible

Paper/dry mode is the default; `--live` submits real orders that spend real money on-chain. A broadcast, filled order cannot be undone, cancelled, refunded, or clawed back — not by this software, not by Simmer, not by you. A prediction-market position can lose 100% of its cost. Live sports markets add latency, suspended-game, feed-correction, order-book, partial-fill, fee, gas, wallet, API-outage, and resolution-rule risk. Kelly sizing is only as good as the probability estimate; a biased or stale estimate turns mathematically neat sizing into mathematically neat losses.

## The ESPN feed is undocumented and can be wrong

ESPN's public site JSON feed is undocumented and unsupported. It can change without notice, lag, omit fields, drop play-by-play, correct or retract plays, misreport delays and suspensions, or go offline entirely. Its win probability is a model output, not truth, and it is not calibrated for trading. The skill fails closed and skips what it cannot validate, which reduces this risk but does not remove it. Never replace a missing feed value with a guessed probability.

## The defaults are not a validated edge

Every shipped default — the `0.25` Kelly multiplier, the `0.05` minimum EV, the `0.90` probability haircut, the 2%-of-bankroll and $25 per-trade caps, $35 per game, $100 daily and portfolio exposure, 3 trades per run, and the spread, slippage, and quote-age gates — is a conservative starting point chosen for safety. None of it is backtested, and none of it has been validated as a trading edge on any market. Treat these as guardrails to test against, not as a recommendation.

## Paper first, then out of sample

Run in paper mode against live prices before you enable `--live`. Measure probability calibration, closing-line value, latency, fill quality, fees, and drawdown, then confirm the result out of sample — on data you did not use to tune. Tighten limits before you loosen them: any change to sizing, EV, or exposure caps re-opens the question of whether the strategy works at all.

## Your responsibility, your jurisdiction

You are solely responsible for how this software is used and for every order it places on your behalf, including orders placed while it runs unattended. Trade only with capital you can afford to lose in full. Comply with all laws, regulations, tax obligations, and sanctions that apply to you, and with the terms of service of Simmer, Polymarket, ESPN, and any other venue or data provider you touch. Prediction markets are restricted or prohibited for some persons and in some jurisdictions; confirming your own eligibility is your job, not this software's. Review each market's resolution criteria yourself — resolution is decided by the venue, not by this code. The software is provided "as is", without warranty of any kind, express or implied, and without any liability for loss or damage arising from its use.
