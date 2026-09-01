## Description:

Install, repair, or customize this OpenClaw cyberpunk chat and dream theme.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kasanuowa](https://clawhub.ai/user/kasanuowa)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to install or repair a cyberpunk chat and dream theme in a target OpenClaw workspace, including replacing the assistant, user, chat background, dream avatar, and dream background visual slots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer modifies the target OpenClaw workspace and live Control UI theme.

Mitigation: Review or retain generated backups, test against the intended workspace, or run with --skip-apply to stage files before applying changes.

Risk: A fresh install with missing default assets can trigger a fallback asset download from ClawHub.

Mitigation: Provide all five asset overrides when avoiding downloads is required, or rely on the installer limits and SHA-256 checks described by the release evidence.

## Reference(s):

- [Theme Slots](references/theme-slots.md)
- [Theme Config Example](references/theme-config.example.json)
- [ClawHub Skill Page](https://clawhub.ai/kasanuowa/skills/cyberpunk-theme)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference user-provided workspace paths and optional visual asset paths.]

## Skill Version(s):

1.0.25 (source: server release metadata and artifact changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
