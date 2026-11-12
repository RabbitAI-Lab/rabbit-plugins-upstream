## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns AI-synthesised market narrative with directional bias score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use the paid signal to review an AI-synthesised market narrative, directional sentiment, and narrative timing before making trading decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calls incur USDC charges on Base, and the documented early-adopter price may change after 2026-12-31.

Mitigation: Check the current price and endpoint before calling, and cap the number of paid requests.

Risk: The skill uses an EVM wallet private key to authorize payment.

Mitigation: Keep EVM_PRIVATE_KEY in a secrets manager and use a dedicated wallet with limited funds.

## Reference(s):

- [Narrative Intelligence signal endpoint](https://apexrunner.ai/signals/narrative-intelligence)

## Skill Output:

**Output Type(s):** [API Calls, JSON data]

**Output Format:** [JSON response with narrative, sentiment, confidence, and timing fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One paid response per call; the skill documents an early-adopter price of $0.007 USDC per call through 2026-12-31 and a standard price of $0.01 per call.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
