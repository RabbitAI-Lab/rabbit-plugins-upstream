## Description:

Reach the user on their phone through agentring — send a message, wait for their reply, or call them (a voice AI talks to them for you and returns the transcript). Use when you need the user's decision or attention and they may be away from the screen, when a long task finishes or fails, or when the user asks you to message or call them. Also use when the user asks to set up, install or connect agentring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mutonby](https://clawhub.ai/user/mutonby)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to reach the user's paired Android phone for async decisions, status updates, and voice conversations. They can also follow its setup guidance to connect agentring with OpenClaw or Hermes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agentring API key grants access to the user's phone.

Mitigation: Have the user enter the key locally, and keep API and voice-provider keys out of messages and call context.

Risk: The security evidence reports one Skillspector self-modification alert, assessed as unlikely to indicate a concern in context.

Mitigation: Review the alert and skill before installation, as recommended by the security guidance.

## Reference(s):

- [Setting up agentring](references/setup.md)
- [agentring](https://agentring.io)
- [OpenClaw connection guide](https://agentring.io/agents/openclaw)
- [Hermes connection guide](https://agentring.io/agents/hermes)
- [Android app on Google Play](https://play.google.com/store/apps/details?id=dev.agentring.app)
- [Self-hosted setup guide](https://github.com/mutonby/agentring/blob/main/docs/setup.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Natural-language messages, replies and call transcripts; Markdown setup guidance with inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Messages and call context are concise text for delivery to the user's phone.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
