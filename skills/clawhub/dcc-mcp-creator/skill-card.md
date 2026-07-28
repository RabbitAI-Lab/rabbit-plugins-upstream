## Description: <br>
Guides developers and agents through creating or modernizing DCC-MCP adapters for DCC hosts such as Nuke, Blender, 3ds Max, Unreal, ZBrush, Houdini, Maya, and custom studio tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to scaffold, review, and modernize DCC-MCP adapter repositories, including server composition, host-thread dispatch, gateway wiring, packaging, runtime integration, validation, and release checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill grants agents shell and file-editing authority for adapter development work. <br>
Mitigation: Use it in repositories where code changes and validation commands are expected, and review proposed changes before deployment. <br>
Risk: Gateway, relay, UI-control, or persistent-memory configuration can affect production DCC environments. <br>
Mitigation: Review those configurations before running them in production, keep scoped operator controls in place, and validate with adapter-specific smoke tests. <br>
Risk: Adapter guidance can introduce incorrect or misleading implementation choices if applied without review. <br>
Mitigation: Run the repository's lint, format, unit, MCP or REST, gateway, and live-DCC smoke checks that match the adapter change. <br>


## Reference(s): <br>
- [DCC-MCP Creator source](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp-creator/SKILL.md) <br>
- [Adapter Workflow](references/ADAPTER_WORKFLOW.md) <br>
- [Host Pattern Matrix](references/HOST_PATTERN_MATRIX.md) <br>
- [Core Escalation Checklist](references/CORE_ESCALATION_CHECKLIST.md) <br>
- [Testing And Release](references/TESTING_AND_RELEASE.md) <br>
- [Adapter skill-load transform hooks RFC](https://github.com/dcc-mcp/dcc-mcp-core/issues/1204) <br>
- [Public DccServerBase resource registration RFC](https://github.com/dcc-mcp/dcc-mcp-core/issues/1205) <br>
- [Reusable adapter readiness binder RFC](https://github.com/dcc-mcp/dcc-mcp-core/issues/1206) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline code and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include repository edits, validation commands, and adapter scaffolding recommendations.] <br>

## Skill Version(s): <br>
0.19.83 (source: server evidence release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
