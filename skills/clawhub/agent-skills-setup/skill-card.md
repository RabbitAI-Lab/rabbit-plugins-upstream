## Description:

Plans, inspects, and migrates local agent skills, instructions, and MCP configuration between supported IDEs or agent products using offline scripts with reviewed apply, rollback, backup, manifest, verification, and secret-redaction controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and engineers use this skill to inventory agent-product context and create reviewed migration plans for skills, instructions, and MCP settings between supported local IDEs or agent tools. After explicit approval, it can apply, verify, or roll back those changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved apply or rollback actions can change local IDE or agent configuration and affect future agent behavior.

Mitigation: Review the saved plan paths, diffs, and manifest before approval; apply only the exact reviewed plan and keep rollback evidence.

Risk: Bulk installed-source mode, bundle restore, plugin transfer, or session handoff can broaden the migration scope.

Mitigation: Confirm the named source, target, object scope, bundle checks, and session-transfer flag before approving any write.

Risk: Agent and MCP configuration can contain credentials or sensitive local state.

Mitigation: Use the skill's offline secret scanning, redaction, subobject-only MCP extraction, and explicit exclusion of raw conversations, tokens, approvals, and trust state.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/luckycat133/skills/agent-skills-setup)
- [IDE Reference Index](references/ide-registry.md)
- [Registry v2](references/registry-v2.json)
- [Migration Safety and Conflicts](references/migration-safety.md)
- [MCP Migration](references/mcp-migration.md)
- [Object Migration](references/object-migration.md)
- [Verification](references/verification.md)
- [Documentation Freshness Checks](references/doc-freshness-checks.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON plan or manifest references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline output may include reviewed migration plans, manifests, diffs, verification results, rollback guidance, and credential-redacted reports.]

## Skill Version(s):

0.9.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
