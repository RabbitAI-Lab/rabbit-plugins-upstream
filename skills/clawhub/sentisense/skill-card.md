## Description:

Provides read-only access to SentiSense US stock market data, including news and social sentiment, company ratings, insider and congressional trades, institutional holdings, options, analyst ratings, earnings, AI-generated insights, and stock prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

AI agents use this skill to retrieve SentiSense market data for user-requested research and screening. It provides informational data only and does not place trades or make purchases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries disclose requested tickers and screening criteria to SentiSense.

Mitigation: Only query tickers and criteria you are comfortable sharing with the service.

Risk: A temporary API key and its claim link are credentials.

Mitigation: Protect both the key and its claim link.

Risk: Optional SDK/CLI code and live service behavior were not audited.

Mitigation: Prefer the direct HTTP workflow when optional packages are unnecessary.

## Reference(s):

- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense ClawHub listing](https://clawhub.ai/thesentitrader/skills/sentisense)

## Skill Output:

**Output Type(s):** [API calls, JSON data, Market data summaries]

**Output Format:** [JSON responses with concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only informational data; not investment advice.]

## Skill Version(s):

2.26.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
