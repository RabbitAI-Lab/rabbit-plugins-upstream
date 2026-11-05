## Description:

Opens the person's Candor workspace, says where their money stands, and routes to the right Candor workflow. Use when the person asks about their money, spending, balances, bills, debts, goals, or plans and no more specific Candor skill fits, including a quick question about a balance, a bill, or a charge, or a life decision that costs or earns money even when money is not named.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

People using Candor and their AI assistants use this skill to review current financial records, answer money questions, and handle follow-up work such as budgeting, goal planning, bill and debt reviews, transaction organization, financial checkups, and tax preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may open financial records for ambiguous life questions and may leave sensitive local copies without clear storage or cleanup rules.

Mitigation: Activate it only for explicit financial requests or established financial context. For local analysis, use private temporary storage and delete raw pages and snapshots afterward.

Risk: The external CLI, hosted service, and their runtime protections were outside this review.

Mitigation: Review those components' protections before deployment. Review saved plans and rules, and give scheduled checks a clear scope and stopping point.

## Reference(s):

- [Candor setup and usage guide](https://candor.money/START.md)
- [Candor Finance release on ClawHub](https://clawhub.ai/candor/skills/candor-finance)
- [Reading Candor records](references/reading-records.md)
- [Candor reports](references/reports.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text, Markdown]

**Output Format:** [Concise conversational text, often with Markdown lists or comparison tables; optional Candor visual panels.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses figures from the person's Candor records; may create saved plans, notes, or reports in Candor.]

## Skill Version(s):

1.3.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
