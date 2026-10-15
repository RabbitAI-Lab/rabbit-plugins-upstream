## Description:

Helps Claude Code users create and manage plugins, marketplaces, caches, statusline settings, and plugin troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to create and bundle Claude Code plugins, maintain marketplaces and caches, test local changes, configure the HUD, and diagnose plugin failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cache cleanup can remove older cached plugin versions and temporary directories.

Mitigation: Preview deletions with --dry-run before cleanup.

Risk: Local development syncing can overwrite files in a marketplace test clone.

Mitigation: Review the source tree and use --dry-run before syncing.

Risk: Enabling a test plugin changes persistent Claude Code settings.

Mitigation: Use --enable only when the intended plugin and marketplace are confirmed.

## Reference(s):

- [cc-plugin release](https://clawhub.ai/drumrobot/skills/cc-plugin)
- [Plugin authoring guide](artifact/create.md)
- [Local plugin testing guide](artifact/dev-reflect.md)
- [Plugin troubleshooting guide](artifact/troubleshoot.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Analysis]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local file and plugin setting changes.]

## Skill Version(s):

0.8.2 (source: ClawHub release and CHANGELOG; skill metadata lists 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
