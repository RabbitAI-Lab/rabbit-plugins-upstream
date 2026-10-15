## Description:

Helps agents search and analyze Swedish property listings, sold prices, market statistics, and mortgage costs using Hemnet data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People researching Swedish housing use this skill to find and compare active and sold properties, examine local sale prices, and estimate monthly mortgage costs.

### Deployment Geography for Use:

Global (Swedish property data)

## Known Risks and Mitigations:

Risk: Broad Swedish housing terms may activate the skill for requests that do not need Hemnet data.

Mitigation: Specify when Hemnet data is not needed for unrelated housing advice.

Risk: Market statistics sample only recent matching sales and may be misleading with small samples.

Mitigation: Check the sample size and compare sampled sales with total matching sales before drawing conclusions.

Risk: Mortgage calculations are estimates based on the stated Swedish rules and inputs.

Mitigation: Check current terms and borrowing costs before relying on an estimate for a purchase decision.

## Reference(s):

- [Hemnet skill release on ClawHub](https://clawhub.ai/chrischall/skills/hemnet)
- [Hemnet property portal](https://hemnet.se)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown or text with property details, comparisons, statistics, and calculations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices in SEK; areas in m²; listing photos may be provided as URLs.]

## Skill Version(s):

1.1.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
