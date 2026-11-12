---
name: altcoin-season
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns altcoin season index — measures capital rotation from BTC to alts."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/altcoin-season
    emoji: "🌀"
---
# altcoin-season

## What It Does
Altcoin season index — measures capital rotation from BTC to alts. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- When sizing altcoin vs BTC positions
- To time rotation trades
- As context alongside btc-dominance

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/altcoin-season
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/altcoin-season",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "index": 38,
  "label": "Bitcoin Season",
  "threshold": 75
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [btc-dominance](https://apexrunner.ai/signals/btc-dominance)
- [capital-rotation-signal](https://apexrunner.ai/signals/capital-rotation-signal)
- [regime](https://apexrunner.ai/signals/regime)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
