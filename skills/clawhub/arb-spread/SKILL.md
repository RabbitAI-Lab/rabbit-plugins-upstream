---
name: arb-spread
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns current arbitrage spread between Kraken and Hyperliquid."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/arb-spread
    emoji: "💱"
---
# arb-spread

## What It Does
Current arbitrage spread between Kraken and Hyperliquid. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- To detect Kraken vs Hyperliquid spread opportunities
- Before cross-exchange arb execution
- To size arb legs appropriately

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/arb-spread
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/arb-spread",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "spread_pct": 0.42,
  "threshold_pct": 0.35,
  "arb_viable": true
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [funding-rate](https://apexrunner.ai/signals/funding-rate)
- [optimal-order-routing](https://apexrunner.ai/signals/optimal-order-routing)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
