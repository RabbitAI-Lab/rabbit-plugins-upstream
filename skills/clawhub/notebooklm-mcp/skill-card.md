## Description:

Use when the user wants to configure, authenticate, or use Google NotebookLM via the nlm CLI or MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure and troubleshoot Google NotebookLM access through the nlm CLI or a local NotebookLM MCP server, including authentication, platform-specific MCP setup, and verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an unofficial NotebookLM client that relies on Google session cookies.

Mitigation: Install only if that is acceptable, use a dedicated low-value Google account and isolated browser profile, and require explicit user consent before authentication.

Risk: Cookie files and cached auth data can expose a full Google session.

Mitigation: Do not log, share, commit, or transmit cookie values; delete cookies.txt immediately after import and keep the auth cache isolated.

Risk: The setup helper can persistently modify multiple agent MCP configuration files.

Mitigation: Back up MCP configs first, run setup with --dry-run, and target one client with --platform when possible.

Risk: Remote HTTP or SSE MCP transport lacks built-in HTTPS, caller authentication, and per-user account isolation.

Mitigation: Prefer local stdio transport; expose remote transport only behind TLS and caller authentication.

## Reference(s):

- [NotebookLM authentication deep dive](references/auth-guide.md)
- [NotebookLM MCP per-platform config reference](references/mcp-config.md)
- [MCP platform config quirks](references/platform-quirks.md)
- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/notebooklm-mcp)
- [Publisher profile](https://clawhub.ai/user/afonsoft)
- [Publisher skills repository](https://github.com/afonsoft/skills)
- [notebooklm-mcp-cli upstream repository](https://github.com/jacob-bd/notebooklm-mcp-cli)
- [notebooklm-mcp-cli authentication guide](https://github.com/jacob-bd/notebooklm-mcp-cli/blob/main/docs/AUTHENTICATION.md)
- [notebooklm-mcp-cli MCP guide](https://github.com/jacob-bd/notebooklm-mcp-cli/blob/main/docs/MCP_GUIDE.md)
- [notebooklm-mcp-cli CLI guide](https://github.com/jacob-bd/notebooklm-mcp-cli/blob/main/docs/CLI_GUIDE.md)
- [notebooklm-mcp-cli PyPI package](https://pypi.org/project/notebooklm-mcp-cli/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local setup and verification commands; cookie values should not be exposed.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
