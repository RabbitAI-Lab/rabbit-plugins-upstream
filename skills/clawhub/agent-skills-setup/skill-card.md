## Description: <br>
Migrate, move, transfer, copy, convert, or sync AI-assistant context between different IDEs or agents, including skills, rules, prompts, commands, and MCP configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luckycat133](https://clawhub.ai/user/luckycat133) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to migrate AI assistant context between supported IDEs and agents while preserving documented boundaries for skills, rules, prompts, commands, and MCP configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change local AI IDE context files during an approved migration. <br>
Mitigation: Use dry-run first, review the source, target, objects, scope, workspace, and strategy, and rely on backup or skip behavior before applying changes. <br>
Risk: MCP configuration may contain credentials, OAuth state, protocol state, or target-specific authorization settings. <br>
Mitigation: Review MCP configuration before enabling migrated servers, redact or reconstruct sensitive values manually, and re-authorize tools in the target client. <br>
Risk: A parsed target configuration does not prove transport compatibility, permissions, or connectivity. <br>
Mitigation: Verify the migrated configuration with the target IDE or agent's native discovery surface after apply. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/luckycat133/skills/agent-skills-setup) <br>
- [IDE reference index](references/ide-registry.md) <br>
- [Migration safety and conflicts](references/migration-safety.md) <br>
- [MCP migration](references/mcp-migration.md) <br>
- [MCP transport and authorization boundaries](references/mcp-transport.md) <br>
- [File-backed object migration](references/object-migration.md) <br>
- [Verification and evidence](references/verification.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands and optional JSON evidence] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce dry-run plans, migration commands, verification notes, and scoped local file changes when the user approves applying a migration.] <br>

## Skill Version(s): <br>
0.7.2 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
