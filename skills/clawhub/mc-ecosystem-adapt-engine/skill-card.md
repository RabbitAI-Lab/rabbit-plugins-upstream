## Description:

One-stop Minecraft mod ecosystem intelligent management tool with enhanced mod search, batch search, category filtering, dynamic categories, and auto-update compatibility library.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liang030214](https://clawhub.ai/user/liang030214)

### License/Terms of Use:

MIT-0

## Use Case:

External Minecraft modpack creators and players use this skill to search and download mods, diagnose modded environments, analyze crashes, assess migration feasibility, and generate compatibility guidance for Forge, NeoForge, Fabric, and Quilt setups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes under-disclosed privacy, payment, and high-impact file-changing behavior.

Mitigation: Review the README and source before installation, and test on non-critical Minecraft folders first.

Risk: Auto-confirm, restore, sync, or fix flows may modify or replace mods and saves.

Mitigation: Keep backups of real Minecraft folders and avoid auto-confirm or restore options until expected changes are understood.

Risk: The skill may make outbound calls to Modrinth, CurseForge, and IP geolocation providers.

Mitigation: Run it only in environments where those network calls and any required API keys are acceptable.

Risk: Payment prompts and local usage/license tracking may appear after usage limits.

Mitigation: Review the payment and usage-limit terms before relying on the skill for repeated workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liang030214/skills/mc-ecosystem-adapt-engine)
- [Project homepage listed by skill](https://github.com/Liang030214/mc-skill-v1)
- [Modrinth API](https://api.modrinth.com/v2)
- [CurseForge API](https://api.curseforge.com/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Text and Markdown reports with JSON/configuration files, shell commands, and generated guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate reports, scripts, downloaded dependency files, compatibility recommendations, and local backups depending on the selected feature.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
