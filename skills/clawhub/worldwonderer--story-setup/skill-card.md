## Description:

Sets up and checks web-fiction writing projects across supported agent environments, including their writing skills, configuration, and hooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and developers use this skill to install or inspect writing-tool infrastructure in a project for Claude Code, OpenCode, Codex, Google Antigravity, ZCode, OpenClaw, Reasonix, or a general-purpose agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deployment installs persistent project hooks that can run during later writing sessions.

Mitigation: Install only in a trusted writing project and review the project hook files before enabling them.

Risk: Codex automation guidance suggests bypassing hook trust checks.

Mitigation: Do not use --dangerously-bypass-hook-trust unless every hook command has been separately allowlisted.

Risk: OpenCode upgrade guidance includes a curl-to-bash installer option.

Mitigation: Prefer npm or a verified installer flow for OpenCode upgrades.

## Reference(s):

- [ClawHub story-setup release](https://clawhub.ai/worldwonderer/skills/story-setup)
- [Project link listed in skill metadata (not verified import provenance)](https://github.com/zenstory-ai/oh-story-claudecode)
- [Deployment diagnostics](references/diagnostics.md)
- [Codex deployment guidance](references/deploy-codex.md)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Guidance]

**Output Format:** [Markdown guidance and project configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can install persistent project hooks and provide an environment diagnostic report.]

## Skill Version(s):

1.1.26 (source: ClawHub release metadata; artifact frontmatter says 1.3.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
