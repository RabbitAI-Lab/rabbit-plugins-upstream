## Description:

Connect to and control Blender via the official Blender MCP Server, including built-in scene tools and arbitrary Blender Python execution for Blender 5.1, 5.2 LTS, and 5.3 Alpha workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taosiuman](https://clawhub.ai/user/taosiuman)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical artists, and automation engineers use this skill to connect an agent to a local Blender MCP Server for scene inspection, viewport capture, rendering, documentation lookup, and Blender Python workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enable unsandboxed Python execution inside Blender with local user privileges.

Mitigation: Keep the MCP server bound to localhost, prefer scoped built-in tools over arbitrary code execution, review generated code before running it, and back up important .blend files.

Risk: Mutable install steps and latest-version package commands can change what is installed over time.

Mitigation: Use pinned or verified package versions and review pipe-to-shell or auto-download install commands before use.

Risk: Auto Start can make Blender accept local MCP control whenever Blender opens.

Mitigation: Enable Auto Start only when needed and confirm the host and port remain local.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/taosiuman/skills/blender-mcp)
- [Publisher profile](https://clawhub.ai/user/taosiuman)
- [Official Blender MCP Server](https://www.blender.org/lab/mcp-server/)
- [Blender MCP addon release](https://projects.blender.org/lab/blender_mcp/releases/download/v1.0.0/mcp-1.0.0.zip)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON configuration, and Python or Blender code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended for local Blender and MCP workflows and may include commands or code that require user review before execution.]

## Skill Version(s):

2.5.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
