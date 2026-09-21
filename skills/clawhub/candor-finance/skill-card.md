## Description:

Use Candor for personal finance: organize the user's accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to operate an authenticated Candor personal-finance workspace: review accounts, spending, budgets, goals, investments, bills, evidence, and follow-up while keeping financial answers grounded in scoped records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive personal-finance records and save internal Candor notes, rules, corrections, budgets, goals, schedules, and follow-ups.

Mitigation: Install and use it only for authenticated Candor personal-finance work, and keep changes scoped to the authority the user gives for the current task.

Risk: Financial conclusions can be misleading when account coverage, freshness, source records, or pagination are incomplete.

Mitigation: Ground answers in scoped Candor records and server calculations, state uncertainty, and inspect relevant records before presenting conclusions or confirming changes.

Risk: Rates, terms, benefits, and tax rules may be stale or may not apply to the user's situation.

Mitigation: Verify material current terms from authoritative sources and preserve source, applicability, and date context before using them in recommendations.

Risk: Personal-finance workflows could be mistaken for authority to perform external actions.

Mitigation: Keep external payments, transfers, trades, filings, benefit elections, cancellations, credential entry, and subscription or payment changes outside the workflow unless separately authorized through the appropriate secure channel.

## Reference(s):

- [Candor Start](https://candor.money/START.md)
- [ClawHub candor-finance skill page](https://clawhub.ai/candor/skills/candor-finance)
- [Evidence handling](references/evidence.md)
- [Setup and access](references/setup.md)
- [Continuity](references/continuity.md)
- [Scheduling](references/monitoring.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise recommendations, supported financial facts, assumptions, follow-up notes, and inline shell command execution when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and update authenticated Candor workspace records when the user authorizes the task; external payments, trades, filings, elections, cancellations, credential entry, and subscription or payment changes remain outside the agent workflow or require separate user authority.]

## Skill Version(s):

0.1.115 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
