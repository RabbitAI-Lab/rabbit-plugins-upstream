## Description:

Ach Publish provides a local MCP stdio and HTTP-SSE communication hub for multi-agent messaging, task orchestration, shared memory, and a web management panel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liuboacean](https://clawhub.ai/user/liuboacean)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to connect MCP-compatible agents through a local hub for messaging, task assignment, context sharing, and operational monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Member-level tools may be under-scoped for some deployments.

Mitigation: Install only in a trusted local agent group and review member-level authorization before production use.

Risk: Optional autonomous executors can send task descriptions, context, and results to external LLM providers or HTTP endpoints.

Mitigation: Decide approved data flows before enabling autonomous execution and restrict HOST_EXEC_ENDPOINT, provider settings, and related secrets.

Risk: Hub token or admin access compromise can expose or alter agent communications and task state.

Mitigation: Lock down HUB_AUTH_TOKEN and admin access, narrow activation triggers, and audit pipeline and dependency ownership checks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/liuboacean/skills/agent-comm-hub)
- [README](README.md)
- [API Reference](docs/API_REFERENCE.md)
- [Host Integration Guide](docs/HOST_INTEGRATION.md)
- [Advanced Orchestration Guide](docs/advanced-orchestration-guide.md)
- [MCP Protocol Specification](https://spec.modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured MCP tool arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce messages, task records, memory entries, status summaries, and setup/configuration instructions for connected agents.]

## Skill Version(s):

3.0.24 (source: SKILL.md frontmatter, package.json, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
