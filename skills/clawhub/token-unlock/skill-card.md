## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns upcoming token unlock events that may create sell pressure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to retrieve upcoming token unlock events as a sell-pressure signal for crypto market risk screening.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The request requires an EVM private key and charges $0.007 USDC per call on Base.

Mitigation: Keep the key in a secure secret store and limit the wallet funds and calls available to the skill.

## Reference(s):

- [Token Unlock Signal](https://apexrunner.ai/signals/token-unlock)
- [Narrative Intelligence Signal](https://apexrunner.ai/signals/narrative-intelligence)
- [Regime Signal](https://apexrunner.ai/signals/regime)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [JSON response containing upcoming token unlock events]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event records can include token, date, and USD value.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
