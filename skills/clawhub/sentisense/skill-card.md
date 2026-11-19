## Description:

Connects agents to SentiSense’s read-only US market data API for stock prices, sentiment, ratings, insider and institutional activity, options, earnings, and AI-generated insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can query read-only US market data and combine prices, sentiment, filings, options, earnings, and company insights for informational research. The skill describes its output as informational, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports unpinned package execution, setup beyond declared permissions, and key provisioning that conflicts with the stated read-only purpose; its analysis is partial and rated suspicious with medium confidence.

Mitigation: Review setup before use, limit the agent's access, and consider the documented HTTPS provisioning path instead of running an unpinned package.

Risk: Temporary API keys and their keep links can grant access to the key.

Mitigation: Keep keys and keep links out of logs, commits, and shared screenshots; pass the keep link only to the person who will retain the key.

## Reference(s):

- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense Rating methodology](https://sentisense.ai/methodology/#sentisense-rating)
- [SentiSense skill page](https://clawhub.ai/thesentitrader/skills/sentisense)

## Skill Output:

**Output Type(s):** [API Calls, Financial data, Analysis, Guidance]

**Output Format:** [Structured market data with concise natural-language research guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only and informational; not investment advice]

## Skill Version(s):

2.32.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
