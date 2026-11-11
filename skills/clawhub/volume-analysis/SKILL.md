---
name: volume-analysis
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns volume profile analysis detecting accumulation or distribution patterns."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/volume-analysis
    emoji: "📉"
---
# volume-analysis

## What It Does
Volume profile analysis detecting accumulation or distribution patterns. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- To confirm breakouts with volume
- To detect accumulation/distribution
- Before momentum entries

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/volume-analysis
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/volume-analysis",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "signal": "accumulation",
  "volume_ratio": 1.34,
  "above_average": true
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [trend-confirmed](https://apexrunner.ai/signals/trend-confirmed)
- [bb-analysis](https://apexrunner.ai/signals/bb-analysis)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
