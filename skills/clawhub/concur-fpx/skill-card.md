## Description:

Read SAP Concur expense data from a shell — your expense reports, each report's line items (vendor, type, amounts, receipts, exceptions), and available expenses not yet on a report — through the user's signed-in Concur browser tab with the fpx CLI. Use when asked about Concur expenses, expense reports, reimbursement/payment status, what's unsubmitted, or unassigned card/receipt expenses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees use this skill to review their Concur expense reports, line items, reimbursement status, and expenses that have not yet been assigned. It reads through the user's signed-in Concur browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser pairing grants reusable access to the user's signed-in Concur account, and the read-only claim is not an enforced boundary against mutations.

Mitigation: Before installing, require an allowlist of the bundled queries or equivalent protection against mutations, and understand that browser pairing grants reusable access to the signed-in Concur account.

## Reference(s):

- [Concur query recipes](references/recipes.md)
- [Concur operations reference](references/operations.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown]

**Output Format:** [GraphQL JSON data and concise text or Markdown expense summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expense data may include report and line-item details, available expenses, statuses, amounts, vendors, and receipt indicators.]

## Skill Version(s):

0.3.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
