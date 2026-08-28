## Description:

Deploys web-novel writing project infrastructure for Claude Code, OpenCode, Codex, Google Antigravity, ZCode, OpenClaw, Reasonix, and generic agent workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and writers use this skill to initialize or refresh a structured web-novel writing workspace with platform-specific agents, hooks, rules, commands, and shared writing references. It supports setup across multiple agent CLIs while preserving user-owned project content and merging managed configuration blocks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs persistent hooks that can run scripts during future agent sessions and file edits.

Mitigation: Install it only in trusted writing projects and review the planned changes to agent directories, AGENTS.md or CLAUDE.md, and .git/hooks/pre-commit before use.

Risk: Some workflows can contact GitHub for update checks.

Mitigation: Set STORY_NO_UPDATE_CHECK=1 when automatic GitHub contact is not acceptable.

Risk: Browser/CDP workflows may reuse a local browser session.

Mitigation: Enable browser or CDP workflows only when that session reuse is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-setup)
- [Publisher profile](https://clawhub.ai/user/worldwonderer)
- [OpenClaw source metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Upgrade guide](UPGRADING.md)
- [Writing reference profiles](references/agent-references/agent-reference-profiles.md)
- [Agent quality reference](references/agent-references/agent-quality.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with generated project files, scripts, hooks, agent definitions, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or merges project-local setup files for supported agent environments; exact changes depend on the selected target CLI and existing workspace state.]

## Skill Version(s):

1.1.21 (source: server release metadata; artifact frontmatter reports 1.2.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
