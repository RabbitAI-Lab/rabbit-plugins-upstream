## Description:

WorldSim helps agents create and run interactive story worlds, import character cards, and maintain local narrative and world-state records across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldsimlife](https://clawhub.ai/user/worldsimlife)

### License/Terms of Use:

MIT

## Use Case:

Storytellers and role-playing users can create a named world, play through character-driven scenes, and save, restore, or revise its ongoing story and state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Story data persists locally, and reset or maintenance actions can change or delete world files.

Mitigation: Use a dedicated worlds directory and confirm the effects of reset or maintenance commands before running them.

Risk: Story and character records may retain sensitive information supplied by users.

Mitigation: Do not include secrets or sensitive personal information in stories or character cards.

## Reference(s):

- [WorldSim on ClawHub](https://clawhub.ai/worldsimlife/skills/worldsim)
- [WorldSim user guide](artifact/README.en.md)
- [WorldSim commands](artifact/references/commands.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration]

**Output Format:** [Narrative text and locally saved Markdown and YAML story records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persists world state and scene narratives between sessions.]

## Skill Version(s):

0.30.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
