---
name: optimal-order-routing
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns recommends best exchange and order type for minimum cost execution."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/optimal-order-routing
    emoji: "🔧"
---
# optimal-order-routing

## What It Does
Recommends best exchange and order type for minimum cost execution. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- To choose between Kraken, Coinbase, and Hyperliquid
- Before any order exceeding $100
- When minimising execution cost matters

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/optimal-order-routing
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/optimal-order-routing",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "order": {"coin": "BTC", "size_usd": 500, "side": "buy"},
  "recommendation": {
    "exchange": "Kraken",
    "order_type": "limit",
    "estimated_total_cost_pct": 0.18
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
- [slippage-forecast](https://apexrunner.ai/signals/slippage-forecast)
- [execution-window-optimizer](https://apexrunner.ai/signals/execution-window-optimizer)
- [arb-spread](https://apexrunner.ai/signals/arb-spread)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
