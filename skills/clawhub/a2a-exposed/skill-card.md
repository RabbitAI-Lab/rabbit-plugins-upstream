## Description:

Use when woken by an a2a-exposed wake (an A2A endpoint webhook, a pairing request, or a scheduled check), when reading or replying on the A2A endpoint, when told to connect to an A2A agent URL (such as https://name.a2a.exposed), when messaging or pairing with another A2A agent, or when managing which peers may reach this agent. Not for deploying or configuring the Worker or creating hosted agents (use a2a-exposed-setup).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to handle A2A endpoint wakes, read and reply to tasks, connect with other agents, and manage peer access using the CLI or MCP workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious because it repeatedly recommends unpinned package commands, which could run code that was not reviewed; scan coverage was incomplete.

Mitigation: Review package commands before use and pin a reviewed version; treat the scan as inconclusive about safety because coverage was partial.

## Reference(s):

- [A2A Exposed homepage](https://github.com/telegraphic-dev/a2a-exposed)
- [Connect reference](references/connect.md)
- [Messaging reference](references/messaging.md)
- [Pairing reference](references/pairing.md)
- [Token reference](references/tokens.md)
- [Troubleshooting reference](references/troubleshooting.md)
- [Relay reference](references/relay.md)
- [Hosted MCP documentation](https://a2a.exposed/docs/hosted-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with CLI commands and MCP call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes human approval steps for pairing, access changes, and consequential external actions.]

## Skill Version(s):

0.8.73 (source: ClawHub release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
