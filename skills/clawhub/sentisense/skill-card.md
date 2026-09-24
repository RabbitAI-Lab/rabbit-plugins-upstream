## Description:

SentiSense provides AI agents with read-only access to US stock market data, including sentiment, ratings, insider and congressional trades, institutional flows, options positioning, analyst ratings, earnings data, AI-generated market insights, and stock prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to connect agents to SentiSense market-data endpoints for stock research, sentiment monitoring, screening, and market summaries. The skill is read-only and its financial outputs are informational, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a SentiSense API key and sends market queries, screener plans, and explicitly requested personalized insight calls to SentiSense.

Mitigation: Install only when this data sharing is acceptable, scope the agent environment to SENTISENSE_API_KEY, and rotate or revoke the key from the SentiSense account settings when needed.

Risk: Market and sentiment outputs may be mistaken for investment advice or personalized recommendations.

Mitigation: Present outputs as informational financial data only and require independent review before any trading or investment decision.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/sentisense)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense methodology](https://sentisense.ai/methodology/)
- [Latest SentiSense skill file](https://sentisense.ai/skill.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, API calls]

**Output Format:** [Markdown with REST endpoint descriptions, inline shell commands, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; uses read-only HTTPS requests to app.sentisense.ai.]

## Skill Version(s):

2.17.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
