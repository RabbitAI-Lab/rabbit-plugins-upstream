## Description:

Provides read-only OKX public market data commands for prices, order books, candles, funding rates, open interest, instruments, screeners, and technical indicators without requiring API credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve OKX public market data, inspect instruments, screen markets, and calculate technical indicators before making their own decisions. The skill is not for account balances, order placement, trading bots, or event-contract execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the required OKX npm package may run an under-disclosed postinstall that adds native OKX binaries under ~/.okx/bin.

Mitigation: Install only in an environment where the OKX npm package is trusted, and review the package behavior before deployment.

Risk: Market data and indicator outputs may be mistaken for financial advice.

Mitigation: Treat outputs as raw market data; interpretation, strategy, and trading decisions remain with the user.

Risk: OKX credentials are not needed for this market-data skill, but related OKX account or trading capabilities may use credentials.

Mitigation: Do not provide or enable OKX credentials unless intentionally using other OKX account or trading capabilities outside this skill.

## Reference(s):

- [OKX website](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-market)
- [Price & Market Data Commands](references/price-data-commands.md)
- [Derivatives & Contract Data Commands](references/derivatives-commands.md)
- [Instrument Discovery Commands](references/instrument-commands.md)
- [Technical Indicator Command Reference](references/indicator-commands.md)
- [Cross-Skill Workflows & MCP Tool Reference](references/workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Market commands can return raw OKX API v5 JSON with --json or environment-wrapped output with --env.]

## Skill Version(s):

1.4.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
