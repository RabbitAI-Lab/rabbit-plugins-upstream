## Description:

Helps users configure, authenticate, and use Google NotebookLM through the nlm CLI or an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to set up NotebookLM access, troubleshoot authentication, and configure CLI or MCP connections, including headless environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google session cookies and locally cached authentication grant broad account access if exposed.

Mitigation: Obtain explicit consent, prefer browser-based login, use a dedicated account, protect auth.json, and delete cookies.txt immediately after import.

Risk: The setup helper can persistently change multiple agent MCP configurations.

Mitigation: Review the proposed changes with --dry-run and target one agent with --platform before applying them.

Risk: The unofficial NotebookLM client may create account or service-access risk.

Mitigation: Have the user review and install a pinned client version themselves, and disclose potential rate limits or account suspension.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/afonsoft/skills/notebooklm-mcp)
- [Authentication guide](references/auth-guide.md)
- [MCP configuration guide](references/mcp-config.md)
- [Platform quirks](references/platform-quirks.md)
- [Upstream authentication documentation](https://github.com/jacob-bd/notebooklm-mcp-cli/blob/main/docs/AUTHENTICATION.md)
- [Upstream MCP documentation](https://github.com/jacob-bd/notebooklm-mcp-cli/blob/main/docs/MCP_GUIDE.md)
- [Upstream CLI documentation](https://github.com/jacob-bd/notebooklm-mcp-cli/blob/main/docs/CLI_GUIDE.md)
- [NotebookLM MCP CLI on PyPI](https://pypi.org/project/notebooklm-mcp-cli/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides setup and troubleshooting guidance; authentication requires user consent and a user-installed unofficial client.]

## Skill Version(s):

1.0.8 (source: ClawHub release; skill frontmatter lists 1.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
