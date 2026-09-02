## Description:

Fetches GitHub Trending repositories daily, filters by language or time range, and optionally pushes summaries to Telegram, DingTalk, or WeCom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[monaxamo](https://clawhub.ai/user/monaxamo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical teams use this skill to monitor GitHub Trending projects and receive scheduled summaries through their chosen notification channel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Notification credentials or webhook URLs may be exposed if users paste real secrets into shell history, cron entries, or shared configuration.

Mitigation: Store Telegram tokens, chat IDs, and webhook URLs securely, and avoid placing live credentials directly in shell history or shared cron files.

Risk: GitHub Trending summaries may be sent to the wrong external notification channel.

Mitigation: Verify the destination channel and webhook before scheduling automatic pushes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/monaxamo/skills/9527-github-trending)
- [GitHub Trending](https://github.com/trending)
- [Telegram Bot API sendMessage](https://api.telegram.org/bot{token}/sendMessage)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration]

**Output Format:** [Console text or JSON output, with optional Markdown notification messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can filter by programming language and daily, weekly, or monthly time range.]

## Skill Version(s):

1.0.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
