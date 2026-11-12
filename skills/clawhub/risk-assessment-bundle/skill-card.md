## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns portfolio heat + liquidation pressure + position exposure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents can retrieve a combined crypto risk snapshot before making large position changes, for periodic risk monitoring, or to populate risk dashboards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The x402 request uses an EVM wallet private key and incurs a USDC payment for each call.

Mitigation: Keep EVM_PRIVATE_KEY in a secret store and use a dedicated wallet funded only for intended endpoint payments.

Risk: The response contains live trading risk indicators and suggested actions that may not capture an agent's full circumstances.

Mitigation: Treat the response as one input to monitoring and review; check it against current positions and other relevant information before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kynto2001-ctrl/skills/risk-assessment-bundle)
- [APEX Runner risk assessment bundle endpoint](https://apexrunner.ai/signals/risk-assessment-bundle)
- [APEX Runner trading intelligence bundle](https://apexrunner.ai/signals/trading-intelligence-bundle)
- [APEX Runner portfolio heat](https://apexrunner.ai/signals/portfolio-heat)
- [APEX Runner agent stress index](https://apexrunner.ai/signals/agent-stress-index)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A single paid request returns portfolio heat, liquidation pressure, and position exposure as a live risk snapshot. The documented price is $0.007 USDC per call on Base through 2027-01-01.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
