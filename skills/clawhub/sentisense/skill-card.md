## Description:

SentiSense is a read-only US stock market data API for AI agents covering sentiment, prices, insider and congressional trades, institutional holdings and flows, options positioning, analyst ratings, earnings, and AI-generated market insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to query SentiSense's read-only market data endpoints for stock research, dashboards, sentiment monitoring, and disclosure or holdings analysis. Outputs are informational financial data, not trading advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key, which gives an agent access to query the user's SentiSense account.

Mitigation: Provide the key only to agents and environments that should access SentiSense, store it in SENTISENSE_API_KEY, and rotate or revoke it if exposure is suspected.

Risk: API calls can consume monthly quotas or require a paid tier for full data.

Mitigation: Monitor API usage, prefer documented discovery endpoints when exploring, and confirm the user's tier before broad or repeated queries.

Risk: Financial outputs may be mistaken for investment advice or current execution-quality market data.

Mitigation: Present results as informational only, preserve the non-advisory disclaimer, and clearly note documented delays or freshness fields for price data.

Risk: Incorrect endpoint assumptions can produce failed calls or misleading partial results.

Mitigation: Follow the documented endpoint paths and response wrappers in the skill, including unwrapping PRO-gated responses via the data field and using current quarter discovery where required.

## Reference(s):

- [SentiSense website](https://sentisense.ai)
- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/sentisense)
- [Get a SentiSense API key](https://app.sentisense.ai/get-api-key)
- [SentiSense Python SDK](https://github.com/SentiSenseApp/sentisense)
- [SentiSense Node.js SDK](https://github.com/SentiSenseApp/sentisense-node)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, JSON data]

**Output Format:** [Markdown guidance with REST endpoint examples, curl and SDK snippets, and JSON response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; API responses are read-only and may be quota-gated, tier-gated, or delayed depending on endpoint.]

## Skill Version(s):

2.9.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
