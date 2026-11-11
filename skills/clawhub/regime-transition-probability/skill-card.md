## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns probabilistic regime transition forecast with timing estimate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading agents use the endpoint to obtain a probabilistic estimate of regime transition risk and timing for strategy allocation and regime-aware hedging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan did not assess the destinations of the three external links.

Mitigation: Review the linked endpoint destinations before use.

Risk: Requests incur USDC charges and require an EVM private key; the documentation lists a $0.007 early-adopter price and a $0.01 standard price.

Mitigation: Confirm the current endpoint price before calling it, store the private key in a managed secret store, and use a wallet funded only for intended calls.

## Reference(s):

- [Regime Transition Probability endpoint](https://apexrunner.ai/signals/regime-transition-probability)
- [Related signal: Regime Transition](https://apexrunner.ai/signals/regime-transition)
- [Related signal: Regime Confluence](https://apexrunner.ai/signals/regime-confluence)
- [ClawHub release page](https://clawhub.ai/kynto2001-ctrl/skills/regime-transition-probability)

## Skill Output:

**Output Type(s):** [API Calls, Analysis]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the current regime, transition probability, most likely next regime, and estimated transition timing in hours.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
