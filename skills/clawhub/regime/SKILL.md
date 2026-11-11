---
name: regime
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns full market regime classification: TRENDING, RANGING, CHOPPY, or CRISIS."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/regime
    emoji: "🗺️"
---
# regime

## What It Does
Full market regime classification: TRENDING, RANGING, CHOPPY, or CRISIS. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- Before selecting a trading strategy
- To route decisions through regime-appropriate logic
- As the primary market context signal

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/regime
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/regime",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "regime": "RANGING",
  "confidence": 0.82,
  "coin": "BTC",
  "timestamp": "2026-06-23T14:00:00Z"
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [regime-micro](https://apexrunner.ai/signals/regime-micro)
- [regime-confluence](https://apexrunner.ai/signals/regime-confluence)
- [regime-transition](https://apexrunner.ai/signals/regime-transition)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
