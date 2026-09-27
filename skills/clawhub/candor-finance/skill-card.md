## Description:

Use Candor to organize personal finances, review accounts and spending, investigate savings, and track approved plans and follow-up with supporting evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

People managing their own finances use this skill with an authenticated Candor workspace to review financial records, investigate potential savings, organize spending, and maintain user-approved budgets, goals, and follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated workspace access exposes sensitive financial records and allows internal records or notes to be changed.

Mitigation: Use only for user-directed tasks, confirm the scope of changes, and review the affected records.

Risk: Saved financial context or scheduled checks could persist beyond the current conversation.

Mitigation: Save only relevant context and schedule checks only when the user explicitly requests them.

Risk: Financial analysis based on incomplete or stale records may mislead decisions.

Mitigation: Check source coverage and freshness, distinguish estimates from verified amounts, and make uncertainty clear.

## Reference(s):

- [Candor setup and documentation](https://candor.money/START.md)
- [Candor Finance on ClawHub](https://clawhub.ai/candor/skills/candor-finance)
- [Setup and access](references/setup.md)
- [Evidence and financial records](references/evidence.md)
- [Continuity and financial memory](references/continuity.md)
- [Scheduled monitoring](references/monitoring.md)

## Skill Output:

**Output Type(s):** [Financial analysis, Guidance, Markdown]

**Output Format:** [Markdown text with supported findings and next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links to supporting Candor records and note approved follow-up.]

## Skill Version(s):

0.1.141 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
