## Description:

Helps users explore Swedish property listings, sold prices, market statistics, and mortgage costs using Hemnet data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People researching Swedish homes can find and compare active listings and sold-price comparables, review local market statistics, and estimate monthly mortgage costs.

### Deployment Geography for Use:

Sweden (property data and mortgage estimates)

## Known Risks and Mitigations:

Risk: Broad Swedish-property requests may trigger Hemnet-specific analysis when it is not wanted.

Mitigation: Specify the desired data source or limit the request to the relevant property question.

Risk: Small sold-listing samples can give misleading local price statistics.

Mitigation: Check sample size before relying on medians or price-per-square-metre figures.

Risk: An address search that reaches its listing limit may miss a matching home.

Mitigation: If the search reports truncation, narrow it with price filters before treating a miss as definitive.

## Reference(s):

- [Hemnet skill release on ClawHub](https://clawhub.ai/chrischall/skills/hemnet)
- [Hemnet property portal](https://hemnet.se)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Property prices in SEK; areas in m².]

## Skill Version(s):

1.1.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
