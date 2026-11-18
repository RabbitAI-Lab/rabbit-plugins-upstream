## Description:

Opens the person's Candor workspace, says where their money stands, and routes to the right Candor workflow. Use when the person asks about their money, spending, balances, bills, debts, goals, or plans and no more specific Candor skill fits, including a quick question about a balance, a bill, or a charge, or a life decision that costs or earns money even when money is not named.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT No Attribution

## Use Case:

People using an authenticated Candor workspace use this skill to understand their finances, answer questions about spending, balances, bills, and debt, and route goals, budgeting, transaction sorting, checkups, tax preparation, and record imports to the relevant workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial records may be saved locally, and the skill may make many finance-related changes without asking each time.

Mitigation: Review the workflow's save behavior before use, and use it only where local storage of raw financial records is acceptable.

Risk: Security analysis was partial, so the scan does not establish that all skill content is safe.

Mitigation: Review the current package contents before use, especially when the release has changed.

## Reference(s):

- [Candor setup guide](https://candor.money/START.md)
- [Candor Finance on ClawHub](https://clawhub.ai/candor/skills/candor-finance)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text, Shell commands]

**Output Format:** [Conversational text and Markdown, with Candor CLI commands where needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Grounded in the connected Candor workspace and its records; may summarize changes saved to the workspace.]

## Skill Version(s):

1.3.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
