## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns active grid levels, spacing, and next buy/sell prices per pair.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and operators use this skill to retrieve current grid levels, spacing, and buy/sell prices for trading pairs. This supports manual inventory management and reporting or dashboard integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each endpoint request incurs a USDC payment, and request volume can increase total charges.

Mitigation: Confirm the current price and monitor request volume before using the endpoint repeatedly.

Risk: The x402 client uses an EVM wallet private key to authorize payment.

Mitigation: Keep EVM_PRIVATE_KEY in a secure secret store and use a wallet funded only for the intended calls.

## Reference(s):

- [Grid Levels endpoint](https://apexrunner.ai/signals/grid-levels)
- [Grid Health signal](https://apexrunner.ai/signals/grid-health)
- [Grid Health Score signal](https://apexrunner.ai/signals/grid-health-score)
- [APEX Runner](https://apexrunner.ai)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [JSON response with per-pair active grid levels, spacing, and next buy/sell prices.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Values reflect live grid state and may change between calls.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
