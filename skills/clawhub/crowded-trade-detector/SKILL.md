---
name: crowded-trade-detector
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns detects when too many agents are in the same trade — liquidation risk."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/crowded-trade-detector
    emoji: "⚠️"
---
# crowded-trade-detector

> **Tier 3 — Strategic Edge**: This signal provides proprietary institutional-grade intelligence computed from APEX's live trading system. Pricing reflects the depth of analysis and the scarcity of the underlying edge.

## What It Does
Detects when too many agents are in the same trade — liquidation risk. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- Before entering popular trades
- To avoid liquidation cascade exposure
- As a risk gate alongside agent-conviction-score

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/crowded-trade-detector
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/crowded-trade-detector",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "crowded_trades": [
    {
      "coin": "BTC",
      "direction": "LONG",
      "crowding_score": 84,
      "severity": "HIGHLY_CROWDED",
      "contrarian_signal": "SHORT",
      "contrarian_strength": "STRONG"
    }
  ],
  "market_consensus": "BULLISH_CROWDED",
  "timestamp": "2026-06-23T14:00:00Z"
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [agent-stress-index](https://apexrunner.ai/signals/agent-stress-index)
- [liquidation-pressure](https://apexrunner.ai/signals/liquidation-pressure)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
