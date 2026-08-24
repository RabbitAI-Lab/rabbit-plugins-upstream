## Description:

AI multi-image generation powered by CellCog via Nano Banana for coherent multi-image projects, character consistency, composition planning, image generation, and image editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to route image generation and editing tasks through CellCog, including multi-image visual projects, character-consistent sequences, product mockups, and style transformations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and images may be sent to CellCog as a third-party image service.

Mitigation: Use only if third-party service processing is acceptable; do not submit secrets, regulated data, proprietary images, or private likenesses without approval and review of CellCog privacy and retention terms.

Risk: The skill requires a CELLCOG_API_KEY credential for service access.

Mitigation: Store the API key in the environment or an approved secret manager and avoid embedding it in prompts, source files, logs, or shared transcripts.

## Reference(s):

- [CellCog](https://cellcog.ai)
- [ClawHub Skill Page](https://clawhub.ai/cellcog/skills/nano-banana-image-cellcog)
- [CellCog Publisher Profile](https://clawhub.ai/user/cellcog)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, text]

**Output Format:** [Markdown with Python code snippets and setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3, the cellcog dependency, and CELLCOG_API_KEY for service access.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
