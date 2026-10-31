## Description:

Grounds Microsoft product and development answers in current Microsoft Learn documentation and code samples. Use for Azure, .NET, Microsoft 365, Power Platform, Entra ID, Windows, SQL Server, APIs, SDKs, CLI commands, or explicit Learn verification. Supports native OpenClaw MCP and CLI fallbacks; no API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ricardodpalmeida](https://clawhub.ai/user/ricardodpalmeida)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to answer Microsoft product and development questions with current Learn documentation and code samples, then cite the supporting source pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and requested documentation URLs are sent to Microsoft and may disclose information included in them.

Mitigation: Use generic queries and exclude secrets, tenant or customer identifiers, and proprietary code.

Risk: The optional CLI fallback runs downloaded software.

Mitigation: Use the documented pinned Microsoft Learn CLI version and run the fallback only when needed.

Risk: Persistent MCP registration changes local configuration.

Mitigation: Register persistent MCP configuration only during setup you authorize.

## Reference(s):

- [Project homepage](https://github.com/Ricardodpalmeida/openclaw-mslearn-mcp)
- [Microsoft Learn MCP server](https://github.com/MicrosoftDocs/mcp)
- [Microsoft Learn MCP endpoint](https://learn.microsoft.com/api/mcp)
- [Microsoft Learn MCP release notes](https://learn.microsoft.com/en-us/training/support/mcp-release-notes)
- [Microsoft Learn CLI](https://www.npmjs.com/package/@microsoft/learn-cli)
- [OpenClaw MCP registry documentation](https://docs.openclaw.ai/cli/mcp/registry)
- [MCP setup and recovery](references/mcp-details.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Text or Markdown with source citations and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation excerpts, source URLs, and relevant code samples; cite pages used and identify unresolved evidence gaps.]

## Skill Version(s):

1.1.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
