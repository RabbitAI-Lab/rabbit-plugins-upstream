---
name: bb-analysis
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns bollinger Band analysis with squeeze detection and breakout probability."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/bb-analysis
    emoji: "📉"
---
# bb-analysis

## What It Does
Bollinger Band analysis with squeeze detection and breakout probability. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- To detect Bollinger Band squeezes
- Before breakout or mean-reversion trades
- To gauge price extremity

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/bb-analysis
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/bb-analysis",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "squeeze": false,
  "position": "mid-band",
  "breakout_probability": 0.38
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [mean-reversion-scan](https://apexrunner.ai/signals/mean-reversion-scan)
- [volume-analysis](https://apexrunner.ai/signals/volume-analysis)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
