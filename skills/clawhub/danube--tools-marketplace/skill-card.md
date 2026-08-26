## Description:

Danube lets agents search, inspect, and execute an organization's tools and catalog services over MCP or curl, with explicit confirmation before actions that write, send, spend, delete, or store credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to give agents governed access to organization tools, public catalog services, skills, workflows, ratings, and wallet controls through Danube. It is intended for agent workflows that need discovery, schema inspection, execution, and clear reporting around tool calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to execute tools that send, write, delete, spend funds, store credentials, or modify skills and workflows.

Mitigation: Require explicit user confirmation with the exact tool name and parameters before those actions or any batch execution.

Risk: A broad Danube API key may expose connected services, wallet funds, and organization tools to agent-mediated actions.

Mitigation: Install only when Danube is trusted, review key permissions and spending limits, and prefer scoped keys where possible.

Risk: Stale tool IDs or changed tool schemas could cause incorrect calls.

Mitigation: Search and inspect the current tool schema before execution, ask for missing required values, and do not reuse tool IDs from memory.

Risk: Credential handling can expose sensitive third-party access if done without clear user intent.

Mitigation: Prefer the Danube dashboard or OAuth flow, and only store credentials explicitly provided by the user after confirmation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/danube/skills/tools-marketplace)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube documentation](https://docs.danubeai.com)
- [Danube API reference](https://docs.danubeai.com/api-reference/introduction)
- [Danube over plain HTTP](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with bash, JSON, and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DANUBE_API_KEY and curl; tool execution should be confirmed before write, send, delete, spend, credential, skill, workflow, or batch actions.]

## Skill Version(s):

8.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
