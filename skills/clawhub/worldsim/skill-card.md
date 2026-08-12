## Description:

WorldSim is a world simulator and story engine for immersive roleplay: it runs persistent local worlds, imports SillyTavern character cards, writes story and state files under worlds/, and uses maintenance scripts for validation, writing, snapshots, reset, deletion, and import.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaowh](https://clawhub.ai/user/zhaowh)

### License/Terms of Use:

MIT

## Use Case:

External users and creators use WorldSim to run persistent, dramatic roleplay worlds where characters, scenes, conflicts, memories, and imported character cards are maintained across sessions. Developers and agent operators can use the bundled scripts and references to manage world creation, scene state, snapshots, rollbacks, and imports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: WorldSim persistently stores story records, world state, snapshots, and imported character cards on local disk.

Mitigation: Do not enter passwords, secrets, or sensitive personal information into stories or imported cards; remove the relevant worlds/ directory when records should be deleted.

Risk: Commands such as /load, /reset, reset-scene, snapshot delete, and reset-world can change or delete local world state.

Mitigation: Review state-changing actions before execution and use --force only for intentional automation.

Risk: The skill invokes local maintenance scripts for validation, writing, snapshots, resets, deletion, and imports.

Mitigation: Install only when local file operations under worlds/ are expected, and review generated or changed files before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaowh/skills/worldsim)
- [README.en.md](README.en.md)
- [WorldSim commands](references/commands.md)
- [SillyTavern character card import](references/import_cards.md)
- [Scene management](references/scene_management.md)
- [Session recovery](references/session_recovery.md)
- [Rollback protocol](references/rollback.md)
- [Write protocol](references/write_protocol.md)
- [Loop machinery](references/loop_machinery.md)
- [WorldSim keys and write semantics](references/keys.md)
- [Knowledge index](references/knowledge_index.md)
- [Foreshadow registry](references/foreshadow.md)
- [Dramatist gate checklist](references/gate_dramatist.md)
- [Writer gate checklist](references/gate_writer.md)
- [Narrative dialogue style](references/narrative_style_dialogue.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Shell commands, Guidance]

**Output Format:** [Narrative text with Markdown and YAML world-state files, plus shell-command-assisted local state operations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persists story records, imported character-card source material, snapshots, and world state under local worlds/ directories.]

## Skill Version(s):

0.4.1 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
