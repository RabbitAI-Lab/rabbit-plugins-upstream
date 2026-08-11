## Description:

WorldSim is a world simulator and story engine for role-play worlds with persistent local state, conflict-driven narration, and SillyTavern character-card import.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaowh](https://clawhub.ai/user/zhaowh)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use WorldSim to run persistent interactive story worlds, import character cards, manage scenes and snapshots, and generate conflict-driven narrative turns while storing world state locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: WorldSim stores narratives, snapshots, world state, and full imported character-card material on local disk.

Mitigation: Do not enter passwords, secrets, or sensitive personal information into stories, and delete the relevant worlds/ directory when local records should be removed.

Risk: Reset, load, delete, and similar maintenance commands can overwrite or remove local world state.

Mitigation: Use the documented confirmation prompts and --force options carefully, and review the target world or snapshot before running destructive operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaowh/skills/worldsim)
- [README.en.md](README.en.md)
- [commands.md](references/commands.md)
- [import_cards.md](references/import_cards.md)
- [scene_management.md](references/scene_management.md)
- [session_recovery.md](references/session_recovery.md)
- [write_protocol.md](references/write_protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Narrative text and Markdown guidance, with local world-state file updates and shell command invocations when maintaining a world.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3 and a local worlds/ directory; generated story state, snapshots, and imported character-card material are kept on local disk.]

## Skill Version(s):

0.3.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
