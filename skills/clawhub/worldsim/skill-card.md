## Description:

动态世界模拟器与故事引擎 (World simulation & story engine)。管理本地持久化世界状态、导入 SillyTavern 角色卡、推进互动剧情，以及执行存档、读档、回滚与状态修复。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaowh](https://clawhub.ai/user/zhaowh)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use WorldSim to run stateful roleplay and story worlds with persistent local narrative records, scene state, snapshots, rollback, and SillyTavern character-card import.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persistently writes story state, narrative records, snapshots, and imported character-card content to local disk.

Mitigation: Do not enter secrets or sensitive personal data into worlds or imported cards, and delete the relevant worlds/{world}/ directory when records should be removed.

Risk: Reset, load, delete, and --force operations can overwrite or remove local world state.

Mitigation: Review before using --force, reset, load, or delete commands; rely on the skill's confirmation flow for destructive operations.

Risk: WORLDSIM_DIR can redirect where the skill stores and reads world data.

Mitigation: Keep WORLDSIM_DIR unset unless storage redirection is intentional.

## Reference(s):

- [ClawHub WorldSim Skill Page](https://clawhub.ai/zhaowh/skills/worldsim)
- [README.en.md](README.en.md)
- [WorldSim Command Reference](references/commands.md)
- [WorldSim Write Protocol](references/write_protocol.md)
- [WorldSim Session Recovery](references/session_recovery.md)
- [WorldSim Rollback Protocol](references/rollback.md)
- [WorldSim SillyTavern Character Card Import](references/import_cards.md)
- [WorldSim Loop Machinery](references/loop_machinery.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with command guidance and local Markdown/YAML state files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stateful local file output under worlds/; requires python3; WORLDSIM_DIR can redirect the skill root.]

## Skill Version(s):

0.5.0 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
