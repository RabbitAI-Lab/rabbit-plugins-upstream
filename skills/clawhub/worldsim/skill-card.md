## Description:

WorldSim is an agent skill that runs a local, persistent world simulator and story engine, importing character cards, advancing interactive narratives, and supporting save, load, rollback, and state repair.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaowh](https://clawhub.ai/user/zhaowh)

### License/Terms of Use:

MIT

## Use Case:

External users and creators use this skill to create and run persistent roleplay worlds with local state, imported character cards, narrative continuity, snapshots, resets, and audits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: World data, narrative logs, snapshots, and imported character card content are persisted on local disk.

Mitigation: Keep worlds in a dedicated directory, use WORLDSIM_WORLDS_DIR when separating data from the skill install, and avoid entering secrets or personal sensitive information.

Risk: Imported character cards may contain untrusted or unauthorized content.

Mitigation: Import only character cards you trust and have rights to use; retain awareness that original imported material is stored under the world's import directory.

Risk: Reset, load, delete, and snapshot deletion operations can remove or overwrite local world state.

Mitigation: Use explicit commands for destructive operations and confirm the intended world, scene, or snapshot before proceeding.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaowh/skills/worldsim)
- [README.en.md](README.en.md)
- [Command reference](references/commands.md)
- [Character card import](references/import_cards.md)
- [Scene management](references/scene_management.md)
- [Session recovery](references/session_recovery.md)
- [Rollback](references/rollback.md)
- [Write protocol](references/write_protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown narrative and guidance with local file, YAML, and shell command artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persists world state, narrative logs, snapshots, imported character card material, and configuration under a local worlds directory.]

## Skill Version(s):

0.7.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
