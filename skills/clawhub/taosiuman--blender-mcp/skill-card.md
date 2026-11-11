## Description:

Connect to a running Blender instance through Blender MCP to inspect scenes, capture screenshots, render, search documentation, or execute bpy code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taosiuman](https://clawhub.ai/user/taosiuman)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to connect an agent to a running Blender instance for scene inspection, screenshots, rendering, documentation lookup, and bpy tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The quick-install command selects a third-party PyPI implementation that differs from the Blender Lab implementation.

Mitigation: Verify the publisher and package source before installing; use Blender Lab's release or source when the official implementation is required.

Risk: Troubleshooting guidance suggests disabling HTTPS inspection for package downloads.

Mitigation: Prefer configuring the system trust store or approved enterprise CA; disable HTTPS inspection only with security administrator approval.

Risk: Code sent through bpy can read or change local files and make network requests.

Mitigation: Review code before execution, keep backups of important Blender projects, and keep the server bound to localhost.

## Reference(s):

- [Blender Lab MCP Server](https://www.blender.org/lab/mcp-server/)
- [Blender Lab MCP add-on release v1.0.3](https://projects.blender.org/lab/blender_mcp/releases/download/v1.0.3/mcp-1.0.3.zip)
- [Built-in tools](references/tools.md)
- [Communication protocol](references/protocol.md)
- [Blender API compatibility notes](references/api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Python and shell examples, JSON configuration, and Blender tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include scene summaries, screenshots, rendered images, or files returned by Blender tools.]

## Skill Version(s):

3.7.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
