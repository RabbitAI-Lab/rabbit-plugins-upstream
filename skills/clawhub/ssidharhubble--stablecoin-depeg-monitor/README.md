# Stablecoin Depeg Monitor

Real-time peg monitoring for major stablecoins (USDT, USDC, DAI, FRAX, TUSD, BUSD, USDP, GUSD). Tracks price across CEXs (Binance, Coinbase, Kraken) and DEXes (Curve 3pool, Uniswap V3) and surfaces deviations from the $1.00 peg.

## What it does

- Checks the current mid-price of every major stable and computes deviation in basis points
- Classifies the state as `PEGGED`, `WOBBLE`, or `DEPEG` based on a configurable threshold
- Streams live updates in watch mode
- Generates a 30-day historical stability summary per stable (samples, max premium/discount, depeg event count, stability score)
- Finds cross-venue arbitrage windows when a stable diverges between venues

## Why it matters

The March 2023 USDC depeg wiped billions of liquidity across DeFi in hours. Peg monitoring is a primitive for treasury teams, market makers, and risk managers. Pegging this to a single Python skill with no dependencies means it runs anywhere — CI, an Airflow box, or a notebook.

## Install

```bash
# Zero deps. Drop into any Python 3.9+ environment.
python3 scripts/depeg_monitor.py check
```

## Configuration

Environment variables:
- `STABLECOIN_THRESHOLD_BPS` (default 50) — alert threshold in basis points
- `STABLECOIN_POLL_INTERVAL` (default 60) — watch-mode poll interval in seconds

## Notes

The bundled script ships with a deterministic mock data source so it runs offline and in tests. In production, replace `fetch_mock_venue_prices` with calls to Curve's subgraph, Binance public REST, Coinbase public REST, and the Uniswap V3 quoter. The schema and CLI do not change.
