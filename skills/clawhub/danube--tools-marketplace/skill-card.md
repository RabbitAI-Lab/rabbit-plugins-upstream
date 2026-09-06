## Description:

Governed tool access for AI agents: one Danube API key unlocks an organization's private tools and a large catalog of services over MCP or REST, with confirmation before actions that write, send, spend, or delete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Danube to discover, inspect, and invoke organization-approved marketplace or private tools through MCP or REST while preserving confirmation steps for write, spend, delete, credential, and batch actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent broad access to tools connected to the user's Danube account.

Mitigation: Use a restricted Danube API key with service/tool limits and spending limits, and install it only when the agent is expected to operate through Danube.

Risk: Some tool calls can write, send, spend funds, delete data, store credentials, or execute batches.

Mitigation: Review the exact tool and parameters and require explicit user confirmation before these actions, including when a confirmation token is returned.

Risk: Credential-related tools or self-hosted paths can expose live secrets when automatic capture or redaction is not available.

Mitigation: Prefer dashboard or OAuth connection, avoid echoing raw secrets, and store only credentials the user explicitly provides and confirms.

Risk: Tool calls can send user or organization data to third-party services in the catalog.

Mitigation: Inspect tool schemas first, pass only task-required parameters, and do not forward unrelated personal or sensitive data.

## Reference(s):

- [Danube OpenClaw Guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube API Reference](https://docs.danubeai.com/api-reference/introduction)
- [Danube REST API Reference](references/rest-api.md)
- [Danube Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Markdown]

**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, and REST/MCP tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference Danube API keys, MCP configuration, tool schemas, confirmations, and execution results.]

## Skill Version(s):

8.1.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
