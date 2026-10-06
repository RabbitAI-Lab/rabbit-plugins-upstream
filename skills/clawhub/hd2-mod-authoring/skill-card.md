## Description:

Guides Helldivers 2 mod authoring, installation, troubleshooting, and static inspection of downloaded mod tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cavadus](https://clawhub.ai/user/cavadus)

### License/Terms of Use:

MIT-0

## Use Case:

Helldivers 2 mod developers use this skill to identify conflicting patches, edit and package mods, verify changes against game logs, and assess downloaded mod tools without executing them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes to local mod-manager files or mod packages may disrupt the installed configuration.

Mitigation: Back up hd2a_data.json before changes and review the packaged mod before deployment.

Risk: Diagnostic game-memory dumps may retain sensitive local game data after troubleshooting.

Mitigation: Review or delete Hd2ProjRecon dumps when finished.

## Reference(s):

- [Skill homepage](https://github.com/Cavadus/hd2-mod-authoring)
- [Install and format reference](references/install-and-format.md)
- [Memory census reference](references/memory-census.md)
- [HUD overlay reference](references/hud-overlay.md)
- [Mods catalog](references/mods-catalog.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include mod packages and diagnostic game-memory dumps.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
