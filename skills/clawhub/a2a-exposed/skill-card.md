## Description:

Use when woken by an a2a-exposed wake (an A2A endpoint webhook, a pairing request, or a scheduled check), when reading or replying on the A2A endpoint, when told to connect to an A2A agent URL (such as https://name.a2a.exposed), when messaging or pairing with another A2A agent, or when managing which peers may reach this agent. Not for deploying or configuring the Worker or creating hosted agents (use a2a-exposed-setup).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to monitor an A2A inbox, handle peer messages and pairing requests, and manage communication with other agents. It guides safe replies, access decisions, and troubleshooting for hosted or self-hosted endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan rates the skill suspicious because it repeatedly runs automatically installed, unpinned package versions; the scan is partial, so its evidence is incomplete.

Mitigation: Review the package source and version before execution, prefer a reviewed pinned version over a changing latest version, and consider the incomplete scan evidence before installing.

## Reference(s):

- [A2A Exposed project](https://github.com/telegraphic-dev/a2a-exposed)
- [ClawHub skill page](https://clawhub.ai/telegraphic-dev/skills/a2a-exposed)
- [Connect to an A2A agent](artifact/references/connect.md)
- [Messaging another agent](artifact/references/messaging.md)
- [Pairing requests](artifact/references/pairing.md)
- [Inbound tokens](artifact/references/tokens.md)
- [Relay operations](artifact/references/relay.md)
- [Troubleshooting](artifact/references/troubleshooting.md)
- [Hosted MCP documentation](https://a2a.exposed/docs/hosted-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-specific instructions depend on endpoint type, peer state, and owner approval.]

## Skill Version(s):

0.8.75 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
