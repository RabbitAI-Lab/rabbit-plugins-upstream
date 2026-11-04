## Description:

Score and tier a list of companies against user-specified ideal customer profile criteria, with an explanation and missing-data notes for each company.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations and sales development teams use this skill to prioritize company leads against a stated ideal customer profile before spending time or enrichment credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company lists, including an initial sample, are sent to Cargo and its enrichment provider.

Mitigation: Submit only lists you are comfortable sharing with those services.

Risk: A full enrichment run can consume credits across every company in the list.

Mitigation: Check the credit estimate before approval and use a small sample before a full run.

Risk: External package versions and optional skill collection behavior are not covered by the supplied artifact review.

Mitigation: Review package versions and the optional collection separately before use.

## Reference(s):

- [Cargo ICP discovery recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/icp-discovery.md)
- [ClawHub score-leads page](https://clawhub.ai/cargo-ai/skills/score-leads)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Markdown table with scores, tiers, reasons, and missing-data notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each company includes a score, reason, tier, and missing fields; companies with insufficient data remain unranked.]

## Skill Version(s):

1.0.3 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
