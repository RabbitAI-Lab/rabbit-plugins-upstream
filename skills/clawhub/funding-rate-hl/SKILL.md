---
name: funding-rate-hl
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns current Hyperliquid perpetual funding rates across tracked coins."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/funding-rate-hl
    emoji: "💰"
---
# funding-rate-hl

## What It Does
Current Hyperliquid perpetual funding rates across tracked coins. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- Before opening or holding Hyperliquid perp positions
- To identify funding arb opportunities
- To avoid paying excessive funding

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/funding-rate-hl
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/funding-rate-hl",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "BTC": 0.0003,
  "ETH": 0.00025,
  "SOL": 0.00041,
  "AVAX": 0.00018,
  "timestamp": "2026-06-23T14:00:00Z"
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [funding-rate](https://apexrunner.ai/signals/funding-rate)
- [arb-spread](https://apexrunner.ai/signals/arb-spread)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
