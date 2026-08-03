## Description: <br>
DCC-MCP helps agents discover, inspect, and operate live Maya, Blender, Houdini, Photoshop, 3ds Max, Nuke, Unreal, Godot, RenderDoc, Substance 3D, and related DCC applications through structured DCC-MCP tools and CLI workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical artists, and agent operators use this skill to route DCC automation requests through DCC-MCP inventory, search, describe, load, and call workflows. It also guides marketplace skill discovery, installation, updates, setup troubleshooting, and safe fallback behavior for shell-capable agents and MCP-native IDE clients. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to control live DCC applications and modify active project state. <br>
Mitigation: Install it only when live DCC-MCP control is intended; inventory the target instance first, prefer structured DCC-MCP tools, and stop when no live instance is registered. <br>
Risk: Marketplace install/update and CLI setup workflows can change local state. <br>
Mitigation: Inspect marketplace packages before installation or update, obtain user consent before setup or mutation steps, and use the documented verified CLI bootstrap that checks the official manifest and SHA-256. <br>
Risk: Remote gateway profiles and raw debug reports can expose project or environment details. <br>
Mitigation: Review remote gateway targets before troubleshooting, use task-scoped gateway statistics when evidence is needed, and share only reviewed public-safe issue reports. <br>


## Reference(s): <br>
- [DCC-MCP ClawHub Package](https://clawhub.ai/loonghao/skills/dcc-mcp) <br>
- [DCC-MCP Homepage](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp/SKILL.md) <br>
- [CLI Cheatsheet](references/CLI_CHEATSHEET.md) <br>
- [Zero Instances CLI Setup Guide](references/ZERO_INSTANCES_CLI.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Markdown, Code] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent-facing workflows depend on available DCC instances, gateway profile state, and user consent for setup, install, update, or remote troubleshooting steps.] <br>

## Skill Version(s): <br>
0.19.90 (source: skill metadata and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
