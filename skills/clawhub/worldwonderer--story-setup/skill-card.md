## Description:

Deploys online-fiction writing infrastructure for Claude Code, OpenCode, Codex, ZCode, OpenClaw, Reasonix, Web AI, and generic agent projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and developers use this skill to initialize or refresh a project with managed writing agents, commands, hooks, rules, and reference materials across supported CLI and agent environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs automatic project hooks and managed agent or command files.

Mitigation: Install only in intended writing projects and review the target CLI hook configuration before trusting the deployed setup.

Risk: Session-start update checks may be undesirable in privacy-sensitive environments.

Mitigation: Set STORY_NO_UPDATE_CHECK=1 when update checks should be disabled.

Risk: Browser automation can inherit logged-in browser sessions.

Mitigation: Use browser-cdp only with an isolated or intentionally selected browser profile.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-setup)
- [OpenClaw metadata source](https://github.com/worldwonderer/oh-story-claudecode)
- [Upgrade guide](UPGRADING.md)
- [Agent reference index](references/agent-references/genre-catalog.md)
- [Quality checklist](references/agent-references/quality-checklist.md)
- [Codex deployment template](references/codex/AGENTS.md.tmpl)
- [OpenCode deployment plugin](references/opencode/plugin.ts)
- [ZCode hook configuration](references/zcode/hooks/hooks.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with proposed file, command, hook, and configuration changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce persistent project files and hook registrations for selected target CLIs.]

## Skill Version(s):

1.1.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
