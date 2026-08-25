## Description:

Compose an account grouping recipe.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and analysts use this skill to convert an account report request into a concise grouping predicate with filters, grouping, aggregation, and projected columns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated report predicates may be incorrect or too broad for a business reporting workflow.

Mitigation: Review the where, group_by, aggregate, and projected_columns fields before using the predicate in reports.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wxt-ai/skills/account-group-report-identifier)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Structured report_predicate object with where, group_by, aggregate, and projected_columns fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the current request's report_request input and does not require credentials or private-file access.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
