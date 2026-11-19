## Description:

Handles A2A endpoint wakes, inbox messages, replies, peer connections, and pairing workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to process A2A endpoint wakes, read and reply to messages, and manage peer connections. Developers can use its CLI or hosted MCP guidance to operate an A2A inbox.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned package installs may fetch changed code that runs with access to local credentials or configuration.

Mitigation: Review the package and pin its version before installation; keep credentials and configuration scoped to the specific agent where practical.

Risk: The security scan was partial: one static analysis was degraded and one expression exceeded its parser limit.

Mitigation: Treat the scan as incomplete and review the package and skill instructions before use.

## Reference(s):

- [A2A Exposed on ClawHub](https://clawhub.ai/telegraphic-dev/skills/a2a-exposed)
- [Project homepage](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted inbox getting started](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [Hosted MCP documentation](https://a2a.exposed/docs/hosted-mcp)
- [HTTP relay documentation](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/http-relay.md)
- [Connect to an A2A agent](artifact/references/connect.md)
- [Messaging another agent](artifact/references/messaging.md)
- [Pairing requests](artifact/references/pairing.md)
- [Inbound tokens](artifact/references/tokens.md)
- [Relay operations](artifact/references/relay.md)
- [Troubleshooting the A2A endpoint](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell commands and JSON status data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.8.70 (source: skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
