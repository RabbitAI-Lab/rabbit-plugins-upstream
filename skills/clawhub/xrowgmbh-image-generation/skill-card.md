## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, revise, or review images for documents, websites, and release artifacts. It guides them to preserve the requested format and validate the final rendered output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The image checker verifies that generated files exist and are newer than their prompts, but it does not assess image quality.

Mitigation: Review the rendered image for visual quality and check downstream documents or pages where it will be used.

Risk: Separately selected image-generation services and build tools are outside this skill package's security review.

Mitigation: Review the selected service and build tooling before using them with project content.

## Reference(s):

- [ClawHub Image Generation release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance and image artifacts in the requested format]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves the requested image format and includes artifact validation guidance.]

## Skill Version(s):

1.127.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
