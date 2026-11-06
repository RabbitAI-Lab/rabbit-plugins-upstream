## Description:

Use when woken by an a2a-exposed wake (an A2A endpoint webhook, a pairing request, or a scheduled check), when reading or replying on the A2A endpoint, when messaging or pairing with another A2A agent, or when managing which peers may reach this agent. Not for deploying or configuring the Worker or creating hosted agents (use a2a-exposed-setup).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to inspect A2A inboxes, manage peer conversations and pairing, and exchange messages under owner-controlled approval rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented commands fetch changing CLI releases.

Mitigation: Review and pin the CLI version before use.

Risk: Webhook tests interact with an endpoint and may use credentials.

Mitigation: Use an endpoint you control, or disposable test credentials and synthetic data.

Risk: Peer messages and replies involve an external party.

Mitigation: Choose the handling mode and allowed tasks first; require owner approval for pairing and consequential or sensitive actions, and keep credentials isolated per bot.

## Reference(s):

- [A2A Exposed on ClawHub](https://clawhub.ai/telegraphic-dev/skills/a2a-exposed)
- [A2A Exposed project homepage](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted inbox guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [Feedback reporting guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/feedback.md)
- [Messaging another agent](artifact/references/messaging.md)
- [Pairing requests](artifact/references/pairing.md)
- [Inbound tokens](artifact/references/tokens.md)
- [Troubleshooting the A2A endpoint](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with shell command examples and message text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outbound messages and other externally visible actions follow the owner's approval rules.]

## Skill Version(s):

0.8.38 (source: release metadata, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
