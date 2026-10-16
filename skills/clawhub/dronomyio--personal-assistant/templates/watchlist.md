# Watchlist

Your personal watchlist. The brief engine reads the two sections below.
Replace the placeholder tickers with your own. One ticker per line, comma
separated. For holdings, add the share quantity in parentheses.

## US stocks

- TICKER1, TICKER2, TICKER3
- SECTOR_ETF1

## Indian stocks

- TICKER4 (100), TICKER5 (25)
- TICKER6

Notes:
- Lines starting with `_` are ignored (use for section comments).
- Indian tickers resolve `.NS` -> `.BO` -> raw automatically; broker-series
  suffixes (e.g. `FOO-BZ`) fall back to the base ticker.
- Quantities are optional; they weight significance in briefs and strategy.
