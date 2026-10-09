## Description:

Guides agents in reading public Hyperliquid prices, order books, funding, candles, and market metadata without trading credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Market analysts and developers use this skill to gather public Hyperliquid market data for briefs, depth and funding analysis, and optional local datasets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional examples can write market data to local CSV files.

Mitigation: Run exports only where the output path and data retention are acceptable.

Risk: Market snapshots can become stale or be confused across networks.

Mitigation: Record the source, network, and UTC time; refresh data before relying on it.

## Reference(s):

- [HyperGrok Hyperliquid Market Data on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-market-data)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Files]

**Output Format:** [Markdown guidance with shell and Python examples; optional CSV datasets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Market figures should identify their source, network, and UTC time.]

## Skill Version(s):

1.5.0 (source: ClawHub release; artifact frontmatter lists 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
