## Description:

Provides a paid x402 API endpoint on Base that returns a live signal about likely crypto market regime transitions for $0.007 per call through 2026-12-31.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading agents use the endpoint to check for likely market regime transitions, inform strategy changes, and consider reducing exposure ahead of uncertainty.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests use an EVM private key and authorize a paid USDC call.

Mitigation: Keep EVM_PRIVATE_KEY in a secret store, use a dedicated wallet with only the funds intended for these calls, and review payment details before requesting the signal.

Risk: The security scan inspected the Markdown skill and found no issues, but some behavioral analyzers were not applicable.

Mitigation: Review the endpoint behavior and payment request before enabling it in an automated workflow.

## Reference(s):

- [Regime transition signal endpoint](https://apexrunner.ai/signals/regime-transition)
- [Regime signal](https://apexrunner.ai/signals/regime)
- [Regime confluence signal](https://apexrunner.ai/signals/regime-confluence)
- [Regime transition probability signal](https://apexrunner.ai/signals/regime-transition-probability)
- [APEX Runner](https://apexrunner.ai)
- [ClawHub release page](https://clawhub.ai/kynto2001-ctrl/skills/regime-transition)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance]

**Output Format:** [JSON signal response with transition_likely, probability, and target_regime fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One paid x402-authenticated request per signal; payment is $0.007 USDC per call through 2026-12-31.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
