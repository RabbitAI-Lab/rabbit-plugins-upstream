## Description:

Governed tool access for AI agents: one Danube API key unlocks an organization's own tools plus a large catalog of services over MCP or curl, with confirmation before anything that writes, sends, spends, or deletes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Danube to discover, inspect, and execute organization and catalog tools over MCP or REST while preserving explicit confirmation for write, spend, delete, credential, workflow, and batch actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration enables broad remote access to connected organization and catalog tools.

Mitigation: Use scoped Danube API keys and spending limits where possible, and require explicit user confirmation before write, spend, delete, credential storage, workflow, or batch actions.

Risk: Credential handling can expose or store sensitive service credentials if used carelessly.

Mitigation: Store only credentials the user explicitly provides and confirms, prefer dashboard or OAuth setup for sensitive services, and avoid echoing unmasked secrets.

Risk: Plan limits or temporarily disabled hosted AI tools can be mistaken for transient failures.

Mitigation: Read the returned status and message, stop retry loops on plan refusals or kill-switch responses, and tell the user whether to wait, upgrade, or choose another tool.

Risk: The available tool catalog and private organization tools can change over time.

Mitigation: Search and describe tools before execution, inspect each tool schema and readiness, and avoid reusing stale tool IDs.

## Reference(s):

- [ClawHub Danube Skill](https://clawhub.ai/preston-thiele/skills/danube)
- [Danube OpenClaw Guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube Documentation](https://docs.danubeai.com)
- [Danube Dashboard](https://danubeai.com/dashboard)
- [Danube MCP Server](https://mcp.danubeai.com/mcp)
- [Danube REST API](https://api.danubeai.com/v1)
- [REST API Reference](references/rest-api.md)
- [Troubleshooting Guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline shell commands, JSON examples, and REST/MCP call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DANUBE_API_KEY and curl; direct tool outputs may be JSON, text, or service-specific payloads returned by Danube.]

## Skill Version(s):

8.1.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
