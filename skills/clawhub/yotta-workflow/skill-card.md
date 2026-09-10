## Description:

A universal workflow standard for AI agents that reads project state on start, stores state nearby in `.workflow`, persists logs, tasks, and decisions while work progresses, and leaves a handoff anchor on finish.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to maintain project continuity across sessions and agents by reading and writing shared Markdown workflow state. It is intended for multi-step project work, handoffs, resumptions, and situations where project progress, tasks, decisions, and logs need to persist.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer behavior can broadly modify agent skill directories and may overwrite or follow unsafe existing targets.

Mitigation: Use a pinned package version and an explicit `--dir` target, inspect any existing `yotta-workflow` destination for symlinks or unexpected files, and avoid global installation unless every target directory is intended.

Risk: The workflow persists project progress, tasks, decisions, and logs into `.workflow` files.

Mitigation: Use it only in repositories where persistent workflow files are acceptable, and avoid sensitive or clean repositories unless these files have been reviewed and approved.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-workflow)
- [FAQ](references/faq.md)
- [Walkthroughs](references/walkthroughs.md)
- [Exception Recovery Playbook](references/exception-playbook.md)
- [npm Package](https://www.npmjs.com/package/@yottameta/yotta-workflow)
- [Agent Skills Standard](https://agentskills.io/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Files, Shell commands, Configuration]

**Output Format:** [Markdown instructions, Markdown state files, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update `.workflow` project state files and handoff anchors during agent work.]

## Skill Version(s):

0.3.0 (source: frontmatter, CHANGELOG, package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
