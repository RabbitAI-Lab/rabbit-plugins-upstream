## Description:

Use when a user names two supported IDEs or agent products to plan, migrate, or inspect specific skills, instructions, and MCP; the skill inventories local paths and runs bundled Bash/Python, and an approved apply or rollback may write targets, create backups/manifests, verify results, and scan or redact secrets while network access is forbidden.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and engineers use this skill to review and migrate portable agent context between supported IDEs and agent products, including skills, instructions, and MCP configuration. It is intended for local, offline planning first, with writes limited to reviewed migration, restore, or rollback plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plan replay and plugin-copy paths can perform high-impact local writes when applied.

Mitigation: Use plan-only review by default, inspect exact target paths and diffs, and apply only a saved plan after explicit approval.

Risk: Bundles or replayed plans from untrusted sources could write unexpected local agent context.

Mitigation: Avoid untrusted bundles, run bundle verification, and require checksum-bound source and target state locks before restore or apply.

Risk: Bulk operations such as all-installed discovery can broaden the set of affected products.

Mitigation: Review the detection table and constrain source, target, scope, workspace, and object types before any write.

Risk: Sensitive local settings may contain credentials or trust state.

Mitigation: Rely on the skill's secret scanning and redaction behavior, and migrate only the reviewed portable subobjects rather than whole settings files.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/luckycat133/skills/agent-skills-setup)
- [IDE registry](references/ide-registry.md)
- [Registry v2](references/registry-v2.json)
- [Migration safety and conflicts](references/migration-safety.md)
- [MCP migration](references/mcp-migration.md)
- [Object migration](references/object-migration.md)
- [Verification and evidence](references/verification.md)
- [Documentation freshness checks](references/doc-freshness-checks.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON plan or manifest paths, and concise migration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce reviewed plan, manifest, verification, rollback, or bundle guidance; network access is forbidden by the skill.]

## Skill Version(s):

0.8.33 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
