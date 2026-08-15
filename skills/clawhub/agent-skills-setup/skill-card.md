## Description:

Use only when a user names two supported IDEs or agent products, identifies specific skills, instructions, prompts, commands, or MCP objects, and asks to plan or perform a migration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inventory, plan, apply, verify, or roll back migrations of agent and IDE skills, instructions, prompts, commands, and MCP configuration between supported products after explicit review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated plans for user-scope skills, instructions, or MCP configuration can affect how future agents run.

Mitigation: Review the saved plan, diff or rebuild manifest, and target paths before approval; approve apply or rollback only when the saved plan exactly matches the intended migration.

Risk: Migrating credentials, OAuth/session state, runtime metadata, approval grants, chat history, databases, or generated memory can expose sensitive data or produce unsafe configuration.

Mitigation: Do not move those objects; use the bundled secret scanning and redaction behavior and manually reconstruct configuration when conversion is unclear.

Risk: Mismatched product profiles or stale target state can cause incorrect writes or partial migrations.

Mitigation: Use profile-aware planning, verify source and target hashes before applying, preserve backups and manifests, and run verification against the checksummed manifest.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/luckycat133/skills/agent-skills-setup)
- [IDE reference index](artifact/references/ide-registry.md)
- [Registry v2](artifact/references/registry-v2.json)
- [Migration safety and conflicts](artifact/references/migration-safety.md)
- [Object migration](artifact/references/object-migration.md)
- [MCP migration](artifact/references/mcp-migration.md)
- [MCP transport](artifact/references/mcp-transport.md)
- [Verification and evidence](artifact/references/verification.md)
- [Documentation freshness checks](artifact/references/doc-freshness-checks.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional JSON plan, manifest, and verification outputs from bundled shell and Python tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include migration plans, diffs, rebuild manifests, checksums, verification results, rollback commands, and manual follow-ups.]

## Skill Version(s):

0.8.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
