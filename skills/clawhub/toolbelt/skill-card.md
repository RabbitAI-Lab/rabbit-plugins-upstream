## Description:

Toolbelt connects an MCP-compatible agent to shared workspaces for document extraction and hybrid search across structured and unstructured data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[toolbeltai](https://clawhub.ai/user/toolbeltai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use Toolbelt to ingest approved documents and query structured and unstructured data together through an MCP-compatible agent. Shared workspaces let agents carry relevant context across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Initial setup may access MCP client configuration and send account or verification information to app.toolbelt.ai.

Mitigation: Review the setup request and the configuration entry, and approve account provisioning and configuration changes before they occur.

Risk: Documents and findings saved to a shared workspace persist beyond the current session.

Mitigation: Upload only task-relevant, user-approved content and avoid sensitive data unless the user has explicitly chosen to use it with Toolbelt.

## Reference(s):

- [Toolbelt](https://toolbelt.ai)
- [Toolbelt documentation](https://toolbelt.ai/docs)
- [Complete Toolbelt documentation](https://toolbelt.ai/llms-full.txt)
- [Toolbelt web app](https://app.toolbelt.ai)
- [Toolbelt MCP endpoint](https://mcp.toolbelt.ai/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Structured data, Configuration instructions, Guidance]

**Output Format:** [Text or Markdown, with structured results returned by MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Depends on the user's connected Toolbelt workspace and permissions.]

## Skill Version(s):

1.1.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
