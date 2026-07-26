# Alpaca Day Trader Strategy

Account: f03a588d-8deb-4521-b5fb-c2619ea83727 (paper). $5,000 cash / $20,000 buying power.
Goal: quick in-and-out NYSE day trades. Small wins, high frequency, flat by close.

## Scope

- **Exchanges:** NYSE-listed stocks and ETFs only.
- **Hold time:** minutes to a few hours. No overnight positions.
- **Direction:** long-only for simplicity (shorting adds complexity and borrow risk).

## Universe

Liquid NYSE names only:

- Index ETFs: SPY, DIA, IWM, QQQ (note: QQQ is Nasdaq-100 but listed on NYSE Arca — kept for liquidity)
- Sector ETFs: XLF, XLE, XLK, XLU, XLI, XLP, XBI, GLD, SLV, USO
- Large caps: JPM, BAC, WFC, XOM, CVX, WMT, HD, DIS, VZ, T, KO, PEP, MCD, UNH, JNJ, PFE, MRK, CAT, BA, GE, HON, MMM, IBM, ORCL, NKE, V, MA, GS, MS, C, AXP

## Risk rules

- Max positions open: 3.
- Position size: $500–$1,000 per trade (~10–20% of cash).
- Max loss per trade: ~$15–$30 (1.5–3x the spread, roughly 0.5–1.0% of position).
- Stop loss: placed immediately on entry, ~0.6–1.0% below entry for ETFs, ~0.8–1.5% below for single stocks.
- Take profit: ~1.5–2.5x the stop distance.
- Flat by 15:55 ET (19:55 UTC) if any positions remain.
- No averaging down. If stopped, move on.
- Minimum cash buffer: keep ~30% cash uncommitted.

## Signals

Opening-range breakout / pullback to VWAP:

1. **Opening range** = first 15 minutes of regular hours (9:30–9:45 ET / 13:30–13:45 UTC).
2. After the opening range:
   - If price breaks above the range high on increasing 1-minute volume, enter long.
   - If price pulls back to the VWAP of the opening range and bounces, enter long.
3. Only trade in the direction of the broader 15-minute trend (range breakout higher = long, lower = skip).

## Execution

- Use **limit orders** for entries where possible to avoid spread slippage.
- Attach bracket stop-loss / take-profit orders on entry.
- Cancel unfilled entry orders after 5 minutes if price moves away.
- **Friction guard:** skip entries where the quoted spread is >0.5% and assume 0.15% slippage when sizing and placing bracket stops.

## Monitoring

- Bot runs every 5 minutes during market hours.
- Logs to `logs/daytrader.log` and `logs/daytrader-trades.log`.
- Manual review is fine; automated flat-at-close is enforced.

## Notes

- Paper account: treat risk as real, but this is explicitly a learning/high-frequency test.
- PDT rule technically applies to sub-$25k accounts, but Alpaca paper may not enforce hard locks. Still keep day-trade count visible in logs.
