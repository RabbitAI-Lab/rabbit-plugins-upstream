## Description: <br>
Infrastructure skill that guides developers and agents through creating or modernizing full DCC-MCP adapters for Nuke, Blender, 3ds Max, Unreal, ZBrush, Houdini, Maya, and custom studio tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create or modernize DCC-MCP adapter infrastructure, including server composition, host-thread dispatch, sidecar and gateway wiring, packaging, runtime integration, diagnostics, and cross-DCC validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to edit adapter code and run local development commands. <br>
Mitigation: Review proposed file changes and shell commands before execution, and run repository-native validation gates before deployment. <br>
Risk: Adapter work may start or configure DCC-MCP services, sidecars, gateways, relays, or live DCC integrations. <br>
Mitigation: Keep service configuration explicit, validate live readiness before routing calls, and require operator review for relays or routed-subnet exposure. <br>
Risk: Raw UI/input automation can affect the operator's desktop or target DCC session. <br>
Mitigation: Keep raw input operator-controlled, scoped to the trusted DCC target, confirmation-gated, and stopped when the workflow ends. <br>
Risk: Durable memory and debug exports may retain workflow context or local evidence. <br>
Mitigation: Use durable memory only when operator-managed, disable it for privacy-sensitive deployments, and review raw debug exports locally before sharing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/loonghao/skills/dcc-mcp-creator) <br>
- [Clawdis homepage](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp-creator/SKILL.md) <br>
- [Adapter Workflow](references/ADAPTER_WORKFLOW.md) <br>
- [Core Escalation Checklist](references/CORE_ESCALATION_CHECKLIST.md) <br>
- [Host Pattern Matrix](references/HOST_PATTERN_MATRIX.md) <br>
- [Testing And Release](references/TESTING_AND_RELEASE.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline code and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces implementation guidance and validation steps for an agent; it does not itself produce a runnable adapter artifact.] <br>

## Skill Version(s): <br>
0.19.86 (source: evidence release and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
