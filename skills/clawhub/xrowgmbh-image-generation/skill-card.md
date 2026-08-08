## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, regenerate, and review image artifacts for documents, web pages, merge requests, and release materials while preserving requested formats and validating generated outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or regenerate image siblings and rebuild downstream documents when image-related work is requested.

Mitigation: Run it only against the intended workspace and review changed artifacts before release.

Risk: Generated image deliverables can drift from the requested format, resolution, or embedded-document requirements.

Mitigation: Validate the final output format, dimensions, DPI where applicable, and generated sibling freshness before marking image work complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)
- [Publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with file edits, generated image artifacts, validation notes, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or refresh .svg, .png, and .webp siblings for *.image.genai prompts and report validation results.]

## Skill Version(s):

1.80.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
