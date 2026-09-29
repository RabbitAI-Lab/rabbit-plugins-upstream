## Description:

Compose an account grouping recipe from a supplied report request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

People preparing account reports use this skill to turn a specified segment, grouping, measure, calculation, and column selection into a report predicate. It does not fetch account data or produce a completed report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A report recipe may be mistaken for a completed account report or a general account-management tool.

Mitigation: Use it only for the documented report_request fields, and verify the predicate against the intended report before relying on it.

## Reference(s):

- [Account Report Recipe Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/account-group-report-identifier)

## Skill Output:

**Output Type(s):** [Configuration]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a report_predicate with where, group_by, aggregate, and projected_columns; does not query account records.]

## Skill Version(s):

1.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
