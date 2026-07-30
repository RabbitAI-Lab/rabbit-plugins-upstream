## Description: <br>
Infrastructure skill that guides developers and agents through creating or modernizing full DCC-MCP adapters for Nuke, Blender, 3ds Max, Unreal, ZBrush, Houdini, Maya, and custom studio tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create or modernize DCC-MCP adapters, including server composition, host-thread dispatch, gateway and sidecar wiring, readiness, resources, diagnostics, packaging, runtime integration, and cross-DCC validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide shell commands, code edits, and DCC-MCP tooling interactions that affect an adapter repository or developer environment. <br>
Mitigation: Use it only for DCC-MCP adapter development and review proposed commands, code, and configuration changes before execution. <br>
Risk: Generated adapter changes may touch UI-control, gateway, sidecar, memory, relay, or system-operation paths. <br>
Mitigation: Review those changes carefully and validate them in tests before running them in a real DCC host. <br>
Risk: Raw UI or system-operation workflows can be powerful if adapter boundaries are weakened. <br>
Mitigation: Preserve operator scoping, confirmation gates, typed bounded operations, and documented stop or resume behavior. <br>


## Reference(s): <br>
- [DCC-MCP Creator ClawHub Skill](https://clawhub.ai/loonghao/skills/dcc-mcp-creator) <br>
- [DCC-MCP Creator Source Homepage](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp-creator/SKILL.md) <br>
- [Adapter Workflow](references/ADAPTER_WORKFLOW.md) <br>
- [Host Pattern Matrix](references/HOST_PATTERN_MATRIX.md) <br>
- [Core Escalation Checklist](references/CORE_ESCALATION_CHECKLIST.md) <br>
- [Testing And Release](references/TESTING_AND_RELEASE.md) <br>
- [DCC-MCP Skill](https://clawhub.ai/loonghao/skills/dcc-mcp) <br>
- [DCC-MCP Skills Creator](https://clawhub.ai/loonghao/skills/dcc-mcp-skills-creator) <br>
- [RFC: Adapter Skill-Load Transform Hooks](https://github.com/dcc-mcp/dcc-mcp-core/issues/1204) <br>
- [RFC: Public DccServerBase Resource Registration Surface](https://github.com/dcc-mcp/dcc-mcp-core/issues/1205) <br>
- [RFC: Reusable Adapter Readiness Binder](https://github.com/dcc-mcp/dcc-mcp-core/issues/1206) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with code, configuration, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose adapter code, configuration changes, validation commands, and release checklist items for DCC-MCP adapter repositories.] <br>

## Skill Version(s): <br>
0.19.87 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
