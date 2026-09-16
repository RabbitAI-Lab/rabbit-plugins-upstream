## Description:

SentiSense gives agents read-only access to US stock market data, including sentiment, stock scores and ratings, insider and congressional disclosures, institutional holdings and flows, options positioning, analyst ratings, earnings, prices, and AI-generated market insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and financial research agents use this skill to retrieve read-only US market data and SentiSense analytics for informational analysis. It supports research workflows such as sentiment monitoring, smart-money tracking, earnings preparation, cross-signal screening, and market dashboards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a SentiSense API key.

Mitigation: Install only in trusted agent environments, store SENTISENSE_API_KEY as an environment secret, and rotate or revoke keys from SentiSense account settings when needed.

Risk: Financial data and AI-generated market insights could be mistaken for investment advice or live trading signals.

Mitigation: Treat outputs as informational only, verify freshness and source context, and do not use the skill for trading, purchases, or personalized recommendations.

Risk: Optional SDK installation adds supply-chain exposure compared with direct REST calls.

Mitigation: Prefer direct HTTPS REST calls unless an SDK is needed, and review SDK source before installation.

Risk: Personalized insight endpoints may use SentiSense watchlist or portfolio context.

Mitigation: Use personalized endpoints only when the user intentionally wants account-contextual results.

## Reference(s):

- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Docs](https://sentisense.ai/docs/api/)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/sentisense)
- [SentiSense API Key Management](https://app.sentisense.ai/get-api-key)
- [SentiSense Python SDK](https://github.com/SentiSenseApp/sentisense)
- [SentiSense Node.js SDK](https://github.com/SentiSenseApp/sentisense-node)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with REST API examples, curl snippets, code snippets, and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only HTTPS API access; requires SENTISENSE_API_KEY; price data may be delayed and access tiers, quotas, and rate limits apply.]

## Skill Version(s):

2.13.0 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
