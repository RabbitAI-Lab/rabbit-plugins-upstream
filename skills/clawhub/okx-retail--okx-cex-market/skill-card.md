## Description:

Provides read-only OKX market data and technical indicator queries through the OKX CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT-0

## Use Case:

External users can query public OKX prices, order books, candles, derivatives data, instrument listings, and technical indicators. The skill returns market information and does not place trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup and automatic software updates are not sufficiently scoped, leaving account access and version changes unclear.

Mitigation: Request a bundled, version-matched preflight that permits public-data use without login or credential-profile checks, keep upgrades user-controlled, and pin the CLI version.

## Reference(s):

- [OKX Market Data Skill](https://clawhub.ai/okx-retail/skills/okx-cex-market)
- [OKX](https://www.okx.com)
- [Price & Market Data Commands](references/price-data-commands.md)
- [Derivatives & Market Data Workflows](references/derivatives-commands.md)
- [Instrument Discovery Commands](references/instrument-commands.md)
- [Technical Indicator Command Reference](references/indicator-commands.md)
- [Cross-skill Workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Readable market-data tables, indicator values, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public market information; commands do not place trades.]

## Skill Version(s):

1.5.0 (source: skill frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
