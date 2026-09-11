## Description:

WorldSim is an agent skill for running persistent interactive story worlds, importing SillyTavern character cards, advancing narrative state, and managing saves, loads, rollbacks, resets, and local state repair.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaowh](https://clawhub.ai/user/zhaowh)

### License/Terms of Use:

MIT

## Use Case:

External users and creators use this skill to create, enter, and continue persistent roleplay worlds where an agent maintains world state, character state, scenes, conflicts, and narrative archives on local storage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes, rewrites, archives, and deletes local story-world files, and server security evidence notes that some destructive operations need review because they are not protected by code-enforced confirmation or verified backups.

Mitigation: Use a dedicated WORLDSIM_WORLDS_DIR, keep independent backups, and review reset, load, delete, and migration operations before execution.

Risk: World files persist narrative, character, and imported-card-derived content on local disk.

Mitigation: Do not store passwords, secrets, real sensitive personal information, or real health information in worlds; delete the relevant worlds directory when records should be removed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaowh/skills/worldsim)
- [README.en.md](artifact/README.en.md)
- [SKILL.md](artifact/SKILL.md)
- [Disclosures](artifact/references/disclosures.md)
- [Commands](artifact/references/commands.md)
- [Write Protocol](artifact/references/write_protocol.md)
- [Import Cards](artifact/references/import_cards.md)
- [Session Recovery](artifact/references/session_recovery.md)
- [Rollback](artifact/references/rollback.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown narrative with shell command proposals and YAML/Markdown state updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create, modify, archive, or delete local world files under worlds/ or the configured WORLDSIM_WORLDS_DIR.]

## Skill Version(s):

0.27.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
