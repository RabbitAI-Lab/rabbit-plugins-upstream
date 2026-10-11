## Description:

Maintains project documentation and agent context files by checking them against the current repository before making changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to create or refresh project documentation and agent context files, checking documented claims against the repository before editing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes to AGENTS.md or CLAUDE.md can influence later agent behavior.

Mitigation: Review context-file changes carefully; use --dry-run or --preserve in sensitive repositories.

Risk: Documentation updates may introduce inaccurate project guidance.

Mitigation: Check documented claims against repository files and commands, and review the diff before accepting edits.

## Reference(s):

- [ia-md-docs release](https://clawhub.ai/iliaal/skills/compound-eng-md-docs)
- [Documentation workflows](references/documentation-workflows.md)
- [Context content and writing](references/context-content-and-writing.md)
- [Monorepo handling](references/monorepo.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown documentation files and text change summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run diff previews and creates adjacent backups before overwriting files.]

## Skill Version(s):

5.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
