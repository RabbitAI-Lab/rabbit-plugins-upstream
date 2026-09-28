## Description:

Compose grouping recipes and build grouped account reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Business users or agents performing account reporting use this skill to compose account grouping recipes and build grouped account reports from supplied report criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account reporting inputs or outputs may include sensitive or inappropriate account data for the intended workflow.

Mitigation: Confirm the backing account-reporting tools and only provide account data appropriate for this reporting workflow.

Risk: Incorrect grouping criteria or aggregates could produce misleading account reports.

Mitigation: Review the report_request, report_predicate, grouping field, aggregate, and projected columns before using the report in business decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/account-group-reporting-desk)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Structured JSON-like objects returned as concise text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces report_predicate and group_report objects for grouped account reporting.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
