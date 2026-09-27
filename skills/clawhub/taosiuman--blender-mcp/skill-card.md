## Description:

Connect to and control Blender via the official Blender MCP Server. Covers 20+ built-in tools plus arbitrary bpy code execution. Compatible with Blender 5.1, 5.2 LTS, and 5.3 Alpha.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taosiuman](https://clawhub.ai/user/taosiuman)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical artists, and agent operators use this skill to connect an agent to a local Blender MCP Server for scene inspection, rendering, documentation search, and Blender Python automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-generated Blender Python can read, modify, or delete local files and alter project data.

Mitigation: Review generated Python before execution, prefer scoped built-in MCP tools when possible, and keep backups of important .blend files.

Risk: Exposing the Blender MCP server beyond the local machine can broaden access to Blender automation.

Mitigation: Keep the server bound to localhost or 127.0.0.1 and do not bind it to 0.0.0.0.

Risk: Anonymous telemetry may be collected by default.

Mitigation: Set DISABLE_TELEMETRY=true when telemetry is not acceptable for the environment.

Risk: Unpinned or unofficial dependencies can change install-time behavior.

Mitigation: Use pinned versions and official downloads for uvx, pip packages, mcporter, and the Blender addon.

## Reference(s):

- [Blender MCP Server](https://www.blender.org/lab/mcp-server/)
- [Blender MCP Addon Release](https://projects.blender.org/lab/blender_mcp/releases/download/v1.0.0/mcp-1.0.0.zip)
- [ClawHub Skill Page](https://clawhub.ai/taosiuman/skills/blender-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON configuration, and Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent to invoke local Blender MCP tools and execute Blender Python after user review.]

## Skill Version(s):

2.5.9 (source: release evidence, frontmatter, README changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
