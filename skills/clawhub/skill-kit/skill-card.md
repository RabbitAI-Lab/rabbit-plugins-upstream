## Description:

Skill Kit helps Claude Code agents create, lint, merge, upgrade, route, publish-check, and maintain multi-topic skills, including trigger hook registration and ecosystem discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to author, maintain, validate, organize, publish-check, and install Claude Code skills while keeping multi-topic skill structure and trigger behavior consistent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist agent hooks and alter Claude settings.

Mitigation: Back up ~/.claude/settings.json before trigger compilation and inspect generated ~/.claude/hooks/trigger-*.sh files with dry-run or list mode before applying changes.

Risk: The skill can scan personal skill folders and install or change skills.

Mitigation: Review searched or installed package sources before use, and avoid default global installs with -g -y unless the source and target path are understood.

Risk: The skill includes workflows that may move backups, persist case history, or prepare repository changes.

Mitigation: Do not allow backup deletion, commits, pushes, PR creation, or case-history persistence unless the user explicitly approved that exact action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/skill-kit)
- [README](README.md)
- [Skill definition](SKILL.md)
- [Trigger guide](trigger.md)
- [Publish scope guide](publish-scope.md)
- [Portability guide](portability.md)
- [Skills ecosystem](https://skills.sh/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, configuration examples, and generated skill files or hook scripts when the user approves changes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or modify local Claude Code skill files, generated trigger hook scripts, and settings changes depending on the selected topic.]

## Skill Version(s):

0.6.1 (source: ClawHub release evidence and CHANGELOG.md, released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
