## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content maintainers use this skill to create, revise, and review generated images for Markdown, PDFs, DOCX, web pages, merge requests, and release artifacts while preserving requested formats and validating final outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated image changes may fail review if they drift from the requested format, style, resolution, or downstream embedding requirements.

Mitigation: Inspect the requested artifact and existing embeds before editing, preserve the requested format and style, rebuild downstream documents, and review generated image changes as normal project edits.

Risk: Repository image prompt files can become inconsistent with generated .svg, .png, or .webp siblings.

Mitigation: Run scripts/check-image-genai.py against the workspace root and address missing or stale generated siblings before final review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and repository file changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update sibling .svg, .png, and .webp image assets from *.image.genai prompts.]

## Skill Version(s):

1.91.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
