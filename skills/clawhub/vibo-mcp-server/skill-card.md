## Description:

Local-first memory for AI agents over MCP: persistent memory (L1/L2/L3), web-search savings, thread memory. Works with Claude Desktop, Cursor, OpenClaw, Windsurf, Codex. Requires a valid ViBo license. Everything is stored locally on the user's machine; use ONLY with the user's explicit consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vnbochkarev-netizen](https://clawhub.ai/user/vnbochkarev-netizen)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to add a local MCP memory service to compatible AI clients, enabling approved facts and thread context to persist across sessions. It is intended for users who want agent memory stored on their own machine with a required ViBo license key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persists agent memory locally, which can retain sensitive or unwanted facts if used without deliberate consent.

Mitigation: Store only facts the user explicitly approves, explain what will be stored before writing memory, and confirm the local .web files can be deleted or wiped later.

Risk: The external npm MCP server package could change or be resolved unexpectedly if installation is not pinned.

Mitigation: Use the pinned package version, verify package integrity and changelog before installation, and prefer a controlled one-time install over recurring npx resolution.

Risk: The ViBo license key is required for operation and could be exposed if broadly shared across processes.

Mitigation: Scope VIBO_API_KEY to the MCP client process and avoid storing it in shared or unrelated environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/vnbochkarev-netizen/skills/vibo-mcp-server)
- [ViBo Site](https://wwwvibo.com)
- [ViBo Documentation](https://github.com/vnbochkarev-netizen/ViBo-memory)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ViBo API key and a pinned MCP server package version for installation.]

## Skill Version(s):

0.2.6 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
