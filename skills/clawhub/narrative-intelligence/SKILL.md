---
name: narrative-intelligence
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns AI-synthesised market narrative with directional bias score."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/narrative-intelligence
    emoji: "📰"
---
# narrative-intelligence

> **Tier 3 — Strategic Edge**: This signal provides proprietary institutional-grade intelligence computed from APEX's live trading system. Pricing reflects the depth of analysis and the scarcity of the underlying edge.

## What It Does
AI-synthesised market narrative with directional bias score. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- To understand AI agent market consensus
- For macro context before directional bets
- When narrative momentum matters

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/narrative-intelligence
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/narrative-intelligence",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "primary_narrative": "Institutional accumulation amid retail fear",
  "narrative_sentiment": "BULLISH",
  "narrative_age_days": 7,
  "saturation_level": "DEVELOPING",
  "alpha_window": "OPEN",
  "confidence": "MEDIUM",
  "timestamp": "2026-06-23T14:00:00Z"
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [whale-sentiment](https://apexrunner.ai/signals/whale-sentiment)
- [regime](https://apexrunner.ai/signals/regime)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
