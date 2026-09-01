## Description:

Builds a single self-contained HTML stock market dashboard that turns SentiSense market data into a read-only morning market briefing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and market research users use this skill to generate a local, static dashboard snapshot covering market mood, sentiment, watchlists, filings, flows, stories, analyst activity, and earnings. The output is read-only and is not intended to place trades or provide investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires a SentiSense API key and sends requested tickers or watchlists to SentiSense for read-only market data.

Mitigation: Use the skill only when that data sharing is acceptable, and keep the API key scoped and handled as a credential.

Risk: The generated dashboard is a static snapshot and may be mistaken for a live feed or trading recommendation.

Mitigation: Include the generation timestamp, freshness notes, and investment-advice disclaimer in the dashboard output.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [SentiSense API Key Setup](https://app.sentisense.ai/get-api-key)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/stock-market-dashboard)

## Skill Output:

**Output Type(s):** [code, files, shell commands, configuration, guidance]

**Output Format:** [Self-contained HTML with inline CSS and JavaScript, plus concise generation notes when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; uses read-only market data calls; the generated dashboard is a timestamped snapshot, not a live feed.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
