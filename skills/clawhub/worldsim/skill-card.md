## Description:

WorldSim is a local persistent world-simulation and story-engine skill for creating, launching, role-playing in, importing character cards into, and managing interactive narrative worlds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaowh](https://clawhub.ai/user/zhaowh)

### License/Terms of Use:

MIT

## Use Case:

External users, role-play players, story creators, and developers use WorldSim to run persistent interactive narrative worlds, continue scenes, import SillyTavern character cards, and manage saves, rollbacks, resets, audits, and local state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Westworld world can steer interactions toward adult, coercive sexual, and violent roleplay.

Mitigation: Install only if mature Westworld content is acceptable, require explicit entry confirmation, and remove or sanitize the bundled demo world if those paths are not wanted.

Risk: World state, narrative history, snapshots, and imported character-card source content are persisted on local disk.

Mitigation: Use a dedicated WORLDSIM_WORLDS_DIR, avoid entering secrets or sensitive personal data, review imported cards before use, and delete the relevant world/import files when retention is not desired.

Risk: The skill uses maintenance scripts that read, write, reset, delete, import, and validate files under the worlds data root.

Mitigation: Run it in a controlled workspace, keep world data in a dedicated directory, and require confirmation before destructive operations such as reset, load, delete, or scene reset.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaowh/skills/worldsim)
- [README](README.md)
- [English README](README.en.md)
- [Commands reference](references/commands.md)
- [Disclosures and confirmations](references/disclosures.md)
- [SillyTavern character-card import](references/import_cards.md)
- [Session recovery](references/session_recovery.md)
- [Scene management](references/scene_management.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown narrative text, local world-state files, YAML configuration/state updates, and shell command guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires local filesystem access to worlds/ and python3; supports optional WORLDSIM_WORLDS_DIR for a dedicated worlds data directory.]

## Skill Version(s):

0.8.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
