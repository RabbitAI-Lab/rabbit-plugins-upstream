## Description:

Volatility analysis and mean reversion signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ssidharhubble](https://clawhub.ai/user/ssidharhubble)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request Bollinger Bands based volatility analysis and mean reversion signals for asset tickers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts an external zocomputer.io API with the ticker supplied by the user.

Mitigation: Review external API use before deployment and avoid sending sensitive or restricted ticker inputs.

Risk: Premium results may require a SOL payment.

Mitigation: Verify the provider identity, pricing page, wallet destination, and payment terms before sending funds.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ssidharhubble/skills/bollinger-bands-pro)
- [Pricing page](https://ssyopros.zo.space/pricing)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [JSON object containing Bollinger Bands signal data, or a JSON payment-required response for premium signals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ticker input is sent to an external zocomputer.io API.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
