## Description:

Compose an account grouping recipe.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to turn an account reporting request into a grouping recipe with a segment filter, aggregate, and selected columns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changing the bundled role configuration could enable behavior outside the reviewed local report transformation.

Mitigation: Review the code and configuration before changing the role or output behavior.

## Reference(s):

- [Account Report Recipe Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/account-group-report-identifier)

## Skill Output:

**Output Type(s):** [Report configuration]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a report predicate with where, group_by, aggregate, and projected_columns; does not persist an artifact.]

## Skill Version(s):

1.1.1 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
