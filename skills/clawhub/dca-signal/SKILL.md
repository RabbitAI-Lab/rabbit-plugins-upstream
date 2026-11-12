---
name: dca-signal
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns DCA entry signal with gate status, regime, and F&G conditions."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/dca-signal
    emoji: "💧"
---
# dca-signal

## What It Does
DCA entry signal with gate status, regime, and F&G conditions. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- At the start of each DCA decision cycle
- To verify all gate conditions are met
- Before placing DCA orders

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/dca-signal
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/dca-signal",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "signal": "hold",
  "gate_open": false,
  "fg": 42,
  "rsi": 51,
  "reason": "F&G not in fear territory"
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [fear-greed](https://apexrunner.ai/signals/fear-greed)
- [portfolio-heat](https://apexrunner.ai/signals/portfolio-heat)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
