## Description:

Real-time institutional transaction monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ssidharhubble](https://clawhub.ai/user/ssidharhubble)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to request institutional transaction signals for asset tickers such as BTC, SPY, or TSLA. Premium results may require independent verification of a manual crypto payment request before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested tickers are sent to an external whale-signal API.

Mitigation: Use the skill only when sharing ticker symbols with the listed API is acceptable.

Risk: Premium responses may present a manual crypto payment request and pricing URL.

Mitigation: Verify the wallet address, pricing page, and business need independently before sending funds.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ssidharhubble/skills/whale-scanner)
- [Publisher profile](https://clawhub.ai/user/ssidharhubble)
- [Whale signal API endpoint](https://x402-money-machine-api-ssyopros.zocomputer.io/api/whale/{ticker})
- [Pricing page](https://ssyopros.zo.space/pricing)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [JSON object from the external API, or a payment-required error object with a message and pricing URL.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ticker input is normalized to uppercase before the API request.]

## Skill Version(s):

1.1.2 (source: server release metadata; artifact/package.json reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
