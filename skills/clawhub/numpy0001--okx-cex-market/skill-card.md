## Description:

Provides read-only OKX public market data commands for prices, order books, candles, funding rates, open interest, instruments, screeners, and technical indicators without API credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[numpy0001](https://clawhub.ai/user/numpy0001)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query OKX public market data, instrument metadata, derivative metrics, screeners, and technical indicators. It is intended for market-data retrieval and command guidance, not account management, order placement, bots, or trading recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install guidance may fetch a globally installed, unpinned CLI version instead of the reviewed @okx_ai/okx-trade-cli@1.3.7 package.

Mitigation: Pin the npm install to @okx_ai/okx-trade-cli@1.3.7 or use a locally scoped install before use.

Risk: Market data and technical indicators can be mistaken for trading advice.

Mitigation: Treat outputs as raw data only; keep interpretation and trading decisions with the user.

Risk: Some instrument categories and historical data requests have constraints that can produce invalid or overly large queries.

Mitigation: Follow the documented instrument formats, verify live instrument state where relevant, and ask for confirmation before large historical ranges.

## Reference(s):

- [OKX Homepage](https://www.okx.com)
- [ClawHub Skill Page](https://clawhub.ai/numpy0001/skills/okx-cex-market)
- [Price & Market Data Commands](references/price-data-commands.md)
- [Derivatives & Contract Data Commands](references/derivatives-commands.md)
- [Instrument Discovery Commands](references/instrument-commands.md)
- [Technical Indicator Command Reference](references/indicator-commands.md)
- [Cross-Skill Workflows & MCP Tool Reference](references/workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown responses with inline shell commands and optional JSON command output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public market data; no API credentials required.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter metadata.version is 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
