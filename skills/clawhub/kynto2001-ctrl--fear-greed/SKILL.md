---
name: fear-greed
description: Composite Fear & Greed index with source and staleness metadata
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
**$0.05/call** — standard price

Early adopters automatically receive 30% off ($0.03/call) until 2026-09-21. Discount tiers apply automatically based on wallet call history:
- Early Adopter (0–9 calls): 30% off
- Engaged (10–49 calls): 15% off
- Loyal (50–199 calls): 15% permanent
- VIP (200+ calls): 20% permanent

Check your tier: `https://apexrunner.ai/signals/my-pricing`

## Related Signals
- [fg-micro](https://apexrunner.ai/signals/fg-micro)
- [dca-signal](https://apexrunner.ai/signals/dca-signal)
- [dca-reentry-gate](https://apexrunner.ai/signals/dca-reentry-gate)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
