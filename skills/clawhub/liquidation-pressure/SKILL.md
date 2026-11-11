---
name: liquidation-pressure
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns aggregate liquidation pressure score across tracked perpetuals."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/liquidation-pressure
    emoji: "💥"
---
# liquidation-pressure

## What It Does
Aggregate liquidation pressure score across tracked perpetuals. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- To monitor systemic perp risk
- Before entering leveraged positions
- As a market-stress overlay

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/liquidation-pressure
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/liquidation-pressure",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "pressure_score": 0.48,
  "at_risk_usd": 120000000,
  "level": "moderate"
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [liquidation-magnet](https://apexrunner.ai/signals/liquidation-magnet)
- [crowded-trade-detector](https://apexrunner.ai/signals/crowded-trade-detector)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
