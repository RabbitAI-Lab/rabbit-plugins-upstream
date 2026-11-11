## Description:

Deploys story-writing project infrastructure, including hooks, rules, agents, reference material, and Claude Code or OpenCode configuration, into a user's project.

This skill is ready for commercial/non-commercial use.

## Publisher:

[9438190](https://clawhub.ai/user/9438190)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and developers use this skill to initialize or update a web-novel writing workspace with Claude Code or OpenCode agents, hooks, commands, rules, and project-local reference material. It supports setup, redeployment, configuration merging, and post-install validation for long-form and short-form story projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs persistent hooks, OpenCode plugins, commands, and Git hook behavior into the user's project.

Mitigation: Review the installation plan and changed files before using it in a real project, especially .claude/settings.local.json, .claude/hooks, .opencode/plugins/story-hooks.ts, .opencode/commands, and .git/hooks/pre-commit.

Risk: The security summary reports a browser research workflow and unsafe shell-command templates.

Mitigation: Avoid using the browser research path with sensitive logged-in browser sessions, and patch or disable the story-researcher shell-command workflow until values are validated and safely serialized.

Risk: Configuration merging can affect existing Claude Code, OpenCode, and Git project behavior.

Mitigation: Inspect merged configuration and hooks after deployment, and keep project-specific customizations separate from story-setup managed blocks where possible.

## Reference(s):

- [Story Setup workflow](SKILL.md)
- [Upgrade guide](UPGRADING.md)
- [OpenClaw source link from metadata](https://github.com/worldwonderer/oh-story-claudecode)
- [Agent reference bundle](references/agent-references/)
- [OpenCode plugin](references/opencode/plugin.ts)
- [Claude Code hooks settings template](references/templates/settings-hooks.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with file edits, shell commands, generated configuration, and installation reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or merge persistent project files, hooks, OpenCode plugins, commands, rules, agents, and sentinel state.]

## Skill Version(s):

1.0.0 (source: server release evidence; artifact frontmatter reports 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
