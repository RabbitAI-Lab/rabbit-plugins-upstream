## Description: <br>
Helps agents plan, preview, apply, and verify scoped migrations of AI-assistant context such as skills, rules, prompts, MCP servers, commands, and project configuration between supported IDEs or agent tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luckycat133](https://clawhub.ai/user/luckycat133) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to migrate selected AI-assistant context between IDEs or agent tools while reviewing path, schema, credential, and conflict-handling differences before writing changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A migration scope that is too broad can move unrelated or product-specific configuration. <br>
Mitigation: Use the named source, target, workspace, and object list; start with a dry run and avoid whole IDE config or project-tree copies unless manually reviewed. <br>
Risk: MCP entries can include secrets, OAuth or session state, runtime protocol metadata, or inherited execution permissions that should not be portable. <br>
Mitigation: Redact credentials, preserve only reviewed endpoint metadata, do not transfer OAuth/session state or tool grants, and re-authorize or review tools in the target client. <br>
Risk: Unsupported formats or ambiguous transport mappings can produce incorrect target configuration. <br>
Mitigation: Use manual reconstruction when a schema, file format, or transport is unsupported or ambiguous, then validate with the target tool's native discovery method. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/luckycat133/skills/agent-skills-setup) <br>
- [IDE Reference Index](references/ide-registry.md) <br>
- [IDE Path Mapping](references/ide-paths.json) <br>
- [Migration Safety and Conflicts](references/migration-safety.md) <br>
- [MCP Migration](references/mcp-migration.md) <br>
- [Object Migration](references/object-migration.md) <br>
- [Verification](references/verification.md) <br>
- [OpenClaw Migration Notes](references/openclaw.md) <br>
- [MCP 2026-07-28 Key Changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog) <br>
- [MCP Streamable HTTP Transport](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http) <br>
- [MCP Authorization Requirements](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON evidence, and configuration edits or previews.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses dry-run previews, explicit consent for writes, credential redaction, and target-native verification where supported.] <br>

## Skill Version(s): <br>
0.6.11 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
