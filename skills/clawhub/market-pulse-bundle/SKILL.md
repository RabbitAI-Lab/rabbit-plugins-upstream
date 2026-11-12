---
name: market-pulse-bundle
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns price tick + Fear & Greed + regime in one call."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/market-pulse-bundle
    emoji: "📦"
---
# market-pulse-bundle

## What It Does
Bundle: price tick + Fear & Greed + regime in one call. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- When a quick market snapshot is needed
- At the start of an agent decision loop
- To reduce latency with a single bundled call

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/market-pulse-bundle
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/market-pulse-bundle",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "btc_price_tick": {"b": 67482.50, "e": 3541.20, "s": 152.30, "a": 24.10, "t": 1750000000},
  "fear_greed": {"value": 42, "classification": "Fear", "zone": "FEAR", "source": "cmc"},
  "regime": {"regime": "RANGING", "confidence": 0.82, "coin": "BTC"},
  "timestamp": "2026-06-23T14:00:00Z"
  // Full nested output of all component signals returned in one call
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [trading-intelligence-bundle](https://apexrunner.ai/signals/trading-intelligence-bundle)
- [regime](https://apexrunner.ai/signals/regime)
- [fear-greed](https://apexrunner.ai/signals/fear-greed)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
