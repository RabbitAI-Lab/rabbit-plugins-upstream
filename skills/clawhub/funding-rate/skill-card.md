## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns funding rate analysis across perps with arb opportunity scoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents can request current perpetual futures funding rate analysis and arb opportunity scoring before opening positions or monitoring funding costs. Each request costs $0.007 USDC on Base and requires an EVM wallet private key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Funding rates and arb opportunity scores are trading signals and may not reflect conditions when a position is opened.

Mitigation: Check current exchange data and apply independent risk limits before trading.

Risk: Requests incur a USDC charge and use an EVM private key for wallet authorization.

Mitigation: Review the per-call price and keep the private key in a secure environment variable; use a wallet funded only for intended calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/kynto2001-ctrl/skills/funding-rate)
- [Funding Rate endpoint](https://apexrunner.ai/signals/funding-rate)
- [Related signal: funding-rate-hl](https://apexrunner.ai/signals/funding-rate-hl)
- [Related signal: arb-spread](https://apexrunner.ai/signals/arb-spread)
- [APEX Runner](https://apexrunner.ai)

## Skill Output:

**Output Type(s):** [Analysis, API Calls]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A response with funding rate, arb score, and recommended action fields.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
