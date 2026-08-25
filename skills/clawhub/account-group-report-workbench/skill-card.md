## Description:

Build a grouped account report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and agents use this skill to create routine grouped account reports from a supplied report predicate. It groups, aggregates, and projects account data supplied in the current request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated account summaries may be inaccurate if the supplied report predicate or account data is incomplete, stale, or incorrect.

Mitigation: Review the generated report for business accuracy before using it for decisions.

Risk: Account report requests may include more business data than needed for the requested grouping.

Mitigation: Provide only the account data needed for the requested report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/account-group-report-workbench)
- [Publisher profile: wxt-ai](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, markdown]

**Output Format:** [Concise grouped account report with report_id, groups, row_count, and projected_columns.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses only the report_predicate and account data supplied in the current request.]

## Skill Version(s):

1.0.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
