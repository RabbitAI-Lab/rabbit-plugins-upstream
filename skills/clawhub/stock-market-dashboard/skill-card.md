## Description:

Creates a self-contained HTML market briefing from SentiSense data, including market mood, sentiment, watchlist metrics, filings, news, and earnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and market researchers use this skill to generate a morning dashboard snapshot for reviewing market sentiment, company signals, and upcoming earnings; it does not provide investment advice or execute trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market prices and analytical data may be delayed or stale in the saved dashboard.

Mitigation: Show the generation time and per-field freshness; use the snapshot for research, not investment advice.

Risk: The dashboard is created locally and a file path or pinned widget may not be the delivery location the user expects.

Mitigation: Confirm the requested output location and verify any delivered path or pinned widget before sharing.

Risk: The skill uses a SentiSense API key to retrieve market data.

Mitigation: Keep the key in the environment for read-only calls to app.sentisense.ai; do not embed it in the generated HTML.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/stock-market-dashboard)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Code, Files]

**Output Format:** [Single self-contained HTML file with inline CSS and optional JavaScript]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline-readable snapshot with generated-at timestamp and market-data freshness labels; requires a SentiSense API key to fetch data at creation time.]

## Skill Version(s):

1.2.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
