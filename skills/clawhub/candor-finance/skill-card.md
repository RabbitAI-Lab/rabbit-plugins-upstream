## Description:

Use Candor for personal finance to organize accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

External users with an authenticated Candor workspace use this skill through an agent to inspect financial records, maintain approved plans, identify savings or recovery opportunities, and preserve evidence-linked follow-up. It is intended for personal finance work that depends on continuity across accounts, transactions, decisions, and scheduled checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read sensitive financial records in an authenticated Candor workspace.

Mitigation: Install it only for users who want an agent to work with their Candor financial workspace, and keep financial details limited to the evidence needed for the current task.

Risk: The skill can create persistent notes, impacts, workspace corrections, and reversible transaction changes during bounded cleanup tasks.

Mitigation: Use explicit user authority for bounded work, confirm preference-bearing choices separately, and preserve evidence-linked follow-up for unfinished outcomes.

Risk: Background monitoring can run unattended scheduled financial checks.

Mitigation: Enable monitoring only after the user accepts a specific cadence and purpose, and keep monitoring silent unless something needs attention.

## Reference(s):

- [Candor OpenClaw getting started](https://candor.money/START.md?v=0.1.27)
- [ClawHub skill page](https://clawhub.ai/candor/skills/candor-finance)
- [Quiet monitoring recipes](artifact/references/monitoring.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with concise financial findings, bounded command recipes, and follow-up instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create persistent Candor notes, impacts, reversible workspace corrections, and scheduled monitoring when authorized.]

## Skill Version(s):

0.1.27 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
