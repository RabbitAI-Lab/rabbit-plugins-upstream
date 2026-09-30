## Description:

Searches Swedish property listings, sold prices, and local market statistics on Booli.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People researching Swedish real estate use this skill to find active listings, compare sold properties, and review area market statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional browser bridge requires installing and pairing an external extension to route requests through a Booli browser tab; the extension implementation is outside this skill's review.

Mitigation: Install only if comfortable with the bridge, limit its use to Booli, and verify its release or build it from source.

Risk: Market statistics based on a small sample may misrepresent the area.

Mitigation: Check the reported sample size before relying on median prices.

## Reference(s):

- [Booli skill on ClawHub](https://clawhub.ai/chrischall/skills/booli)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown or structured property results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices in SEK; floor areas in m²; listings are paginated.]

## Skill Version(s):

2.1.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
