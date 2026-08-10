## Description:

This skill helps agents configure one-time reminders, recurring cron jobs, and background automation in SkillHub Gateway, including session targeting, delivery channels, and execution logs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and automation users use this skill to set up scheduled agent tasks such as reminders, recurring summaries, project reports, and cron-based background workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scheduled background jobs may run repeatedly or in isolated sessions without sufficient review.

Mitigation: Review each job before enabling it, including schedule, timezone, session target, prompt content, retry behavior, and whether it should be deleted after running.

Risk: Job results can be delivered to Telegram, WhatsApp, webhooks, or other external channels.

Mitigation: Confirm the recipient, retention expectations, and data sensitivity before sending email, calendar, project, credential, personal, or operational data to external channels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cron-scheduler-setup)
- [SkillHub skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cron expressions, timezone settings, session targeting, delivery channel settings, and execution log paths.]

## Skill Version(s):

1.0.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
