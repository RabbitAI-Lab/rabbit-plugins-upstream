## Description:

Installs, repairs, or customizes an OpenClaw cyberpunk chat and dream theme with swappable avatars and background images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kasanuowa](https://clawhub.ai/user/kasanuowa)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to install or reapply a cyberpunk visual theme, swap five visual asset slots, and restore compatibility after OpenClaw Control UI updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer writes theme files into the selected workspace and can apply changes to the live OpenClaw Control UI.

Mitigation: Use --skip-apply to stage files first, then review the workspace path and generated apply script before applying the theme.

Risk: Default visual assets may be downloaded when they are not bundled locally.

Mitigation: Install only when the ClawHub release source is acceptable for the workspace and rely on the installer SHA-256 checks for downloaded defaults.

## Reference(s):

- [Theme Slots](references/theme-slots.md)
- [Theme Config Example](references/theme-config.example.json)
- [ClawHub Skill Page](https://clawhub.ai/kasanuowa/skills/cyberpunk-theme)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference workspace paths and optional visual asset paths.]

## Skill Version(s):

1.0.26 (source: server release metadata and artifact changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
