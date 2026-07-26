---
name: stablecoin-depeg-monitor
description: Real-time stablecoin depeg detection and alerting for USDT, USDC, DAI, FRAX, and other major stablecoins. Monitors on-chain DEX prices (Curve, Uniswap) and CEX prices (Binance, Coinbase) for deviations from the $1.00 peg. Detects early signs of stablecoin stress, bank run risk, and arbitrage opportunities. Tracks peg recovery velocity, liquidity depth, and historical depeg events. Useful for DeFi risk management, treasury operations, and trading strategies. Built for crypto traders, DeFi protocols, and risk managers who need to know the instant a stablecoin wobbles.
compatibility: Created for Zo Computer
metadata:
  author: ssyopros.zo.computer
allowed-tools: Bash
---

# Stablecoin Depeg Monitor

Monitor stablecoin pegs in real time. Detect deviations from $1.00 across major DEX and CEX venues, get alerts on depeg events, and analyze historical stability for risk decisions.

## When to use

- User asks "is USDT depegged" or "monitor stablecoin prices"
- Building a DeFi treasury or risk dashboard
- Watching for stablecoin stress events (USDC March 2023 style)
- Hunting arbitrage between depegged stables and the peg
- Tracking historical peg stability for due diligence

## Commands

```bash
python3 scripts/depeg_monitor.py check          # Check all major stables vs $1
python3 scripts/depeg_monitor.py check USDT     # Check specific stable
python3 scripts/depeg_monitor.py watch          # Stream live updates (60s polling)
python3 scripts/depeg_monitor.py history USDC   # Historical stability record
python3 scripts/depeg_monitor.py arb            # Find active arbitrage opportunities
```

## Output

Returns JSON with: stable, mid_price, deviation_bps, venues (per-exchange price), liquidity (USD depth at ±1% band), status (PEGGED, WOBBLE, DEPEG), and timestamp.

## Environment

- `STABLECOIN_THRESHOLD_BPS` - Alert threshold in basis points (default: 50 = 0.5%)
- `STABLECOIN_POLL_INTERVAL` - Watch mode seconds (default: 60)
- Works offline with mock data; production connects to Curve subgraph, Binance, Coinbase public APIs
