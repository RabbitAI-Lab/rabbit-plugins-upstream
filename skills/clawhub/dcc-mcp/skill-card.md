## Description: <br>
DCC-MCP helps agents discover, route, and operate supported live DCC applications through structured DCC-MCP CLI and gateway tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and technical artists use this skill to control live DCC applications, discover marketplace Skills, and follow consent-gated setup or troubleshooting workflows through DCC-MCP CLI and gateway paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent actions can change live DCC application sessions, creative project state, or local DCC-MCP tooling. <br>
Mitigation: Use the skill only when live DCC control is expected, run inventory and structured discovery before actions, and require user approval before setup, install, update, or UI-control fallback steps. <br>
Risk: CLI bootstrap or updates can replace local executable tooling. <br>
Mitigation: Use the consent-gated verified installer path, which accepts the official release manifest, checks the asset URL and version, verifies SHA-256, and preserves the existing CLI on verification failure. <br>
Risk: Telemetry and Skill-reflection evidence can be incomplete when direct local control bypasses gateway stats. <br>
Mitigation: Use --require-gateway with a stable --agent-session-id from the first measured call whenever gateway stats are required evidence. <br>
Risk: Timeouts, DCC restarts, or unreachable instances can make mutation status ambiguous. <br>
Mitigation: Preserve operation identifiers, refresh inventory, query status through the declared recovery path, and avoid blindly replaying non-idempotent mutations. <br>


## Reference(s): <br>
- [DCC-MCP ClawHub Skill Page](https://clawhub.ai/loonghao/skills/dcc-mcp) <br>
- [DCC-MCP Skill Homepage](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp/SKILL.md) <br>
- [CLI cheatsheet](references/CLI_CHEATSHEET.md) <br>
- [Zero instances CLI setup guide](references/ZERO_INSTANCES_CLI.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code, markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON arguments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Live DCC actions depend on available DCC-MCP instances; setup, install, update, and UI-control fallback actions require user consent.] <br>

## Skill Version(s): <br>
0.19.87 (source: server release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
