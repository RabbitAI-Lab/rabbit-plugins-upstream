## Description:

Slack API integration with managed OAuth for sending messages, managing channels, searching conversations, getting user info, and automating Slack workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to a Slack workspace through Maton-managed OAuth, inspect Slack resources, and perform approved Slack actions such as posting messages, managing channels, searching conversations, and working with users or files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify Slack workspace data through authorized Maton-mediated access.

Mitigation: Use OAuth with the narrowest Slack scopes available, confirm the intended workspace or connection before use, and require explicit user approval before creating connections or performing write operations.

Risk: Slack responses may contain personal, confidential, or adversarial workspace content.

Mitigation: Treat Slack content as untrusted data, extract only fields needed for the task, and avoid logging or persisting raw responses unless the user explicitly asks.

Risk: Using a Maton API key instead of OAuth can expose a long-lived credential through environment variables, logs, shell history, or pasted output.

Mitigation: Prefer OAuth and the Maton CLI; when raw HTTP is unavoidable, keep the key in the process environment only, never print or persist it, and send it only to api.maton.ai.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/slack-api)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Slack API Methods](https://api.slack.com/methods)
- [Slack Web API Reference](https://api.slack.com/web)
- [Slack Block Kit Reference](https://api.slack.com/reference/block-kit)
- [Slack Message Formatting](https://api.slack.com/reference/surfaces/formatting)
- [Slack Rate Limits](https://api.slack.com/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request examples, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Slack identifiers, command examples, request payloads, and approval prompts for write operations.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
