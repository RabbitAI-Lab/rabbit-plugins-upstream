## Description:

SentiSense gives AI agents read-only access to US stock market data, including prices, sentiment, SentiSense scores and ratings, insider and congressional trading disclosures, institutional flows, options intelligence, analyst ratings, earnings information, and AI-generated market insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and AI-agent builders use this skill to retrieve read-only US equity market data, sentiment, institutional, insider, politician, options, earnings, and research signals from the SentiSense API. It supports market research and dashboard workflows, not trading execution or investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys and requested tickers, entities, and research queries are sent to SentiSense and may count against account quota.

Mitigation: Use the SENTISENSE_API_KEY environment variable, rotate or revoke keys when needed, and monitor tier and quota limits before automated use.

Risk: Market data and AI-generated outputs may be delayed, previewed, incomplete, or informational rather than suitable for trading decisions.

Mitigation: Treat outputs as research context, check freshness and tier indicators, and do not use the skill for trade execution or personalized investment advice.

Risk: The optional CLI authentication flow can store credentials locally.

Mitigation: Prefer the environment-variable API key flow unless local credential storage is intentional, and remove stored credentials when no longer needed.

## Reference(s):

- [SentiSense ClawHub listing](https://clawhub.ai/thesentitrader/skills/sentisense)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense API key management](https://app.sentisense.ai/get-api-key)
- [SentiSense methodology](https://sentisense.ai/methodology/)
- [SentiSense Python SDK](https://github.com/SentiSenseApp/sentisense)
- [SentiSense Node.js SDK](https://github.com/SentiSenseApp/sentisense-node)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with REST examples, shell commands, code snippets, and JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; API responses may be tiered, quota-limited, delayed, or previewed depending on endpoint and account.]

## Skill Version(s):

2.12.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
