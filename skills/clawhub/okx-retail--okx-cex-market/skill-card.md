## Description:

Provides read-only OKX market prices, instrument data, derivatives metrics, and technical indicators without requiring API credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can retrieve public OKX prices, order books, candles, instrument listings, funding rates, open interest, and technical indicator values for market analysis. Account access and order placement are outside this skill's scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires a global installation of the OKX CLI.

Mitigation: Review and approve the CLI installation before using it for public market-data lookups.

Risk: Event-contract discovery appears in the command references despite the skill's market-data-only scope.

Mitigation: Route event-contract trading and order requests to the trading skill; do not use this skill to place orders or access accounts.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/okx-retail/skills/okx-cex-market)
- [OKX website](https://www.okx.com)
- [Price and market data commands](artifact/references/price-data-commands.md)
- [Derivatives and contract data commands](artifact/references/derivatives-commands.md)
- [Instrument discovery commands](artifact/references/instrument-commands.md)
- [Technical indicator commands](artifact/references/indicator-commands.md)
- [Cross-skill workflows](artifact/references/workflows.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Text or Markdown market-data summaries and tables; optional JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public, read-only queries; no API credentials required]

## Skill Version(s):

1.4.9 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
