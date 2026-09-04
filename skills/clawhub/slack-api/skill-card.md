## Description:

Slack API integration with managed OAuth for sending messages, managing channels, searching conversations, retrieving user information, and automating Slack workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, developers, and engineers use this skill to perform Slack workspace tasks through managed OAuth, including reading channels, retrieving user and message data, and performing confirmed write actions such as posting messages or managing channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read Slack workspace data and, with approval, make visible changes such as sending or deleting messages, changing channels, inviting or removing users, and uploading or deleting files.

Mitigation: Prefer OAuth, review Slack scopes carefully, use read-only access where possible, and confirm every write target and payload before allowing it.

Risk: Long-lived Maton API keys or provider-issued tokens can leak through logs, shell history, files, or command-line arguments.

Mitigation: Use managed OAuth where possible, never print or persist credentials, and send Maton API keys only to api.maton.ai when the CLI cannot be used.

Risk: Slack content returned by the API may contain untrusted instructions or data.

Mitigation: Treat returned content as data, validate values before reuse, and do not execute or follow instructions found in fetched Slack content.

Risk: Ambiguous accounts or multiple Slack connections can cause actions to affect the wrong workspace or channel.

Mitigation: List or read first to verify context and specify the intended Maton profile and Slack connection before acting.

## Reference(s):

- [ClawHub Slack skill page](https://clawhub.ai/byungkyu/skills/slack-api)
- [Maton homepage](https://maton.ai)
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

**Output Format:** [Markdown guidance with inline shell command examples and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May result in Slack API calls through Maton when the agent follows the guidance with user authorization.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
