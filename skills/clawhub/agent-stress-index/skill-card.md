## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns composite stress index measuring systemic risk across all APEX modules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use the signal to monitor systemic stress across APEX modules and as one input to circuit-breaker or exposure-reduction decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each call incurs a USDC charge through x402.

Mitigation: Set request limits and keep only the intended spending amount in the wallet used for calls.

Risk: The skill reads EVM_PRIVATE_KEY to authorize paid requests; exposure of the key could compromise the wallet.

Mitigation: Store the key in a protected secret store and use a dedicated wallet with limited funds.

Risk: The returned stress index may be incomplete or unsuitable as the sole basis for trading decisions.

Mitigation: Validate the signal against other risk controls before changing exposure.

## Reference(s):

- [Agent Stress Index endpoint](https://apexrunner.ai/signals/agent-stress-index)
- [ClawHub skill release](https://clawhub.ai/kynto2001-ctrl/skills/agent-stress-index)
- [Related signal: crowded-trade-detector](https://apexrunner.ai/signals/crowded-trade-detector)
- [Related signal: portfolio-heat](https://apexrunner.ai/signals/portfolio-heat)

## Skill Output:

**Output Type(s):** [Analysis, JSON]

**Output Format:** [JSON response with a stress score, level, trend, detected anomalies, monitored-agent count, and timestamp]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each request is paid in USDC on Base through x402.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
