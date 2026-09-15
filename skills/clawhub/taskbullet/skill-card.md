## Description:

Delegates user-approved last-mile work to TaskBullet virtual assistants for phone calls, physical-world actions, subjective QA, long manual work, and owner-authorized account steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[griffmurder](https://clawhub.ai/user/griffmurder)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to hand off tasks that need a human assistant, such as phone calls, manual QA, physical-world follow-up, or owner-authorized login and captcha steps. The skill is intended for accounts and workspaces the operator owns or is authorized to use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delegated work can spend prepaid TaskBullet hours.

Mitigation: Confirm the user's spending cap before submitting paid work and stop if the account cannot delegate.

Risk: Task descriptions are sent to a third-party human assistant service and may involve account access.

Mitigation: Delegate only work on accounts the operator owns or is authorized to use, and never include passwords, OTP codes, recovery keys, session cookies, or API keys in task fields.

Risk: Exposed API keys could allow unauthorized TaskBullet use.

Mitigation: Keep TASKBULLET_API_KEY only in Gateway environment settings and never paste it into chat, task descriptions, or shared rooms.

## Reference(s):

- [TaskBullet Agent API documentation](https://taskbullet.com/docs/agent-api.md)
- [ClawHub TaskBullet skill page](https://clawhub.ai/griffmurder/skills/taskbullet)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline configuration, command examples, and task handoff text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return TaskBullet task IDs, balance information, task status, and completed task results.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
