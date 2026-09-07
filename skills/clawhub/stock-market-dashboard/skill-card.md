## Description:

Builds a self-contained, read-only HTML stock market dashboard from SentiSense market data, including market mood, breadth, sector tone, watchlist sentiment, options, filings, flows, stories, ratings, and earnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate a static morning market briefing or watchlist dashboard from read-only market data. The skill supports research and reporting workflows and does not perform trading, purchases, write operations, or wallet access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key for read-only market-data calls.

Mitigation: Install only if providing that key to the agent is acceptable, and scope the key to read-only use where possible.

Risk: A generated dashboard can be mistaken for live market data after time passes.

Mitigation: Render the dashboard as a static snapshot and include the generation timestamp and freshness notes in the output.

Risk: Hosted widget or session-dashboard delivery may not be desired when the user wants only a local file.

Mitigation: Ask the agent to avoid OpenClaw's pinned widget or session dashboard delivery route when a local file-only workflow is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-market-dashboard)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, code, configuration, guidance]

**Output Format:** [Self-contained HTML file with inline CSS and optional inline JavaScript.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Static data snapshot generated from read-only SentiSense API calls; requires SENTISENSE_API_KEY.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
