## Description:

邮件日报专业版 helps agents aggregate multiple mailbox accounts, summarize and classify email, schedule digest reports, and push alerts through configured channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, teams, and developers use this skill to generate daily email digests, classify important messages, configure scheduled reports, and route alerts to approved notification channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive email content through logged-in browser sessions and external push channels.

Mitigation: Use only mailboxes and push channels you control, avoid broad browser-session access where possible, and minimize or redact report content before sending.

Risk: Scheduled pushes and alerts can send email summaries to unintended destinations.

Mitigation: Confirm every scheduled report, alert rule, webhook, and recipient before enabling automated delivery.

Risk: Command execution and scheduling increase operational impact if commands or destinations are misconfigured.

Mitigation: Review proposed commands and schedules before execution and keep them scoped to the intended mailbox, report path, and notification channel.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/email-digest)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce email digest reports in text, HTML, or Markdown and notification-channel configuration guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
