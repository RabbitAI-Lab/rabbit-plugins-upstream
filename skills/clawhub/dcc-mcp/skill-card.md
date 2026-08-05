## Description: <br>
DCC-MCP routes agents to DCC-MCP CLI or MCP workflows for controlling live Maya, Blender, Houdini, Photoshop, 3ds Max, Nuke, Unreal, Godot, RenderDoc, Substance 3D, and related marketplace skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical artists, and agent operators use this skill to discover live DCC instances, search or invoke structured DCC capabilities, and manage DCC-MCP marketplace skill packages with consent-gated setup and update steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct an agent to operate live DCC applications and affect important project files. <br>
Mitigation: Use it only for intended DCC automation tasks and review prompts carefully before allowing changes to live applications or project files. <br>
Risk: The skill can guide local installs, updates, adapter execution, gateway profile changes, or remote gateway use. <br>
Mitigation: Require explicit user consent before those actions and follow the documented consent-gated setup and update paths. <br>


## Reference(s): <br>
- [DCC-MCP Skill Page](https://clawhub.ai/loonghao/skills/dcc-mcp) <br>
- [DCC-MCP Source Skill](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp/SKILL.md) <br>
- [CLI cheatsheet](references/CLI_CHEATSHEET.md) <br>
- [Zero instances CLI setup guide](references/ZERO_INSTANCES_CLI.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent-facing workflow guidance; command outputs may be JSON or compact text depending on CLI flags.] <br>

## Skill Version(s): <br>
0.19.91 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
