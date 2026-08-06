## Description:

Claude Code plugin lifecycle management for creating, installing, updating, caching, troubleshooting, clustering, and configuring plugin workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to manage Claude Code plugin authoring, marketplace setup, cache cleanup, local reflection testing, HUD configuration, clustering recommendations, and plugin troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace clone, update, and dev-reflect workflows can change which plugin code and hooks are available to Claude Code.

Mitigation: Verify repository and source paths before running clone, update, or dev-reflect, review changes before pulling, and restart only after confirming the intended plugin source.

Risk: The dev-reflect --enable path can persistently enable a plugin in settings.

Mitigation: Use --enable only when the plugin should remain active in future sessions, keep the generated settings backup until verified, and prefer dry-run first.

Risk: Cache cleanup can delete older plugin cache versions and temporary git directories.

Mitigation: Run cache cleanup with --dry-run before deletion and confirm all affected paths are under ~/.claude/plugins/cache.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/cc-plugin)
- [SKILL.md](artifact/SKILL.md)
- [Cache Cleanup](artifact/cache.md)
- [Plugin Clustering Recommendation](artifact/clustering.md)
- [Plugin Creation](artifact/create.md)
- [Dev Reflect](artifact/dev-reflect.md)
- [OMC HUD Statusline Configuration](artifact/hud.md)
- [Marketplace Management](artifact/marketplace.md)
- [Plugin Troubleshooting](artifact/troubleshoot.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose file edits, cache cleanup commands, marketplace updates, and local test reflection steps.]

## Skill Version(s):

0.5.2 (source: server release metadata and changelog, released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
