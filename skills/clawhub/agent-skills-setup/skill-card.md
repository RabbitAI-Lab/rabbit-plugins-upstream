## Description:

Migrates, backs up, restores, compares, and moves AI-coding-agent context across supported tools with secret redaction, preview, verification, and rollback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan and execute reviewed migrations of agent skills, instructions, MCP settings, and portable bundles between AI coding tools or computers. It helps them preview changes, redact secrets, verify results, and roll back when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unreviewed migration plans could write incorrect or misleading agent context into a target tool.

Mitigation: Review the generated plan, diff, target paths, and manifest before applying; use explicit approval only for the reviewed plan.

Risk: MCP entries and plugin packages can change agent behavior or require credentials that should not be copied blindly.

Mitigation: Review MCP changes separately, reattach credentials through the target tool or environment, and treat plugin copies as manual or draft-disabled when required.

Risk: Agent settings may contain credentials, trust state, session history, or machine-specific state.

Mitigation: Rely on the skill's secret redaction, strict object allowlists, sub-object extraction, and exclusion of raw conversations, tokens, approval state, and generated memory.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/luckycat133/skills/agent-skills-setup)
- [IDE Registry](references/ide-registry.md)
- [Registry v2](references/registry-v2.json)
- [Migration Safety](references/migration-safety.md)
- [MCP Migration](references/mcp-migration.md)
- [MCP Transport](references/mcp-transport.md)
- [Object Migration](references/object-migration.md)
- [Verification](references/verification.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON plan or manifest artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline operation; write actions require reviewed plans and explicit approval.]

## Skill Version(s):

0.9.1 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
