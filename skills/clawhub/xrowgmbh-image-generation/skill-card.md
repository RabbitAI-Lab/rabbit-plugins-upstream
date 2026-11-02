## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and reviewers use this skill to create or review images for documents, web pages, and release artifacts while preserving the requested format and checking generated files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled checker only verifies generated image sibling files and timestamps, so it may not catch image quality issues or problems in rebuilt documents.

Mitigation: Review generated images and inspect rebuilt documents after running the checker.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [Files, Guidance, Code, Shell commands]

**Output Format:** [Image files in the requested format, plus Markdown guidance and Python checker code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves the requested image format and source resolution; generated image siblings may include SVG, PNG, and WebP.]

## Skill Version(s):

1.124.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
