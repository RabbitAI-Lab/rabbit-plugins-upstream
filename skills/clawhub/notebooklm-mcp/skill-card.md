## Description:

notebooklm-mcp helps agents configure, authenticate, troubleshoot, and use Google NotebookLM through the unofficial `nlm` CLI and `notebooklm-mcp` MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to set up NotebookLM access through the `nlm` CLI or an MCP server, especially on headless systems and MCP clients such as Claude Code, Cursor, Devin, Gemini CLI, OpenCode, and OpenClaw. It also guides authentication repair, cookie handling, platform-specific MCP configuration, and verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an unofficial NotebookLM client that depends on reusable Google session cookies.

Mitigation: Use a dedicated or least-sensitive Google account, require user consent before cookie extraction or import, keep credential files out of projects and backups, set restrictive file permissions, and delete temporary cookie files after import.

Risk: Setup guidance and helper scripts can modify agent MCP configuration files.

Mitigation: Run setup in dry-run mode or target a single platform first, review configuration changes before restarting the agent, and remove the server entry if the wrong client was configured.

Risk: HTTP or SSE MCP transport can expose NotebookLM access if made reachable without protection.

Mitigation: Prefer local stdio transport; do not expose HTTP transport unless a reverse proxy provides TLS, authentication, and access controls.

Risk: Installing an unpinned package version could pull an unexpected upstream release.

Mitigation: Pin and verify the `notebooklm-mcp-cli` package version from PyPI and the upstream project before installation.

## Reference(s):

- [NotebookLM authentication guide](references/auth-guide.md)
- [NotebookLM MCP configuration reference](references/mcp-config.md)
- [MCP platform configuration quirks](references/platform-quirks.md)
- [notebooklm-mcp-cli project](https://github.com/jacob-bd/notebooklm-mcp-cli)
- [notebooklm-mcp-cli authentication documentation](https://github.com/jacob-bd/notebooklm-mcp-cli/blob/main/docs/AUTHENTICATION.md)
- [notebooklm-mcp-cli MCP guide](https://github.com/jacob-bd/notebooklm-mcp-cli/blob/main/docs/MCP_GUIDE.md)
- [notebooklm-mcp-cli CLI guide](https://github.com/jacob-bd/notebooklm-mcp-cli/blob/main/docs/CLI_GUIDE.md)
- [notebooklm-mcp-cli on PyPI](https://pypi.org/project/notebooklm-mcp-cli/)
- [afonsoft skills collection](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include platform-specific setup steps, authentication checks, and security handling guidance.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
