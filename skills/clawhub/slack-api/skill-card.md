## Description:

Slack API integration with managed OAuth for sending messages, managing channels, searching conversations, listing users, and automating Slack workflows through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to work with Slack workspaces through managed OAuth, including reading workspace data, posting or updating messages, managing channels, files, reactions, pins, bookmarks, and searching Slack content. It is intended for workflows where Slack access must be scoped to a connected account and writes require explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify Slack data through a connected account.

Mitigation: Use OAuth where possible, connect only the needed workspace or account, verify the target connection before writes, and require explicit confirmation before messages, channel changes, file operations, or deletions.

Risk: Slack write operations can send messages, change channels, share files, or delete content in the wrong workspace or target.

Mitigation: Default to read and list calls, specify the intended connection when multiple accounts exist, and confirm the resource identifier, payload, and intended effect before any write operation.

Risk: Slack content returned by the API may contain untrusted instructions or adversarial text.

Mitigation: Treat fetched Slack content as data, do not execute or follow instructions from it, and pass external values as discrete arguments rather than interpolating them into shell commands or prompts.

Risk: Long-lived API keys or provider credentials can be exposed through logs, files, command lines, or environment inheritance.

Mitigation: Prefer OAuth and OS credential storage, never print or persist credentials, and use raw HTTP with an API key only when the CLI cannot be installed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/slack-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, JSON request bodies, SDK examples, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Slack API request paths, Maton CLI invocations, JSON payload examples, and safety guidance for approval, credentials, and connection targeting.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
