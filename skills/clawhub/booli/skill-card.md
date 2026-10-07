## Description:

Search and analyze Swedish real estate on Booli, including active listings, sold prices, area matches, and market statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People researching Swedish property use this skill to find for-sale listings, inspect sold-price comparables, and summarize area market statistics on Booli.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional browser bridge requires installing an extension and pairing it with a Booli browser tab.

Mitigation: Review the extension source or verify its release checksum before installing, and approve pairing only for intended Booli queries.

Risk: Market medians based on few sold listings may be unrepresentative.

Mitigation: Check the reported sample size before relying on market statistics.

## Reference(s):

- [Booli skill on ClawHub](https://clawhub.ai/chrischall/skills/booli)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only property listings and market summaries; prices in SEK and areas in m².]

## Skill Version(s):

2.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
