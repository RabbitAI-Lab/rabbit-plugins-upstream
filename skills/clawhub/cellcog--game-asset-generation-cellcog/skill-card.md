## Description:

AI game asset generation and game development powered by CellCog. Character-consistent art, sprites, tilesets, music, UI, 3D models, GDDs, level design, game prototypes. Cohesive game assets across every modality from a single prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and game creators use this skill to request cohesive game assets, design documents, interface concepts, 3D model guidance, and prototype-oriented game development outputs through CellCog.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The examples install or rely on the CellCog dependency without a pinned version.

Mitigation: Install only after trusting the CellCog publisher, and prefer pinned or verified dependency versions where the agent environment supports them.

Risk: CELLCOG_API_KEY is a service credential required by the skill.

Mitigation: Store the key in the agent environment secret store or shell environment, avoid logging it, and rotate it if exposure is suspected.

Risk: Private project files or unreleased game assets may be sent to CellCog during asset generation workflows.

Mitigation: Review the CellCog skill or SDK documentation before submitting sensitive files, and send only content approved for third-party processing.

## Reference(s):

- [Game Asset Generation on ClawHub](https://clawhub.ai/cellcog/skills/game-asset-generation-cellcog)
- [CellCog](https://cellcog.ai)
- [CellCog Publisher Profile](https://clawhub.ai/user/cellcog)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown and text responses with Python or shell snippets; generated game assets may be returned as files or links by CellCog.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3, the cellcog dependency, and CELLCOG_API_KEY; supports darwin, linux, and windows per ClawHub metadata.]

## Skill Version(s):

1.0.18 (source: server release metadata, released 2026-08-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
