## Description:

Publish Clean guides agents through designing and applying custom UI themes for OpenClaw Control UI, DSH web UI, and other web projects, including palette derivation, accessibility checks, injection guidance, self-healing setup, and feedback capture.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hanhan1137](https://clawhub.ai/user/hanhan1137)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and UI maintainers use this skill to plan, generate, validate, and maintain custom themes for OpenClaw Control UI, DSH web UI, static mockups, or other web interfaces. It is most useful when a user wants guided style selection, accessible color tokens, implementation snippets, and repeatable post-upgrade theme restoration steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Theme application can edit UI build files and inject CSS or JavaScript, which may change local web UI behavior.

Mitigation: Require explicit confirmation before file changes, keep backups, review generated CSS and JavaScript, and run the documented validation checks before accepting the theme.

Risk: Persistent self-healing can register a daily cron job and restore theme injection after upgrades.

Mitigation: Inspect crontab after setup, confirm the scheduled command matches the intended theme, and use the documented uninstall path when removing or switching themes.

Risk: Local preference logging can record theme choices for future recommendations.

Mitigation: Review stored preference data and only persist preferences the user explicitly approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hanhan1137/skills/ui-theme-coach)
- [Skill README](artifact/README.md)
- [Minecraft worked example](artifact/references/minecraft-example.md)
- [Open source checklist](artifact/references/open-source-checklist.md)
- [Style templates](artifact/references/styles/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline CSS, JavaScript, JSON, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose file edits, cron setup, snapshots, and validation commands for the target UI; users should approve environment changes before execution.]

## Skill Version(s):

1.5.0 (source: frontmatter, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
