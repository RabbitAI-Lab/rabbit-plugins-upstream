## Description:

Dotfile helps agents manage local dotfile synchronization across AI tool configurations, chezmoi, MCP server lists, Syncthing, and Serena memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and power users use this skill to synchronize agent skills, rules, and configuration directories, manage chezmoi-backed dotfiles and MCP settings, diagnose Syncthing issues, and preserve useful session knowledge in Serena memory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide changes to local dotfile, agent configuration, MCP, and Syncthing state.

Mitigation: Review target paths and generated commands before execution, and confirm backups exist before replacing directories or files with links.

Risk: Knowledge-sync workflows may save session-derived content into project documentation or Serena memory.

Mitigation: Preview extracted knowledge and remove secrets, stale facts, or project-private material before persisting it.

Risk: Syncthing maintenance guidance includes manual administrative operations such as Task Scheduler changes and database resets.

Mitigation: Treat these steps as exceptional recovery actions, verify the affected folder and device state first, and avoid running them as routine maintenance.

## Reference(s):

- [Dotfile skill page](https://clawhub.ai/drumrobot/skills/dotfile)
- [Multi-Agent Shared Layout](agents.md)
- [Chezmoi Template Management](chezmoi.md)
- [Knowledge Sync](knowledge.md)
- [MCP Server Synchronization](mcp.md)
- [Syncthing Integration](syncthing.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with inline shell commands and configuration paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local filesystem changes, symlinks, hard links, backups, MCP updates, and Syncthing maintenance steps for user review before execution.]

## Skill Version(s):

0.5.1 (source: server release metadata and CHANGELOG, released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
