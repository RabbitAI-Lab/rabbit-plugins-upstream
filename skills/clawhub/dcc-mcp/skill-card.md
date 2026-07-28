## Description: <br>
DCC-MCP routes agents through dcc-mcp-cli or gateway MCP tools to discover, inspect, and operate live DCC applications and marketplace skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical artists, and agent operators use DCC-MCP to route DCC automation requests through live instance inventory, capability search, schema inspection, and guarded calls for applications such as Maya, Blender, Houdini, Photoshop, 3ds Max, Nuke, Unreal, Godot, RenderDoc, and Substance 3D. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate live DCC applications through dcc-mcp-cli or a configured gateway. <br>
Mitigation: Confirm the intended DCC instance and operation before tool calls; use the inventory, search, describe, and guarded call sequence rather than direct scripting. <br>
Risk: CLI, adapter, marketplace install, or update actions can change local state. <br>
Mitigation: Require explicit user consent, inspect the returned plan or package first, and rely on the documented verified manifest and SHA-256 checks for CLI bootstrap. <br>
Risk: Remote gateway profiles extend control to another machine. <br>
Mitigation: Use remote profiles only for trusted machines and stop for unreachable gateways until the user approves troubleshooting. <br>
Risk: Direct local calls may not appear in gateway stats or skill reflection evidence. <br>
Mitigation: Use --require-gateway with a stable --agent-session-id when measured evidence is required, and do not treat zero stats as proof that no calls occurred. <br>


## Reference(s): <br>
- [ClawHub DCC-MCP skill page](https://clawhub.ai/loonghao/skills/dcc-mcp) <br>
- [DCC-MCP source skill homepage](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp/SKILL.md) <br>
- [CLI cheatsheet](references/CLI_CHEATSHEET.md) <br>
- [Zero instances CLI setup guide](references/ZERO_INSTANCES_CLI.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with bash command examples and JSON arguments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands and tool calls are selected through inventory, search, describe, and call workflows; install, update, and setup actions require user consent.] <br>

## Skill Version(s): <br>
0.19.83 (source: evidence release and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
