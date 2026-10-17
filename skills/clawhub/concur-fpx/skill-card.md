## Description:

Reads SAP Concur expense reports, line items, and unassigned expenses through the user's signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and their agents can look up Concur expense reports, reimbursement status, report line items, and unassigned expenses from a signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill accesses Concur through a live authenticated browser session.

Mitigation: Review before installing, and keep the paired browser and session under your control.

Risk: Custom GraphQL operations are not technically restricted to read-only access and could modify Concur data.

Mitigation: Use only the supplied read-only queries for expense lookups; avoid custom GraphQL files unless you understand whether they can write data.

## Reference(s):

- [Concur FPX on ClawHub](https://clawhub.ai/chrischall/skills/concur-fpx)
- [Concur query recipes](references/recipes.md)
- [Concur operations reference](references/operations.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text or Markdown summaries of JSON expense data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report status, amounts, receipts, and line items depend on the signed-in user's access.]

## Skill Version(s):

0.3.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
