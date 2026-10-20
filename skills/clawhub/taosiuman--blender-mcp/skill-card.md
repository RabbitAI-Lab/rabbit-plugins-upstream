## Description:

Connects an agent to a running Blender instance for scene inspection, rendering, navigation, documentation lookup, and bpy code execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taosiuman](https://clawhub.ai/user/taosiuman)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and 3D artists use the skill to inspect and control an active Blender session, automate scene tasks, render or capture results, and troubleshoot Blender workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation instructions combine Blender components with a third-party executable server, so the intended package pairing may be unclear.

Mitigation: Resolve the exact server package and add-on pairing against the official Blender MCP documentation before following quick-start commands.

Risk: Executing bpy code can affect Blender projects and access local files or network resources.

Mitigation: Keep connections local, review generated Python before execution, back up important projects, and disable telemetry if desired.

## Reference(s):

- [Blender MCP Server](https://www.blender.org/lab/mcp-server/)
- [ClawHub Blender MCP release](https://clawhub.ai/taosiuman/skills/blender-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Python, shell command, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bpy code and commands for controlling a Blender session.]

## Skill Version(s):

3.5.0 (source: server-resolved release metadata, SKILL.md frontmatter, and README changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
