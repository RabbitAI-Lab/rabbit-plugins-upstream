## Description:

US stock market data API for AI agents: news and social sentiment, the SentiSense Score, the SentiSense Rating daily A to F letter grade, insider Form 4 trades, congressional STOCK Act disclosures, institutional 13F holdings and flows, options positioning, analyst ratings, the earnings calendar, AI-generated market insights, and stock prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to query read-only SentiSense market data for US equities, including sentiment, prices, filings, options, earnings, and AI-generated market insights. It supports market research workflows and dashboards while treating outputs as informational market data, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a SentiSense API key and sends ticker queries, screener filters, and requested SentiSense account data to app.sentisense.ai.

Mitigation: Store the key only in SENTISENSE_API_KEY, restrict use to HTTPS requests to app.sentisense.ai, and rotate or revoke the key from the SentiSense account settings when needed.

Risk: Market data and AI-generated insights could be mistaken for investment advice or used as execution-ready trading signals.

Mitigation: Present outputs as informational market data only and require human review before making investment or trading decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/sentisense)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense hosted skill file](https://sentisense.ai/skill.md)
- [SentiSense Python SDK](https://github.com/SentiSenseApp/sentisense)
- [SentiSense Node.js SDK](https://github.com/SentiSenseApp/sentisense-node)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with REST endpoint descriptions and inline bash, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY and sends read-only HTTPS requests to app.sentisense.ai.]

## Skill Version(s):

2.17.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
