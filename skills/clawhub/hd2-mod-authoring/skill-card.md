## Description:

Guides agents through authoring, installing, debugging, and checking Helldivers 2 mods, including patch packaging and game-memory modifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cavadus](https://clawhub.ai/user/cavadus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and mod authors use this skill to identify mod formats and conflicts, prepare and deploy patches, validate changes against game logs, and assess downloaded mod tools before running them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Game-process memory reads and writes can crash the game or corrupt its state.

Mitigation: Work only on your own launched game, keep backups, verify each target before writing, and recheck layouts after game updates.

Risk: Edits to mod and configuration files or deployed packages may replace working versions.

Mitigation: Back up files, check for conflicting mods, and verify the deployed package and game log after changes.

Risk: Diagnostic add-ons can leave behind game-memory dumps.

Mitigation: Run diagnostics only on your own game and delete Hd2ProjRecon dumps when finished.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cavadus/skills/hd2-mod-authoring)
- [Project homepage](https://github.com/Cavadus/hd2-mod-authoring)
- [Installation and patch formats](references/install-and-format.md)
- [Memory census](references/memory-census.md)
- [HUD overlay](references/hud-overlay.md)
- [Mod catalog](references/mods-catalog.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown with code blocks and mod or configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include packaged mod archives and diagnostic outputs]

## Skill Version(s):

0.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
