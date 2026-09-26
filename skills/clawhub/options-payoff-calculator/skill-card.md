## Description:

Creates an offline, interactive options payoff chart for stocks and ETFs using delayed SentiSense market data and modeled premiums.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use the skill to explore expiry profit and loss, breakevens, and expected-move bands for common options strategies using a market-data snapshot. The charts are educational, not trading recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generating a chart requires a SentiSense API key for read-only market data requests.

Mitigation: Provide the key through the environment only if comfortable sharing it with SentiSense; do not embed it in the generated file.

Risk: Delayed prices and modeled premiums may be mistaken for live options quotes or trading advice.

Mitigation: Label premiums as modeled, disclose the data delay, and use the payoff chart for education rather than trade execution or recommendations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/options-payoff-calculator)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [HTML file, Text guidance]

**Output Format:** [Self-contained interactive HTML chart and concise plain-text explanation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Works offline after generation; premiums are modeled, and market prices are delayed.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
