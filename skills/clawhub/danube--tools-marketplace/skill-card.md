## Description:

Governed tool access for AI agents: one Danube API key lets an agent discover, inspect, and execute organization tools and catalog services over MCP or curl, with confirmation before actions that write, send, spend, store credentials, or delete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to connect agents to Danube's governed tool gateway, search available tools, inspect schemas and readiness, execute MCP or REST calls, and handle credentials, plan limits, confirmation handshakes, workflows, and troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can route agents to tools that write, send, spend wallet funds, store credentials, or delete data.

Mitigation: Require explicit user confirmation for those operations and review exact tool parameters before approval.

Risk: The skill requires a Danube API key that may grant access to connected services.

Mitigation: Install only when the publisher is trusted, use scoped keys where available, and keep returned or user-provided credentials out of chat history and later tool calls.

Risk: Plan limits, hosted AI caps, rate limits, or service kill switches can make calls fail in ways that resemble transient errors.

Mitigation: Read the returned status and message, tell the user when upgrade or waiting is required, and avoid retry loops for documented quota and disablement cases.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/danube/skills/tools-marketplace)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube documentation](https://docs.danubeai.com)
- [Danube REST API reference](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with inline bash, JSON, and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DANUBE_API_KEY and curl; outputs are procedural instructions and API call patterns for using Danube safely.]

## Skill Version(s):

8.1.9 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
