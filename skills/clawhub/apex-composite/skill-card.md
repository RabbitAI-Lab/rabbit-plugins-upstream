## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns composite APEX score combining regime, momentum, and risk metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Crypto market analysts and agents use the live composite APEX score to rank opportunity quality and inform trading decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broadly worded activation condition could trigger paid endpoint calls in unrelated situations.

Mitigation: Limit activation to explicit APEX score requests and set per-task call and spend limits.

Risk: Each request makes a paid call using a wallet private key supplied through EVM_PRIVATE_KEY.

Mitigation: Keep the key in secret storage, use a dedicated wallet with limited USDC, and review payment details before enabling calls.

## Reference(s):

- [APEX Composite signal endpoint](https://apexrunner.ai/signals/apex-composite)
- [APEX Runner](https://apexrunner.ai)
- [Combined Alpha signal](https://apexrunner.ai/signals/combined-alpha)
- [Signal Intelligence](https://apexrunner.ai/signals/signal-intelligence)
- [APEX Alpha Score](https://apexrunner.ai/signals/apex-alpha-score)
- [ClawHub skill page](https://clawhub.ai/kynto2001-ctrl/skills/apex-composite)

## Skill Output:

**Output Type(s):** [JSON data]

**Output Format:** [JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Composite score with momentum, regime fit, and risk values. Each call costs $0.007 USDC during the stated early-adopter period; requests use an EVM wallet on Base.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
