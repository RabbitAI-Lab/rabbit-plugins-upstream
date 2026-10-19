## Description:

Creates an offline stock and ETF position-size calculator using a delayed SentiSense quote and the user's own risk inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Individual investors and research assistants use it to calculate whole-share counts, position value, account exposure, dollar risk, and an optional target's R multiple from an account size, risk percentage, entry, and stop. It does not select trades or recommend a position.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A delayed quote or historical range may not reflect the current market.

Mitigation: Check current prices and confirm the entry and stop before relying on the calculation.

Risk: Gaps, slippage, and unmodeled trading costs can make actual losses exceed the displayed risk.

Mitigation: Treat the result as arithmetic, not investment advice; verify risk settings and account for execution and costs independently.

Risk: The skill needs an API key for market context and writes a local HTML file.

Mitigation: Provide the key through the environment and review where the generated file is saved before sharing it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/position-size-calculator)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Files, Guidance]

**Output Format:** [Self-contained HTML calculator and brief text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The HTML opens offline with a delayed last price, historical range, and optional SentiSense Score bound at creation; users adjust the account, risk, entry, stop, and optional target locally.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
