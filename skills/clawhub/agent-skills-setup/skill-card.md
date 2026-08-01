## Description: <br>
Helps agents preview and perform scoped AI-assistant context migrations between IDEs or agent tools, including skills, rules, prompts, commands, and MCP configuration, with writes gated by approval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luckycat133](https://clawhub.ai/user/luckycat133) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan, preview, and apply controlled migrations of AI-assistant context between supported IDEs and agent clients. It is intended for user-approved migration work, not general explanation, debugging, validation, installation, or same-tool copies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A migration can target the wrong IDE path, workspace, or object type if scope is unclear. <br>
Mitigation: Resolve source, target, workspace, objects, and strategy first; run a dry-run and review the exact paths before any approved write. <br>
Risk: MCP credentials, OAuth state, sessions, or literal secrets can be exposed or copied incorrectly. <br>
Mitigation: Do not copy secrets or OAuth/session state; blank literal credentials when converting and manually re-authorize credentials in the target IDE. <br>
Risk: Whole config files or opaque project trees can overwrite unrelated user settings. <br>
Mitigation: Avoid whole config/project migration, preserve unrelated settings, and use backup or manual reconstruction when formats are unsupported. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/luckycat133/skills/agent-skills-setup) <br>
- [Migration safety](references/migration-safety.md) <br>
- [MCP migration](references/mcp-migration.md) <br>
- [Object migration](references/object-migration.md) <br>
- [Verification](references/verification.md) <br>
- [IDE registry](references/ide-registry.md) <br>
- [IDE paths](references/ide-paths.json) <br>
- [Script usage](scripts/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, configuration snippets, and JSON evidence when commands are run with JSON output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should preserve source files, preview with dry-run before approved writes, redact or avoid secrets, and report migration evidence after apply.] <br>

## Skill Version(s): <br>
0.6.12 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
