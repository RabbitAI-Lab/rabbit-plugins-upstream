## Description:

Use Candor for personal finance: organize the user's accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

People using an authenticated Candor workspace use this skill to have an agent investigate, organize, and maintain personal financial records, budgets, goals, recurring bills, investment evidence, and follow-up. It is intended for finance tasks grounded in the user's Candor data and approved authority.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may access sensitive personal financial records through an authenticated Candor workspace.

Mitigation: Use the skill only for explicit finance tasks and keep the requested scope clear before allowing workspace reads.

Risk: The skill can create or change internal financial records, notes, budgets, goals, recurring schedules, and follow-up state when authority is granted.

Mitigation: Ask the agent to confirm scope before record-changing or recurring work, and require it to inspect the effective result after any authorized change.

Risk: Raw financial pages or command output may contain private financial details if retained outside the workspace.

Mitigation: Avoid retaining raw JSON financial pages outside a private temporary location; share only bounded counts, aggregates, and necessary candidate records.

Risk: Local shell execution through the Candor CLI expands operational impact beyond passive guidance.

Mitigation: Review commands before installation and keep shell use tied to authenticated Candor operations needed for the user's explicit task.

## Reference(s):

- [Candor setup and start](https://candor.money/START.md)
- [ClawHub skill page](https://clawhub.ai/candor/skills/candor-finance)
- [Evidence handling](references/evidence.md)
- [Setup and access](references/setup.md)
- [Continuity](references/continuity.md)
- [Scheduled work](references/monitoring.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or concise text with referenced commands and financial evidence summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include supported amounts, dates, assumptions, uncertainty, record links, planned follow-up, and reversible workspace changes when authorized.]

## Skill Version(s):

0.1.114 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
