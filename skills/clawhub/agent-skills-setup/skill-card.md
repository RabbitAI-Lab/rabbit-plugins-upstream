## Description: <br>
Helps agents plan, preview, apply, and verify scoped migrations of AI-assistant context between IDEs and agent tools, including skills, rules, prompts, MCP servers, and project configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luckycat133](https://clawhub.ai/user/luckycat133) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to migrate AI IDE or agent context between selected tools with a scoped plan, compatibility notes, a dry-run preview, consent-gated writes, and verification evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A migration can write to the wrong source, target, scope, or workspace if the request is ambiguous. <br>
Mitigation: Keep source, target, object list, scope, and workspace explicit, and run a dry-run preview before any apply step. <br>
Risk: MCP, config, project, hooks, agents, and memory migrations can carry product-specific behavior or sensitive settings. <br>
Mitigation: Review these objects manually before applying changes and prefer human-readable context where portability is uncertain. <br>
Risk: Literal credentials may be removed or need reconstruction after migration. <br>
Mitigation: Expect copied credential values to be cleared, preserve the original source, and re-enter secrets only in the intended target IDE. <br>
Risk: Region-specific targets can differ in behavior and compatibility. <br>
Mitigation: Choose targets deliberately, especially variants such as Trae CN versus international Trae, and call out those boundaries in the migration plan. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/luckycat133/skills/agent-skills-setup) <br>
- [IDE reference index](references/ide-registry.md) <br>
- [IDE path mapping](references/ide-paths.json) <br>
- [Migration safety and conflicts](references/migration-safety.md) <br>
- [MCP migration](references/mcp-migration.md) <br>
- [Object migration](references/object-migration.md) <br>
- [Verification](references/verification.md) <br>
- [OpenClaw migration notes](references/openclaw.md) <br>
- [Migration script entry points](scripts/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON evidence] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dry-run previews, resolved path notes, credential handling notes, and verification summaries.] <br>

## Skill Version(s): <br>
0.6.9 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
