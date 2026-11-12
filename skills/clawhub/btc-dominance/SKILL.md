---
name: btc-dominance
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns BTC dominance percentage with trend direction signal."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/btc-dominance
    emoji: "👑"
---
# btc-dominance

## What It Does
BTC dominance percentage with trend direction signal. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- When deciding BTC vs altcoin allocation
- To detect altcoin season onset
- As context for capital rotation signals

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/btc-dominance
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/btc-dominance",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "dominance_pct": 54.3,
  "trend": "rising",
  "altcoin_season": false
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [altcoin-season](https://apexrunner.ai/signals/altcoin-season)
- [capital-rotation-signal](https://apexrunner.ai/signals/capital-rotation-signal)
- [regime](https://apexrunner.ai/signals/regime)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
