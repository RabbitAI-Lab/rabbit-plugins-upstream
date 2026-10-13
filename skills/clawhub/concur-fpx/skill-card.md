## Description:

Reads expense reports, report line items, reimbursement status, and unassigned expenses from the user's signed-in SAP Concur session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees can ask an agent to review their Concur expense reports, line items, payment status, and expenses not yet assigned to a report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser bridge can access expense data in the user's signed-in Concur session.

Mitigation: Install and pair only if this session access is acceptable; limit access to an authorized Concur account.

Risk: A custom GraphQL document passed to the helper could include mutations that change Concur data, despite the packaged queries being read-oriented.

Mitigation: Review custom GraphQL documents before execution and use the packaged read queries for routine expense lookups.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/concur-fpx)
- [Concur query recipes](references/recipes.md)
- [Concur operation reference](references/operations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Natural-language summaries or tables, optionally with shell commands and query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an open, signed-in Concur browser tab; packaged queries do not retrieve receipt images or travel itineraries.]

## Skill Version(s):

0.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
