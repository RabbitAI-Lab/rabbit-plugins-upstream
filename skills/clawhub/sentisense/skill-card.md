## Description:

SentiSense guides agents in using a read-only SentiSense market-data API for U.S. stocks, including sentiment, ratings, prices, filings, institutional flows, options, analyst coverage, earnings, and AI-generated market insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent builders use this skill to fetch and interpret SentiSense market data through documented REST examples. It supports stock research, sentiment tracking, market dashboards, screeners, and earnings or filing workflows while keeping outputs informational rather than advisory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a SentiSense API key and HTTPS requests to app.sentisense.ai.

Mitigation: Store the key in SENTISENSE_API_KEY, use a revocable or scoped key where available, rotate it when needed, and limit network access to the documented SentiSense host.

Risk: Optional SDK installation adds dependency and supply-chain exposure beyond the documented REST examples.

Mitigation: Prefer direct REST calls from the skill unless an SDK is specifically needed, and review SDK source and package metadata before installation.

Risk: Personalized insights can use account-based watchlist or portfolio-derived results.

Mitigation: Call personalized insight endpoints only when the user explicitly asks for account-specific results.

Risk: Market data, AI-generated insights, and sentiment outputs could be mistaken for investment advice or live trading signals.

Mitigation: Present outputs as informational, preserve the non-advisory disclaimer, and note documented constraints such as delayed prices, preview tiers, quotas, and read-only behavior.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API Documentation](https://sentisense.ai/docs/api/)
- [SentiSense Methodology](https://sentisense.ai/methodology/)
- [ClawHub SentiSense Skill](https://clawhub.ai/thesentitrader/skills/sentisense)
- [SentiSense Python SDK](https://github.com/SentiSenseApp/sentisense)
- [SentiSense Node.js SDK](https://github.com/SentiSenseApp/sentisense-node)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with REST examples, curl commands, code snippets, endpoint notes, and expected JSON response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SENTISENSE_API_KEY for authenticated HTTPS requests to app.sentisense.ai; data access and response depth vary by free and PRO tiers.]

## Skill Version(s):

2.12.22 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
