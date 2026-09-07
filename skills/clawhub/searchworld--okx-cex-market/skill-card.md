## Description:

Provides read-only OKX public market data commands for prices, tickers, order books, candles, funding rates, open interest, instrument discovery, market screening, pair spreads, and technical indicators without requiring API credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to retrieve OKX public market data, discover instruments, inspect derivatives metrics, and compute objective technical indicator values before making their own decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flagged a suspicious verdict due to an unpinned global CLI install and inconsistent event-contract scope.

Mitigation: Prefer a pinned or local install of @okx_ai/okx-trade-cli@1.4.6, review the package contents before installation, and keep event-contract trading routed to the appropriate trade skill.

Risk: Market data and indicator values may be mistaken for trading recommendations.

Mitigation: Treat outputs as raw market data only; do not provide credentials or use this skill for account access, order placement, strategy, recommendation, or optimization logic.

## Reference(s):

- [OKX homepage](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-market)
- [Price & Market Data Commands](artifact/references/price-data-commands.md)
- [Derivatives & Contract Data Commands](artifact/references/derivatives-commands.md)
- [Instrument Discovery Commands](artifact/references/instrument-commands.md)
- [Technical Indicator Command Reference](artifact/references/indicator-commands.md)
- [Cross-Skill Workflows & MCP Tool Reference](artifact/references/workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public market data; commands can emit raw OKX API v5 JSON with --json.]

## Skill Version(s):

1.4.6 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
