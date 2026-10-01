## Description:

Provides agents with read-only SentiSense market data and research on US stocks, including prices, sentiment, ratings, filings, options, and earnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can retrieve US stock market data and summarize sentiment, ratings, filings, institutional activity, options, and earnings for informational research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market queries require network access and a SentiSense API key.

Mitigation: Provide a key only if comfortable sending requested queries to SentiSense; use personalized endpoints only when account-linked watchlist or portfolio context is intended.

Risk: Market data or AI-generated insights could be mistaken for investment advice.

Mitigation: Treat results as informational research, not personalized investment recommendations.

## Reference(s):

- [SentiSense ClawHub skill](https://clawhub.ai/thesentitrader/skills/sentisense)
- [SentiSense API documentation](https://sentisense.ai/docs/api/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown summaries and optional API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only data; availability and freshness depend on the endpoint and access tier.]

## Skill Version(s):

2.20.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
