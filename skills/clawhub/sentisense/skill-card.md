## Description:

Provides read-only US stock market data and research signals through the SentiSense API, including prices, news and social sentiment, insider and congressional disclosures, institutional activity, options, analyst ratings, earnings, and AI-generated insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research agents use this skill to retrieve US stock market data and summarize company and market signals for informational analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can request a temporary API key when the user has not supplied one, and its keep link can transfer that key to an account.

Mitigation: Prefer a user-provided key; review and obtain confirmation before provisioning a temporary key, and keep the key and keep link out of logs and shared materials.

Risk: Market data and generated signals could be mistaken for investment advice.

Mitigation: Present results as informational only and verify important figures before relying on them in financial decisions.

## Reference(s):

- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API key management](https://app.sentisense.ai/get-api-key)
- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/sentisense)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text, Markdown]

**Output Format:** [JSON API responses with concise text or Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only financial information; not investment advice.]

## Skill Version(s):

2.29.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
