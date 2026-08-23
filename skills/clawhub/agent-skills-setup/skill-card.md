## Description:

Agent Skills Setup helps agents plan, inspect, snapshot, and migrate local skills, instructions, and MCP configuration between supported IDEs using offline Bash and Python workflows with explicit approval for writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and engineers use this skill to inventory supported local IDE and agent-product profiles, build reviewed migration plans, and move portable skills, instructions, and MCP entries between tools while preserving backups and excluding secrets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write reviewed migration targets when an apply, restore, or rollback action is explicitly approved.

Mitigation: Review the generated plan, target paths, scopes, and manifest before using --yes, and apply only the reviewed plan file.

Risk: Untrusted plan or bundle files could propose unwanted configuration changes.

Mitigation: Do not apply untrusted plan or bundle files without reading them; use bundle verification, checksums, and plan-only review before execution.

Risk: Credentials, sessions, OAuth state, approvals, and other runtime secrets are not portable through this migration flow.

Mitigation: Rebind secrets manually in the destination tool instead of expecting credentials or sessions to migrate.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/luckycat133/skills/agent-skills-setup)
- [IDE Reference Index](references/ide-registry.md)
- [Registry v2](references/registry-v2.json)
- [Migration Safety and Conflicts](references/migration-safety.md)
- [MCP Migration](references/mcp-migration.md)
- [Object Migration](references/object-migration.md)
- [Verification and Evidence](references/verification.md)
- [Documentation Freshness Checks](references/doc-freshness-checks.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance with shell commands and JSON plan, manifest, bundle, and verification artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline workflows require bash and python3; apply, restore, and rollback require explicit user approval.]

## Skill Version(s):

0.8.28 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
