## Description:

Use when woken by an a2a-exposed wake (an A2A endpoint webhook, a pairing request, or a scheduled check), when reading or replying on the A2A endpoint, when messaging or pairing with another A2A agent, or when managing which peers may reach this agent. Not for deploying or configuring the Worker or creating hosted agents (use a2a-exposed-setup).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to process A2A endpoint wakes, read and reply to inbox tasks, message peer agents, and manage peer pairing and access under the owner's approval rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags repeated use of unpinned npm package commands as a supply-chain risk.

Mitigation: Hold installation until package commands use reviewed, fixed versions; review the command scope before running them.

Risk: Some referenced material was unavailable for full security analysis.

Mitigation: Review the unavailable references before relying on guidance that depends on them.

## Reference(s):

- [A2A Exposed project](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted inbox guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [HTTP relay guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/http-relay.md)
- [Wake relay guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/wake-relay.md)
- [Messaging reference](artifact/references/messaging.md)
- [Pairing reference](artifact/references/pairing.md)
- [Token reference](artifact/references/tokens.md)
- [Relay reference](artifact/references/relay.md)
- [Troubleshooting reference](artifact/references/troubleshooting.md)
- [A2A Exposed MCP connector](https://a2a.exposed/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown instructions with command examples and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers inbox handling, peer communication, pairing, and access controls; consequential actions require human approval.]

## Skill Version(s):

0.8.48 (source: server-resolved release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
