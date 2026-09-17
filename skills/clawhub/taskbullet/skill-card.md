## Description:

Delegate last-mile human work to TaskBullet virtual assistants on accounts the operator owns and authorized.

This skill is ready for commercial/non-commercial use.

## Publisher:

[griffmurder](https://clawhub.ai/user/griffmurder)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to delegate approved phone calls, physical-world actions, subjective QA, long manual work, and owner-authorized login or captcha steps to TaskBullet virtual assistants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Task descriptions may expose passwords, OTP codes, recovery keys, session cookies, or API keys.

Mitigation: Keep secrets out of chat and delegated task fields; have the human enter required codes in their own authorized session.

Risk: Delegated work can spend prepaid TaskBullet hours.

Mitigation: Confirm the spend cap with the human before delegation and stop when additional approval is needed.

Risk: Delegation could be requested for account takeover or work on accounts the operator does not own.

Mitigation: Confirm account ownership for login or captcha tasks and refuse account takeover, credential stuffing, and work on someone else's account.

## Reference(s):

- [TaskBullet Agent API documentation](https://taskbullet.com/docs/agent-api.md)
- [TaskBullet skill page](https://clawhub.ai/griffmurder/skills/taskbullet)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Markdown]

**Output Format:** [Markdown guidance with inline commands, configuration snippets, and TaskBullet task identifiers or task status results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require TASKBULLET_API_KEY and prepaid TaskBullet hours before delegation.]

## Skill Version(s):

1.0.9 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
