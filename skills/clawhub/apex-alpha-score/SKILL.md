---
name: apex-alpha-score
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns APEX proprietary alpha score for current market opportunity quality."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/apex-alpha-score
    emoji: "⚡"
---
# apex-alpha-score

> **Tier 3 — Strategic Edge**: This signal provides proprietary institutional-grade intelligence computed from APEX's live trading system. Pricing reflects the depth of analysis and the scarcity of the underlying edge.

## What It Does
APEX proprietary alpha score for current market opportunity quality. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- To rank overall opportunity quality
- Before deploying significant capital
- As the primary entry gate for high-value trades

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/apex-alpha-score
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/apex-alpha-score",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "alpha_score": 0.71,
  "percentile": 82,
  "signal_count": 9,
  "confidence": "high"
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [combined-alpha](https://apexrunner.ai/signals/combined-alpha)
- [agent-conviction-score](https://apexrunner.ai/signals/agent-conviction-score)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
