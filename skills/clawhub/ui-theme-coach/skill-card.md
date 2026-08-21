## Description:

Guided UI theme design assistant for OpenClaw Control UI, DSH web UI, and other Web projects, producing palettes, style guidance, injection snippets, accessibility checks, and an optional self-healing workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hanhan1137](https://clawhub.ai/user/hanhan1137)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use this skill to plan and apply custom visual themes for OpenClaw Control UI, DSH web UI, or other Web interfaces. It helps translate style goals into CSS variables, theme assets, validation steps, and implementation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to modify UI build files.

Mitigation: Require explicit confirmation before file edits and keep the documented backup and validation steps before accepting theme changes.

Risk: The self-healing workflow can add a daily cron job that reapplies theme changes.

Mitigation: Use the palette and design guidance without cron when persistence is not needed, or require explicit approval before registering scheduled self-healing.

Risk: The skill can store local theme preferences.

Mitigation: Write preference data only after the user explicitly confirms that a style or color choice should be remembered.

## Reference(s):

- [OpenClaw UI Theme Coach on ClawHub](https://clawhub.ai/hanhan1137/skills/ui-theme-coach)
- [Minecraft worked example](references/minecraft-example.md)
- [Open source checklist](references/open-source-checklist.md)
- [Pixel and game style template](references/styles/pixel-game.md)
- [Cyberpunk style template](references/styles/cyberpunk.md)
- [Cartoon and cute style template](references/styles/cartoon-cute.md)
- [Minimal modern style template](references/styles/minimal-modern.md)
- [Dark tech style template](references/styles/dark-tech.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CSS, HTML/JavaScript, and shell command snippets; may also produce local theme files when applied.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include palette variables, contrast-check results, backup steps, cron guidance, and theme self-healing commands.]

## Skill Version(s):

1.4.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
