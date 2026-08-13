## Description:

Use when a user asks to migrate or transfer AI-assistant context between two named supported IDEs or agent products, including selected skills, rules, prompts, commands, or MCP configuration with a scoped, verifiable plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inventory, plan, apply, verify, and roll back migrations of local assistant context between supported IDEs and agent products. It is intended for scoped movement of file-backed skills, instructions, prompts, commands, and MCP configuration while preserving review points, backups, and loss reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify selected local assistant configuration files during apply operations.

Mitigation: Review the generated plan, source and target paths, migration scope, and object list before allowing apply.

Risk: Broad user-scope migrations can change assistant configuration under a user's home directory.

Mitigation: Prefer project-scoped migrations unless user-scope changes are intentional and reviewed.

Risk: Migrated context may contain secrets, session state, runtime metadata, or unsupported UI-managed configuration.

Mitigation: Use the skill's secret checks and manual reconstruction guidance; do not migrate secrets, OAuth or session state, generated memory, approval grants, chat history, databases, or unclear UI-managed settings.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/luckycat133/skills/agent-skills-setup)
- [IDE registry](references/ide-registry.md)
- [Registry v2 schema](references/registry-v2.schema.json)
- [Migration safety](references/migration-safety.md)
- [MCP migration](references/mcp-migration.md)
- [Object migration](references/object-migration.md)
- [Verification](references/verification.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce migration plans, manifests, loss reports, verification results, rollback commands, and target-discovery summaries.]

## Skill Version(s):

0.8.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
