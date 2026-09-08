## Description:

Manages project documentation including CLAUDE.md, AGENTS.md, README.md, CONTRIBUTING.md, and DOCS.md for update, creation, and initialization workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to initialize or refresh repository documentation after inspecting the actual codebase, commands, and project structure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify repository documentation and context files, including AGENTS.md, README.md, CONTRIBUTING.md, DOCS.md, and CLAUDE.md links.

Mitigation: Use dry-run mode where possible, review proposed diffs before accepting changes, and keep backups created before overwrites.

Risk: Documentation snippets or repository commands may have unintended side effects if executed without review.

Mitigation: Review any proposed command or snippet execution explicitly and avoid deploy, migration, install, shell, or network-touching examples unless that side effect is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-md-docs)
- [SKILL.md](artifact/SKILL.md)
- [SPEC.md](artifact/SPEC.md)
- [Documentation workflows](artifact/references/documentation-workflows.md)
- [Context content and writing](artifact/references/context-content-and-writing.md)
- [Initialize Context Workflow](artifact/references/init-agents.md)
- [Monorepo Handling](artifact/references/monorepo.md)
- [Update Context Files Workflow](artifact/references/update-agents.md)
- [Update README Workflow](artifact/references/update-readme.md)
- [Update CONTRIBUTING Workflow](artifact/references/update-contributing.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown documents, concise status summaries, and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write or update repository documentation files and create context-file links when the selected workflow calls for it.]

## Skill Version(s):

4.5.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
