## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and reviewers use this skill to create, revise, or inspect image artifacts for documents, web pages, merge requests, and releases while preserving the requested format and checking the final output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security scan coverage is incomplete because some referenced paths were not matched to bundled files.

Mitigation: Review the bundled skill files and referenced paths before installation; treat the scanner result as partial evidence.

Risk: An image may miss the requested format, resolution, or readability requirements and fail in its final document or web context.

Mitigation: Inspect the actual output format, dimensions, print metadata when required, and readability in the final consumer.

## Reference(s):

- [Image Generation skill on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [Image files, Text, Shell commands, Guidance]

**Output Format:** [Requested image format(s), such as PNG, SVG, or WebP, with Markdown review notes when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves the requested format and resolution; validation notes may cover dimensions, metadata, embedding, and visual quality.]

## Skill Version(s):

1.152.2 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
