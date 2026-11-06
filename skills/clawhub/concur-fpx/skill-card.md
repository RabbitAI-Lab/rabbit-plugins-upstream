## Description:

Read SAP Concur expense data from a shell — your expense reports, each report's line items (vendor, type, amounts, receipts, exceptions), and available expenses not yet on a report — through the user's signed-in Concur browser tab with the fpx CLI. Use when asked about Concur expenses, expense reports, reimbursement/payment status, what's unsubmitted, or unassigned card/receipt expenses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees who use SAP Concur can ask the agent to review expense reports, reimbursement or payment status, report line items, and expenses that have not yet been assigned to a report. It retrieves this information through the user's signed-in Concur browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser access and the unrestricted query runner exceed the skill's stated read-only limits.

Mitigation: Review browser permissions before installation and restrict the runner to approved queries before relying on read-only behavior.

Risk: Expense information returned by the skill may be sensitive.

Mitigation: Protect returned expense information and revoke the browser extension pairing when finished.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chrischall/skills/concur-fpx)
- [Concur recipes](references/recipes.md)
- [Concur spend-graphql operations](references/operations.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance]

**Output Format:** [GraphQL JSON responses, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.4.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
