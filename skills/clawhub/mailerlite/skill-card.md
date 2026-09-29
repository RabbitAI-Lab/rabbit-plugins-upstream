## Description:

Helps agents manage MailerLite subscribers, groups, campaigns, forms, and automations through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and developers use this skill to inspect MailerLite data and, with user confirmation, manage subscribers, groups, campaigns, and related workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account authorization or changes to subscribers and campaigns can affect live marketing data.

Mitigation: Authorize only with the user's approval, start with read/list requests, and confirm every write or campaign action.

Risk: Hosted automations, triggers, or webhooks can persistently forward data.

Mitigation: Confirm each deployment and persistent destination; use only hosts the user controls and understands.

## Reference(s):

- [MailerLite skill release](https://clawhub.ai/byungkyu/skills/mailerlite)
- [Maton homepage](https://maton.ai)
- [MailerLite API documentation](https://developers.mailerlite.com/docs/)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MailerLite API responses; share only fields needed for the user's task.]

## Skill Version(s):

1.2.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
