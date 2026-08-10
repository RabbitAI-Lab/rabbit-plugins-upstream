## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content maintainers use this skill to create, regenerate, or review images, diagrams, screenshots, and generated graphics for Markdown, PDF, DOCX, web pages, merge requests, and release artifacts while preserving requested formats and validating final outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated image assets can drift from their .image.genai prompt or omit expected sibling formats.

Mitigation: Run the bundled checker against the target workspace and regenerate missing or stale .svg, .png, and .webp siblings before review.

Risk: Image revisions can satisfy metadata checks while still using the wrong requested format, resolution, or embedded output.

Mitigation: Inspect the final artifact and downstream document or web embedding, including format, dimensions, DPI metadata, and readability.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with inline shell commands and repository file conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to create or validate .svg, .png, and .webp image siblings from .image.genai prompt files.]

## Skill Version(s):

1.81.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
