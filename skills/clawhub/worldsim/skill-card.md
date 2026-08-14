## Description:

WorldSim is an agent skill for creating persistent local story worlds, importing SillyTavern character cards, advancing interactive narratives, and managing save, load, rollback, and state repair workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaowh](https://clawhub.ai/user/zhaowh)

### License/Terms of Use:

MIT

## Use Case:

External users, roleplay players, and narrative creators use WorldSim to run persistent local story worlds with stateful characters, conflict progression, scene history, snapshots, and character-card imports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persistently stores story worlds, narrative history, snapshots, mutable state, and imported character-card source material on local disk.

Mitigation: Use it only for content you are comfortable storing locally, avoid entering secrets or sensitive personal information, and delete the relevant worlds/ directory when records should be removed.

Risk: Reset, load, delete, and rollback workflows can overwrite or remove world state.

Mitigation: Review the requested action and scope before destructive commands, rely on snapshots where available, and use force options only for intentional automation.

Risk: Some worlds or character templates can include mature, sexualized, violent, or coercive themes.

Mitigation: Review world settings, imported cards, and character templates before use, and only continue into worlds whose content gates match the user's intent.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaowh/skills/worldsim)
- [Commands Reference](references/commands.md)
- [SillyTavern Character Card Import](references/import_cards.md)
- [Rollback Protocol](references/rollback.md)
- [Session Recovery and World Lifecycle](references/session_recovery.md)
- [Scene Management](references/scene_management.md)
- [Write Protocol](references/write_protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown narrative and guidance with shell commands plus local Markdown and YAML world-state files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces and mutates local world files under worlds/, including narrative history, state, snapshots, imported card material, and scene metadata.]

## Skill Version(s):

0.6.0 (source: server release metadata; artifact frontmatter states 0.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
