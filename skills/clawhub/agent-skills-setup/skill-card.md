## Description: <br>
Helps an agent migrate selected AI-assistant skills, rules, prompts, commands, and MCP configuration between supported IDEs or agent products with scoped planning and verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luckycat133](https://clawhub.ai/user/luckycat133) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to move AI-assistant context between supported IDEs and agent products while preserving source files, avoiding unsupported objects, and producing verifiable migration evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change local AI-assistant configuration and copied skills. <br>
Mitigation: Use --dry-run first, keep the default backup strategy unless overwrite is intentional, and review emitted evidence before enabling migrated content. <br>
Risk: Migrated MCP servers or skills may include credentials, unsupported transports, or settings that do not work in the target tool. <br>
Mitigation: Review migrated MCP servers and skills before enabling them; reconstruct unclear credentials, OAuth state, and unsupported transport details manually. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/luckycat133/skills/agent-skills-setup) <br>
- [IDE reference index](artifact/references/ide-registry.md) <br>
- [IDE path mapping](artifact/references/ide-paths.json) <br>
- [Migration safety and conflicts](artifact/references/migration-safety.md) <br>
- [MCP migration](artifact/references/mcp-migration.md) <br>
- [File-backed object migration](artifact/references/object-migration.md) <br>
- [Verification and evidence](artifact/references/verification.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; JSON evidence when migration commands use --json.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local filesystem migration guidance; dry-run previews and backup strategy are expected before writes.] <br>

## Skill Version(s): <br>
0.7.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
