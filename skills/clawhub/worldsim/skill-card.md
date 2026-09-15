## Description:

WorldSim is an agent skill for running persistent interactive story worlds, importing SillyTavern character cards, advancing roleplay narratives, and supporting save, load, rollback, reset, and state repair workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldsimlife](https://clawhub.ai/user/worldsimlife)

### License/Terms of Use:

MIT

## Use Case:

External users, creators, and roleplay developers use this skill to create and continue persistent fictional worlds with autonomous characters, structured dramatic conflict, scene state, and archived narrative output. It is also useful for importing compatible character cards into a local world while preserving user review points for sensitive or untrusted material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A deletion path may persistently remove world records without the confirmation and recovery controls described in the documentation.

Mitigation: Keep backups before delete, reset, or load workflows, and review destructive operations before installing or using the skill.

Risk: World data is persisted locally and story content may include sensitive or personal information entered by the user.

Mitigation: Do not enter passwords, secrets, sensitive personal information, or real health information into stories.

Risk: Misconfigured WORLDSIM_WORLDS_DIR can put generated world data in an unsafe or overly broad filesystem location.

Mitigation: Point WORLDSIM_WORLDS_DIR only at a dedicated worlds directory, not a home directory, project root, drive root, or system directory.

Risk: Imported character cards are untrusted input and may contain prompt injection, sensitive content, copyright issues, or excessive size.

Mitigation: Review imported card content and proceed only after explicit user confirmation when risks are disclosed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldsimlife/skills/worldsim)
- [README.en.md](README.en.md)
- [commands.md](references/commands.md)
- [disclosures.md](references/disclosures.md)
- [import_cards.md](references/import_cards.md)
- [write_protocol.md](references/write_protocol.md)
- [WorldSim demo story](https://worldsim.life/welcome_center.htm)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with local file-backed world state, YAML state updates, and shell command invocations when maintenance scripts are needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persists narrative archives, snapshots, and state under worlds/ or the directory configured by WORLDSIM_WORLDS_DIR.]

## Skill Version(s):

0.29.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
