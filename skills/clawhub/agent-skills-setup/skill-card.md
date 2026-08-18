## Description:

Agent Skills Setup & Migration helps agents plan, inspect, and migrate supported IDE or agent skills, instructions, and MCP configuration using local Bash/Python workflows with explicit approval for writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inventory, plan, apply, verify, roll back, snapshot, and restore portable agent context between supported IDEs and agent products. It is intended for local, offline migration workflows where configuration changes are reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect and modify local IDE or agent configuration files during approved apply, restore, or rollback flows.

Mitigation: Prefer plan-only and bundle-verify flows first, review every target path and diff, and keep an external backup before apply or rollback.

Risk: Broad object selections can touch higher-risk surfaces such as plugins, hooks, or handoff data.

Mitigation: Select only the specific objects needed and avoid plugins, hooks, or handoff unless the migration requires them.

Risk: Private credentials, sessions, approval grants, runtime state, chat history, or generated memory could be harmful if migrated.

Mitigation: Use the documented secret scanning, strict allowlists, and non-migratable state exclusions before restoring or applying changes.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/luckycat133/skills/agent-skills-setup)
- [IDE Reference Index](references/ide-registry.md)
- [Migration Safety and Conflicts](references/migration-safety.md)
- [File-Backed Object Migration](references/object-migration.md)
- [MCP Migration](references/mcp-migration.md)
- [Verification and Evidence](references/verification.md)
- [Registry v2](references/registry-v2.json)
- [Documentation Freshness Checks](references/doc-freshness-checks.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands plus JSON plan, manifest, inventory, verification, and bundle metadata artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires local bash and python3; network access is forbidden by the skill evidence.]

## Skill Version(s):

0.8.22 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
