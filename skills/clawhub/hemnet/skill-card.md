## Description:

Helps users search and analyze Swedish property listings, sold prices, market statistics, and mortgage costs using Hemnet data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People exploring Swedish property can find and compare homes, review sold-price comparables and local statistics, and estimate Sweden-specific mortgage costs.

### Deployment Geography for Use:

Sweden

## Known Risks and Mitigations:

Risk: Searches may send locations or addresses to Hemnet's public API.

Mitigation: Avoid entering sensitive address information unless the user agrees to the lookup.

Risk: Mortgage estimates follow Swedish conventions and are not personalized financial advice.

Mitigation: Treat estimates as illustrative and confirm current terms and eligibility with a qualified lender.

Risk: Thin sold-price samples or truncated address searches may mislead comparisons or omit matching homes.

Mitigation: Check sample sizes and truncation flags; narrow or repeat searches before drawing conclusions.

## Reference(s):

- [Hemnet skill release](https://clawhub.ai/chrischall/skills/hemnet)
- [Hemnet property portal](https://www.hemnet.se/)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Text or Markdown with property details, comparisons, statistics, and cost estimates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices and monthly costs in SEK; areas in m².]

## Skill Version(s):

1.1.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
