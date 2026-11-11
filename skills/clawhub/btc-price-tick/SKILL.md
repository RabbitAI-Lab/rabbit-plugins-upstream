---
name: btc-price-tick
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns real-time BTC price tick from live exchange feeds."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/btc-price-tick
    emoji: "💹"
---
# btc-price-tick

## What It Does
Real-time BTC price tick from live exchange feeds. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- When you need a low-latency BTC price reference
- Inside high-frequency polling loops
- As a baseline for spread or momentum calculations

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/btc-price-tick
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/btc-price-tick",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "b": 67482.50,
  "e": 3541.20,
  "s": 152.30,
  "a": 24.10,
  "t": 1750000000
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [market-tick](https://apexrunner.ai/signals/market-tick)
- [apex-pulse](https://apexrunner.ai/signals/apex-pulse)
- [btc-dominance](https://apexrunner.ai/signals/btc-dominance)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
