## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and reviewers use this skill to create, regenerate, and review image assets for documents, PDFs, web pages, merge requests, and release artifacts while preserving the requested format and checking downstream outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled checker verifies image sibling presence and timestamps, but does not assess visual quality.

Mitigation: Review regenerated images and downstream documents directly, and check that the result matches the requested format and readability requirements.

## Reference(s):

- [Image Generation release on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Requested image formats (such as PNG, SVG, or WebP), with Markdown review notes and validation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves requested format and source resolution; dimensions and metadata depend on the target artifact.]

## Skill Version(s):

1.130.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
