---
name: liquidation-magnet
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns identifies price levels with dense liquidation clusters."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/liquidation-magnet
    emoji: "🧲"
---
# liquidation-magnet

## What It Does
Identifies price levels with dense liquidation clusters. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- To identify high-risk price zones
- Before setting stop losses
- When sizing positions near dense liquidation clusters

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/liquidation-magnet
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/liquidation-magnet",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "magnet_levels": [67000, 65500],
  "risk": "moderate",
  "distance_pct": 2.2
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [liquidation-pressure](https://apexrunner.ai/signals/liquidation-pressure)
- [crowded-trade-detector](https://apexrunner.ai/signals/crowded-trade-detector)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
