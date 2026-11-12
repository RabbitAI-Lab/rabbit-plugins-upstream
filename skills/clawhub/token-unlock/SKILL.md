---
name: token-unlock
description: "Paid x402 endpoint: $0.007 USDC per call on Base. Returns upcoming token unlock events that may create sell pressure."
metadata:
  openclaw:
    requires:
      env:
        - EVM_PRIVATE_KEY
    primaryEnv: EVM_PRIVATE_KEY
    homepage: https://apexrunner.ai/signals/token-unlock
    emoji: "🔓"
---
# token-unlock

## What It Does
Upcoming token unlock events that may create sell pressure. This signal is computed in real time from APEX Runner's live autonomous trading system operating across Kraken, Coinbase Advanced Trade, and Hyperliquid — not from backtests or third-party aggregators.

## When to Use
- To avoid buying into upcoming sell pressure
- For fundamental risk filtering
- As a macro risk overlay

## How to Use
The agent makes an x402-authenticated GET request to:

```
https://apexrunner.ai/signals/token-unlock
```

The x402 client handles payment authorisation automatically. No API key, no account, no subscription required — just an EVM wallet with USDC on Base mainnet.

```python
# Example using the x402-python client
from x402.client import x402_get

response = x402_get(
    url="https://apexrunner.ai/signals/token-unlock",
    private_key=os.environ["EVM_PRIVATE_KEY"]
)
print(response.json())
```

## Example Response
```json
{
  "upcoming_unlocks": [{"token": "ARB", "date": "2026-07-01", "usd_value": 42000000}]
}
```

## Pricing
**$0.01/call** — standard price

Every caller is charged $0.007/call until 2027-01-01 under the
early-adopter discount (30% off the standard price). No tier, no wallet
history, no enrolment — that is simply the price.

## Related Signals
- [narrative-intelligence](https://apexrunner.ai/signals/narrative-intelligence)
- [regime](https://apexrunner.ai/signals/regime)

---
*APEX Runner — autonomous AI crypto trading signals. [apexrunner.ai](https://apexrunner.ai)*
