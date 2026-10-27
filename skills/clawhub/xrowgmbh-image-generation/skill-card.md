## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and reviewers use this skill to create or revise images for Markdown, PDFs, DOCX files, web pages, merge requests, and release artifacts while preserving requested formats and checking the delivered assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A passing freshness check does not confirm image format, visual quality, or correct embedding in downstream documents.

Mitigation: Run the checker with the intended repository root, then inspect the generated files and downstream PDF, DOCX, or web output for format, dimensions, readability, and correct embedding.

## Reference(s):

- [Image Generation on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)
- [xrowgmbh publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Image files, Guidance, Shell commands]

**Output Format:** [Requested image formats, with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves the requested format; image dimensions and print resolution depend on the target use.]

## Skill Version(s):

1.122.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
