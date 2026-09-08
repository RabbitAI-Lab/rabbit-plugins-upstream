## Description:

Use Candor for personal finance: organize the user's accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to work with an authenticated Candor workspace for personal-finance review, record organization, budgeting, goals, evidence tracking, and follow-up. It helps agents inspect financial records, preserve approved decisions, and identify bounded next steps while keeping high-impact external actions behind separate user authority.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent access to an authenticated personal-finance workspace.

Mitigation: Install it only when the user wants ongoing agent support for that Candor workspace and keep account access, source connections, subscriptions, and external actions as visible consent moments.

Risk: Bounded cleanup can create or disable rules that affect past and future financial records.

Mitigation: Review cleanup requests carefully, limit changes to the requested scope, and verify the after-state or recovery path before treating the work as complete.

Risk: Background monitoring can run scheduled unattended checks of financial workspace data.

Mitigation: Enable monitoring only after explicit user approval and make the monitored condition, cadence, stopping point, and notification conditions clear.

## Reference(s):

- [Candor Finance Start](https://candor.money/START.md?v=0.1.66)
- [ClawHub Skill Page](https://clawhub.ai/candor/skills/candor-finance)
- [Quiet monitoring recipes](references/monitoring.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and concise text with shell commands or configuration snippets when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include exact amounts, dates, uncertainty, evidence references, follow-up notes, and user-authority boundaries.]

## Skill Version(s):

0.1.66 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
