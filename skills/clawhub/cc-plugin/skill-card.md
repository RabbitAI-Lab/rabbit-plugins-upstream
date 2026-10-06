## Description:

Guides Claude Code plugin creation, marketplace maintenance, cache cleanup, local development sync, configuration, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Claude Code plugin developers and maintainers use this skill to plan plugin bundles, create and test plugins, maintain marketplace installations, and diagnose plugin failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Helper scripts can modify plugin caches and persistent Claude Code settings.

Mitigation: Review changes first with --dry-run; back up settings and plugin cache content before syncing or cleanup, and use --enable only when intended.

Risk: Insufficient path-scope safeguards can affect unintended files during sync or cleanup.

Mitigation: Run scripts only against trusted local repositories and marketplace metadata, and verify source and target paths before applying changes.

## Reference(s):

- [ClawHub cc-plugin release](https://clawhub.ai/drumrobot/skills/cc-plugin)
- [Plugin authoring guide](create.md)
- [Local development sync guide](dev-reflect.md)
- [Plugin troubleshooting guide](troubleshoot.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.8.1 (source: ClawHub release and bundled changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
