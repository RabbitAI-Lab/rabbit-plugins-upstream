## Description:

Returns real-time momentum, whale sentiment, and regime confluence signals through a paid x402 endpoint costing $0.007 USDC per call on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve combined momentum, whale sentiment, and market-regime signals in one paid API call before making multi-factor trading decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation conditions may trigger unintended calls to a paid endpoint.

Mitigation: Limit activation to relevant user requests and check the current per-call price before invoking the endpoint.

## Reference(s):

- [Trading Intelligence Bundle endpoint](https://apexrunner.ai/signals/trading-intelligence-bundle)
- [ClawHub skill release](https://clawhub.ai/kynto2001-ctrl/skills/trading-intelligence-bundle)
- [Market Pulse Bundle](https://apexrunner.ai/signals/market-pulse-bundle)
- [Risk Assessment Bundle](https://apexrunner.ai/signals/risk-assessment-bundle)
- [APEX Composite](https://apexrunner.ai/signals/apex-composite)

## Skill Output:

**Output Type(s):** [Market signal data, JSON data]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Combined momentum, whale sentiment, and regime confluence signals in one endpoint response.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
