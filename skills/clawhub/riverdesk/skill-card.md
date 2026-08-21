## Description:

Connect OpenClaw to the RiverDesk task app: install the openclaw-riverdesk channel plugin, pair with a one-time code from web.riverdesk.ai, and verify the agent is online.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riverdesk-ai](https://clawhub.ai/user/riverdesk-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an OpenClaw agent to RiverDesk, configure the channel plugin, pair the gateway with a one-time code, verify connectivity, and troubleshoot offline RiverDesk channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pairing enables RiverDesk to route messages to the configured local agent through the gateway.

Mitigation: Confirm the RiverDesk service and openclaw-riverdesk plugin package are trusted before installation and pairing.

Risk: Pairing codes, plugin tokens, keypairs, and state files are sensitive credentials.

Mitigation: Treat these values as secrets; do not print, log, or transmit them, and remove the pairing code from configuration after successful pairing.

Risk: Gateway configuration changes can disrupt existing OpenClaw channels or active sessions.

Mitigation: Back up the OpenClaw gateway configuration, merge only the RiverDesk channel block, and warn users before restarting the gateway.

## Reference(s):

- [RiverDesk](https://riverdesk.ai)
- [RiverDesk Web App](https://web.riverdesk.ai)
- [ClawHub RiverDesk Skill Page](https://clawhub.ai/riverdesk-ai/skills/riverdesk)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes plugin installation, gateway configuration, pairing, verification, troubleshooting, and secret-handling guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
