# Alpaca Paper Trading - Strategy

Account: PA3BJ0TMYV0B (paper). Started 2026-07-16 with $60,000.
Goal: grow the account. This is paper money, so controlled risk-taking is fine,
but treat it like real money: process over gambling.

## Approach

Swing trading, holding periods of days to weeks. Long-biased (market is in an
uptrend mid-2026). Mix of:

- Core ETF exposure (SPY/QQQ) so the account tracks the market even when
  individual picks lag.
- Momentum large caps riding current themes (AI/semis, banks post-earnings).
- Small speculative sleeve (max ~10% of equity) for high-beta or crypto.

## Risk rules

- Max position size: 15% of equity at entry (~$9k at start).
- Speculative sleeve positions: max 5% of equity each.
- Every stock entry gets a bracket order: stop loss ~5-8% below entry,
  take profit ~12-20% above (or trailing for runners). No naked positions.
- Max portfolio heat (sum of open risk to stops): 40% of equity.
- Keep at least 20% of equity in cash for opportunities/dips.
- No more than 3 new positions per day. No revenge trading after a stopped loss.
- Review every position at least once per market day via cron check.

## Process

1. Pre-market: read news/research, update watchlist.
2. Market hours: check positions 2-3x, adjust stops, take profits per plan.
3. Log every trade with thesis in logs/trades.log. Weekly review of P/L vs SPY.

## Current market context (2026-07-16)

- Filled from research briefing (see logs/research-2026-07-16.md).
