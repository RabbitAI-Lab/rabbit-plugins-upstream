## Description:

Connects an agent to Blender for scene inspection, screenshots and rendering, API documentation lookup, and Python code execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taosiuman](https://clawhub.ai/user/taosiuman)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and 3D artists use the skill to connect an agent to Blender, inspect and manage scenes, render or capture views, and get help with Blender's Python API and compatibility issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The quick-start material combines the official Blender add-on with a separately published community server, which can make package identity and publisher unclear.

Mitigation: Confirm which server package belongs with the add-on, review installers and generated Python, keep the server local, and verify telemetry settings for the installed server.

Risk: Python code sent through bpy can access files and the network and can modify or damage Blender projects.

Mitigation: Review code before execution, prefer scoped tools where practical, keep the connection local, and back up important .blend files.

## Reference(s):

- [Official Blender MCP server](https://www.blender.org/lab/mcp-server/)
- [Official Blender MCP add-on release](https://projects.blender.org/lab/blender_mcp/releases/download/v1.0.3/mcp-1.0.3.zip)
- [ClawHub skill page](https://clawhub.ai/taosiuman/skills/blender-mcp)

## Skill Output:

**Output Type(s):** [Analysis, Code, Shell commands, Configuration instructions, Images]

**Output Format:** [Markdown guidance, code snippets, configuration examples, scene-inspection results, and rendered images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Code execution operates in the connected Blender instance; rendered outputs are saved to configured or tool-reported paths.]

## Skill Version(s):

3.5.1 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
