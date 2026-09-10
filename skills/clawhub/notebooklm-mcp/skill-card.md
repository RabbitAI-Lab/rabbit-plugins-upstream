## Description:

Helps agents configure and use Google NotebookLM through the third-party `nlm` CLI and `notebooklm-mcp` MCP server, including cookie-based authentication, headless setup, platform-specific MCP configuration, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to connect AI agents to NotebookLM through the `nlm` CLI or MCP server, especially on headless systems or when MCP clients fail to list NotebookLM tools. It guides installation, authentication, configuration, verification, and troubleshooting across common agent platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles live Google session cookies through `cookies.txt` and cached `auth.json` files.

Mitigation: Require explicit user consent before cookie extraction or import, run login commands as black-box operations, keep credential files private with restrictive permissions, and delete temporary cookie files after successful import.

Risk: The setup helper can persistently modify multiple agent MCP configuration files.

Mitigation: Use `--dry-run` first, target a single platform with `--platform` where possible, and review the proposed configuration before applying changes.

Risk: NotebookLM access relies on an unofficial third-party client with access to a Google browser session.

Mitigation: Pin and verify the `notebooklm-mcp-cli` package version, review the upstream project before installation, and prefer a dedicated Google account or isolated browser profile.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/notebooklm-mcp)
- [Publisher profile](https://clawhub.ai/user/afonsoft)
- [notebooklm-mcp-cli project](https://github.com/jacob-bd/notebooklm-mcp-cli)
- [notebooklm-mcp-cli PyPI package](https://pypi.org/project/notebooklm-mcp-cli/)
- [Authentication guide](https://github.com/jacob-bd/notebooklm-mcp-cli/blob/main/docs/AUTHENTICATION.md)
- [MCP guide](https://github.com/jacob-bd/notebooklm-mcp-cli/blob/main/docs/MCP_GUIDE.md)
- [CLI guide](https://github.com/jacob-bd/notebooklm-mcp-cli/blob/main/docs/CLI_GUIDE.md)
- [Artifact authentication reference](references/auth-guide.md)
- [Artifact MCP configuration reference](references/mcp-config.md)
- [Artifact platform quirks reference](references/platform-quirks.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local CLI commands, MCP client configuration changes, and credential-handling steps for user review.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
