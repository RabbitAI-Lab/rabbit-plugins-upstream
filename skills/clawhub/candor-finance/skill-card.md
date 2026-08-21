## Description:

Use Candor for personal finance: organize the user's accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to work with an authenticated Candor finance workspace for budgeting, cash flow, recurring bills, money recovery, income checks, benefits, tax preparation, investment-fee review, and evidence-backed follow-up. It helps the agent inspect financial records, preserve approved plans, and answer with exact amounts, dates, uncertainty, and next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill operates on sensitive personal-finance data through an authenticated Candor workspace and CLI.

Mitigation: Install and use it only when the user is comfortable giving Candor and its CLI ongoing access to the relevant financial workspace.

Risk: Durable corrections, rules, recurring policies, or notes can affect future finance reviews.

Mitigation: Apply durable changes only within the user's task-scoped authority, preserve evidence links, keep changes reversible where possible, and review affected records after writing.

Risk: Background monitoring can create ongoing access and follow-up behavior beyond the immediate conversation.

Mitigation: Configure monitoring only after the user explicitly accepts a cadence and purpose, verify the recurrence once, and avoid storing scheduler state in finance notes.

Risk: Financial rates, terms, deadlines, tax rules, and product limits can become stale or depend on the user's circumstances.

Mitigation: Use current authoritative sources when workspace records do not establish a material fact, and preserve retrieval date, applicability, and caveats.

## Reference(s):

- [Candor getting started](https://candor.money/START.md?v=0.1.29)
- [ClawHub skill listing](https://clawhub.ai/candor/skills/candor-finance)
- [Quiet monitoring recipes](references/monitoring.md)
- [Financial review method](methods/candor-financial-review/METHOD.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell command examples and finance-method recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce evidence-backed findings, bounded next steps, durable Candor notes or records, and monitoring configuration when authorized.]

## Skill Version(s):

0.1.29 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
