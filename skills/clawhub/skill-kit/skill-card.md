## Description:

Claude Code skill authoring and management toolkit for creating, linting, merging, upgrading, routing, publishing, dependency graphing, trigger registration, discovery, and invocation discipline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to create, maintain, validate, consolidate, publish, discover, and route Claude Code skills. It also supports trigger compilation, dependency graph extraction, language consistency checks, and invocation discipline for multi-topic skill workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trigger compilation can persistently change local hook scripts and ~/.claude/settings.json.

Mitigation: Run trigger dry-run first, inspect the proposed hook and settings changes, and verify settings JSON before enabling generated hooks.

Risk: Skill discovery and installation workflows can install third-party skills globally and skip confirmation.

Mitigation: Review source and publisher reputation before installing, prefer project-local installs when possible, and avoid -g -y for unreviewed skills.

Risk: Merge, deduplication, conversion, and upgrade workflows can move or remove skill and agent files.

Mitigation: Keep backups until converted or merged skills are verified, and require explicit confirmation before delete or cross-skill write operations.

Risk: Upgrade workflows can stage and commit changes with broad repository impact.

Mitigation: Inspect git status and changed files before committing, isolate public-skill work on the intended branch, and commit only the files in scope.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/skill-kit)
- [README](artifact/README.md)
- [Skill Definition](artifact/SKILL.md)
- [Trigger Guide](artifact/trigger.md)
- [Find Skills Guide](artifact/find.md)
- [Skills CLI Ecosystem](https://skills.sh/)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code blocks, shell commands, configuration examples, and generated skill files or scripts when used by an agent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or perform file edits, hook registration, skill installation, backups, commits, and dependency graph generation depending on the selected topic and user confirmation.]

## Skill Version(s):

0.7.0 (source: server release metadata and changelog, released 2026-08-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
