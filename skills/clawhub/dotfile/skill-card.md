## Description:

dotfile helps agents manage dotfile synchronization, shared AI-agent configuration, MCP server sharing, knowledge sync, and Syncthing diagnostics across local tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to keep dotfiles, agent configuration, MCP server settings, session knowledge, and Syncthing state consistent across local AI tools and machines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make broad changes to AI-agent configuration through symlinks, hard links, and backups across Claude, Codex, Gemini, and Antigravity directories.

Mitigation: Review each source and destination path before running the bootstrap scripts, and inspect any generated .bak backups before deleting them.

Risk: Knowledge sync workflows can persist information extracted from project sessions into Serena memory.

Mitigation: Avoid storing secrets or sensitive session content in memory, and review proposed knowledge candidates before writing them.

Risk: Syncthing workflows use a local API key and include API calls that can modify folder configuration and encryption password fields.

Mitigation: Treat the Syncthing API key as sensitive, keep requests local, and confirm the target folder or device configuration before applying API PUT changes.

Risk: Database reset and Windows service migration steps can stop services, rebuild indexes, or create hidden startup behavior.

Mitigation: Use these procedures only after confirming the operational impact, preserving backups, and verifying Syncthing health before cleanup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/dotfile)
- [Agents shared layout guide](agents.md)
- [Chezmoi template management guide](chezmoi.md)
- [Knowledge sync guide](knowledge.md)
- [MCP server synchronization guide](mcp.md)
- [Syncthing integration guide](syncthing.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell, PowerShell, JSON, XML, and MCP tool examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local file, symlink, hard-link, MCP, and Syncthing configuration changes for user review.]

## Skill Version(s):

0.6.0 (source: server release metadata and CHANGELOG, released 2026-08-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
