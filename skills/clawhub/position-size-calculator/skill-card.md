## Description:

Builds an offline stock or ETF position-size calculator using delayed SentiSense market data and the user's own risk inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and other external users enter their account size, risk percentage, entry and stop to see the resulting whole-share count, position value, dollar risk and optional target R multiple. The calculator provides arithmetic and market context, not a trading recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A delayed quote or historical range may not reflect the current market.

Mitigation: Check current prices before acting; treat the displayed range as historical context, not a forecast.

Risk: Gaps, slippage, failed stop execution and unmodeled costs can make actual losses exceed the displayed risk.

Mitigation: Treat the result as arithmetic on user inputs, not an assured loss limit or trading advice.

Risk: Generating the file requires a SentiSense API key for read-only market-data requests.

Mitigation: Supply the key through the environment and avoid including it in the generated file or shared output.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/position-size-calculator)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Files, Text]

**Output Format:** [Self-contained interactive HTML file with brief explanatory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Opens offline with a delayed last price, 14-session average true range, and optional SentiSense Score; the user adjusts account size, risk, entry, stop and target in the page. No trades or account changes.]

## Skill Version(s):

1.0.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
