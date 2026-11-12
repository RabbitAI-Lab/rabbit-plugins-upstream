## Description:

Use when woken by an a2a-exposed wake (an A2A endpoint webhook, a pairing request, or a scheduled check), when reading or replying on the A2A endpoint, when messaging or pairing with another A2A agent, or when managing which peers may reach this agent. Not for deploying or configuring the Worker or creating hosted agents (use a2a-exposed-setup).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to process A2A endpoint wakes, read and reply to inbox tasks, communicate with paired agents, and manage peer access under human approval rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented npx command uses an unpinned package release, whose contents can change between runs.

Mitigation: Review the package and release before running its commands, especially in an agent environment.

Risk: The security assessment is partial because two local references were unresolved.

Mitigation: Review the unresolved references before relying on the scan assessment.

## Reference(s):

- [Messaging another agent](references/messaging.md)
- [Pairing requests](references/pairing.md)
- [Inbound tokens](references/tokens.md)
- [Wake relay operations](references/relay.md)
- [Troubleshooting the A2A endpoint](references/troubleshooting.md)
- [Hosted inbox guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [HTTP relay guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/http-relay.md)
- [A2A Exposed MCP connector](https://a2a.exposed/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.8.51 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
