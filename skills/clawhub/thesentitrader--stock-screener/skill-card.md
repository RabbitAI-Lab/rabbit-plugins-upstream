## Description:

Stock Screener helps agents translate plain-language US stock and ETF screening requests into valid SentiSense screener plans and research-oriented results using sentiment, analyst, technical, momentum, price, and market-cap filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to run read-only US stock and ETF screens, including curated screens and custom filters, for research workflows. It is suited for finding candidates by sentiment, analyst ratings, technicals, momentum, price, market cap, and watchlist constraints, not for trading or personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses SentiSense as an external financial-data provider and requires a SENTISENSE_API_KEY.

Mitigation: Install only if that external provider and API-key requirement are acceptable for the deployment environment.

Risk: The CLI path can persist credentials locally when auth storage is used.

Mitigation: Prefer environment-variable authentication when local credential persistence is not desired.

Risk: Screening output can be mistaken for personalized investment advice.

Mitigation: Treat the results as research context and keep the skill's read-only, informational framing visible to users.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/stock-screener)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only screener plans and result summaries; requires SENTISENSE_API_KEY for live SentiSense requests.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
