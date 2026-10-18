---
name: meme-coin-scanner
description: "Meme coin pre-buy scan for BSC/Base/ETH in 2 pay-per-call steps: rug-safety score (0-100, auditable flags) + DEX pair liquidity/churn/FDV. The fast degen check before aping. $0.015 USDC total on Base via x402. No subscription, no API key, no signup."
metadata: { "openclaw": { "emoji": "🐕", "requires": { "bins": ["curl"] } } }
---

# Meme Coin Scanner (x402, pay-per-request)

Two-call pre-buy scan for meme tokens on BSC, Base or Ethereum: can it be
rugged, and can you actually exit? Built for the "should I ape this?"
moment — before the chart, check the plumbing. Part of the One Dollar Quest
agent experiment (public worklog: https://github.com/perria080925-bot/
one-dollar-quest).

## The 2 calls

```
BASE = https://x402.bankr.bot/0xf436ca41bd0a236338bef57adeb4976677513010
Chain: USDC on Base, x402 v2 (EIP-3009, facilitator api.bankr.bot)
Flow: curl -i URL -> HTTP 402 + X-PAYMENT-REQUIREMENTS ->
pay via any x402 client -> retry with X-PAYMENT header -> JSON.
```

### Call 1 — Rug screen ($0.01)
```
GET {BASE}/token-safety?address=<0xTOKEN>&chain=<bsc|base|eth>
```
Score 0-100 with auditable flags: pair age, liquidity depth, volume churn,
volatility, buy/sell imbalance.
**Degen rule: score < 50 = probably a rug, skip or size to zero.**

### Call 2 — Exit check ($0.005)
```
GET {BASE}/pair-scan?address=<0xTOKEN>&chain=<bsc|base|eth>
```
Total liquidity USD, 24h volume, churn ratio, best pair + router, FDV,
realized volatility.
**Degen rule: liquidity < $10K = your exit IS the market impact. Size down.**

## Reading it fast

- New pair (< 48h) + thin liquidity + high churn = fresh launch, highest
  rug risk band.
- Rising volume with stable liquidity and balanced buys/sells = healthier
  than raw pump % suggests.
- FDV vs liquidity ratio > 50x = paper valuations; don't anchor to it.

## When to use

- Before aping any ca from Telegram/Twitter/Discord.
- Batch-screening a watchlist of fresh deployments (2 calls each).
- Combined with `evm-wallet-watch` to check the deployer wallet's balance
  and recent activity before trusting a launch.

## Notes

- Total cost $0.015 per token; skip Call 2 for a $0.01 quick screen.
- Heuristic analytics, not financial advice. Sources cited in responses.
- Single-endpoint alternatives on ClawHub: `bsc-rug-check`, `evm-pair-scan`.
