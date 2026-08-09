## Description:

WorldSim is a world simulation and story engine where users and an LLM co-create fantasy-world narratives through user actions, stateful scene records, and a three-role narrative framework.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaowh](https://clawhub.ai/user/zhaowh)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to create, start, continue, and reset interactive fictional worlds with persistent characters, conflicts, scenes, and world state. It is suited for immersive narrative roleplay and story simulation workflows where the agent writes prose and maintains local story files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Normal play can silently modify local story files, and reset or load commands can overwrite or remove dynamic world state.

Mitigation: Use the skill only in a dedicated workspace, keep backups or version control for worlds, and review reset, load, and snapshot actions before relying on them.

Risk: Bundled story worlds may produce adult, dark, sexual, or violent narrative content without strong default safety boundaries.

Mitigation: Set explicit narrative boundaries before use and avoid placing sensitive personal material in world data.

Risk: The security evidence marks the release as suspicious because file mutation and destructive operations are part of normal behavior.

Mitigation: Review the skill before installing and limit it to workspaces where local file changes are expected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaowh/skills/worldsim)
- [Server-resolved GitHub source](https://github.com/zhaowh/worldsim)
- [Commands reference](references/commands.md)
- [Scene management reference](references/scene_management.md)
- [Session recovery reference](references/session_recovery.md)
- [Write protocol reference](references/write_protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with local YAML, Markdown, and command-oriented world-state updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist or reset local world, scene, character, conflict, and snapshot files during normal use.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
