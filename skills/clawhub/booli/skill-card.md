## Description:

Search and analyze Swedish real estate listings, sold prices, and area market statistics on Booli.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People researching Swedish property use this skill to find active listings, compare sold prices, and review local market statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser bridge requires an extension and a pairing approval to query Booli through an open tab.

Mitigation: Verify the ContextMint Bridge source or release checksum, limit the bridge to the Booli workflow, and approve pairing only when you intend to run a Booli query.

Risk: Market statistics can be misleading when based on a small page of sales.

Mitigation: Check the reported sample size and per-metric counts before drawing conclusions.

## Reference(s):

- [Booli skill on ClawHub](https://clawhub.ai/chrischall/skills/booli)
- [Booli property portal](https://www.booli.se)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Analysis]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only listing details, sold-price comparisons, and market summaries; prices in SEK and areas in m².]

## Skill Version(s):

2.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
