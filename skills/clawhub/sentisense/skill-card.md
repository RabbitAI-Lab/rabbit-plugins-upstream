## Description:

US stock market data API for AI agents covering news and social sentiment, SentiSense Score and Rating, insider Form 4 trades, congressional STOCK Act disclosures, institutional 13F holdings and flows, options positioning, analyst ratings, earnings calendar data, AI-generated market insights, and stock prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and market-research agents use this skill to query SentiSense's read-only market-data API for stock prices, sentiment, ownership flows, filings, options analytics, earnings data, and generated market insights. Outputs should be treated as informational market research, not investment advice or trade execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a SentiSense API key.

Mitigation: Provide the key through SENTISENSE_API_KEY, keep it out of prompts and logs, rotate it when needed, and avoid running optional SDKs with unrelated secrets in the environment.

Risk: Market-data queries, watchlists, and screener criteria are sent to SentiSense.

Mitigation: Use the skill only when sharing those requests with SentiSense is acceptable, and keep sensitive research lists or client-specific criteria out of requests unless approved.

Risk: Financial market outputs may be mistaken for current trading signals or personalized investment advice.

Mitigation: Present results as informational market research, disclose delayed prices and preview limits where relevant, and do not use the skill for trading, purchases, wallet access, or personalized recommendations.

## Reference(s):

- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Documentation](https://sentisense.ai/docs/api/)
- [SentiSense Application](https://app.sentisense.ai)
- [Get SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/sentisense)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with REST endpoint descriptions, curl examples, SDK snippets, and API usage notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY and HTTPS access to app.sentisense.ai; API responses may include tier-specific previews, quota limits, and delayed market prices.]

## Skill Version(s):

2.12.21 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
