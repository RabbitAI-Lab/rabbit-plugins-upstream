---
name: funding-rate
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns funding rate analysis across perps with arb opportunity scoring."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/funding-rate
    emoji: "💸"
---
# funding-rate

## What It Does
Funding rate analysis across perps with arb opportunity scoring. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- Before opening perp positions
- To identify funding arb opportunities
- To monitor ongoing funding costs

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/funding-rate
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/funding-rate",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "avg_rate_8h": 0.00031,
  "arb_score": 0.54,
  "recommended_action": "hold"
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [funding-rate-hl](https://apexrunner.ai/signals/funding-rate-hl)
- [arb-spread](https://apexrunner.ai/signals/arb-spread)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
