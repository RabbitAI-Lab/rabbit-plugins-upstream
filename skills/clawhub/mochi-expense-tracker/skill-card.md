## Description:

Log income, spending and refunds through conversation, summarize by currency and category, and track monthly budgets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and households can use this skill to record income, expenses, and refunds, review summaries by category and currency, and track monthly budgets through conversation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workspace ledger contains unencrypted financial records, including voided entries.

Mitigation: Restrict access to the workspace and protect and back up its financial records.

Risk: Financial details shared in conversation are available to the configured agent and model.

Mitigation: Share only information appropriate for the configured agent and model to process.

## Reference(s):

- [Input contract](references/input.md)
- [MochiLab website](https://mochilab.bz)
- [ClawHub skill release](https://clawhub.ai/hznetnewpower/skills/mochi-expense-tracker)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Concise conversational summaries and structured JSON operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Amounts use integer minor units, and summaries keep currencies separate.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
