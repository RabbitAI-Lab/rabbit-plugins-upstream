## Description:

Dotfile helps agents manage shared AI tool configuration, dotfile templates, MCP server synchronization, knowledge sync, and Syncthing diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to coordinate dotfiles and AI tool configuration across Claude, Codex, Gemini, Antigravity, Cursor, UTCP, chezmoi, Serena, and Syncthing workflows. It provides guidance and commands for sharing configuration, syncing MCP server lists, capturing session knowledge, and diagnosing sync state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make a shared ~/.agents source control multiple AI tool configurations and can move existing local folders into backups before linking.

Mitigation: Install and run linking scripts only when shared control is intended; inspect the proposed source and target paths and confirm backups before execution.

Risk: Knowledge sync workflows can persist conversation-derived project details into Serena memory.

Mitigation: Review candidate knowledge before writing memory and exclude secrets, credentials, sensitive project details, or one-time troubleshooting notes.

Risk: Syncthing recovery, database reset, service migration, and cleanup commands can change sync state, startup behavior, or local files.

Mitigation: Check paths, stop services intentionally, make backups, and verify sync health before deleting indexes, changing services, or applying recovery commands.

Risk: MCP and chezmoi workflows can propagate configuration changes across several tools.

Mitigation: Review generated MCP server entries and chezmoi changes before applying them to shared configuration targets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/dotfile)
- [SKILL.md](SKILL.md)
- [Multi-Agent Shared Layout](agents.md)
- [Chezmoi Template Management](chezmoi.md)
- [Knowledge Sync](knowledge.md)
- [MCP Server Synchronization](mcp.md)
- [Syncthing Integration](syncthing.md)
- [CHANGELOG](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose filesystem, symlink, hard-link, MCP, chezmoi, Syncthing, and memory-write operations that should be reviewed before execution.]

## Skill Version(s):

0.6.1 (source: server release metadata and changelog, released 2026-09-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
