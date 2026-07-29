## Description: <br>
DCC-MCP lets agents discover, connect to, and operate live DCC applications such as Maya, Blender, Houdini, Photoshop, 3ds Max, Nuke, Unreal, Godot, RenderDoc, and Substance 3D through structured DCC-MCP tools and CLI workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, technical artists, and automation engineers use this skill to route DCC-control requests through dcc-mcp-cli or gateway MCP tools, inspect live DCC inventory, call supported capabilities, and search marketplace skills before recommending or installing them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run a high-authority DCC control workflow that changes live DCC scenes. <br>
Mitigation: Use inventory, search, describe, and explicit user intent before calls; review requested scene changes before execution. <br>
Risk: Setup, CLI install or update, remote gateway use, adapter install, marketplace install or update, replay, and UI-control fallback can change local state or interact with live applications. <br>
Mitigation: Require user approval before those actions and follow the documented consent-gated setup, verified manifest, SHA-256, and fallback checks. <br>
Risk: Gateway telemetry may be absent when local direct calls are used. <br>
Mitigation: Use --require-gateway with a stable --agent-session-id when gateway stats or skill reflection evidence is required. <br>
Risk: UI-control fallback and replay can act on the wrong target if scope or coordinates are stale. <br>
Mitigation: Bind the exact target, snapshot after each action, stop UI control when complete, and require fresh approval before replay. <br>


## Reference(s): <br>
- [Published ClawHub skill page](https://clawhub.ai/loonghao/skills/dcc-mcp) <br>
- [DCC-MCP homepage](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp/SKILL.md) <br>
- [CLI cheatsheet](references/CLI_CHEATSHEET.md) <br>
- [Zero instances CLI setup guide](references/ZERO_INSTANCES_CLI.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON and bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may contact local or configured remote DCC-MCP gateways and can modify live DCC scenes when the user authorizes the requested action.] <br>

## Skill Version(s): <br>
0.19.86 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
