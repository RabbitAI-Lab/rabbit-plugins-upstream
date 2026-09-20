## Description:

Connect to and control Blender via the official Blender MCP Server, including built-in scene tools and arbitrary bpy code execution for Blender 5.1, 5.2 LTS, and 5.3 Alpha.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taosiuman](https://clawhub.ai/user/taosiuman)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, technical artists, and automation-focused Blender users use this skill to connect an agent to a local Blender MCP Server for scene inspection, navigation, rendering, documentation search, and controlled bpy automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can execute unsandboxed Python inside Blender through raw execute_blender_code or direct socket workflows.

Mitigation: Keep the server bound to localhost, review generated code before execution, and prefer scoped built-in tools when full bpy access is not required.

Risk: Agent actions can modify Blender scenes, assets, render outputs, or export paths.

Mitigation: Use backups for important .blend files and choose safe, explicit output paths for renders and exports.

Risk: The workflow depends on local Blender MCP and mcporter components.

Mitigation: Install only trusted packages, prefer pinned package versions, and verify the Blender MCP package path before enabling automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/taosiuman/skills/blender-skill)
- [Server-resolved source repository](https://github.com/taosiuman/blender-skill)
- [Server-resolved source commit](https://github.com/taosiuman/blender-skill/commit/469917697ddbcb6c7aeddba9671b0ba8c020d44b)
- [Blender MCP Server](https://www.blender.org/lab/mcp-server/)
- [Blender MCP addon release](https://projects.blender.org/lab/blender_mcp/releases/download/v1.0.0/mcp-1.0.0.zip)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, API calls]

**Output Format:** [Markdown with inline shell, Python, JSON, and MCP command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Blender MCP commands, bpy snippets, JSON request and response examples, render or export paths, and security guidance.]

## Skill Version(s):

2.5.7 (source: server release metadata; artifact frontmatter lists 2.5.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
