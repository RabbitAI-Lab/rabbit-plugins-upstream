## Description:

notify-hub lets agents send text, structured cards, and files to Feishu, WeCom, DingTalk, Slack, Telegram, and email from one notification workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiyanjun](https://clawhub.ai/user/xiyanjun)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use notify-hub as the dispatch step for reports, monitoring alerts, reminders, and other agent outputs that need to reach one or more configured messaging or email destinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured webhooks, bot tokens, and SMTP passwords can authorize outbound messages if exposed.

Mitigation: Treat every credential as a secret, keep credentials out of repositories and shell history, and review the skill before installing it in workspaces with sensitive reports or production alert channels.

Risk: Broadcasting to all configured destinations can send sensitive or unsuitable content to unintended recipients.

Mitigation: Use --dry-run before live sends, specify --to explicitly, and reserve --to all for content that is safe for every configured destination.

Risk: The security verdict is suspicious because the skill handles powerful messaging credentials and outbound broadcasts.

Mitigation: Follow the provided security guidance and limit installation to workspaces where the notification destinations, credentials, and message contents have been reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiyanjun/skills/notify-hub)
- [Channel schema and format reference](references/channels-schema.md)
- [Example card payload](examples/card_report.json)
- [Feishu custom bot documentation](https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON card examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run previews, explicit target selection, broadcast targets, and channel-specific rendering fallbacks.]

## Skill Version(s):

1.0.0 (source: frontmatter, manifest, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
