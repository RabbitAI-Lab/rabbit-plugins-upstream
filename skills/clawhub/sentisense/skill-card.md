## Description:

SentiSense gives agents read-only access to US stock market data, sentiment, ratings, insider and congressional trades, institutional flows, options positioning, analyst ratings, earnings data, AI-generated market insights, and delayed stock prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query SentiSense for market research data and summarize stock, sentiment, institutional, insider, congressional, options, analyst, earnings, and price signals. Outputs are informational and do not authorize trades, purchases, write operations, wallet access, or investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a SentiSense API key.

Mitigation: Provide the key only through SENTISENSE_API_KEY, install only when API access is intended, and rotate or revoke the key when access is no longer needed.

Risk: Financial data and AI-generated market insights may be mistaken for investment advice or a trading instruction.

Mitigation: Treat outputs as informational, verify important data before acting, and do not use the skill to place trades or make automated purchase decisions.

Risk: Personalized insights can use SentiSense watchlist or portfolio context.

Mitigation: Use personalized endpoints only when the user intentionally wants results based on their SentiSense account context.

## Reference(s):

- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense homepage](https://sentisense.ai)
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/sentisense)
- [SentiSense API key management](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code, REST endpoint examples, and API response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY and HTTPS access to app.sentisense.ai; outputs should be treated as informational market data.]

## Skill Version(s):

2.16.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
