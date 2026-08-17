## Description:

A Minecraft mod ecosystem management skill for mod search, environment setup, Mixin conflict scanning, crash analysis and repair guidance, translation, migration assessment, save synchronization, and local usage management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liang030214](https://clawhub.ai/user/liang030214)

### License/Terms of Use:

MIT-0

## Use Case:

Minecraft players, modpack authors, and developers use this skill to inspect mod JARs, find compatible mods, assess loader or version migrations, analyze crashes, and generate setup or repair guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may contact third-party services during localization, mod lookup, or crash analysis.

Mitigation: Use offline mode for privacy-sensitive crash analysis and disable downloads when only search or assessment output is needed.

Risk: The skill can download, replace, back up, restore, or repackage local Minecraft files.

Mitigation: Review planned file changes before execution, avoid auto-confirm for unreviewed fixes, and keep separate backups of worlds and mod folders.

Risk: Save restoration from an untrusted or shared sync folder may be unsafe until ZIP path validation is fixed.

Mitigation: Restore only from trusted backup archives and inspect sync-folder contents before extracting them into a game directory.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/liang030214/skills/mc-ecosystem-adapt-engine)
- [Modrinth API](https://api.modrinth.com/v2)
- [CurseForge API](https://api.curseforge.com/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Text, Markdown reports, JSON results, and command-line guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local reports, caches, backups, downloaded mod JARs, and save archives when the corresponding feature is used.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
