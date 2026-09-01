## Description:

Claude Code plugin lifecycle management for creating, installing, updating, caching, troubleshooting, and maintaining plugin marketplace workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to manage Claude Code plugin authoring, marketplace registration, local cache cleanup, load-error troubleshooting, HUD statusline configuration, and pre-push plugin testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change persistent Claude Code plugin settings, marketplace clones, cache directories, and enabled plugin state.

Mitigation: Use it only for trusted local plugin development and maintenance, keep backups of ~/.claude settings and marketplace files, and prefer dry-run modes where available.

Risk: The security evidence reports a concrete command-injection risk in one helper script.

Mitigation: Do not run dev-reflect or cache-sync commands against untrusted repository paths, marketplaces, or plugins until the helper and raw fallback guidance are tightened.

Risk: Cache cleanup behavior can delete old plugin cache versions and temporary directories.

Mitigation: Run cache cleanup in dry-run mode first and confirm the cache root and target versions before allowing deletion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/cc-plugin)
- [Skill overview](artifact/SKILL.md)
- [Plugin creation guide](artifact/create.md)
- [Marketplace management guide](artifact/marketplace.md)
- [Plugin troubleshooting guide](artifact/troubleshoot.md)
- [Cache cleanup guide](artifact/cache.md)
- [Dev reflect guide](artifact/dev-reflect.md)
- [OMC HUD configuration guide](artifact/hud.md)
- [Plugin clustering guide](artifact/clustering.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell, JSON, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend local file edits, cache cleanup commands, marketplace synchronization steps, and plugin troubleshooting checks.]

## Skill Version(s):

0.6.1 (source: server release metadata and CHANGELOG, released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
