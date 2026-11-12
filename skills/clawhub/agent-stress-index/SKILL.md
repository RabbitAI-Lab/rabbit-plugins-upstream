---
name: agent-stress-index
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns composite stress index measuring systemic risk across all APEX modules."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/agent-stress-index
    emoji: "🔥"
---
# agent-stress-index

> **Tier 3 — Strategic Edge**: This signal provides proprietary institutional-grade intelligence computed from APEX's live trading system. Pricing reflects the depth of analysis and the scarcity of the underlying edge.

## What It Does
Composite stress index measuring systemic risk across all APEX modules. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- To monitor systemic risk across APEX modules
- As a circuit-breaker signal
- When stress is rising and exposure should reduce

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/agent-stress-index
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/agent-stress-index",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "stress_score": 44,
  "stress_level": "MODERATE",
  "stress_trend": "RISING",
  "anomalies_detected": [
    {
      "pattern": "APEX-STRESS-002",
      "severity": "LOW",
      "signal": "Unusual query pattern detected"
    }
  ],
  "agents_monitored": 3,
  "timestamp": "2026-06-23T14:00:00Z"
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [crowded-trade-detector](https://apexrunner.ai/signals/crowded-trade-detector)
- [portfolio-heat](https://apexrunner.ai/signals/portfolio-heat)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
