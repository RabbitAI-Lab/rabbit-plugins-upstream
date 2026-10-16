## Description:

Helps an agent connect a Zalo bot to a specified chat, send a test message, and provide reminder and alert examples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thinhbuiii](https://clawhub.ai/user/thinhbuiii)

### License/Terms of Use:

MIT-0

## Use Case:

Zalo bot owners and their agents use this skill to connect a bot to an authorized chat, test delivery, and prepare group reminders or alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bot token may be exposed through chat history, shared logs, or shell history.

Mitigation: Confirm the token privately, avoid logging or echoing it, and rotate it if shared through an unsafe channel.

Risk: Setup edits the gateway environment and restarts the gateway.

Mitigation: Allow configuration changes only for the authorized owner, confirm the parsed token and chat ID, and preserve existing environment values.

Risk: The setup sends a real test message to the selected Zalo chat.

Mitigation: Verify the destination chat and obtain approval before sending the test message.

## Reference(s):

- [ENT Zalo Connect on ClawHub](https://clawhub.ai/thinhbuiii/skills/ent-zalo-connect)
- [Zalo Bot Platform](https://bot.zaloplatforms.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with shell and Python examples and a connection status report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the test result and message ID when available; does not display the bot token.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
