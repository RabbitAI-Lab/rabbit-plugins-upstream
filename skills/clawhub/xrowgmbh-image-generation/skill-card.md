## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content maintainers use this skill to create, revise, and review generated images for documents, web pages, merge requests, and release artifacts while preserving requested formats and validating output quality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated image assets or downstream documents may be stale, in the wrong format, or visually unsuitable for the requested consumer.

Mitigation: Inspect the final image files and rebuilt Markdown, PDF, DOCX, web, or release artifacts; run the included generated-image checker when using *.image.genai prompt files.

Risk: Image-generation work may update binary media and related documents that are hard to review from source diffs alone.

Mitigation: Review generated binaries and rebuilt artifacts before merging, consistent with the release security guidance.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, Code, Files]

**Output Format:** [Markdown guidance with inline shell commands and generated image assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes validation expectations for image formats, dimensions, generated siblings, and downstream document artifacts.]

## Skill Version(s):

1.84.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
