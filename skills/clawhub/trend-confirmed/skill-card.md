## Description:

Returns whether the current trend has sufficient momentum to trade.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and traders can request a real-time momentum confirmation before considering a trend-following entry or filtering a possible breakout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A positive momentum signal could be mistaken for a guarantee or a complete trading recommendation.

Mitigation: Use the signal as one input, and independently assess market conditions and trading risk before placing an order.

Risk: Each request incurs a USDC charge, and the client requires access to an EVM wallet private key.

Mitigation: Set wallet spending controls and keep the private key in protected secret storage; fund the wallet only for intended calls.

## Reference(s):

- [Trend Confirmed signal endpoint](https://apexrunner.ai/signals/trend-confirmed)
- [Regime signal](https://apexrunner.ai/signals/regime)
- [APEX composite signal](https://apexrunner.ai/signals/apex-composite)

## Skill Output:

**Output Type(s):** [API Calls, JSON data]

**Output Format:** [JSON response with confirmation, direction, and strength fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Real-time signal; calls are paid in USDC on Base through x402.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
