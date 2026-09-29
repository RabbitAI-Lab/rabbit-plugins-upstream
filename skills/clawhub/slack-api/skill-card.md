## Description:

Helps agents use an authorized Slack connection to find conversations, manage channels, send messages, and set up approved automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to let an agent search and read Slack information, send approved messages, and configure explicitly authorized channel automations through a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Messages or changes may affect the wrong workspace or channel.

Mitigation: Confirm the account, workspace, channel, and exact action before writes; start with read-only checks.

Risk: Triggers can continuously forward sensitive Slack events to an overly broad destination.

Mitigation: Scope triggers to approved channels, minimize forwarded fields, and require explicit approval for each destination.

Risk: Exposed Maton or Slack credentials can permit unauthorized access.

Mitigation: Keep credentials out of files, logs, command lines, and third-party webhook destinations.

## Reference(s):

- [ClawHub Slack skill release](https://clawhub.ai/byungkyu/skills/slack-api)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Slack API methods](https://docs.slack.dev/reference/methods)
- [Slack trigger reference](references/slack/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with shell commands, API examples, and optional automation code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Slack access requires an authorized connection; writes and automations require user approval.]

## Skill Version(s):

1.2.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
