## Description:

Agent Skills Setup helps agents plan, apply, verify, and roll back context migrations between supported AI IDEs and agent products using local Bash and Python tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inventory local AI IDE and agent context, generate migration plans, and apply reviewed transfers of skills, rules, prompts, and MCP settings between supported products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Short natural-language migration requests can authorize local IDE or agent configuration changes.

Mitigation: Use plan-only or saved-plan workflows first, inspect the affected paths and diffs, and give explicit confirmation only after review.

Risk: Snapshot and restore workflows can create or restore local bundles of agent context files.

Mitigation: Use snapshot or restore only when that local bundle behavior is intended, and review the planned source and destination paths before approving writes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/luckycat133/skills/agent-skills-setup)
- [Publisher profile](https://clawhub.ai/user/luckycat133)
- [IDE Reference Index](references/ide-registry.md)
- [Registry v2](references/registry-v2.json)
- [Migration safety and conflicts](references/migration-safety.md)
- [MCP migration](references/mcp-migration.md)
- [File-backed object migration](references/object-migration.md)
- [Verification and evidence](references/verification.md)
- [Documentation freshness checks](references/doc-freshness-checks.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown text with inline shell commands and JSON plan or manifest paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local plan, manifest, backup, verification, snapshot, or restore artifacts when the user approves write workflows.]

## Skill Version(s):

0.8.4 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
