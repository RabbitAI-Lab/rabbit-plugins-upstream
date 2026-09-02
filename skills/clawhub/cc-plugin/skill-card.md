## Description:

Claude Code plugin lifecycle management for creating, installing, updating, caching, troubleshooting, marketplace handling, clustering, and HUD configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use cc-plugin to manage Claude Code plugin authoring, marketplace setup, local release testing, cache cleanup, load troubleshooting, bundle membership analysis, and HUD configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plugin management commands can persistently change which plugins and executable components load in future Claude Code sessions.

Mitigation: Review proposed changes before installing or enabling plugins, inspect settings and cache diffs, and restart only after confirming the intended plugin set.

Risk: Repair and dev-reflect workflows can operate on marketplace clones, cache paths, and plugin settings.

Mitigation: Use trusted marketplace and source paths, run dry-run modes first when available, and avoid --enable unless future session plugin activation is intended.

Risk: Cache cleanup removes old cache versions and temporary plugin cache directories.

Mitigation: Run the cleanup helper with --dry-run first and confirm the listed paths are disposable cache entries before deletion.

## Reference(s):

- [cc-plugin skill page](https://clawhub.ai/drumrobot/skills/cc-plugin)
- [Cache Cleanup](cache.md)
- [Plugin Clustering Recommendation](clustering.md)
- [Plugin Creation](create.md)
- [Dev Reflect](dev-reflect.md)
- [OMC HUD Statusline Configuration](hud.md)
- [Marketplace Management](marketplace.md)
- [Plugin Troubleshooting](troubleshoot.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose filesystem changes under Claude Code plugin marketplace, cache, HUD, and settings paths.]

## Skill Version(s):

0.6.2 (source: server evidence release.version and target metadata; changelog released 2026-09-01)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
