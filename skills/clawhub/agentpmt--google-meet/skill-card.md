## Description:

Google Meet: Create and manage Google Meet meeting spaces, view conference history including participants and join/leave times, and use AgentPMT-hosted remote tool calls for meeting workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, developers, and operations teams use this skill to create and manage Google Meet spaces, review organizer-accessible conference history, inspect participant attendance, and retrieve recording or transcript metadata for follow-up workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive meeting history, participant information, transcript metadata, and recording metadata may be routed through a third-party service.

Mitigation: Connect only authorized accounts, scope requests to the minimum meeting data needed, and avoid broad transcript or recording retrieval unless the workflow requires it.

Risk: The skill can end an active conference.

Mitigation: Require explicit user confirmation before invoking end_conference and verify the target space_name or meeting code.

Risk: Mutable remote schema or instruction lookups may differ from the reviewed local artifact.

Mitigation: Use live schema lookups only when needed, review returned changes before acting on them, and prefer pinned or OpenClaw setup paths over unpinned npx commands.

Risk: Credential or payment material could be exposed if placed in prompts or logs.

Mitigation: Use the setup skills for credential handling and keep secrets, wallet private keys, mnemonics, signatures, and payment headers out of prompts and logs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/agentpmt/skills/google-meet)
- [AgentPMT Google Meet Connector](https://www.agentpmt.com/marketplace/google-meet-connector)
- [Generated Action Schema](artifact/schema.md)
- [AgentPMT Account MCP/REST Setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)
- [What AgentPMT Is](https://clawhub.ai/agentpmt/what-is-agentpmt)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, JSON]

**Output Format:** [Markdown instructions with JSON request examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defines 14 AgentPMT-hosted Google Meet actions and returns JSON from remote tool calls.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
