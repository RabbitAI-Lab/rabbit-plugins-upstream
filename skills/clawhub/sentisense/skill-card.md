## Description:

SentiSense provides a read-only US stock market data API for AI agents covering prices, news and social sentiment, the SentiSense Score, insider and congressional trades, institutional 13F data, options intelligence, analyst ratings, earnings calendar data, and AI-generated market insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to query SentiSense's read-only financial intelligence API for market research, dashboards, screeners, watchlists, and stock analysis. Outputs are informational financial research and are not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a SentiSense API key, and API requests are attributed to that account.

Mitigation: Install only when that account-level access is acceptable, provide the key through SENTISENSE_API_KEY, and rotate or revoke the key from SentiSense account settings when needed.

Risk: Financial market outputs could be mistaken for trading advice or live execution data.

Mitigation: Treat responses as informational financial research only, preserve the not-investment-advice posture, and do not use the skill for trading or execution decisions.

Risk: The optional CLI can store credentials locally.

Mitigation: Use CLI credential storage only when a saved local key is desired; otherwise keep credentials in the environment and remove stored credentials with the documented auth removal flow.

## Reference(s):

- [SentiSense website](https://sentisense.ai)
- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense methodology](https://sentisense.ai/methodology/)
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/sentisense)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with curl, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; API responses vary by endpoint, access tier, quota, and rate limits.]

## Skill Version(s):

2.12.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
