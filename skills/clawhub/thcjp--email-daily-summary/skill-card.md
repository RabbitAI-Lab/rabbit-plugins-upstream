## Description:

基于 browser-use 自动登录多邮箱，抓取当日邮件生成邮件摘要与统计日报，支持定时调度和跨账号汇总。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to automate daily webmail review, summarize important messages, collect mailbox statistics, and produce Markdown email reports across one or more accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automates sensitive webmail sessions and may expose mailbox metadata or screenshots if outputs are stored carelessly.

Mitigation: Use a private output directory, limit retention, avoid logging message bodies or credentials, and review generated reports before sharing.

Risk: The workflow can reuse a logged-in browser session to access email accounts.

Mitigation: Install only when comfortable granting the agent that access, keep two-factor verification human-controlled, and review scheduled cron or launchd jobs before enabling them.

Risk: The artifact advertises anti-crawler bypass behavior for some webmail services.

Mitigation: Avoid anti-bot or anti-crawler bypass use and comply with each mail provider's terms and security controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/email-daily-summary)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration instructions, Files, Guidance]

**Output Format:** [Markdown reports with inline shell commands and local screenshot files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate dated local summaries and inbox screenshots when the agent executes the suggested browser-use workflow.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
