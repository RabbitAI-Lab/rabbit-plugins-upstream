## Description:

Helps agents read SAP Concur expense reports, line items, payment status, and unassigned expenses through the user's signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and their authorized agents use this skill to check Concur expense reports, reimbursement status, report entries, and expenses not yet assigned to a report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can access sensitive expense data through a live signed-in Concur session.

Mitigation: Install only if comfortable granting access to that session, and limit use to authorized expense data.

Risk: The custom GraphQL caller can run queries beyond the packaged read-only examples, potentially including changes to Concur data.

Mitigation: Use the packaged read queries unless a change is explicitly intended; review any custom GraphQL file before running it.

## Reference(s):

- [Concur FPX on ClawHub](https://clawhub.ai/chrischall/skills/concur-fpx)
- [Concur query recipes](references/recipes.md)
- [Concur operations reference](references/operations.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON]

**Output Format:** [Markdown guidance and JSON expense query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a paired browser extension and a signed-in Concur tab; packaged queries return report and expense data.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
