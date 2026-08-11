## Description:

Skill-kit helps Claude Code users create, lint, merge, upgrade, route, publish, and maintain multi-topic skills, including dependency graphs and hook-trigger tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to create, validate, refactor, discover, and publish Claude Code skills while keeping frontmatter, topic routing, dependency references, and hook-trigger behavior consistent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to make lasting changes to Claude configuration, hooks, installed skills, and repositories.

Mitigation: Use dry-run or list modes before applying changes, review proposed file diffs, and keep backups of configuration files such as ~/.claude/settings.json.

Risk: Trigger compilation can generate hook scripts and register them in settings.json.

Mitigation: Inspect generated hook scripts and settings.json changes before enabling them, and avoid compiling triggers from untrusted skills.

Risk: Install, convert, dedup cleanup, and upgrade workflows may change local skill files or repositories.

Mitigation: Run these workflows only in intended workspaces, prefer non-global installs when possible, and confirm the scope of edits or commits before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/skill-kit)
- [skills.sh ecosystem](https://skills.sh/)
- [README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)
- [Trigger guide](artifact/trigger.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, generated skill files, and dependency graph text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to edit skill files, generate hook scripts, update settings.json, create dependency graphs, and run installation or repository commands.]

## Skill Version(s):

0.6.2 (source: evidence.release.version and artifact/CHANGELOG.md, released 2026-08-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
