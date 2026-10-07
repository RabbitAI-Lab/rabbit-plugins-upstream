## Description:

Guides Helldivers 2 mod authors through install audits, conflict checks, Lua and resource patching, game-log verification, HUD changes, and static review of downloaded mod tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cavadus](https://clawhub.ai/user/cavadus)

### License/Terms of Use:

MIT-0

## Use Case:

Game mod developers use this skill to author and verify Helldivers 2 patches, avoid conflicting installs, and inspect downloaded mod tools before running them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Runtime memory edits can crash the game or corrupt game state.

Mitigation: Back up mod files and Arsenal configuration; restrict edits to your own game process, verify each target before writing, and check the result afterward.

Risk: Downloaded mod managers or tools may be unsafe to execute.

Mitigation: Inspect downloaded tools without running them and skip suspicious installers.

Risk: Local memory dumps may expose data, and game or platform rules may limit modding.

Mitigation: Review dumps before sharing and confirm the applicable game and platform rules before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cavadus/skills/hd2-mod-authoring)
- [Project homepage listed in skill metadata](https://github.com/Cavadus/hd2-mod-authoring)
- [Install audit and patch format](artifact/references/install-and-format.md)
- [Read-only memory census](artifact/references/memory-census.md)
- [HUD overlay and game-object state](artifact/references/hud-overlay.md)
- [Mod catalog](artifact/references/mods-catalog.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline code and commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes mod classification, conflict checks, and verification steps.]

## Skill Version(s):

0.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
