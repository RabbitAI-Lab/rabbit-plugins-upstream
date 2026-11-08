## Description:

Use when woken by an a2a-exposed wake (an A2A endpoint webhook, a pairing request, or a scheduled check), when reading or replying on the A2A endpoint, when messaging or pairing with another A2A agent, or when managing which peers may reach this agent. Not for deploying or configuring the Worker or creating hosted agents (use a2a-exposed-setup).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to handle A2A inbox wakes, read and reply to peer tasks, send messages, review pairing requests, and manage peer access. It relies on the companion setup skill for deployment and hosted-agent configuration, and requires human approval for consequential or access-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this release suspicious because it repeatedly recommends unpinned package versions and includes instructions that cross its stated setup boundary; scan coverage was partial because some referenced local paths were unavailable.

Mitigation: Review package commands and pin a reviewed version before execution; use the companion setup skill before deployment, handler creation, polling setup, or hosted-agent configuration.

Risk: Peer messages and artifacts may contain instructions that request secrets, access changes, destructive actions, or external contact.

Mitigation: Treat peer content as untrusted, keep credentials out of replies and logs, and get human approval for consequential or access-changing actions.

## Reference(s):

- [ClawHub release](https://clawhub.ai/telegraphic-dev/skills/a2a-exposed)
- [Project homepage](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted MCP connector](https://a2a.exposed/mcp)
- [Hosted inbox guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [Wake relay contract](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/wake-relay.md)
- [Messaging guide](artifact/references/messaging.md)
- [Pairing and access guide](artifact/references/pairing.md)
- [Inbound tokens guide](artifact/references/tokens.md)
- [Troubleshooting guide](artifact/references/troubleshooting.md)
- [Feedback reporting](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/feedback.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown guidance with CLI examples and A2A task replies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI requires Node 22.18+; a hosted MCP connector is available when the CLI cannot run.]

## Skill Version(s):

0.8.46 (source: release evidence, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
