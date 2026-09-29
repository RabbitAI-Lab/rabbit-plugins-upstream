## Description:

Claude Code plugin lifecycle management for creating, managing, reflecting, troubleshooting, and cleaning plugin and marketplace state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to author Claude Code plugins, manage marketplace clones, troubleshoot plugin loading issues, configure HUD statusline behavior, and clean plugin cache state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dev-reflect helper can bulk-sync or delete plugin files in marketplace clones and cached plugin version directories.

Mitigation: Run with --dry-run first, review source and marketplace paths, and confirm the marketplace clone is not the source repository or a worktree of the same repository before syncing.

Risk: The optional --enable flow persistently changes Claude Code settings.

Mitigation: Use --enable only when intentionally enabling a plugin, review the resulting settings.json change, and keep the generated backup until the plugin behavior is verified.

Risk: Cache cleanup can remove old plugin cache versions and temporary marketplace directories.

Mitigation: Use --dry-run to preview deletions and confirm the cache path and retained latest version before allowing cleanup.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/cc-plugin)
- [SKILL.md](artifact/SKILL.md)
- [Cache Cleanup](artifact/cache.md)
- [Plugin Clustering Recommendation](artifact/clustering.md)
- [Plugin Creation](artifact/create.md)
- [Dev Reflect](artifact/dev-reflect.md)
- [OMC HUD Statusline Configuration](artifact/hud.md)
- [Marketplace Management](artifact/marketplace.md)
- [Plugin Troubleshooting](artifact/troubleshoot.md)
- [Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend or run local filesystem operations for Claude Code plugin directories when the agent is given appropriate tools.]

## Skill Version(s):

0.8.0 (source: server release metadata, released 2026-09-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
