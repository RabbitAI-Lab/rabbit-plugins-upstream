## Description:

DCC-MCP helps agents connect to and operate live DCC applications such as Maya, Blender, Houdini, Photoshop, 3ds Max, Nuke, Unreal, Godot, RenderDoc, and Substance 3D through structured DCC-MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical artists, and agent operators use this skill to route DCC-control requests, discover live DCC instances or marketplace skills, and execute approved operations through DCC-MCP CLI or gateway tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect and control live DCC sessions and may modify open projects through local or configured remote gateways.

Mitigation: Use the documented inventory, search, consent, and post-step verification flow before executing actions that affect a DCC session.

Risk: Installation, update, marketplace, remote gateway registration, and UI-control fallback workflows can change local state or broaden control scope.

Mitigation: Require explicit user approval for these workflows and review prompts carefully before proceeding.

Risk: Missing or unavailable live DCC instances can lead to incorrect fallback behavior if the workflow is bypassed.

Mitigation: Stop on zero inventory and follow the zero-instance setup guide only after explicit user approval.

## Reference(s):

- [CLI cheatsheet](references/CLI_CHEATSHEET.md)
- [Zero instances CLI setup guide](references/ZERO_INSTANCES_CLI.md)
- [DCC-MCP source skill homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp/SKILL.md)
- [ClawHub package page](https://clawhub.ai/loonghao/skills/dcc-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with shell command examples and structured CLI/MCP call instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing commands may return compact text or JSON depending on the documented CLI mode.]

## Skill Version(s):

0.19.92 (source: evidence.release.version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
