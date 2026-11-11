## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns multi-timeframe regime agreement score for higher-confidence entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading agents use this paid live signal to check agreement across multiple market timeframes before evaluating a crypto trade. The returned regime score can help assess alignment but should be considered alongside other analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each request incurs a USDC charge, and pricing may change after the stated early-adopter period.

Mitigation: Check the current endpoint price and wallet balance before making requests; account for the charge on every call.

Risk: The request uses an EVM private key to authorize payment.

Mitigation: Keep EVM_PRIVATE_KEY in a secure environment or secret manager and do not expose it in prompts, logs, or generated output.

Risk: A live regime agreement score may be mistaken for a reliable trade outcome prediction.

Mitigation: Treat the score as one input, review other evidence, and make trading decisions using appropriate independent checks.

## Reference(s):

- [Regime Confluence endpoint](https://apexrunner.ai/signals/regime-confluence)
- [Related regime signal](https://apexrunner.ai/signals/regime)
- [Related regime transition signal](https://apexrunner.ai/signals/regime-transition)

## Skill Output:

**Output Type(s):** [JSON, Guidance, Code]

**Output Format:** [JSON signal response with a confluence score, aligned timeframe count, and dominant regime; Markdown guidance with a Python example.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The signal is retrieved through a paid x402 call at $0.007 USDC per request through 2027-01-01; it requires an EVM wallet key and USDC on Base.]

## Skill Version(s):

1.0.1 (source: server-resolved Clawhub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
