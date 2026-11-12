## Description:

Paid x402 access to a Base endpoint that returns an aggregated signal quality score across all active APEX modules for $0.007 USDC per call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents can query an aggregated quality score across APEX signals to help calibrate confidence before acting on those signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may rely on an aggregated trading signal when deciding whether to commit capital.

Mitigation: Treat the score as one input, verify current conditions, and apply independent risk controls before trading.

Risk: The skill requires an EVM wallet private key to authorize paid requests.

Mitigation: Store EVM_PRIVATE_KEY in a secure secret store and avoid exposing it in prompts, logs, or shared files.

## Reference(s):

- [Signal Intelligence endpoint](https://apexrunner.ai/signals/signal-intelligence)
- [APEX Composite signal](https://apexrunner.ai/signals/apex-composite)
- [Combined Alpha signal](https://apexrunner.ai/signals/combined-alpha)
- [APEX Alpha Score signal](https://apexrunner.ai/signals/apex-alpha-score)
- [ClawHub release page](https://clawhub.ai/kynto2001-ctrl/skills/signal-intelligence)

## Skill Output:

**Output Type(s):** [API Calls, JSON]

**Output Format:** [JSON response with quality_score, signals_active, and confidence fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A call costs $0.007 USDC on Base; it requires an EVM wallet with USDC and EVM_PRIVATE_KEY.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
