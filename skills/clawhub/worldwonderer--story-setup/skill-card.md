## Description:

Deploys web-novel writing infrastructure for Claude Code, OpenCode, Codex, ZCode, OpenClaw, Reasonix, and generic agent projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and developers use this skill to initialize or refresh a story-writing project with platform-specific agents, hooks, commands, templates, and reference material while preserving user-owned configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes persistent local project changes, including agent files, hooks, commands, templates, sentinel metadata, and Git hook configuration.

Mitigation: Install only in writing projects where this automation is expected, and review the changed paths before continuing normal work.

Risk: Installed hooks may run automatically during sessions, file writes, compaction, and commits.

Mitigation: Review hook registrations for the selected platform and disable or remove unwanted automation before using the project.

Risk: The Claude hook may check GitHub releases unless update checks are disabled.

Mitigation: Set STORY_NO_UPDATE_CHECK=1 when release checks are not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-setup)
- [Metadata source repository](https://github.com/zenstory-ai/oh-story-claudecode)
- [Skill definition](SKILL.md)
- [Upgrade guide](UPGRADING.md)
- [Claude deployment template](references/templates/CLAUDE.md.tmpl)
- [Codex deployment template](references/codex/AGENTS.md.tmpl)
- [OpenCode deployment template](references/opencode/AGENTS.md.tmpl)
- [ZCode deployment template](references/zcode/AGENTS.md.tmpl)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline commands, file edits, and configuration changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local project files, hooks, agent definitions, templates, and sentinel metadata.]

## Skill Version(s):

1.1.20 (source: release metadata; bundled SKILL.md reports 1.2.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
