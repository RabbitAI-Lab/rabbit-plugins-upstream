## Description:

Governed tool access for AI agents: one Danube API key unlocks an organization's own tools plus a large catalog of services over MCP or curl, with confirmation before actions that write, send, spend, or delete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Danube to discover, inspect, and run organization-approved tools, skills, and workflows through a single API key. The skill guides agents to search current capabilities, inspect schemas, request confirmation for sensitive actions, and report execution specifics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to execute tools that write, send, delete, spend funds, store credentials, or change workflows and skills.

Mitigation: Require explicit user confirmation with the exact tool and parameters before any sensitive action, and honor Danube confirmation tokens only after that consent.

Risk: Tool tasks and connected-service data may be processed by Danube or third-party services reached through Danube.

Mitigation: Install only when Danube is trusted for the requested tasks, pass only the required parameters, and use scoped API keys and spending limits where available.

Risk: Credential setup can expose or store live secrets if handled carelessly.

Mitigation: Prefer dashboard or OAuth setup, store only credentials the user explicitly provides and confirms, and avoid echoing secrets in later prompts or tool parameters.

## Reference(s):

- [OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube documentation](https://docs.danubeai.com)
- [Danube MCP server](https://mcp.danubeai.com/mcp)
- [REST API reference](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration instructions, Markdown]

**Output Format:** [Markdown with inline shell commands, JSON snippets, and REST or MCP usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DANUBE_API_KEY and curl; instructs agents to get explicit consent before state-changing, credential, spending, batch, skill, or workflow actions.]

## Skill Version(s):

8.1.8 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
