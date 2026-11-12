---
name: fg-micro
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns lightweight Fear & Greed index snapshot for high-frequency polling."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/fg-micro
    emoji: "📊"
---
# fg-micro

## What It Does
Lightweight Fear & Greed index snapshot for high-frequency polling. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- In fast loops where full F&G overhead is too costly
- To gate trade decisions on market sentiment
- Before calling more expensive intelligence signals

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/fg-micro
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/fg-micro",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "v": 42,
  "l": "Fear",
  "t": 1750000000
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [fear-greed](https://apexrunner.ai/signals/fear-greed)
- [regime-micro](https://apexrunner.ai/signals/regime-micro)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
