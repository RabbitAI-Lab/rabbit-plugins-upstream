## Description:

Opens the person's Candor workspace, says where their money stands, and routes to the right Candor workflow. Use when the person asks about their money, spending, balances, bills, debts, goals, or plans and no more specific Candor skill fits, including a quick question about a balance, a bill, or a charge, or a life decision that costs or earns money even when money is not named.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

People use this skill to review their finances in a Candor workspace, keep plans, records, and notes current, and route questions through focused budgeting, transaction, goal, tax-preparation, and check-in workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial summaries depend on the accuracy and coverage of the records in the Candor workspace.

Mitigation: Use a verified Candor CLI or included Candor tools, read current records and coverage, and state when the data limits a figure.

Risk: Rules can change matching past and future transactions, and saved corrections or plans can shape later reviews.

Mitigation: Preview rule reach, verify affected records after saving, and use the documented undo or revert path when a change is wrong.

Risk: External financial actions can have consequences beyond the workspace.

Mitigation: Get the person's request or approval before payments, transfers, cancellations, disputes, messages, applications, or trades.

## Reference(s):

- [Candor setup and usage guide](https://candor.money/START.md)
- [Candor Finance on ClawHub](https://clawhub.ai/candor/skills/candor-finance)
- [Candor workspace](https://app.candor.money)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, HTML reports]

**Output Format:** [Conversational guidance and summaries, Candor record updates, and optional HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated Candor workspace and the included Candor tools or Candor CLI 0.3.165 or newer.]

## Skill Version(s):

1.3.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
