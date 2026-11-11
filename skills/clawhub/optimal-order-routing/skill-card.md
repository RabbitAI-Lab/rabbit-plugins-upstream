## Description:

Uses a paid x402 endpoint to recommend an exchange and order type for lower-cost crypto execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and trading agents use this skill to compare Kraken, Coinbase Advanced Trade, and Hyperliquid and choose an exchange and order type before placing an order.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests use a wallet private key to authorize a paid USDC call on Base.

Mitigation: Keep the key in a secrets manager, use a wallet with a limited balance, and check the per-call price before use.

Risk: The returned execution-cost estimate may not match conditions when an order is placed.

Mitigation: Review the recommendation and verify current fees and market conditions before placing the order.

## Reference(s):

- [APEX Runner optimal-order-routing endpoint](https://apexrunner.ai/signals/optimal-order-routing)
- [ClawHub skill release](https://clawhub.ai/kynto2001-ctrl/skills/optimal-order-routing)
- [Related signal: slippage-forecast](https://apexrunner.ai/signals/slippage-forecast)
- [Related signal: execution-window-optimizer](https://apexrunner.ai/signals/execution-window-optimizer)
- [Related signal: arb-spread](https://apexrunner.ai/signals/arb-spread)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance]

**Output Format:** [JSON recommendation containing the exchange, order type, estimated total cost percentage, and timestamp]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One recommendation per request; calls are paid in USDC on Base.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
