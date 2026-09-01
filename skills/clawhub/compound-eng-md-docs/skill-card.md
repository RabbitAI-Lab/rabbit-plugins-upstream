## Description:

Manages project documentation files such as CLAUDE.md, AGENTS.md, README.md, CONTRIBUTING.md, and DOCS.md by verifying them against codebase state before writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to create, refresh, and verify project-facing Markdown documentation and agent context files against the current repository state. It is intended for documentation maintenance workflows, not general Markdown editing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change persistent agent context and project documentation files, which may affect future agent behavior or developer workflows.

Mitigation: Review proposed diffs before allowing writes, use dry-run where possible, and keep the skill's backup behavior before overwriting files.

Risk: The skill may replace or symlink CLAUDE.md and AGENTS.md during context initialization or migration.

Mitigation: Confirm the migration with the user before renaming or symlinking context files, and do not perform this migration as a side effect of unrelated documentation work.

Risk: Documentation verification can surface deploy, migration, credentialed, or otherwise state-changing commands.

Mitigation: Do not run state-changing commands solely to verify documentation unless the user explicitly intends that action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-md-docs)
- [Update Context Files Workflow](artifact/references/update-agents.md)
- [Update README Workflow](artifact/references/update-readme.md)
- [Update CONTRIBUTING Workflow](artifact/references/update-contributing.md)
- [Initialize Context Workflow](artifact/references/init-agents.md)
- [Monorepo Handling](artifact/references/monorepo.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown files and concise status reports with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or write documentation files and context-file symlinks; supports dry-run previews when requested.]

## Skill Version(s):

4.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
