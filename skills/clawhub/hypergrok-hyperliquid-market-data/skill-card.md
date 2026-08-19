## Description:

Read live Hyperliquid market data from the desk computer with curl or the Python SDK - mid, mark and oracle prices, order book depth, funding (current, predicted, historical), open interest, volume, candles, perp and spot metadata, margin tiers, and how to save datasets for the strategy lab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and developers use this skill to retrieve read-only Hyperliquid market data for market briefs, depth reads, funding questions, metadata checks, and local dataset preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public market data can become stale quickly, especially order book and depth snapshots.

Mitigation: Report the request type, network, and UTC fetch time with figures, and refresh snapshots before making time-sensitive decisions.

Risk: The skill may guide an agent to issue public Hyperliquid API requests and optionally save CSV files locally.

Mitigation: Review commands before execution, keep usage read-only, and confirm local output paths before saving datasets.

Risk: Funding-rate comparisons can be misleading when venues use different funding intervals.

Mitigation: Convert rates to a common time basis and disclose the formula before comparing venues.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-market-data)
- [Hyperliquid mainnet API endpoint](https://api.hyperliquid.xyz)
- [Hyperliquid testnet API endpoint](https://api.hyperliquid-testnet.xyz)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline bash and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local CSV dataset paths when the agent follows the dataset-saving workflow.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
