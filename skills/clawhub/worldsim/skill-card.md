## Description:

WorldSim.Life is an agent skill for running local persistent story worlds, importing SillyTavern character cards, advancing interactive narratives, and managing save, load, rollback, and state-repair workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaowh](https://clawhub.ai/user/zhaowh)

### License/Terms of Use:

MIT

## Use Case:

Players, writers, and creators use this skill to create and continue local interactive story worlds with persistent character, scene, conflict, and narrative state. It also supports importing SillyTavern-compatible character cards and managing world saves, loads, resets, snapshots, audits, and scene changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: World records, narratives, snapshots, and imported character cards are persisted on local disk and may contain sensitive user-provided content.

Mitigation: Do not put passwords, secrets, or sensitive personal data into stories or character cards; use WORLDSIM_WORLDS_DIR to place world data on controlled local storage.

Risk: Reset, load, delete, rollback, and force operations can overwrite or remove world progress.

Mitigation: Review confirmation prompts carefully and keep snapshots or backups before destructive operations.

Risk: Imported character cards may contain untrusted, private, or inappropriate material.

Mitigation: Import cards only from trusted sources and review the generated character files and stored import material before continuing the world.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaowh/skills/worldsim)
- [README.en.md](README.en.md)
- [Command Reference](references/commands.md)
- [Disclosure and Confirmation Rules](references/disclosures.md)
- [Character Card Import](references/import_cards.md)
- [Session Recovery](references/session_recovery.md)
- [WorldSim Example Story](https://worldsim.life/welcome_center.htm)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration]

**Output Format:** [Narrative text and Markdown guidance with local world-state files, YAML configuration, and shell command usage.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persists story, scene, character, conflict, snapshot, and imported-card records under the configured worlds data directory.]

## Skill Version(s):

0.9.4 (source: server release metadata; artifact frontmatter says 0.9.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
