## Description:

Use Candor for personal finance: organize the user's accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and their agents use this skill to work with a signed-in Candor financial workspace, inspect personal finance records, preserve approved plans, investigate savings or recovery opportunities, and keep evidence-linked follow-up together.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and update sensitive financial records in a Candor workspace.

Mitigation: Install only when this access is intended, keep work scoped to finance tasks, and preserve visible consent moments for account access, source connections, subscription changes, preference-bearing records, and external actions.

Risk: Optional background monitoring can create scheduled finance checks beyond a one-time conversation.

Mitigation: Keep monitoring off unless scheduled checks are desired, and use the skill's monitoring reference to keep each check bounded, evidence-linked, and reversible where applicable.

Risk: Credentials or payment details could be exposed if handled in chat.

Mitigation: Use Candor secure pages for account connection, credential repair, disconnection, subscription, and payment changes instead of collecting those details in the agent conversation.

## Reference(s):

- [Candor setup and OpenClaw materials](https://candor.money/START.md?v=0.1.53)
- [ClawHub skill page](https://clawhub.ai/candor/skills/candor-finance)
- [Monitoring reference](references/monitoring.md)
- [Financial review method](methods/candor-financial-review/METHOD.md)
- [Evidence capture method](methods/candor-evidence-capture/METHOD.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands and concise financial findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should cite observed records, dates, amounts, uncertainty, and practical limits; external financial actions require recoverable user authority.]

## Skill Version(s):

0.1.53 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
