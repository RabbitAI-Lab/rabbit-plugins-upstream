---
name: combined-alpha
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns combined alpha signal merging momentum, mean-reversion, and sentiment."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/combined-alpha
    emoji: "🎯"
---
# combined-alpha

## What It Does
Combined alpha signal merging momentum, mean-reversion, and sentiment. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- To combine momentum and mean-reversion views
- Before high-stakes entries
- As a tie-breaker between competing signals

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/combined-alpha
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/combined-alpha",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "alpha_score": 0.63,
  "momentum_component": 0.58,
  "mean_reversion_component": 0.41
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [apex-composite](https://apexrunner.ai/signals/apex-composite)
- [signal-intelligence](https://apexrunner.ai/signals/signal-intelligence)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
