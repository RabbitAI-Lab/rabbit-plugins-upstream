## Description:

Provides read-only access to US stock prices, sentiment, insider and congressional trades, institutional activity, options, earnings, and AI-generated market research through the SentiSense API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to retrieve and summarize US stock market data for informational research and monitoring. Its outputs are not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SentiSense receives the symbols and filters queried, including submitted watchlists.

Mitigation: Avoid sending watchlists or filters that contain information the user does not want shared with SentiSense.

Risk: Temporary API keys and their keep links can grant access to the key; the skill may create a temporary key when none is supplied.

Mitigation: Prefer a user-provided API key when desired, and keep API keys and key-claim links private and out of logs, commits, and shared screenshots.

## Reference(s):

- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense website](https://sentisense.ai)
- [Get or manage an API key](https://app.sentisense.ai/get-api-key)
- [SentiSense on ClawHub](https://clawhub.ai/thesentitrader/skills/sentisense)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Analysis, Text, Markdown]

**Output Format:** [Structured market data and informational research summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results; available fields and coverage depend on endpoint and access tier.]

## Skill Version(s):

2.28.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
