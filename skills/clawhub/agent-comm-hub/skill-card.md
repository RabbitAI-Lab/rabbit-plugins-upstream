## Description:

Connects local AI agents through MCP and HTTP/SSE for messaging, task coordination, shared memory, and a web dashboard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liuboacean](https://clawhub.ai/user/liuboacean)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to connect local agents, exchange messages, coordinate tasks, and share context through a communication hub.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent messages, tasks, and approval events may be exposed too broadly by authorization weaknesses.

Mitigation: Use only with trusted agents in an isolated local environment; fix authorization issues before production use.

Risk: An HTTP/SSE server or an untrusted hub endpoint can expose coordination data.

Mitigation: Keep the server off untrusted networks and restrict HUB_URL to a known local or internal origin.

Risk: Watcher, bridge, or automatic execution paths may act on events from untrusted agents or token holders.

Mitigation: Disable those paths unless every participating agent and token holder is trusted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liuboacean/skills/agent-comm-hub)
- [API reference](artifact/docs/API_REFERENCE.md)
- [Host integration guide](artifact/docs/HOST_INTEGRATION.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Text and structured MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a running hub and an authorized agent identity.]

## Skill Version(s):

3.0.25 (source: frontmatter, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
