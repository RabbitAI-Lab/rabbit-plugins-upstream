## Description:

Slack API integration with managed OAuth for sending messages, managing channels, searching conversations, and automating Slack workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent perform approved Slack workspace tasks through Maton, such as listing channels and users, posting or updating messages, searching messages and files, and setting up narrowly scoped Slack automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the Maton CLI or SDK introduces ordinary third-party package supply-chain risk.

Mitigation: Install only when Maton and the package source are trusted, and keep package versions pinned to reviewed releases.

Risk: Slack OAuth scopes and connections can expose workspace messages, files, users, and channel metadata available to the connected account.

Mitigation: Prefer OAuth, grant only the scopes needed for the task, specify the intended connection when multiple connections exist, and revoke unused connections.

Risk: Write operations and automation setup can change Slack content or create ongoing workflows.

Mitigation: Default to read and list calls, then get explicit user confirmation for every write, connection creation, hosted function, trigger, and destination change.

Risk: Trigger destinations can continuously forward Slack event data or other connected-app event data to another host.

Mitigation: Keep destinations on Maton-controlled endpoints unless the user explicitly approves a named third-party host, and forward only the minimum fields required.

Risk: Raw API keys and event payloads may leak through logs, command lines, files, or untrusted local handlers.

Mitigation: Prefer OAuth over API keys, never print or persist credentials, treat event payloads as untrusted data, and avoid local event execution unless the user provided and approved the handler.

## Reference(s):

- [ClawHub Slack Skill](https://clawhub.ai/byungkyu/skills/slack-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Slack API Methods](https://docs.slack.dev/reference/methods)
- [Slack Block Kit Reference](https://docs.slack.dev/block-kit/)
- [Slack Message Formatting](https://docs.slack.dev/messaging/formatting-message-text)
- [Slack Web API Rate Limits](https://docs.slack.dev/apis/web-api/rate-limits)
- [Slack Trigger Reference](artifact/references/slack/triggers.md)
- [Time Trigger Reference](artifact/references/time/triggers.md)
- [Calendly Trigger Reference](artifact/references/calendly/triggers.md)
- [GitHub Trigger Reference](artifact/references/github/triggers.md)
- [Gmail Trigger Reference](artifact/references/google-mail/triggers.md)
- [HubSpot Trigger Reference](artifact/references/hubspot/triggers.md)
- [Linear Trigger Reference](artifact/references/linear/triggers.md)
- [Notion Trigger Reference](artifact/references/notion/triggers.md)
- [Stripe Trigger Reference](artifact/references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request bodies, and Python or JavaScript SDK examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Maton CLI commands, raw HTTP request examples, SDK snippets, trigger configuration guidance, and safety checks for user approval.]

## Skill Version(s):

1.2.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
