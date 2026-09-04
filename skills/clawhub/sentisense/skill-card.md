## Description:

SentiSense gives agents read-only access to US stock market data, including sentiment, ratings, prices, institutional flows, insider and congressional trading, analyst ratings, earnings, options positioning, and AI-generated market insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to retrieve SentiSense financial intelligence for market research, watchlists, dashboards, and data-backed stock analysis. Outputs are informational financial data, not investment advice or trading instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market queries, watchlists or tickers, and the SentiSense API key are sent to SentiSense endpoints.

Mitigation: Use the skill only when the user accepts that data sharing; keep the API key in an environment variable, rotate or revoke it when needed, and avoid storing it locally unless that convenience is intentional.

Risk: Financial outputs could be mistaken for personalized investment advice or trading recommendations.

Mitigation: Present results as informational market data and require independent user judgment before any investment decision.

Risk: Optional CLI or SDK packages add package-execution and dependency risk.

Mitigation: Prefer direct REST calls unless the CLI or SDK source and package version have been reviewed for the deployment context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/sentisense)
- [SentiSense](https://sentisense.ai)
- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense methodology](https://sentisense.ai/methodology/)
- [SentiSense Python SDK](https://github.com/SentiSenseApp/sentisense)
- [SentiSense Node.js SDK](https://github.com/SentiSenseApp/sentisense-node)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with HTTP, curl, Python, JavaScript, and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; responses may include tiered previews, quota limits, delayed prices, and informational financial data.]

## Skill Version(s):

2.12.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
