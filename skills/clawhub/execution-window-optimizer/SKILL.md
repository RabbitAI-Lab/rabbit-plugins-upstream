---
name: execution-window-optimizer
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns identifies optimal execution windows based on volatility and liquidity."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/execution-window-optimizer
    emoji: "⏱️"
---
# execution-window-optimizer

## What It Does
Identifies optimal execution windows based on volatility and liquidity. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- To time order placement for lowest impact
- During high-volatility periods
- When latency-sensitive execution is required

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/execution-window-optimizer
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/execution-window-optimizer",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "current_window_rating": "GOOD",
  "execute_now_recommendation": true,
  "best_windows": [
    {"utc_hours": "02:00-04:00", "avg_quality_score": 92}
  ],
  "timestamp": "2026-06-23T14:00:00Z"
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [slippage-forecast](https://apexrunner.ai/signals/slippage-forecast)
- [optimal-order-routing](https://apexrunner.ai/signals/optimal-order-routing)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
