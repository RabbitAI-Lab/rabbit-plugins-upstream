## Description:

SentiSense gives AI agents read-only access to US stock market data, including prices, sentiment, insider trades, congressional disclosures, institutional holdings, options positioning, analyst ratings, earnings calendars, and AI-generated market insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to query SentiSense market-data endpoints for research workflows, dashboards, screeners, and stock analysis. Outputs are informational data and guidance only, not investment advice or trade execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key and sends market-data queries to SentiSense.

Mitigation: Install only when that API use is acceptable; scope, rotate, and revoke the key through SentiSense account settings when needed.

Risk: Financial data and AI-generated market insights can be mistaken for investment advice.

Mitigation: Treat outputs as informational research data and avoid presenting them as recommendations or trade instructions.

Risk: Some endpoints are quota-gated, paid PRO features, or delayed market data.

Mitigation: Check tier labels, response wrappers, rate limits, and price freshness before using the data in workflows.

Risk: Optional CLI authentication can store credentials locally.

Mitigation: Prefer environment variables when appropriate, or remove stored CLI credentials when no longer needed.

## Reference(s):

- [SentiSense API Documentation](https://sentisense.ai/docs/api/)
- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Key Management](https://app.sentisense.ai/get-api-key)
- [ClawHub Skill Release](https://clawhub.ai/thesentitrader/skills/sentisense)
- [SentiSense Python SDK](https://github.com/SentiSenseApp/sentisense)
- [SentiSense Node.js SDK](https://github.com/SentiSenseApp/sentisense-node)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with REST API examples, curl commands, endpoint notes, and JSON response-shape guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only API usage; requires SENTISENSE_API_KEY; outputs may include delayed market data, quota-gated responses, and paid PRO feature previews.]

## Skill Version(s):

2.12.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
