## Description:

Stock screener for AI agents that filters US stocks and ETFs by SentiSense sentiment signals, analyst data, technicals, momentum, price, and market cap, with curated screens and plain-language screen planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to translate stock or ETF screening requests into valid SentiSense screener plans, run read-only screens, and review results as research context. It is intended for informational screening, not financial advice or trading instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Screening criteria and watchlist tickers are sent to SentiSense when the skill runs screens.

Mitigation: Use the skill only when sharing those criteria and tickers with SentiSense is acceptable.

Risk: The optional CLI auth flow can store the SentiSense API key locally.

Mitigation: Use environment-based credentials unless local CLI auth storage is desired, and remove stored auth when it is no longer needed.

Risk: Screening output may be mistaken for investment advice or trade instructions.

Mitigation: Present results as research context and avoid personalized buy, sell, or trade recommendations.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [SentiSense Screener Execute API](https://app.sentisense.ai/api/v1/screener/execute)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/stock-screener)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, API request examples, and screen plan summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are read-only research context and should include the screen plan used with matched and displayed result counts when results are returned.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
