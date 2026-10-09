## Description:

Creates an offline, interactive options payoff chart for a stock or ETF using delayed market data and modeled option premiums.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use the skill to compare expiry payoffs, breakevens, and expected-move bands for common options strategies on stocks and ETFs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an API key and sends the requested ticker to SentiSense.

Mitigation: Provide the key only when comfortable with this data access, and keep the key in the environment rather than the generated file.

Risk: Delayed prices and modeled premiums may be mistaken for executable options quotes or trading advice.

Mitigation: Label premiums as modeled, show the snapshot date, and treat the chart as educational modeling rather than a quote or recommendation.

Risk: A free earnings-calendar preview may omit a report beyond its one-week window.

Mitigation: Present the next report as unknown when the calendar is incomplete; do not describe it as unscheduled.

## Reference(s):

- [Options Payoff Calculator on ClawHub](https://clawhub.ai/thesentitrader/skills/options-payoff-calculator)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)
- [SentiSense](https://sentisense.ai)

## Skill Output:

**Output Type(s):** [HTML file, Text guidance]

**Output Format:** [Self-contained interactive HTML chart with a short written summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Renders offline from a build-time market-data snapshot; premiums are modeled, not live quotes.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
