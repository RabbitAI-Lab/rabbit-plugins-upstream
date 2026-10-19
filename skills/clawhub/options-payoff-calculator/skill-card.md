## Description:

Builds an interactive, offline options payoff chart for stocks and ETFs using SentiSense market data and modeled premiums.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Traders, analysts, and other users explore expiration payoffs, breakevens, and potential gains and losses for common stock and ETF options strategies using a market-data snapshot. The chart is educational, not a trade recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Modeled premiums and delayed market data could be mistaken for executable quotes or investment advice.

Mitigation: Label premiums as modeled, show data dates, and present the chart as educational scenario analysis rather than a recommendation.

Risk: The build-time data request uses a SentiSense API key.

Mitigation: Supply the key through the environment and allow only the disclosed read-only SentiSense requests; keep credentials out of shared output.

Risk: Free-tier previews can omit longer expiries or leave a future earnings date unknown.

Mitigation: Disclose missing expiries and calendar coverage rather than interpreting absent data as no scheduled earnings.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/options-payoff-calculator)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Code, Text]

**Output Format:** [Self-contained interactive HTML file with a brief written explanation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Opens offline; shows modeled expiration payoffs, breakevens, maximum gain and loss, and an expected-move band.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
