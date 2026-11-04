## Description:

Opens the person's Candor workspace, says where their money stands, and routes to the right Candor workflow. Use when the person asks about their money, spending, balances, bills, debts, goals, or plans and no more specific Candor skill fits, including a quick question about a balance, a bill, or a charge, or a life decision that costs or earns money even when money is not named.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

People using Candor use this skill to understand their financial position and work through budgets, spending, debt, goals, recurring charges, tax preparation, and financial-record organization in their Candor workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may access financial records during indirectly related conversations and may retain personal details or change saved plans automatically.

Mitigation: Limit activation to explicit financial help and agree which personal notes and plan changes may be saved automatically.

Risk: The separate Candor CLI and service controls for retention, deletion, and proposal enforcement were not audited.

Mitigation: Keep financial exports in private temporary storage and remove them afterward; review the service's retention and deletion controls before relying on them.

## Reference(s):

- [Candor setup and usage](https://candor.money/START.md)
- [Candor Finance on ClawHub](https://clawhub.ai/candor/skills/candor-finance)
- [Access and recovery](references/access-and-recovery.md)
- [Reports](references/reports.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text, Markdown, JSON]

**Output Format:** [Conversational text and structured Markdown or JSON; may include Candor reports and chart summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated Candor workspace and Candor tools or CLI 0.3.165 or newer; service use requires an active subscription.]

## Skill Version(s):

1.3.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
