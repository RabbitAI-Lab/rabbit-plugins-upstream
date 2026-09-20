## Description:

Skill-Kit helps Claude Code agents create, validate, maintain, discover, graph, and publish multi-topic skills and related hook configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use Skill-Kit to author and maintain Claude Code skills, validate frontmatter, merge or upgrade related skills, inspect dependency graphs, and manage declarative hook registration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trigger compilation can persistently register automatic scripts from installed skills.

Mitigation: Use trigger dry-run or list before compile, review every discovered trigger and script source, avoid compiling triggers from untrusted marketplaces, and inspect ~/.claude/settings.json and ~/.claude/hooks afterward.

Risk: The skill can manage and modify local Claude Code skills and related configuration.

Mitigation: Review proposed file changes and validation output before deployment, and verify paths before running backup cleanup or deletion examples.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/skill-kit)
- [README](README.md)
- [Skill definition](SKILL.md)
- [Skill lint guide](lint.md)
- [Trigger guide](trigger.md)
- [Skill graph guide](graph.md)
- [Changelog](CHANGELOG.md)
- [skills.sh ecosystem](https://skills.sh/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, configuration examples, and generated files or diagrams when a topic calls for them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or modify local skill files, hook scripts, settings, dependency graphs, and validation reports depending on the selected topic]

## Skill Version(s):

0.9.0 (source: server release metadata and CHANGELOG, released 2026-09-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
