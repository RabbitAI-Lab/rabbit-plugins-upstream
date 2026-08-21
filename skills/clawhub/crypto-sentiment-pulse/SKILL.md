---
name: "crypto-sentiment-pulse"
description: "Crypto Fear & Greed index + market sentiment via the x402 pay-per-call API. Know the market mood before your agent takes a position. WARNING: PAID API call — each run costs money (x402, USDC) and sends your API key to the API."
metadata: {"clawbot": {"requires": {"python3": true, "network": ["https://186.240.156.169:8791"], "env": ["X402_API_KEY"]}}}
---

# Crypto Sentiment Pulse 💓🪙

Market sentiment for your agent: Fear & Greed index and sentiment data before entries.

## Usage

```bash
export X402_API_KEY=sk-...
python3 scripts/sentiment.py
```

Returns: Fear & Greed score (0-100) + label (Extreme Fear / Fear / Neutral / Greed / Extreme Greed).

## Payment
Pay-per-call via x402 (USDC on Base).

## How it helps
- Extreme Fear (0-25): historically good buy zones for longs
- Extreme Greed (75-100): correction risk — be careful with longs
- Combine with DRT signals for A+ setups
