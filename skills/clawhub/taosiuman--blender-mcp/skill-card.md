## Description:

Connect to and control Blender via the official Blender MCP Server. Covers 20+ built-in tools plus arbitrary bpy code execution. Compatible with Blender 5.1, 5.2 LTS, and 5.3 Alpha.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taosiuman](https://clawhub.ai/user/taosiuman)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical artists use this skill to connect an agent to a local Blender session for scene inspection, rendering, navigation, documentation lookup, and controlled bpy automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables powerful local Blender and Python control through an agent connection.

Mitigation: Use it only for trusted workflows, prefer scoped built-in tools, and review raw execute_blender_code snippets before running them.

Risk: A broadly exposed Blender MCP server could allow unintended local control.

Mitigation: Keep the server bound to localhost or 127.0.0.1.

Risk: Rendering and code execution can create or modify files in local project locations.

Mitigation: Direct render outputs to a dedicated project or output folder and keep backups of important blend files.

## Reference(s):

- [Blender MCP Server](https://www.blender.org/lab/mcp-server/)
- [Blender MCP Releases](https://projects.blender.org/lab/blender_mcp/releases)
- [ClawHub Skill Page](https://clawhub.ai/taosiuman/skills/blender-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline bash, JSON, and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local Blender commands, MCP configuration, bpy snippets, and file output paths.]

## Skill Version(s):

2.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
