## Description:

Builds a one-file, read-only stock market dashboard from SentiSense data for a morning market briefing with market mood, sentiment breadth, sector tone, watchlist context, flows, stories, rating moves, and earnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and market-research users use this skill to generate a static browser-openable market dashboard from read-only SentiSense API data. It is intended for informational market research and not for trading, purchases, recommendations, or wallet activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a SentiSense API key during dashboard generation.

Mitigation: Use the key only for read-only SentiSense requests, avoid embedding it in generated HTML, and avoid sharing logs or files that expose credentials.

Risk: A static financial dashboard can be mistaken for live market data or investment advice.

Mitigation: Include generation timestamps, per-field freshness notes, and a clear disclaimer that the content is informational and not a recommendation to buy or sell securities.

Risk: Incorrect metric windows, sentiment scales, or wrapped API payload handling can produce misleading dashboard values.

Mitigation: Use the documented 30-day market mood and metric windows, keep SentiSense Score separate from sentiment polarity, unwrap v1 endpoint data payloads, and review generated figures before sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-market-dashboard)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance that leads the agent to produce a single self-contained HTML file with inline CSS, optional inline JavaScript, and baked-in market data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for read-only data calls; generated dashboard is a static snapshot and should include freshness notes and a financial-content disclaimer.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
