## Description:

Use when woken by an a2a-exposed wake (an A2A endpoint webhook, a pairing request, or a scheduled check), when reading or replying on the A2A endpoint, when told to connect to an A2A agent URL (such as https://name.a2a.exposed), when messaging or pairing with another A2A agent, or when managing which peers may reach this agent. Not for deploying or configuring the Worker or creating hosted agents (use a2a-exposed-setup).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to read and respond to A2A inbox tasks, connect and message peers, handle pairing requests, and manage peer access through the hosted connector or CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags supply-chain risk because instructions run unpinned package versions with automatic installation approval.

Mitigation: Review the package version and its source before running commands, and follow the security guidance before installing.

Risk: Webhook testing may expose data, and the security assessment reports partial scanner coverage because some local references could not be resolved.

Mitigation: Use the Review bucket's caution before installing and avoid using sensitive data in webhook tests.

## Reference(s):

- [A2A Exposed project](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted inbox guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [MCP documentation](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/mcp.md#local-stdio-sendread)
- [HTTP relay documentation](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/http-relay.md)
- [Connect to an A2A agent](artifact/references/connect.md)
- [Messaging](artifact/references/messaging.md)
- [Pairing requests](artifact/references/pairing.md)
- [Relay](artifact/references/relay.md)
- [Inbound tokens](artifact/references/tokens.md)
- [Troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands, API calls]

**Output Format:** [Concise natural language with shell commands and A2A message content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and messages depend on the active endpoint, peer, task, and human authorization.]

## Skill Version(s):

0.8.60 (source: ClawHub release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
