## Description:

Deploys online-fiction writing infrastructure for Claude Code, OpenCode, Codex, ZCode, OpenClaw, Reasonix, and generic agent environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and writing teams use this skill to set up project-local writing workflows, agent routing, hooks, commands, and reference material for long-form and short-form online fiction projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs persistent hooks and command files that can affect future agent sessions and repository behavior.

Mitigation: Review generated hook and command files before enabling the skill in an important repository, and inspect configured hook locations after deployment.

Risk: The skill can configure browser-capable tooling that may interact with logged-in browser sessions.

Mitigation: Use a separate browser profile for browser automation when accounts or sensitive browsing state are involved.

Risk: The skill may perform update checks or automated writing-tool setup that is not appropriate for every project.

Mitigation: Install only in repositories where persistent writing automation is intended, and set STORY_NO_UPDATE_CHECK=1 when update checks are unwanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/worldwonderer/skills/story-setup)
- [OpenClaw metadata source](https://github.com/worldwonderer/oh-story-claudecode)
- [Skill definition](artifact/SKILL.md)
- [Upgrade guide](artifact/UPGRADING.md)
- [Agent reference bundle](artifact/references/agent-references/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions and status reports plus generated project files, hook scripts, command files, and configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or merge persistent project configuration and hook registrations for the selected agent environment.]

## Skill Version(s):

1.1.16 (source: server release metadata; artifact frontmatter reports 1.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
