## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and reviewers use this skill to create, regenerate, or review images for Markdown, PDF, DOCX, web pages, and release artifacts. It helps preserve requested formats and validate generated assets in their final context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled checker verifies expected image files and freshness, but does not assess image quality or format.

Mitigation: Review the generated files themselves for format, dimensions, readability, and any required DPI in the final consumer.

Risk: Image-generation services or build tools selected separately are outside this package's security review.

Mitigation: Review those services and tools separately before using them with project content.

## Reference(s):

- [ClawHub Image Generation release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Image files in the requested format (including PNG, SVG, and WebP when applicable), with Markdown guidance or shell commands as needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserve requested image format and source resolution; validate generated assets in their intended consumer.]

## Skill Version(s):

1.129.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
