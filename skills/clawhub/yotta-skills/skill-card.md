## Description:

元阁 yotta-skills helps agents route tasks to YottaMeta skill combinations, inventory installed skills, and install or update selected yotta-* skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to choose suitable YottaMeta skill combinations, inspect locally installed skills, and install or update skill sets for supported agents or target directories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can ask an agent to add persistent routing guidance to memory files, affecting future sessions.

Mitigation: Require explicit user approval before editing AGENTS.md, CLAUDE.md, or equivalent persistent memory, and review the exact text before saving it.

Risk: Installer, update, and optional MCP/client configuration flows can change local skill directories or agent configuration.

Mitigation: Use dry-run and --pin where appropriate, review the planned changes, and require explicit confirmation before installs, updates, or configuration writes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [README](artifact/README.md)
- [Install Flow](artifact/references/install-flow.md)
- [Orchestration](artifact/references/orchestration.md)
- [Skill List](artifact/references/skill-list.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, plain text, JSON, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include installation previews, routing recommendations, local inventory data, and MCP or client configuration snippets.]

## Skill Version(s):

0.6.1 (source: server release, SKILL.md frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
