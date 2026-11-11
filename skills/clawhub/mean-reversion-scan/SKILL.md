---
name: mean-reversion-scan
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns mean-reversion opportunity scan across RANGING and CHOPPY regimes."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/mean-reversion-scan
    emoji: "↩️"
---
# mean-reversion-scan

## What It Does
Mean-reversion opportunity scan across RANGING and CHOPPY regimes. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- To find oversold/overbought setups
- In RANGING or CHOPPY regimes only
- Before mean-reversion entries

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/mean-reversion-scan
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/mean-reversion-scan",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "opportunity": true,
  "coin": "SOL",
  "rsi": 28,
  "signal": "oversold"
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [bb-analysis](https://apexrunner.ai/signals/bb-analysis)
- [regime](https://apexrunner.ai/signals/regime)
- [liquidation-magnet](https://apexrunner.ai/signals/liquidation-magnet)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
