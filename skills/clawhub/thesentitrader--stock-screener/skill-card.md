## Description:

Stock Screener helps agents translate plain-language US stock and ETF screening requests into SentiSense screen plans using sentiment, analyst, technical, momentum, price, and market-cap filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run read-only stock and ETF screens, translate fuzzy screening asks into explicit filter plans, and review candidate rows with the selected plan visible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional CLI path runs a pinned npm package and can store the SentiSense API key locally.

Mitigation: Prefer documented REST calls in stricter environments, keep the API key narrowly scoped and revocable, and avoid persistent auth storage unless it is needed.

Risk: Screening outputs may be mistaken for personalized investment advice.

Mitigation: Present results as informational candidates only, show the screen plan and matched count, and avoid buy, sell, or trading instructions.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [SentiSense Screener Execute API](https://app.sentisense.ai/api/v1/screener/execute)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/stock-screener)

## Skill Output:

**Output Type(s):** [guidance, shell commands, API calls, configuration]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only screener plans and result summaries; no trading, purchase, wallet, or account-modification output.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
