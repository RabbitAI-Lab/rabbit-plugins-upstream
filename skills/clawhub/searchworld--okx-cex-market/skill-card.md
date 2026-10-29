## Description:

Provides read-only OKX public market data, including prices, order books, candles, funding rates, open interest, instrument discovery, market screening, and technical indicators without requiring API credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and market analysts use this skill to retrieve OKX public market data and objective indicator values before making their own analysis or routing account and order actions to separate reviewed skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the skill adds a global npm CLI that may query live public OKX market endpoints.

Mitigation: Review the package before installation and make the active demo or live context clear when it affects the user's market-data request.

Risk: Users may mistake indicator values or market data summaries for trading advice.

Mitigation: Present outputs as objective data only and route account, position, and order actions to separate reviewed skills.

Risk: Large historical candle requests can consume excessive context or return more data than intended.

Mitigation: Estimate the requested candle count and ask for confirmation before fetching ranges above the documented threshold.

## Reference(s):

- [OKX homepage](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-market)
- [Price & Market Data Commands](references/price-data-commands.md)
- [Derivatives & Contract Data Commands](references/derivatives-commands.md)
- [Instrument Discovery Commands](references/instrument-commands.md)
- [Technical Indicator Command Reference](references/indicator-commands.md)
- [Cross-Skill Workflows & MCP Tool Reference](references/workflows.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown responses with inline OKX CLI commands and optional JSON market-data output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public market data; no API credentials required.]

## Skill Version(s):

1.4.8 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
