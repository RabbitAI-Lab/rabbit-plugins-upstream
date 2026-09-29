## Description:

Maintains project context and documentation files by checking their contents against the codebase before creating or updating them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to initialize and update AGENTS.md, CLAUDE.md, README.md, CONTRIBUTING.md, and DOCS.md using verified repository details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands or code snippets found in documentation may be executed without clear confirmation or isolation.

Mitigation: Use only in trusted repositories and require approval before running commands or snippets from documentation.

Risk: Changes to AGENTS.md or CLAUDE.md can persist as instructions for future agent sessions.

Mitigation: Review generated context-file changes before later sessions rely on them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-md-docs)
- [Documentation workflows](artifact/references/documentation-workflows.md)
- [Context content and writing](artifact/references/context-content-and-writing.md)
- [Context file initialization](artifact/references/init-agents.md)
- [Monorepo documentation](artifact/references/monorepo.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [Markdown documentation files, change summaries, or diff previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run previews and backups before overwriting existing files.]

## Skill Version(s):

5.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
