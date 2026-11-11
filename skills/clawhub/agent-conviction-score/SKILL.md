---
name: agent-conviction-score
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns measures conviction strength of current APEX trade signals."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/agent-conviction-score
    emoji: "🎯"
---
# agent-conviction-score

> **Tier 3 — Strategic Edge**: This signal provides proprietary institutional-grade intelligence computed from APEX's live trading system. Pricing reflects the depth of analysis and the scarcity of the underlying edge.

## What It Does
Measures conviction strength of current APEX trade signals. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- To measure signal strength before trading
- As a confidence multiplier for position sizing
- When comparing multiple trade setups

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/agent-conviction-score
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/agent-conviction-score",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "conviction": 0.81,
  "signals_aligned": 7,
  "direction": "long",
  "confidence": "high"
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [apex-alpha-score](https://apexrunner.ai/signals/apex-alpha-score)
- [signal-intelligence](https://apexrunner.ai/signals/signal-intelligence)
- [crowded-trade-detector](https://apexrunner.ai/signals/crowded-trade-detector)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
