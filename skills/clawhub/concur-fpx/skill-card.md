## Description:

Helps an agent read the signed-in user's SAP Concur expense reports, line items, and unassigned expenses through their browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees can ask an agent to review their own Concur reports, reimbursement status, line items, and expenses not yet assigned to a report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive expense details from the user's signed-in Concur session.

Mitigation: Use it only for explicit Concur requests and limit sharing of returned financial details.

Risk: The browser pairing and profile may remain trusted after a request ends.

Mitigation: Clear the fpx trust pairing when access is no longer needed, and review future extensions before enabling writes.

## Reference(s):

- [Concur FPX release on ClawHub](https://clawhub.ai/chrischall/skills/concur-fpx)
- [Expense query recipes](references/recipes.md)
- [Concur operation reference](references/operations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown text with optional shell commands and expense summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only access to the signed-in user's expense data; no report changes or receipt-image downloads.]

## Skill Version(s):

0.3.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
