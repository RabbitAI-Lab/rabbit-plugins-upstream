---
name: grid-levels
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns active grid levels, spacing, and next buy/sell prices per pair."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/grid-levels
    emoji: "📏"
---
# grid-levels

## What It Does
Active grid levels, spacing, and next buy/sell prices per pair. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- To know exact grid buy/sell prices
- When managing grid inventory manually
- For reporting and dashboard integration

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/grid-levels
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/grid-levels",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "BTC": {"next_buy": 66800, "next_sell": 67600, "levels_active": 7},
  "ETH": {"next_buy": 3490, "next_sell": 3570, "levels_active": 6}
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [grid-health](https://apexrunner.ai/signals/grid-health)
- [grid-health-score](https://apexrunner.ai/signals/grid-health-score)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
