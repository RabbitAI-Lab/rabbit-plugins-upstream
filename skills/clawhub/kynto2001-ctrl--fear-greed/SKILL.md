---
name: fear-greed
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns composite Fear & Greed index with source and staleness metadata."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/fear-greed
    emoji: "😱"
---
# fear-greed

## What It Does
Composite Fear & Greed index with source and staleness metadata. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- Before entering DCA positions
- To calibrate position sizing
- When evaluating overall market risk appetite

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/fear-greed
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/fear-greed",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "value": 42,
  "classification": "Fear",
  "zone": "FEAR",
  "source": "cmc",
  "timestamp": "2026-06-23T14:00:00Z"
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [fg-micro](https://apexrunner.ai/signals/fg-micro)
- [dca-signal](https://apexrunner.ai/signals/dca-signal)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
