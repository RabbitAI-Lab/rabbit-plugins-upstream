## Description:

Governed tool access for AI agents: one Danube API key unlocks an organization's own tools plus a large catalog of services over MCP or curl, with confirmation before actions that write, send, spend, or delete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to discover, inspect, and execute organization-approved tools through Danube while preserving consent checkpoints for sensitive, paid, credential, or destructive operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables broad tool access through a user-provided Danube key, including services connected to the user's account or organization.

Mitigation: Install only when the operator trusts Danube for connected tools, prefer OAuth or narrowly scoped API keys, and keep the Danube key secret.

Risk: Agent actions can write, send, spend, delete, store credentials, or run batches when a chosen tool supports those effects.

Mitigation: Require explicit user confirmation with the exact tool and parameters before sensitive, paid, destructive, credential, workflow, or batch execution.

Risk: Some credential-returning tools or deployment modes can expose unmasked live secrets in tool results.

Mitigation: Treat any unmasked credential as live secret material: do not echo it, log it, or pass it into later calls; direct the user to store it securely.

Risk: Catalog entries, tool availability, schemas, deprecations, and usage limits can change over time.

Mitigation: Search and inspect tools in the current session, read readiness and deprecation fields, avoid replaying stale IDs, and follow documented handling for plan limits or missing upstream tools.

## Reference(s):

- [Danube OpenClaw Guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube Documentation](https://docs.danubeai.com)
- [Danube REST API Reference](references/rest-api.md)
- [Danube Troubleshooting](references/troubleshooting.md)
- [Danube MCP Server](https://mcp.danubeai.com/mcp)
- [Danube API](https://api.danubeai.com/v1)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool names, REST endpoints, JSON request bodies, confirmation prompts, and execution reporting guidance.]

## Skill Version(s):

8.1.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
