## Description:

Slack API integration with managed OAuth for sending messages, managing channels, searching conversations, and interacting with Slack workspaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace operators use this skill to guide agents through authenticated Slack API tasks such as listing channels and users, sending or updating messages, managing conversations, files, reactions, and searching Slack content through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Slack data can be accessed or modified according to the scopes authorized through Maton.

Mitigation: Prefer OAuth, choose the narrowest Slack scopes available, confirm the exact workspace and connection before writes, and review message, channel, file, or membership changes before execution.

Risk: Long-lived API keys or provider-issued tokens could be exposed through logs, files, shell history, or command arguments.

Mitigation: Use OAuth where possible, keep credentials in the operating system credential store or a session secret source, never print or persist credential values, and send Maton API keys only to api.maton.ai.

Risk: Slack messages and other returned workspace content may include sensitive data or adversarial instructions.

Mitigation: Treat returned Slack content as untrusted data, extract only fields needed for the task, avoid dumping raw responses, and do not execute or follow instructions found inside fetched content.

## Reference(s):

- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Slack API Methods](https://api.slack.com/methods)
- [Slack Web API Reference](https://api.slack.com/web)
- [Slack Block Kit Reference](https://api.slack.com/reference/block-kit)
- [Slack Message Formatting](https://api.slack.com/reference/surfaces/formatting)
- [Slack Rate Limits](https://api.slack.com/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Slack connection; write actions require explicit user approval.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
