## Description:

Claude Code plugin lifecycle management for creating, installing, updating, caching, troubleshooting, and configuring plugin workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to manage Claude Code plugin authoring, marketplace operations, cache cleanup, local development reflection, HUD configuration, clustering decisions, and troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cache cleanup and development reflection can delete old cache directories or overwrite local marketplace clone files when run with write mode enabled.

Mitigation: Use --dry-run first, confirm trusted local source and marketplace names, and review the affected paths before running write operations.

Risk: Enabling a reflected plugin can modify ~/.claude/settings.json and affect which plugin version Claude Code loads in later sessions.

Mitigation: Review the settings change and keep the documented backup until the enabled plugin has been verified in a new session.

Risk: Troubleshooting steps may copy plugin assets or MCP configuration into cache locations, which can mask the difference between source-of-truth files and loaded cache files.

Mitigation: Verify the marketplace, plugin name, source path, and destination path before copying, and persist durable fixes in the source repository or marketplace entry.

## Reference(s):

- [cc-plugin on ClawHub](https://clawhub.ai/drumrobot/skills/cc-plugin)
- [SKILL.md](SKILL.md)
- [Cache Cleanup](cache.md)
- [Plugin Clustering Recommendation](clustering.md)
- [Plugin Creation](create.md)
- [Dev Reflect](dev-reflect.md)
- [OMC HUD Statusline Configuration](hud.md)
- [Marketplace Management](marketplace.md)
- [Plugin Troubleshooting](troubleshoot.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON/configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local file operations for Claude Code plugin cache, marketplace clones, hooks, and settings; dry-run modes are documented for write-capable helper scripts.]

## Skill Version(s):

0.5.3 (source: release evidence and CHANGELOG, released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
