## Description:

story-setup deploys a Chinese web-novel writing toolkit across Claude Code, OpenCode, Codex, ZCode, OpenClaw, Reasonix, and generic agent environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and writing teams use this skill to bootstrap project-local agents, hooks, commands, rules, and reference material for long-form Chinese web-novel projects while preserving existing user configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent hooks and project configuration can run shell, Node, or Python during agent sessions or tool use.

Mitigation: Install only in trusted writing projects and review generated .claude, .codex, .opencode, .zcode, AGENTS.md, CLAUDE.md, skills/, and .git/hooks changes before use.

Risk: A passive GitHub version check may make an outbound network call.

Mitigation: Set STORY_NO_UPDATE_CHECK when this network behavior is not desired.

Risk: Browser/CDP-related routes may interact with the current browser session.

Mitigation: Use browser/CDP-related routes only when that session access is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-setup)
- [metadata.openclaw.source](https://github.com/worldwonderer/oh-story-claudecode)
- [UPGRADING.md](UPGRADING.md)
- [Writing Craft Reference](references/agent-references/writing-craft.md)
- [Quality Checklist Reference](references/agent-references/quality-checklist.md)
- [Genre Catalog Reference](references/agent-references/genre-catalog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with code, shell, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or merge project-local agent, hook, command, settings, and reference files depending on the selected target CLI.]

## Skill Version(s):

1.1.18 (source: ClawHub release metadata; artifact frontmatter reports 1.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
