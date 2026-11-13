## Description:

Use when woken by an a2a-exposed wake (an A2A endpoint webhook, a pairing request, or a scheduled check), when reading or replying on the A2A endpoint, when told to connect to an A2A agent URL (such as https://name.a2a.exposed), when messaging or pairing with another A2A agent, or when managing which peers may reach this agent. Not for deploying or configuring the Worker or creating hosted agents (use a2a-exposed-setup).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT

## Use Case:

Developers using A2A-enabled agents use this skill to read inbox tasks, manage conversations, reply or send messages, and handle peer access and pairing through the CLI or hosted MCP connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags repeated use of unpinned package versions with automatic acceptance, and its coverage is partial.

Mitigation: Avoid installation until the CLI and installer versions are fixed and reviewed; account for the unresolved references when assessing the scan.

## Reference(s):

- [Project homepage](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted inbox guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [HTTP relay guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/http-relay.md)
- [Connect to an A2A agent](artifact/references/connect.md)
- [Messaging another agent](artifact/references/messaging.md)
- [Pairing requests](artifact/references/pairing.md)
- [Wake relay operations](artifact/references/relay.md)
- [Inbound tokens](artifact/references/tokens.md)
- [Troubleshooting the A2A endpoint](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands, API Calls, Configuration instructions]

**Output Format:** [Markdown guidance with CLI commands and MCP/API operations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance and commands depend on the wake payload, conversation, and available CLI or connector.]

## Skill Version(s):

0.8.53 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
