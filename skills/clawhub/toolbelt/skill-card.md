## Description:

Toolbelt connects MCP-compatible agents to shared workspaces for document ingestion, entity extraction, and natural-language retrieval across structured and unstructured data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[toolbeltai](https://clawhub.ai/user/toolbeltai)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and teams use Toolbelt to ingest approved documents, query structured and unstructured data together, and share findings across agent sessions through an MCP-connected workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan flags possible access to MCP configuration files and account-claim behavior that may cross documented network and credential boundaries; analysis coverage is incomplete.

Mitigation: Review the account-claim and token instructions before installation, assess the required configuration access and credential scope, and account for incomplete analysis coverage.

Risk: Documents and findings persist in shared workspaces, and a share URL can grant access to that namespace.

Mitigation: Upload only user-approved, task-relevant content; avoid sensitive data unless specifically required; confirm sharing intent and recipients before creating a share link.

## Reference(s):

- [Toolbelt skill page](https://clawhub.ai/toolbeltai/skills/toolbelt)
- [Toolbelt website](https://toolbelt.ai)
- [Toolbelt documentation](https://toolbelt.ai/docs)
- [Toolbelt agent-readable documentation](https://toolbelt.ai/llms-full.txt)
- [Toolbelt human web app](https://app.toolbelt.ai)
- [Toolbelt MCP endpoint](https://mcp.toolbelt.ai/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands, API calls, Text]

**Output Format:** [Markdown instructions with shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before account provisioning or MCP configuration changes.]

## Skill Version(s):

1.1.9 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
