## Description:

Story Setup deploys online-fiction writing project infrastructure for Claude Code, OpenCode, Codex, ZCode, OpenClaw, Reasonix, and generic agent workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, writers, and writing-tool maintainers use this skill to initialize or refresh a story-writing workspace with agents, hooks, commands, templates, and reference material across supported agent CLIs. It is intended for dedicated writing projects where automated project configuration is acceptable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs persistent hooks and broad command routing into writing projects.

Mitigation: Use it only in a dedicated writing workspace and review generated hook and configuration changes before relying on them.

Risk: Some generated configurations can affect files such as .claude/settings.local.json, .codex/hooks.json, .zcode/config.json, opencode.json, and .git/hooks/pre-commit.

Mitigation: Inspect those files after setup or upgrade and confirm that managed sections match the intended target agent environments.

Risk: Browser-CDP and cover-generation workflows may use browser login state or external APIs when invoked separately.

Mitigation: Run those workflows only when the user has approved the browser or external-service access needed for the writing task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-setup)
- [Metadata source link](https://github.com/worldwonderer/oh-story-claudecode)
- [Upgrade guide](UPGRADING.md)
- [Agent reference materials](references/agent-references/)
- [Claude Code deployment templates](references/templates/)
- [Codex adapter files](references/codex/)
- [OpenCode adapter files](references/opencode/)
- [ZCode adapter files](references/zcode/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with generated or merged project files, shell commands, hooks, agent definitions, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces workspace changes for selected agent environments and reports deployment or upgrade actions.]

## Skill Version(s):

1.1.19 (source: server release evidence; artifact frontmatter reports 1.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
