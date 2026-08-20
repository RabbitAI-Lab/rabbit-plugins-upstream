## Description:

Provides Obsidian command-line workflow guidance for vault file operations, search, templates, plugin and theme management, Sync and history tasks, developer debugging, workspace management, and TUI usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, advanced Obsidian users, and teams use this skill to ask an agent for CLI-oriented Obsidian vault administration, including note operations, audits, templates, plugin/theme workflows, Sync history recovery, and debugging steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad vault-changing actions such as delete, overwrite, restore, Sync toggles, plugin/theme installs, snippet changes, and arbitrary JavaScript eval commands.

Mitigation: Require explicit user confirmation before destructive or state-changing commands, keep backups or version history enabled, and review generated commands before execution.

Risk: Installing untrusted Obsidian plugins or themes can introduce code or content risks in a vault.

Mitigation: Install only trusted plugins and themes, verify plugin identifiers and sources, and avoid enabling new extensions without review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/obsidian-cli-tool-pro)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include operational checklists, troubleshooting guidance, and command examples for Obsidian CLI workflows.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
