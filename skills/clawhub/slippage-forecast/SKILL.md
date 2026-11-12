---
name: slippage-forecast
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns predicts expected slippage for a given order size and market condition."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/slippage-forecast
    emoji: "📐"
---
# slippage-forecast

## What It Does
Predicts expected slippage for a given order size and market condition. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- Before placing large orders
- To estimate realistic execution cost
- When comparing venues for best execution

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/slippage-forecast
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/slippage-forecast",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "slippage_forecast": {
    "BTC": {
      "kraken": {
        "small_order": {
          "size_range": "<$500",
          "avg_slip_pct": 0.02,
          "confidence": "HIGH"
        }
      }
    }
  },
  "timestamp": "2026-06-23T14:00:00Z"
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [optimal-order-routing](https://apexrunner.ai/signals/optimal-order-routing)
- [execution-window-optimizer](https://apexrunner.ai/signals/execution-window-optimizer)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
