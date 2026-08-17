## Description:

Use when a user names two supported IDEs or agent products to plan, migrate, or inspect specific skills, instructions, and MCP; the skill inventories local paths, runs bundled Bash/Python, and may write approved migration targets while forbidding network access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inventory, plan, verify, and selectively migrate local agent or IDE context such as skills, instructions, MCP settings, prompts, commands, workflows, agents, and hooks between supported products. It is most appropriate when the user can review generated plans, paths, diffs, backups, and manifests before any approved write.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent agent configuration paths and migration targets may be under-scoped.

Mitigation: Review the generated plan, resolved paths, file list, diffs, backups, and manifests before using `--yes` or approving any apply or restore action.

Risk: Plugin, handoff, or session-related migration behavior may copy more than the user intended.

Mitigation: Avoid those object types unless the package is corrected and the exact copied files and restore targets can be verified first.

Risk: MCP changes can alter which tools an agent can call.

Mitigation: Treat MCP diffs as sensitive configuration changes, verify them in the target client's native discovery surface, and preserve unrelated settings.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/luckycat133/skills/agent-skills-setup)
- [IDE Reference Index](references/ide-registry.md)
- [Registry v2](references/registry-v2.json)
- [Migration Safety and Conflicts](references/migration-safety.md)
- [MCP Migration](references/mcp-migration.md)
- [Object Migration](references/object-migration.md)
- [Verification and Evidence](references/verification.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON plan, manifest, verification, or bundle artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local migration plans, backups, manifests, diffs, checksums, redaction results, and manual follow-up notes when the user approves those workflows.]

## Skill Version(s):

0.8.18 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
