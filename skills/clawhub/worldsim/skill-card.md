## Description:

WorldSim.Life is an agent skill for persistent local world simulation, roleplay, and interactive narrative, including world state files, SillyTavern character-card import, story progression, saves, loads, rollbacks, and state repair.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaowh](https://clawhub.ai/user/zhaowh)

### License/Terms of Use:

MIT

## Use Case:

External users and creators use this skill to run persistent local roleplay worlds, import character cards, progress interactive stories, and manage saved world state across sessions. Developers and power users can also use its scripts and command references to validate, reset, snapshot, import, and repair local world files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads and writes local world files and runs maintenance scripts for validation, writing, snapshots, reset, and import.

Mitigation: Install only when these local file operations are acceptable, and keep world data in a controlled directory such as the configured WORLDSIM_WORLDS_DIR path.

Risk: Stories and imported character cards can retain sensitive personal data or secrets on local disk until the world or import files are deleted.

Mitigation: Do not place passwords, secrets, or sensitive personal information in stories or imported character cards; delete the relevant world or import files when retention is no longer wanted.

Risk: Load, reset, scene reset, and delete operations can overwrite or remove local world progress.

Mitigation: Use explicit start/load/reset commands and review confirmation prompts before destructive operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaowh/skills/worldsim)
- [README.en.md](README.en.md)
- [Commands reference](references/commands.md)
- [Disclosures and confirmations](references/disclosures.md)
- [SillyTavern character-card import](references/import_cards.md)
- [Session recovery and world lifecycle](references/session_recovery.md)
- [Write protocol](references/write_protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown narrative and status text, local Markdown/YAML state files, and shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes and retains local world state, narratives, snapshots, and imported card material under the configured worlds directory.]

## Skill Version(s):

0.10.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
