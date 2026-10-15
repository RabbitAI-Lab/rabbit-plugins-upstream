## Description:

Guides read-only retrieval and interpretation of Hyperliquid prices, order books, funding, market metadata, and research datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

Market analysts, developers, and other users query live Hyperliquid market data, prepare timestamped market briefs, and collect historical data for research without authorizing trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stale or incomplete market data can be mistaken for a current, complete view of liquidity or funding.

Mitigation: Identify the network, source, and UTC time; disclose depth and dataset coverage gaps and normalize funding rates by their stated interval.

Risk: Read-only API requests and optional local dataset saves can exceed the user's intended scope.

Mitigation: Use the expected Hyperliquid network and an approved output path; do not treat market data or doctor warnings as trading authorization or risk approval.

## Reference(s):

- [HyperGrok Hyperliquid Market Data on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-market-data)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown with optional shell and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Market figures identify their source, network, and UTC time; requested research bundles report coverage and verification status.]

## Skill Version(s):

1.6.1 (source: ClawHub release; bundled skill metadata says 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
