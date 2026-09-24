## Description:

Use Candor for personal finance to organize accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

External users with an authenticated Candor workspace use this skill to ask an agent to analyze personal financial records, preserve approved financial context, make authorized workspace updates, and prepare grounded recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive personal-finance records and may persist notes, approved financial state, and scheduled checks.

Mitigation: Install only when the user trusts Candor with this data, keep work scoped to the authenticated workspace, and preserve evidence, dates, uncertainty, and user authority in financial answers.

Risk: Authorized workspace writes could record incorrect budgets, goals, categorization, or follow-up if evidence is stale or incomplete.

Mitigation: Make changes only within the user's authority, verify the effective result after write actions, and retain a way to undo or correct internal workspace updates.

Risk: Financial actions outside Candor, including money movement, filings, elections, credential entry, and subscription changes, carry higher user-control and authorization requirements.

Mitigation: Keep those actions outside the skill, use separate secure user-controlled flows, and require fresh explicit authority before treating external action as intended.

## Reference(s):

- [Candor setup and access](https://candor.money/START.md)
- [Evidence handling](references/evidence.md)
- [Setup and access](references/setup.md)
- [Continuity](references/continuity.md)
- [Scheduling and monitoring](references/monitoring.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command recipes and financial-answer structure]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated Candor workspace and Candor CLI >=0.3.136 <0.4.0; financial claims should stay grounded in scoped records, server calculations, dates, and visible uncertainty.]

## Skill Version(s):

0.1.132 (source: ClawHub release metadata, released 2026-09-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
