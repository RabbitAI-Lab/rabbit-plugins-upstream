## Description:

Slack API integration with managed OAuth for sending messages, managing channels, searching conversations, listing users, and automating Slack workflows through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business users use this skill to operate approved Slack workspace connections from an agent, including reading Slack data, posting messages, managing channels, and configuring user-approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read, write, and automate Slack workflows using user-approved OAuth access.

Mitigation: Confirm Slack scopes and target connections before use, and require explicit user approval for writes, new connections, hosted functions, triggers, and destinations.

Risk: Raw Maton API keys can expose long-lived credentials if OAuth or the CLI is not available.

Mitigation: Prefer managed OAuth and the Maton CLI, keep API keys out of logs and command lines, and rotate any key that was printed, committed, or pasted.

Risk: Slack responses can contain personal or business-sensitive data.

Mitigation: Extract only the fields needed for the task and avoid storing or displaying raw API responses unless the user explicitly requests it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/slack-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Slack API Methods](https://docs.slack.dev/reference/methods)
- [Slack Block Kit Reference](https://docs.slack.dev/block-kit/)
- [Slack Message Formatting](https://docs.slack.dev/messaging/formatting-message-text)
- [Slack API Rate Limits](https://docs.slack.dev/apis/web-api/rate-limits)
- [Slack Trigger Reference](references/slack/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, markdown]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Slack API call plans, Maton CLI commands, hosted function examples, and trigger configuration steps for user-approved Slack workflows.]

## Skill Version(s):

1.2.8 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
