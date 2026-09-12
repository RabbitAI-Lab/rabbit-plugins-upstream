## Description:

This skill helps agents configure, authenticate, and use Google NotebookLM through the third-party nlm CLI and NotebookLM MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to install and verify the unofficial NotebookLM CLI, authenticate NotebookLM on desktop or headless systems, and configure MCP clients for NotebookLM notebook operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an unofficial NotebookLM client that can access reusable Google session cookies.

Mitigation: Use the skill only with explicit user consent, prefer desktop login or a dedicated Google/browser profile, avoid manual cookie files unless necessary, delete cookies.txt immediately after import, and restrict auth.json permissions.

Risk: The setup helper can modify MCP configuration for multiple agent platforms.

Mitigation: Run the setup helper with --dry-run first and use --platform to target one specific client before applying changes.

Risk: Installing or running an unpinned unofficial CLI can expose users to unexpected upstream behavior.

Mitigation: Verify the package source before installation and install notebooklm-mcp-cli with an explicit pinned version.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/notebooklm-mcp)
- [Publisher skills repository](https://github.com/afonsoft/skills)
- [notebooklm-mcp-cli repository](https://github.com/jacob-bd/notebooklm-mcp-cli)
- [notebooklm-mcp-cli authentication documentation](https://github.com/jacob-bd/notebooklm-mcp-cli/blob/main/docs/AUTHENTICATION.md)
- [notebooklm-mcp-cli MCP guide](https://github.com/jacob-bd/notebooklm-mcp-cli/blob/main/docs/MCP_GUIDE.md)
- [notebooklm-mcp-cli CLI guide](https://github.com/jacob-bd/notebooklm-mcp-cli/blob/main/docs/CLI_GUIDE.md)
- [notebooklm-mcp-cli PyPI package](https://pypi.org/project/notebooklm-mcp-cli/)
- [Artifact authentication guide](references/auth-guide.md)
- [Artifact MCP configuration reference](references/mcp-config.md)
- [Artifact platform quirks reference](references/platform-quirks.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include platform-specific MCP configuration changes, authentication checks, and troubleshooting steps.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
