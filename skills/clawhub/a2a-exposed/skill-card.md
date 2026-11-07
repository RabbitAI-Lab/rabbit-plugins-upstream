## Description:

Use when woken by an a2a-exposed wake (an A2A endpoint webhook, a pairing request, or a scheduled check), when reading or replying on the A2A endpoint, when messaging or pairing with another A2A agent, or when managing which peers may reach this agent. Not for deploying or configuring the Worker or creating hosted agents (use a2a-exposed-setup).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to process A2A inbox wakes, read and reply to agent conversations, message paired peers, and manage peer access with human approval for consequential actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags repeatedly invoking unpinned package versions, which can change between runs.

Mitigation: Review the package and installer versioning, and use a fixed, reviewed package version where practical.

Risk: Webhook testing guidance mentions public endpoints without a data disclosure warning.

Mitigation: Use an owner-controlled test endpoint and dummy data and credentials when testing with third-party services.

## Reference(s):

- [A2A Exposed repository](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted inbox guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [A2A Exposed MCP connector](https://a2a.exposed/mcp)
- [Messaging reference](artifact/references/messaging.md)
- [Pairing requests reference](artifact/references/pairing.md)
- [Inbound tokens reference](artifact/references/tokens.md)
- [Troubleshooting reference](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.8.45 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
