## Description:

Governed tool access for AI agents — one Danube API key unlocks your organization's own tools plus a large, growing catalog of services, over MCP or curl, with confirmation before anything that writes, sends, spends, or deletes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and agent operators use Danube to discover, inspect, and call organization-approved tools through MCP or REST while preserving consent checks for actions that write, send, spend, delete, store credentials, or change workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill brokers broad access to Danube-connected tools, including actions that can write, send, spend, delete, store credentials, or modify skills and workflows.

Mitigation: Review exact tool names and parameters before approval, require explicit user confirmation for sensitive actions, and report what was executed and returned.

Risk: Credential handling can expose or misuse third-party secrets if raw keys are accepted or references are used on unsupported execution paths.

Mitigation: Prefer dashboard or OAuth connection when available; only store credentials the user explicitly provides and confirms, and use references only where the deployment supports resolution.

Risk: A long-running workflow may still be running after a timeout or running response, and re-running it can duplicate writes or exhaust limits.

Mitigation: Poll the existing execution when an execution ID is available, supply a fresh execution ID for REST workflow runs, and avoid re-posting the same workflow after timeouts.

Risk: Truncated tool responses can look malformed or incomplete, especially for large JSON or text payloads.

Mitigation: Check truncation metadata, request a larger response limit or follow cursors where available, and do not report a tool as broken solely because a response was intentionally trimmed.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [ClawHub Danube skill page](https://clawhub.ai/danube/skills/tools-marketplace)
- [REST API reference](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)
- [Danube API documentation](https://docs.danubeai.com/api-reference/introduction)
- [Danube MCP endpoint](https://mcp.danubeai.com/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Text]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and REST/MCP call patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DANUBE_API_KEY and curl; sensitive actions require explicit user confirmation before execution.]

## Skill Version(s):

8.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
