## Description:

Connect to and control Blender via the official Blender MCP Server. Covers 20+ built-in tools plus arbitrary bpy code execution. Compatible with Blender 5.1, 5.2 LTS, and 5.3 Alpha.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taosiuman](https://clawhub.ai/user/taosiuman)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical artists use this skill to connect an agent to a local Blender MCP Server for scene inspection, rendering, navigation, documentation lookup, and controlled execution of Blender Python snippets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes arbitrary Blender Python execution through an unsandboxed local MCP channel.

Mitigation: Run it only in a controlled local environment, keep the service bound to localhost, and review every generated Python snippet before execution.

Risk: Installation paths and package retrieval may be unpinned.

Mitigation: Prefer pinned versions and trusted package sources, and avoid pipe-to-shell installers unless they have been reviewed.

Risk: Generated Blender actions can modify or damage project files.

Mitigation: Use disposable copies or backups of important .blend files before running generated code.

## Reference(s):

- [ClawHub blender-mcp skill page](https://clawhub.ai/taosiuman/skills/blender-mcp)
- [Blender MCP Server](https://www.blender.org/lab/mcp-server/)
- [Blender MCP add-on release ZIP](https://projects.blender.org/lab/blender_mcp/releases/download/v1.0.0/mcp-1.0.0.zip)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, Python snippets, JSON examples, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Blender Python snippets and local MCP or mcporter commands that require user review before execution.]

## Skill Version(s):

2.5.4 (source: frontmatter, release evidence, README.md, release_notes_v2.5.4.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
