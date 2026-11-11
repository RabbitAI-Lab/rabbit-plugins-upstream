---
name: grid-health
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns grid bot health: fill rate, inventory, and level status across pairs."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/grid-health
    emoji: "🔲"
---
# grid-health

## What It Does
Grid bot health: fill rate, inventory, and level status across pairs. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- To monitor grid bot performance
- Before adjusting grid parameters
- When diagnosing poor fill rates

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/grid-health
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/grid-health",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "fill_rate_pct": 84,
  "inventory_pct": 61,
  "active_pairs": 4,
  "status": "healthy"
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [grid-health-score](https://apexrunner.ai/signals/grid-health-score)
- [grid-levels](https://apexrunner.ai/signals/grid-levels)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
