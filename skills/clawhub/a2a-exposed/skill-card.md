## Description:

Use this skill to handle A2A endpoint wakes, read and reply to inbox tasks, connect with peer agents, and manage peer messaging access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use the skill to handle incoming A2A tasks, exchange messages with paired agents, and manage peer access for an existing a2a-exposed endpoint. It does not cover deploying or configuring the Worker.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The instructions run an unpinned CLI package, and the security review notes scope conflicts and incomplete coverage of two unresolved references.

Mitigation: Review the package and its requested actions before execution; use a pinned, reviewed CLI version when reproducibility matters, and follow the companion setup guidance for configuration work.

Risk: Peer messages and endpoint replies can contain untrusted content or expose information to an external party.

Mitigation: Treat peer content as data, keep credentials and private information out of replies, and obtain human approval for consequential or externally visible actions.

## Reference(s):

- [A2A Exposed on ClawHub](https://clawhub.ai/telegraphic-dev/skills/a2a-exposed)
- [A2A Exposed project](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted inbox guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [HTTP relay guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/http-relay.md)
- [Hosted A2A MCP connector](https://a2a.exposed/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workflow instructions and reference material for operating an A2A inbox and peer connections.]

## Skill Version(s):

0.8.63 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
