## Description:

Use Candor for personal finance: organize the user's accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and their agents use this skill to work with an authenticated Candor workspace for personal-finance review, organization, follow-up, and bounded record maintenance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read sensitive financial records when money-related tasks are in scope.

Mitigation: Install it only for an authenticated Candor workspace you intend the agent to use, and keep financial-source access changes on secure Candor pages.

Risk: The skill may persist bounded notes or corrections in the Candor workspace.

Mitigation: Use writebacks only for user-authorized organization, tracking, or follow-up, and keep uncertainty, evidence, and reversible scope explicit.

Risk: Quiet monitoring can run finance checks without an active chat session.

Mitigation: Enable background monitoring only after explicit opt-in to a cadence and purpose, and rely on the configured scheduler rather than Candor notes for recurrence state.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/candor/skills/candor-finance)
- [Candor OpenClaw Start](https://candor.money/START.md?v=0.1.67)
- [Quiet monitoring recipes](references/monitoring.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell-command recipes, concise financial findings, and bounded note or configuration artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated Candor workspace and Candor CLI 0.3.94 or newer; may read sensitive financial records and create bounded Candor notes or corrections when authorized.]

## Skill Version(s):

0.1.67 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
