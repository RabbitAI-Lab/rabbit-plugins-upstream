## Description:

Read SAP Concur expense data from a shell — your expense reports, each report's line items (vendor, type, amounts, receipts, exceptions), and available expenses not yet on a report — through the user's signed-in Concur browser tab with the fpx CLI. Use when asked about Concur expenses, expense reports, reimbursement/payment status, what's unsubmitted, or unassigned card/receipt expenses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees can use the skill to retrieve their Concur expense reports, report line items, and expenses not yet assigned to a report, including reimbursement status and receipt-related details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private expense details may enter the agent's context when the skill reads Concur data.

Mitigation: Approve only the intended Concur profile in the browser and handle the resulting context as private financial information.

Risk: Custom GraphQL query files are not technically restricted to read operations.

Mitigation: Prefer the bundled queries and review any custom query before running it.

## Reference(s):

- [Concur Fpx release](https://clawhub.ai/chrischall/skills/concur-fpx)
- [Concur recipes](references/recipes.md)
- [Concur spend-graphql operations](references/operations.md)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [GraphQL JSON, which can be filtered or formatted as text and tables with jq]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the signed-in user's Concur data and requested query.]

## Skill Version(s):

0.3.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
