## Description:

WorldSim is an agent skill for collaborative world simulation and narrative play, where an LLM runs conflict, narration, continuity, local state, and SillyTavern character-card import.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaowh](https://clawhub.ai/user/zhaowh)

### License/Terms of Use:

MIT

## Use Case:

External users and agent-skill developers use WorldSim to run persistent roleplay worlds, create or resume scenes, manage character and conflict state, and import SillyTavern-compatible character cards into local world files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: WorldSim silently persists generated story text, state files, snapshots, and imported character-card material in local world directories.

Mitigation: Avoid entering secrets or sensitive personal material, and review or remove local worlds, snapshots, and import files before sharing or publishing the skill directory.

Risk: Bundled demo worlds include mature sexual, coercive, and violent scenarios without an explicit opt-in gate.

Mitigation: Review bundled worlds before use and remove or restrict mature demo content when deploying for audiences that have not opted in.

Risk: Reset, load, delete, snapshot, and import commands can overwrite or remove local story state.

Mitigation: Use the documented dry-run, save, and validation commands where available, keep simple world and snapshot names, and back up worlds before destructive operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaowh/skills/worldsim)
- [README.en.md](README.en.md)
- [commands.md](references/commands.md)
- [import_cards.md](references/import_cards.md)
- [write_protocol.md](references/write_protocol.md)
- [scene_management.md](references/scene_management.md)
- [session_recovery.md](references/session_recovery.md)
- [loop_machinery.md](references/loop_machinery.md)
- [narrative_style_dialogue.md](references/narrative_style_dialogue.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown narrative text with shell commands and YAML-oriented state updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes persistent local world, scene, character, conflict, snapshot, and imported-card files under the skill's worlds directory.]

## Skill Version(s):

0.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
