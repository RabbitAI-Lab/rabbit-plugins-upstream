## Description:

Read messages from Slack channels and post replies. Use when the user asks about Slack channels, channel history, posting Slack messages, or any Slack-related operation. Credentials are auto-injected when Slack is connected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[berkgungor](https://clawhub.ai/user/berkgungor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Slack workspace and channel context, resolve users, post threaded replies, and manage message reactions through a Slack bot.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bot can read Slack channel data in channels where it is a member.

Mitigation: Install only in appropriate workspaces, review Slack app scopes and channel membership, and avoid sending secrets to the bot.

Risk: The bot can post replies or manage reactions in Slack.

Mitigation: Require explicit user intent before posting messages or changing reactions.

## Reference(s):

- [Slack Web API](https://slack.com/api)
- [ClawHub skill page](https://clawhub.ai/berkgungor/skills/slack)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions with CLI commands; commands return a single JSON object on stdout.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Slack Web API calls require an injected bot token and access only to channels where the bot is a member.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
