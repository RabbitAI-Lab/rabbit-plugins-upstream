## Description:

Provides read-only OKX public market data commands for prices, tickers, order books, candles, derivatives data, instrument discovery, market screening, and technical indicators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT

## Use Case:

External users, analysts, developers, and agents use this skill to retrieve OKX public market data and indicator values before analysis, reporting, or user-directed trading workflows. It is intended for data access and command guidance, not account management or order placement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented skill commands are read-only market data, but the installed global OKX CLI can also perform account and trading operations when credentials are configured.

Mitigation: Install and run the skill without trading credentials unless that broader capability is intended; use dedicated or demo OKX credentials for agent-accessible environments.

Risk: The installed package may download persistent helper executables into ~/.okx/bin.

Mitigation: Review package-level behavior before installation, prefer an isolated environment, and inspect downloaded helper executables before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-market)
- [OKX homepage](https://www.okx.com)
- [Price & Market Data Commands](references/price-data-commands.md)
- [Derivatives & Contract Data Commands](references/derivatives-commands.md)
- [Instrument Discovery Commands](references/instrument-commands.md)
- [Technical Indicator Command Reference](references/indicator-commands.md)
- [Cross-Skill Workflows & MCP Tool Reference](references/workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are documented as read-only market-data calls and do not require API credentials.]

## Skill Version(s):

1.4.4 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
