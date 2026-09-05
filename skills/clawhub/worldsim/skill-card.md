## Description:

WorldSim is an agent skill for running persistent local story worlds, importing SillyTavern character cards, advancing interactive narrative, and managing save, load, rollback, and state repair workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaowh](https://clawhub.ai/user/zhaowh)

### License/Terms of Use:

MIT

## Use Case:

Players, creators, and agent-skill users use WorldSim to create or enter persistent fictional worlds, role-play through scenes, import character cards, and turn the resulting stateful play into ongoing narrative records. It is intended for users who want deep interactive storytelling with local world state that can be saved, loaded, audited, repaired, or reset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill keeps persistent local story records and may read, write, or delete world data files during gameplay state management.

Mitigation: Use a dedicated worlds directory, review destructive actions before confirming them, and keep backups for important worlds.

Risk: Story text and imported character cards may contain private or sensitive material that becomes part of local world records.

Mitigation: Do not store passwords, secrets, or sensitive personal information in stories, character cards, or imported content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaowh/skills/worldsim)
- [README.en.md](README.en.md)
- [Commands Reference](references/commands.md)
- [Write Protocol](references/write_protocol.md)
- [Session Recovery](references/session_recovery.md)
- [Import Cards](references/import_cards.md)
- [Evaluation README](evals/README.md)
- [WorldSim Welcome Center Example](https://worldsim.life/welcome_center.htm)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown narrative prose with local Markdown/YAML world-state files and occasional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persists world data under worlds/ or WORLDSIM_WORLDS_DIR; destructive load, reset, and delete actions require user confirmation.]

## Skill Version(s):

0.25.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
