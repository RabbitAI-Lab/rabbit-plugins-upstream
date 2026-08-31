## Description:

WorldSim is an agent skill for running persistent local story worlds: it creates and updates world state, imports SillyTavern character cards, advances interactive narrative, and supports save, load, rollback, and state repair.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaowh](https://clawhub.ai/user/zhaowh)

### License/Terms of Use:

MIT

## Use Case:

External users and creators use WorldSim to create, enter, and continue persistent roleplay worlds where character state, scene history, conflicts, and narrative archives are maintained across turns. Developers and advanced users can also import compatible character cards and manage local world data with the included maintenance scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: World data and narrative archives are stored on local disk and may include user-provided story content.

Mitigation: Use a dedicated worlds directory and avoid entering passwords, secrets, or sensitive personal information into worlds or character cards.

Risk: Save, load, reset, delete, and rollback workflows can overwrite or delete world state files.

Mitigation: Read confirmation prompts carefully and keep snapshots before destructive operations.

Risk: Imported SillyTavern or compatible character cards can contain prompt-injection, sensitive, or copyrighted content.

Mitigation: Review imported card content and proceed only after the skill's import disclosure and confirmation flow.

Risk: Misconfigured WORLDSIM_WORLDS_DIR could direct writes toward an unintended local path.

Mitigation: Point WORLDSIM_WORLDS_DIR only at a dedicated worlds directory, not a home directory, project root, drive root, or system directory.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaowh/skills/worldsim)
- [WorldSim README](README.en.md)
- [Commands Reference](references/commands.md)
- [Disclosures and Confirmations](references/disclosures.md)
- [SillyTavern Card Import](references/import_cards.md)
- [Evaluation README](evals/README.md)
- [Evaluation Cases](evals/evals.json)
- [WorldSim Releases](https://github.com/worldsimlife/worldsim/releases)
- [Example WorldSim Story](https://worldsim.life/welcome_center.htm)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown narrative and status guidance with shell commands and local file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and updates local world, scene, state, snapshot, and narrative files under worlds/ or WORLDSIM_WORLDS_DIR.]

## Skill Version(s):

0.23.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
