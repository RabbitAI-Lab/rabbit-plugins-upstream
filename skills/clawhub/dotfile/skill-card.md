## Description: <br>
Dotfile helps agents manage synchronization workflows for shared AI-tool configuration, chezmoi-managed dotfiles, MCP server lists, Serena knowledge memory, and Syncthing diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to keep local agent, dotfile, MCP, memory, and Syncthing configuration workflows consistent across machines and tools. It provides operational guidance, command patterns, and helper scripts for reviewing and applying synchronization changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Knowledge-sync workflows can move project notes into memory and may capture credentials, personal data, customer data, or confidential infrastructure details. <br>
Mitigation: Review and redact memory candidates before writing them to Serena memory or other persistent stores. <br>
Risk: Syncthing cleanup, database reset, and rescan guidance can affect local synchronization state. <br>
Mitigation: Verify exact paths, folder IDs, and backup state before running cleanup or reset commands. <br>
Risk: Shared AI-tool linking scripts can move existing local configuration directories into backups and replace them with links. <br>
Mitigation: Confirm that ~/.agents is the intended source of truth and inspect backup paths before and after running the scripts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/dotfile) <br>
- [Skill overview](SKILL.md) <br>
- [Multi-agent shared layout](agents.md) <br>
- [chezmoi template management](chezmoi.md) <br>
- [Knowledge sync](knowledge.md) <br>
- [MCP server synchronization](mcp.md) <br>
- [Syncthing integration](syncthing.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, code, configuration] <br>
**Output Format:** [Markdown guidance with inline shell, PowerShell, JSON, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local file changes, synchronization cleanup, or shell commands for user review before execution.] <br>

## Skill Version(s): <br>
0.5.0 (source: server release metadata and CHANGELOG, released 2026-08-03) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
