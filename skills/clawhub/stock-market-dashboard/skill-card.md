## Description:

Guides an agent to create a self-contained HTML stock-market briefing from read-only SentiSense market data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, market researchers, and other external users can ask an agent to assemble a read-only morning briefing with market mood, watchlist sentiment, filings, and upcoming earnings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent uses a SentiSense API key to retrieve market data.

Mitigation: Use a key only if comfortable sharing it with the agent for read-only market-data calls; do not embed it in the HTML output.

Risk: A saved dashboard can be mistaken for current market data or trading advice.

Mitigation: Show generation and per-field freshness labels, check timestamps before relying on the data, and present the briefing as research and education rather than trading advice.

Risk: Preview or partial datasets can give a misleading impression of complete coverage.

Mitigation: Label preview counts and incomplete filing coverage; avoid claims about missing activity or intent from partial data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/stock-market-dashboard)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Code, Files, Text]

**Output Format:** [One self-contained HTML file with an accompanying briefing]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Static market-data snapshot with generation and field-freshness labels; no backend or build step.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
