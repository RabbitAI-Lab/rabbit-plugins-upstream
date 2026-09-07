## Description:

Set up an autonomous, customer-facing support agent inside an Intercom inbox across WhatsApp, Instagram, Facebook, in-app Messenger, SMS, and email.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othreecodes](https://clawhub.ai/user/othreecodes)

### License/Terms of Use:

MIT-0

## Use Case:

External support teams and developers use this skill to configure an OpenClaw agent that replies directly to customers in Intercom-connected channels, applies tags and notes, and escalates conversations to humans when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill configures an autonomous agent that can reply to real customers under a teammate identity.

Mitigation: Confirm authorization with the support workspace owner before enabling the channel, pilot on a narrow allowedChannels scope, and monitor initial customer conversations closely.

Risk: The Intercom access token and webhook secret can expose sensitive support workflows if over-scoped or mishandled.

Mitigation: Use a dedicated Intercom app with only required permissions, store the token and webhook secret carefully, and keep credentials easy to rotate or revoke.

Risk: Plugin upgrades can change production customer-support behavior.

Mitigation: Pin the reviewed plugin version, verify the pinned source and publisher before installation, and review changelogs before upgrading.

## Reference(s):

- [Intercom Support Channel on ClawHub](https://clawhub.ai/othreecodes/skills/intercom-support-channel)
- [openclaw-intercom source and configuration reference](https://github.com/othreecodes/openclaw-intercom)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes setup sequence, Intercom app permission guidance, webhook configuration, staged rollout guidance, and human escalation requirements.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
