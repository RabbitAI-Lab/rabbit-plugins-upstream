## Description:

Returns grid bot health metrics across pairs through a paid x402 endpoint ($0.007 USDC per call on Base).

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

External grid bot operators use the skill to monitor fill rates, inventory, and active pair status, then investigate poor fills or decide whether to adjust grid parameters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each endpoint request makes a paid USDC call; the documentation lists a current $0.007 price and a $0.01 standard price.

Mitigation: Confirm the current endpoint price and set a call budget before enabling repeated requests.

Risk: The x402 client uses EVM_PRIVATE_KEY for a wallet on Base.

Mitigation: Store the key in a secret manager, restrict it to a wallet funded only for intended calls, and avoid exposing it in logs or messages.

## Reference(s):

- [Grid Health endpoint](https://apexrunner.ai/signals/grid-health)
- [APEX Runner](https://apexrunner.ai)
- [Related signal: Grid Health Score](https://apexrunner.ai/signals/grid-health-score)
- [Related signal: Grid Levels](https://apexrunner.ai/signals/grid-levels)

## Skill Output:

**Output Type(s):** [Structured data (JSON)]

**Output Format:** [JSON response with fill rate, inventory, active pair count, and status fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live grid health values for the requested signal]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
