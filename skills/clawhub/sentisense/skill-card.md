## Description:

Provides agents read-only access to U.S. stock prices, sentiment, insider and institutional activity, options, earnings, analyst data, and market insights through the SentiSense API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use the skill to retrieve U.S. market data and sentiment for watchlists, screening, and informational research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags automatic API-key provisioning despite the stated read-only purpose, describing a disclosure and authorization mismatch; it does not indicate clear malicious intent.

Mitigation: Review whether temporary key provisioning is acceptable and whether watchlists or screening criteria should be sent to SentiSense. The assessment says scan coverage is incomplete because many local references were unresolved.

## Reference(s):

- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense Rating methodology](https://sentisense.ai/methodology/#sentisense-rating)
- [Get an API key](https://app.sentisense.ai/get-api-key)
- [Python SDK](https://github.com/SentiSenseApp/sentisense)
- [Node.js SDK](https://github.com/SentiSenseApp/sentisense-node)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [JSON market data with concise natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only, informational output; not investment advice.]

## Skill Version(s):

2.29.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
