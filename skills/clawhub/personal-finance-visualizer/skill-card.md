## Description:

Turn user-provided personal finance records into a local interactive report with spending, income, transfers and cash movement in English or Chinese.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jasonhmy](https://clawhub.ai/user/jasonhmy)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals use this skill to turn authorized financial records into a local interactive report for reviewing spending, income, transfers, and cash movement. It is not for bank-account actions or investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial records and report links or exports may expose sensitive personal information.

Mitigation: Provide only records needed for the report, keep report links and exported HTML private, and stop the local server when finished.

## Reference(s):

- [Input schema](artifact/references/schema.md)
- [Workflow guidance](artifact/references/workflow.md)
- [ClawHub skill page](https://clawhub.ai/jasonhmy/skills/personal-finance-visualizer)
- [Repository listed in skill metadata (provenance unavailable)](https://github.com/JasonHMY/personal-finance-visualizer)

## Skill Output:

**Output Type(s):** [HTML, Visualizations, Text]

**Output Format:** [Interactive local HTML report, optionally exported as an HTML file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [English or Chinese; report contains sensitive financial details]

## Skill Version(s):

1.1.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
