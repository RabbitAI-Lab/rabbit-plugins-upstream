## Description:

Helps agents read SAP Concur expense reports, line items, payment status, and unassigned expenses through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and their agents use this skill to look up Concur expense reports, reimbursement status, report line items, and expenses not yet assigned to a report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can access sensitive expense and session data through the signed-in Concur browser.

Mitigation: Pair only in the browser holding the intended Concur session, protect returned expense data, and clear the fpx trust and profile when no longer needed.

Risk: A custom GraphQL mutation file could create, submit, change, or delete real Concur records.

Mitigation: Use the bundled read-only queries for lookup; run custom mutations only when intentionally making changes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/concur-fpx)
- [Concur query recipes](artifact/references/recipes.md)
- [Concur operation reference](artifact/references/operations.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Plain text or Markdown; query results are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only bundled queries; requires a signed-in Concur browser session]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
