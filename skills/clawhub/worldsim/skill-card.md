## Description:

WorldSim is an agent skill for running persistent local world simulations and roleplay narratives, including world creation, character-card import, story progression, save/load, rollback, and state repair.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaowh](https://clawhub.ai/user/zhaowh)

### License/Terms of Use:

MIT

## Use Case:

Players and creators use WorldSim to create or enter persistent fictional worlds, import compatible character cards, continue interactive stories, and maintain local narrative state across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes, resets, and can delete local world, story, state, snapshot, and archive files.

Mitigation: Use a dedicated WorldSim data directory with WORLDSIM_WORLDS_DIR, review destructive operations before confirming them, and avoid --force except for intentional automation.

Risk: The included demo and generated stories may involve adult, coercive, violent, harassment, or health-history content.

Mitigation: Start sensitive worlds only after explicit consent, review content warnings, and do not enter medical, mental-health, identifying, password, or secret information.

Risk: The skill may invoke image generation when an agent has an image tool available.

Mitigation: Review image-generation requests before allowing them, and disable or avoid image tools when generated media is not desired.

## Reference(s):

- [ClawHub WorldSim skill page](https://clawhub.ai/zhaowh/skills/worldsim)
- [WorldSim demo story](https://worldsim.life/welcome_center.htm)
- [WorldSim README](README.en.md)
- [Command reference](references/commands.md)
- [Disclosure and confirmation rules](references/disclosures.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown narrative with YAML state updates and inline shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local world, scene, state, snapshot, archive, and temporary import files when running a world.]

## Skill Version(s):

0.22.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
