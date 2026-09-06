## Description:

WorldSim is an agent skill that runs a local persistent story-world simulator for interactive roleplay, character-card import, narrative progression, saves, loads, rollback, and state repair.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaowh](https://clawhub.ai/user/zhaowh)

### License/Terms of Use:

MIT

## Use Case:

External users and creators use WorldSim to create or enter persistent story worlds, import compatible character cards, advance interactive scenes, and maintain local narrative and state files through agent-guided workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persistently writes, updates, and can delete local story-world files.

Mitigation: Use a dedicated WORLDSIM_WORLDS_DIR and do not point it at a home directory, project root, drive root, or system directory.

Risk: Stories, world state, and imported character cards may contain secrets or sensitive personal information.

Mitigation: Do not enter passwords, secrets, health information, or sensitive personal data into stories or imported cards.

Risk: Maintenance scripts can alter or repair world data when run against a target directory.

Mitigation: Run maintenance scripts only against intended WorldSim world directories and avoid arbitrary paths.

Risk: Optional scene image generation may send story content to an image tool.

Mitigation: Enable scene images only when the user accepts the image tool's data handling for that content.

Risk: Some worlds or examples may include mature, violent, coercive, or otherwise sensitive themes.

Mitigation: Require explicit user intent and content disclosure before loading or creating worlds with sensitive themes.

## Reference(s):

- [WorldSim ClawHub page](https://clawhub.ai/zhaowh/skills/worldsim)
- [README.en.md](artifact/README.en.md)
- [Commands reference](artifact/references/commands.md)
- [User disclosures](artifact/references/disclosures.md)
- [Character card import reference](artifact/references/import_cards.md)
- [Evaluation README](artifact/evals/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown prose with YAML/Markdown state files and occasional shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local world state, scene, snapshot, and narrative files under worlds/ or WORLDSIM_WORLDS_DIR.]

## Skill Version(s):

0.26.3 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
