## Description:

Read messages from Slack channels and post replies. Use when the user asks about Slack channels, channel history, posting Slack messages, or any Slack-related operation. Credentials are auto-injected when Slack is connected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[berkgungor](https://clawhub.ai/user/berkgungor)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to inspect Slack channel context visible to the connected bot and perform explicit Slack actions such as posting replies or changing reactions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Slack read requests can expose more visible channel history than intended.

Mitigation: Use channel-history bounds such as --limit, --oldest, or --latest, and query only channels where the bot has been intentionally invited.

Risk: Write commands can post messages or change reactions in Slack.

Mitigation: Treat send-message and reaction changes as explicit user-approved actions and review the target channel, thread, text, and emoji before execution.

Risk: Private-channel access depends on bot membership and can include sensitive workspace content.

Mitigation: Use --include-private only when private-channel lookup is necessary and confirm the bot's channel membership matches the intended access scope.

## Reference(s):

- [Slack Web API](https://slack.com/api)
- [ClawHub Slack Skill Page](https://clawhub.ai/berkgungor/skills/slack)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON objects on stdout, with Markdown command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require an injected Slack bot token; channel history can be bounded with --limit, --oldest, and --latest.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
