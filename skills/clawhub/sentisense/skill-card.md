## Description:

US stock market data API for AI agents: news and social sentiment, the SentiSense Score, the SentiSense Rating daily A to F letter grade, insider Form 4 trades, congressional STOCK Act disclosures, institutional 13F holdings and flows, options positioning, analyst ratings, the earnings calendar, AI-generated market insights, and stock prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query SentiSense's read-only financial intelligence API for stock sentiment, prices, insider and congressional trades, institutional flows, options positioning, analyst ratings, earnings calendars, and AI-generated market insights. The skill is intended for informational market research and does not support trading, purchases, write operations, wallet access, or investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent receives access to the SentiSense API key.

Mitigation: Store the key in SENTISENSE_API_KEY, avoid exposing it in prompts or logs, and rotate or revoke it from the SentiSense account settings if access changes.

Risk: Market data and generated insights could be mistaken for investment advice or live execution data.

Mitigation: Present outputs as informational research only, preserve delay and freshness notes, and do not use the skill for trade execution or personalized recommendations.

Risk: Some API calls may consume quota or require a paid tier.

Mitigation: Check endpoint access tiers, rate limits, and preview wrappers before building workflows that make repeated or broad requests.

## Reference(s):

- [SentiSense website](https://sentisense.ai)
- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense app](https://app.sentisense.ai)
- [Get a SentiSense API key](https://app.sentisense.ai/get-api-key)
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/sentisense)
- [Python SDK](https://github.com/SentiSenseApp/sentisense)
- [Node.js SDK](https://github.com/SentiSenseApp/sentisense-node)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline HTTP, shell, Python, and JavaScript examples; API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY and HTTPS access to app.sentisense.ai; some endpoints may consume quota or require a paid tier.]

## Skill Version(s):

2.12.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
