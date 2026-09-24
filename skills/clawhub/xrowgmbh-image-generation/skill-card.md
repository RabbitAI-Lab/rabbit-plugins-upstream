## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content maintainers use this skill to create, revise, validate, and review generated image assets for documentation, PDFs, DOCX files, web pages, merge requests, and release artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated or revised image assets may be stale, unreadable, or mismatched with the requested output format.

Mitigation: Inspect the final embedded artifact and run scripts/check-image-genai.py to confirm expected generated siblings are present and current.

Risk: The workflow may read and update image-related files in the active workspace.

Mitigation: Review generated file diffs before publishing, merging, or releasing the artifacts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with file edits, generated image files, and shell validation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update .image.genai prompt files and sibling .svg, .png, and .webp assets.]

## Skill Version(s):

1.94.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
