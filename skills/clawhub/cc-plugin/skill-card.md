## Description:

Helps Claude Code users create, manage, test, troubleshoot, and clean up plugins and plugin marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to manage Claude Code plugin lifecycles, including plugin authoring, marketplace setup, cache cleanup, local development reflection, HUD configuration, clustering recommendations, and troubleshooting. It provides operational guidance plus shell commands and configuration examples for local plugin workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persistently modify Claude Code plugin files, installed cache directories, and settings under ~/.claude.

Mitigation: Use documented dry-run modes first, review planned filesystem changes, and run commands only for plugin sources and marketplaces you trust.

Risk: The dev-reflect workflow documents a same-repository and worktree hazard where sync operations can overwrite active development files.

Mitigation: Before running dev reflection, verify the marketplace clone and source repository are not the same path, symlink target, or worktree of the same repository.

Risk: Cache cleanup removes older plugin version directories and temporary marketplace cache directories.

Mitigation: Run cache cleanup with dry-run output first and confirm that the selected cache directories are disposable before allowing deletion.

Risk: Troubleshooting guidance can include build, install, or cache-copy commands for plugin artifacts.

Mitigation: Avoid npm install/build and cache-copy commands for untrusted plugins, and inspect plugin source and generated files before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/cc-plugin)
- [Skill entrypoint](artifact/SKILL.md)
- [Plugin creation guide](artifact/create.md)
- [Marketplace guide](artifact/marketplace.md)
- [Dev reflection guide](artifact/dev-reflect.md)
- [Troubleshooting guide](artifact/troubleshoot.md)
- [Cache cleanup guide](artifact/cache.md)
- [Plugin clustering guide](artifact/clustering.md)
- [HUD configuration guide](artifact/hud.md)
- [Release changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local file edits and commands that modify Claude Code plugin marketplaces, caches, settings, hooks, skills, commands, and plugin component directories.]

## Skill Version(s):

0.7.2 (source: ClawHub release metadata and CHANGELOG, released 2026-09-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
