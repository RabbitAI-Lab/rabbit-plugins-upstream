## Description:

One-stop Minecraft mod ecosystem intelligent management tool with 10+ features including mod search, environment setup, Mixin conflict scanning, crash fix, translation, migration assessment, and intelligent multi-language support (11 languages with auto-detection via IP geolocation).

This skill is ready for commercial/non-commercial use.

## Publisher:

[liang030214](https://clawhub.ai/user/liang030214)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, modpack maintainers, and Minecraft players use this skill to inspect mod JARs, search for compatible mods, configure Minecraft environments, scan Mixin conflicts, analyze crashes, apply backed-up auto-fixes, translate mod resources, and assess cross-version or cross-loader migrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use automatic third-party IP geolocation for language detection.

Mitigation: Prefer explicit language selection where available and review whether automatic location detection is acceptable before deployment.

Risk: The skill can query third-party mod services and download executable JAR files.

Mitigation: Use offline mode when network access is not needed, and manually review downloaded mods before adding them to a game environment.

Risk: Auto-fix and save-restore features can mutate Minecraft directories and replace files.

Mitigation: Require manual review and backups before auto-fix or restore operations, especially when using auto-confirm options.

Risk: The skill stores local licensing and usage-state data.

Mitigation: Review local state-file behavior and retention expectations before installing in managed or shared environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liang030214/skills/mc-ecosystem-adapt-engine)
- [Project homepage declared in ClawHub metadata](https://github.com/Liang030214/mc-skill-v1)
- [Modrinth API](https://api.modrinth.com/v2)
- [CurseForge API](https://api.curseforge.com/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and JSON with inline shell commands and generated reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate local reports, backups, downloads, logs, translated resources, and mod compatibility recommendations.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
