## Description:

skill-kit helps Claude Code agents create, validate, merge, convert, route, publish, and maintain multi-topic skills, including trigger hooks and dependency graphs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent-skill maintainers use this skill to author, lint, upgrade, deduplicate, convert, route, publish-scope, and operate Claude Code skills. It also guides trigger registration, dependency graph extraction, language consistency, portability checks, and invocation discipline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The trigger workflow can create hook scripts and update local agent settings.

Mitigation: Run trigger compile in dry-run or list mode first, inspect the generated hook behavior, and apply changes only after review.

Risk: The find and install workflows can introduce third-party skills into the local environment.

Mitigation: Review the publisher, source files, and requested install scope before installing or globally enabling any discovered skill.

Risk: Dedup, merge, convert, and upgrade workflows can move, rewrite, or restructure skill files.

Mitigation: Keep backups, inspect planned file operations, and review generated edits before relying on the modified skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/skill-kit)
- [README](artifact/README.md)
- [Skill topic index](artifact/SKILL.md)
- [skills.sh ecosystem](https://skills.sh/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, checklists, generated skill files, hook configuration, and JSON graph output when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or apply local skill-file changes, backup moves, hook scripts, and settings updates depending on the selected topic.]

## Skill Version(s):

0.6.3 (source: server release metadata and CHANGELOG, released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
