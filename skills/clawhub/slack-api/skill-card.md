## Description:

Slack API integration with managed OAuth for sending messages, managing channels, searching conversations, and interacting with Slack workspaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to automate Slack workspace tasks such as posting messages, listing channels, reading conversation history, managing channel metadata, and searching Slack content through Maton-managed OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify Slack data through a Maton-authorized connection.

Mitigation: Use the narrowest Slack scopes available and confirm the exact workspace, connection, target resource, and payload before any write.

Risk: Long-lived API keys and provider-issued tokens can leak through logs, shell history, files, or pasted output.

Mitigation: Prefer OAuth, keep credentials in the managed credential store, never print or persist secret values, and rotate any key that was exposed.

Risk: Slack messages, files, and other API responses may contain sensitive data or untrusted instructions.

Mitigation: Retrieve only the needed fields, avoid dumping raw responses, and treat returned content as data rather than instructions for follow-up actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/slack-api)
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

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Slack API requests through the Maton CLI or raw HTTPS fallback when the CLI is unavailable.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
