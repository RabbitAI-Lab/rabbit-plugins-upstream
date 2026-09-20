## Description:

mcp-config helps agents add, move, format, catalog, and diagnose MCP server configuration across Claude Code, Cursor, and Antigravity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to configure MCP servers, choose local/user/project scopes, validate JSON formats, move servers between scopes, and troubleshoot connection failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide persistent changes to agent MCP configuration.

Mitigation: Review proposed scope, file path, and server name before applying changes, and reload or reconnect the agent only after confirming the intended configuration.

Risk: Some catalog examples run external packages with npx or uvx, including unpinned package references.

Mitigation: Pin package versions where possible and verify package publishers before running generated commands.

Risk: MCP configuration and debug logs may contain secrets, local paths, or machine-specific settings.

Mitigation: Avoid committing secrets or machine-specific paths to project configuration, and treat agent config files and debug logs as sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/mcp-config)
- [CHANGELOG 0.3.3](artifact/CHANGELOG.md)
- [Add MCP Server](artifact/add.md)
- [MCP Server Catalog](artifact/catalog.md)
- [MCP Server Connection Diagnostics](artifact/diagnostics.md)
- [MCP Server Format](artifact/format.md)
- [Move MCP Server](artifact/move.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose persistent agent configuration changes and external package execution commands.]

## Skill Version(s):

0.3.3 (source: server release metadata and changelog, released 2026-09-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
