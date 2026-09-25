## Description:

Governed tool access for AI agents: one Danube API key lets an agent search, inspect, and execute an organization's tools and a catalog of services over MCP or curl, with confirmation guidance for actions that write, send, spend, store credentials, or delete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and employees use this skill to give an agent governed access to Danube-discovered tools, service schemas, execution APIs, workflow operations, wallet controls, and troubleshooting guidance. It is intended for tasks that need tool discovery, tool execution, REST or MCP setup, credential configuration, and careful reporting of results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can broker access to broad external tools and organization-specific services.

Mitigation: Use a scoped Danube API key and search, inspect, and report the exact tool and parameters before execution.

Risk: Tool calls may write, send, delete, spend funds, store credentials, change limits, or run workflows.

Mitigation: Get explicit user confirmation before these actions, before any batch execution, and before storing credentials or changing wallet and spending settings.

Risk: Danube profile data and past-call examples can contain personal or task-specific information.

Mitigation: Apply least-data handling: read only what the task needs and do not forward unrelated profile data or copied example values into third-party tool parameters.

Risk: Paid tools, rate limits, and plan caps can cause refusals or unexpected cost-related decisions.

Mitigation: Read pricing and limit messages carefully, tell the user the cost or limit that applies, and do not retry or raise limits unless the user asks for that specific action.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube REST API reference](references/rest-api.md)
- [Danube troubleshooting](references/troubleshooting.md)
- [ClawHub skill listing](https://clawhub.ai/danube/skills/tools-marketplace)
- [Danube MCP server](https://mcp.danubeai.com/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl commands, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DANUBE_API_KEY for authenticated Danube calls; curl is required for the REST workflow, and MCP setup is optional.]

## Skill Version(s):

8.1.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
