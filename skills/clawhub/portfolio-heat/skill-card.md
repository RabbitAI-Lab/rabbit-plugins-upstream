## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns current portfolio heat level: normal, elevated, or emergency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Agents managing portfolio risk can check the portfolio heat signal before adding positions, enforcing risk limits, or reducing exposure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calls use an EVM private key and can spend USDC on Base for each request.

Mitigation: Protect the key in the environment, use a dedicated wallet with only the intended USDC balance, and check the current charge before calling.

## Reference(s):

- [APEX Runner portfolio-heat endpoint](https://apexrunner.ai/signals/portfolio-heat)
- [ClawHub skill page](https://clawhub.ai/kynto2001-ctrl/skills/portfolio-heat)
- [APEX Runner agent-stress-index signal](https://apexrunner.ai/signals/agent-stress-index)
- [APEX Runner risk-assessment-bundle signal](https://apexrunner.ai/signals/risk-assessment-bundle)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [JSON response with heat_level, heat_score, and action fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A current portfolio heat signal intended to inform risk decisions.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
