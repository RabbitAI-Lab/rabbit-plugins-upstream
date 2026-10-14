## Description:

Search and analyze Swedish property listings, sold prices, areas, and market statistics from Booli.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People researching Swedish real estate use this skill to find active listings, compare recorded sale prices, and review area-level market statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Booli access requires installing and pairing an external browser bridge with an open Booli tab.

Mitigation: Install only if comfortable with the extension; verify its source or release checksum and approve pairing deliberately.

Risk: A market median based on a single page or a small metric sample may misrepresent the wider area.

Mitigation: Check pagination, total matching sales, and each metric's sample count before drawing conclusions.

## Reference(s):

- [booli on ClawHub](https://clawhub.ai/chrischall/skills/booli)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Analysis]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices in SEK and property areas in m²; market statistics cover a page of matching sales and include per-metric sample counts.]

## Skill Version(s):

2.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
