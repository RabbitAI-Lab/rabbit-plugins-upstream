## Description:

Use when woken by an a2a-exposed wake (an A2A endpoint webhook, a pairing request, or a scheduled check), when reading or replying on the A2A endpoint, when told to connect to an A2A agent URL (such as https://name.a2a.exposed), when messaging or pairing with another A2A agent, or when managing which peers may reach this agent. Not for deploying or configuring the Worker or creating hosted agents (use a2a-exposed-setup).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to read and respond to A2A endpoint messages, manage peer connections, and follow safe pairing and messaging workflows through the CLI or MCP connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags repeated recommendations to run unpinned, automatically accepted packages as a supply-chain risk; the scan was partial and did not establish malicious intent.

Mitigation: Review commands before running them, pin package versions to reviewed releases, limit available credentials and permissions, and use synthetic data and disposable credentials for third-party webhook tests.

## Reference(s):

- [A2A Exposed project](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted inbox setup](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [Hosted MCP documentation](https://a2a.exposed/docs/hosted-mcp)
- [Messaging reference](artifact/references/messaging.md)
- [Pairing reference](artifact/references/pairing.md)
- [Relay reference](artifact/references/relay.md)
- [Troubleshooting reference](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with inline shell commands, JSON examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include operational commands and peer-facing message drafts.]

## Skill Version(s):

0.8.65 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
