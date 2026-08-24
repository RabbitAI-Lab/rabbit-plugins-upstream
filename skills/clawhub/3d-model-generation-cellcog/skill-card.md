## Description:

AI 3D model generation powered by CellCog for text-to-3D, image-to-3D, and batch creation of production-ready GLB files for games, AR/VR, e-commerce, and 3D printing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, artists, and product teams use this skill to ask an agent to generate single or batch 3D assets from text descriptions, sketches, product photos, concept art, or item lists. The skill is intended for workflows that need GLB models for games, AR/VR, product visualization, education, or 3D printing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced images or files may be processed by CellCog's external service.

Mitigation: Avoid submitting confidential or regulated assets unless the use is approved for external processing.

Risk: The skill requires a CELLCOG_API_KEY for service access.

Mitigation: Store the API key in an environment variable or secret manager and avoid embedding it in prompts, files, or source code.

Risk: Installation depends on the CellCog package or skill source.

Mitigation: Verify the package or skill source during installation before using it in production workflows.

## Reference(s):

- [CellCog](https://cellcog.ai)
- [ClawHub Skill Page](https://clawhub.ai/cellcog/skills/3d-model-generation-cellcog)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Python examples and setup commands; generated agent work typically produces GLB model files through CellCog.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and CELLCOG_API_KEY; supports GLB output requests for single assets and batches.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
