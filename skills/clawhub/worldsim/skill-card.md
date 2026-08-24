## Description:

WorldSim is an agent skill for creating and running persistent local story worlds with interactive narrative, roleplay, SillyTavern character-card import, saves, loads, rollback, and state repair.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaowh](https://clawhub.ai/user/zhaowh)

### License/Terms of Use:

MIT

## Use Case:

Players, writers, roleplay creators, and developers use WorldSim to create or enter interactive worlds, continue story sessions, import character cards, and maintain local narrative state across turns. It is intended for agent clients that can run Python scripts and manage local skill files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: WorldSim writes, restores, and may delete local story-world state under a worlds directory.

Mitigation: Install only when persistent local story worlds are expected, keep WORLDSIM_WORLDS_DIR pointed at a dedicated folder, and review destructive operations before confirming them.

Risk: Stories and imported character cards may contain sensitive personal data or prompt-injection content supplied by users or third-party files.

Mitigation: Avoid putting secrets or sensitive personal information into stories or character cards, and complete the built-in import review before generating a character file.

Risk: The --force option can bypass interactive confirmation for destructive maintenance commands.

Mitigation: Use --force only in controlled maintenance or test contexts after confirming the target world and operation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaowh/skills/worldsim)
- [README.en.md](README.en.md)
- [LICENSE](LICENSE)
- [Command Reference](references/commands.md)
- [Write Protocol](references/write_protocol.md)
- [Disclosures](references/disclosures.md)
- [Evaluation README](evals/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown narrative text plus local Markdown and YAML world-state files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains persistent local world data under worlds/ or WORLDSIM_WORLDS_DIR; requires python3 and PyYAML.]

## Skill Version(s):

0.20.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
