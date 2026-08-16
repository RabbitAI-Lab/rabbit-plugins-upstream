## Description:

US stock market data API for AI agents: news and social sentiment, the SentiSense Score, insider Form 4 trades, congressional STOCK Act disclosures, institutional 13F holdings and flows, options positioning, analyst ratings, the earnings calendar, AI-generated market insights, and stock prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent users use this skill to retrieve read-only U.S. stock market data, sentiment, filings, institutional flows, options intelligence, analyst data, earnings information, AI-generated market insights, and delayed stock prices from SentiSense.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key.

Mitigation: Install only when the user is comfortable granting the agent access to SENTISENSE_API_KEY, and keep the key scoped to SentiSense API access.

Risk: The personalized insights endpoint can retrieve account-specific insight output based on a SentiSense watchlist or portfolio.

Mitigation: Avoid personalized insights unless the user explicitly intends the agent to access account-specific SentiSense output.

Risk: The skill provides informational market data and AI-generated market insights, not investment advice.

Mitigation: Use outputs for research context only and require user review before financial decisions.

## Reference(s):

- [SentiSense website](https://sentisense.ai)
- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense ClawHub skill page](https://clawhub.ai/thesentitrader/skills/sentisense)
- [SentiSense Python SDK](https://github.com/SentiSenseApp/sentisense)
- [SentiSense Node.js SDK](https://github.com/SentiSenseApp/sentisense-node)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with API endpoint guidance, HTTP examples, shell commands, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; API responses are read-only market-data outputs and may include account-personalized insight output when the personalized insights endpoint is used.]

## Skill Version(s):

2.10.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
