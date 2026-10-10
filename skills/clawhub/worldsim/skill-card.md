## Description:

WorldSim helps users create and run interactive story worlds with persistent local characters, narrative history, and save states.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldsimlife](https://clawhub.ai/user/worldsimlife)

### License/Terms of Use:

MIT

## Use Case:

People using an agent-compatible client can create a story world, import character cards, play through interactive scenes, and revisit or restore locally saved stories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deleting world records may bypass the confirmation promised in the skill documentation.

Mitigation: Back up important worlds and review delete commands or batches containing ###DELETE: before use.

Risk: World state and narrative text are written to local files, which may retain sensitive story content.

Mitigation: Use a dedicated WORLDSIM_WORLDS_DIR and avoid entering secrets or sensitive personal data.

## Reference(s):

- [WorldSim ClawHub release](https://clawhub.ai/worldsimlife/skills/worldsim)
- [WorldSim story example](https://worldsim.life/welcome_center.htm)
- [WorldSim command reference](references/commands.md)
- [WorldSim writing and storage protocol](references/write_protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration]

**Output Format:** [Narrative text and local Markdown/YAML world records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [World records are stored locally and can be modified or deleted.]

## Skill Version(s):

0.31.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
