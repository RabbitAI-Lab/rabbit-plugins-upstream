## Description: <br>
DCC-MCP connects agents to live DCC applications such as Maya, Blender, Houdini, Photoshop, 3ds Max, Nuke, Unreal, Godot, RenderDoc, and Substance 3D through structured DCC-MCP tools and CLI workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical artists, and agent operators use this skill to discover live DCC instances, route DCC tasks to structured tools, find marketplace skills, and invoke safe CLI or gateway workflows for scene and content operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct an agent to control live DCC applications and affect active scenes. <br>
Mitigation: Inventory live instances first, use structured discovery before calls, and verify results after operations. <br>
Risk: CLI installation, adapter execution, marketplace install or update, remote gateway profile use, and daemon lifecycle commands can change local state. <br>
Mitigation: Obtain explicit user consent before these actions and follow the documented consent-gated workflows. <br>
Risk: Direct local calls may not provide complete gateway statistics for post-task evidence. <br>
Mitigation: Use --require-gateway with a stable --agent-session-id when measured evidence or skill reflection is required. <br>


## Reference(s): <br>
- [DCC-MCP ClawHub Package](https://clawhub.ai/loonghao/skills/dcc-mcp) <br>
- [DCC-MCP Skill Homepage](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp/SKILL.md) <br>
- [CLI Cheatsheet](references/CLI_CHEATSHEET.md) <br>
- [Zero Instances CLI Setup Guide](references/ZERO_INSTANCES_CLI.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent-facing commands may produce JSON or compact text output depending on CLI flags; setup, install, update, remote profile, and daemon actions require user consent.] <br>

## Skill Version(s): <br>
0.19.89 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
