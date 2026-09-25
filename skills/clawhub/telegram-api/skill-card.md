## Description:

Telegram Bot API integration with managed authentication for sending messages, managing chats, handling updates, and interacting with Telegram users through a bot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to a Telegram bot through Maton, make Telegram Bot API calls, and set up approved automation for bot workflows. It is suited for sending or editing messages, reading bot updates, managing bot commands, and configuring webhooks or scheduled checks with explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to operate a Telegram bot, including message sends, edits, deletes, webhook changes, hosted functions, triggers, and destinations.

Mitigation: Require explicit user approval for each connection, write action, webhook, function, trigger, or destination, and summarize the affected account, host, data, and persistence before execution.

Risk: Webhooks and trigger destinations can continuously forward future chat or event data.

Mitigation: Confirm the destination host, narrow update or trigger scope to the minimum needed, avoid temporary inspection endpoints for live data, and remove or update standing routes when they are no longer needed.

Risk: Using raw HTTP or environment variables for API-key access can expose long-lived credentials.

Mitigation: Prefer OAuth through the Maton CLI and operating-system credential storage; use raw HTTP only when the CLI cannot be installed, and keep credentials out of logs, files, and broad process environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/telegram-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code blocks, shell commands, JSON examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Telegram Bot API calls, Maton CLI commands, webhook settings, hosted function code, trigger configuration, and credential-handling guidance.]

## Skill Version(s):

1.2.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
