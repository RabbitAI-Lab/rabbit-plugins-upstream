---
name: capital-rotation-signal
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns detects capital rotation between BTC, ETH, alts, and stables."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/capital-rotation-signal
    emoji: "🔁"
---
# capital-rotation-signal

> **Tier 3 — Strategic Edge**: This signal provides proprietary institutional-grade intelligence computed from APEX's live trading system. Pricing reflects the depth of analysis and the scarcity of the underlying edge.

## What It Does
Detects capital rotation between BTC, ETH, alts, and stables. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- To time rotation between BTC, ETH, and alts
- When sector allocation matters
- To front-run capital flow shifts

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/capital-rotation-signal
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/capital-rotation-signal",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "rotation_state": "ALT_SEASON_EARLY",
  "conviction": "MEDIUM",
  "from_asset": "BTC",
  "to_assets": ["ETH", "SOL"],
  "recommended_allocation": {
    "BTC": "REDUCE",
    "ETH": "ACCUMULATE"
  },
  "rotation_phase": "EARLY",
  "timestamp": "2026-06-23T14:00:00Z"
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [btc-dominance](https://apexrunner.ai/signals/btc-dominance)
- [altcoin-season](https://apexrunner.ai/signals/altcoin-season)
- [regime-transition](https://apexrunner.ai/signals/regime-transition)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
