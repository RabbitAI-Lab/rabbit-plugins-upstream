## Description:

Configure, verify, repair, or minimize Dataify MCP for Claude Desktop, Codex, Cursor, Windsurf, or another MCP client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure, verify, repair, or minimize a Dataify MCP server connection and select the smallest Dataify tool preset needed for a client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dataify API tokens may be written into MCP client configuration URLs and copied into backup files.

Mitigation: Use a limited-scope token where possible, review generated configuration and backup files, avoid pasting tokens into chat, and rotate the token after testing.

Risk: Bundled workflow and task-polling scripts can run Dataify scraping or search workflows beyond MCP setup.

Mitigation: Invoke only the MCP configuration and verification path unless you separately intend to run those Dataify workflows, and review the skill before installation.

## Reference(s):

- [Dataify documentation](https://doc.dataify.com)
- [Dataify support](https://www.dataify.com/)
- [Tool presets](references/tool-presets.md)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce redacted configuration previews, token setup guidance, MCP verification results, and configuration file updates when explicitly requested.]

## Skill Version(s):

1.1.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
