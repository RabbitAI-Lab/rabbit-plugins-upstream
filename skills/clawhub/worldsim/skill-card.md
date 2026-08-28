## Description:

WorldSim is an agent skill that runs persistent local story worlds, imports SillyTavern character cards, advances interactive roleplay, and supports save, load, rollback, reset, and state repair workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaowh](https://clawhub.ai/user/zhaowh)

### License/Terms of Use:

MIT

## Use Case:

External users, roleplay players, and narrative creators use this skill to create and run persistent simulated worlds, generate character and scene files, import compatible character cards, and continue stories across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores story state locally and can modify or delete world records.

Mitigation: Use a dedicated WORLDSIM_WORLDS_DIR, keep backups for important worlds, and review reset, load, delete, and path-bearing commands before execution.

Risk: Some helper scripts may read or write outside the declared world folder when crafted paths are supplied.

Mitigation: Import only files you selected, avoid untrusted file paths, and run the skill with filesystem access limited to the intended worlds directory.

Risk: Stories and imported character cards can contain sensitive personal data, secrets, prompt injection, or copyrighted material.

Mitigation: Do not place secrets or sensitive personal information in story content, and perform the documented import-card risk review before generating character files.

## Reference(s):

- [ClawHub WorldSim skill page](https://clawhub.ai/zhaowh/skills/worldsim)
- [GitHub releases](https://github.com/zhaowh/worldsim/releases)
- [WorldSim example story](https://worldsim.life/welcome_center.htm)
- [Command reference](references/commands.md)
- [Import card reference](references/import_cards.md)
- [Disclosures and destructive-operation confirmations](references/disclosures.md)
- [Evaluation README](evals/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown narrative text, YAML-backed world state, and local Python command invocations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persists world records under worlds/ by default or under WORLDSIM_WORLDS_DIR when configured.]

## Skill Version(s):

0.21.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
