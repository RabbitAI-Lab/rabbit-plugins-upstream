## Description:

Helps migrate, back up, restore, compare, and move AI-coding-agent context across supported local agent profiles, with reviewed planning, secret redaction, verification, and rollback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and engineers use this skill to plan and execute portable migration of skills, instructions, rules, and reviewed MCP configuration between AI coding tools or computers. It is most useful when the user needs an offline, reviewable workflow with backups, manifests, verification, and rollback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and rewrite local AI-agent configuration, so an overly broad or incorrect migration plan could change important agent behavior.

Mitigation: Use plan-only or preview flows first, review the exact file list and diff, and apply only a saved plan after explicit approval.

Risk: Server security evidence flags a path that can persist MCP environment or header values in unmanaged temporary files.

Mitigation: Avoid all-installed restore or snapshot flows until the flagged MCP merge handling is fixed, and review generated bundles and plans for credential-free output before applying.

Risk: Bulk restore and snapshot flows may cover many installed profiles and increase the chance of migrating unwanted context.

Mitigation: Prefer named source and target profiles with explicit object scopes, and keep trust state, chat history, generated memory, approvals, and session data out of migrations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/luckycat133/skills/agent-skills-setup)
- [IDE Reference Index](references/ide-registry.md)
- [Registry v2](references/registry-v2.json)
- [Migration safety and conflicts](references/migration-safety.md)
- [MCP migration](references/mcp-migration.md)
- [File-backed object migration](references/object-migration.md)
- [Verification and evidence](references/verification.md)
- [Documentation freshness checks](references/doc-freshness-checks.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON plans and manifests, and generated configuration changes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline operation; migration writes require a reviewed plan and explicit approval; outputs are intended to redact credential-looking values.]

## Skill Version(s):

0.9.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
