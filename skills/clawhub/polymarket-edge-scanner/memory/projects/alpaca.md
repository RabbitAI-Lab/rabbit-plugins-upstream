# Alpaca Paper Trading

## Accounts

| Account | Purpose | Equity | Cash | Positions | Unrealized P/L |
|---------|---------|--------|------|-----------|----------------|
| Main swing (`PA3BJ0TMYV0B`) | Long-biased swing, core ETFs + momentum | $59,383.54 | $13,663.91 | 5 | −$616.46 |
| Day trader (`f03a588d-8deb-4521-b5fb-c2619ea83727`) | NYSE day trades, flat by close | $4,971.87 | $3,543.08 | 2 | −$17.20 |

## Automation

| Script | Schedule | Purpose |
|--------|----------|---------|
| `alpaca_trading/bot.py` | Hourly 14:00–19:00 UTC, Mon–Fri | Main swing bot (core + momentum entries, bracket orders) |
| `alpaca_trading/daytrader.py` | Every 5 min 13:30–19:55 UTC, Mon–Fri | Day-trader bot (opening-range breakout / VWAP bounce, flat by close) |
| `scripts/alpaca-heartbeat.py` | Every 30 min | Snapshot both accounts, check risk rules, log alerts |

All trading scripts run under `flock` so overlapping invocations don't pile up.

## Risk rules

- Swing: max 15% equity per position, 20% minimum cash, bracket stops, review daily.
- Day trader: max 3 positions, $500–$1,000 per trade, ~30% cash buffer, flat by 15:55 ET.

## Current notes / alerts

- Swing account has two positions above the 15% rule **on a current-market-value basis**: SPY 21.3%, AAPL 15.3%. This is because they appreciated past the entry sizing limit; the strategy rule applies at entry.
- Swing positions missing visible stop-loss orders: AAPL, GOOGL, MSFT, QQQ. SPY has a GTC stop at $735.83.
- Day-trader positions (SPY, VOO) are small and have no visible stops; the day-trader bot normally attaches bracket stops on entry, but these positions may be carry-over.

## Files

- `/root/.openclaw/workspace/alpaca_trading/STRATEGY.md`
- `/root/.openclaw/workspace/alpaca_trading/DAYTRADE_STRATEGY.md`
- `/root/.openclaw/workspace/alpaca_trading/bot.py`
- `/root/.openclaw/workspace/alpaca_trading/daytrader.py`
- `/root/.openclaw/workspace/scripts/alpaca-heartbeat.py`
- `/root/.openclaw/workspace/logs/alpaca-heartbeat.log`
