## Description:

Ground answers about Azure, .NET, Microsoft 365, Power Platform, Entra ID, Windows and SQL Server in official Microsoft Learn docs and code samples, through Microsoft's free Learn MCP server (native OpenClaw MCP, no API key). Use when the user asks about a Microsoft product, service, API or CLI, or wants an answer checked against Microsoft Learn.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ricardodpalmeida](https://clawhub.ai/user/ricardodpalmeida)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and engineers can use this skill to answer questions about Microsoft products with current Microsoft Learn documentation and official code samples. It helps agents search and cite relevant sources, fetch focused documentation when needed, and provide grounded guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries are sent to Microsoft and could disclose sensitive or proprietary details.

Mitigation: Keep queries generic; do not include secrets, customer names, tenant IDs, or proprietary code.

Risk: Persistent MCP setup changes the user's OpenClaw configuration.

Mitigation: Prefer an existing MCP connection and obtain user approval before registering a persistent server.

Risk: The CLI fallback runs a downloaded npm package.

Mitigation: Use the version pinned by the skill, @microsoft/learn-cli 1.0.0, and update it deliberately.

## Reference(s):

- [Microsoft Learn MCP reference](references/mcp-details.md)
- [Microsoft Learn MCP endpoint](https://learn.microsoft.com/api/mcp)
- [MicrosoftDocs MCP project](https://github.com/MicrosoftDocs/mcp)
- [Microsoft Learn documentation](https://learn.microsoft.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with citations and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cites Microsoft Learn URLs; the workflow searches first and fetches at most two pages per question.]

## Skill Version(s):

1.1.2 (source: CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
