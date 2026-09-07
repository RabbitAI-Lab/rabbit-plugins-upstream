## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation maintainers use this skill to create, regenerate, review, and validate images for Markdown, PDF, DOCX, web pages, merge requests, and release artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or refresh generated image siblings such as SVG, PNG, and WebP files when working with *.image.genai prompts.

Mitigation: Review changed artifacts, confirm the requested format and dimensions, and run the generated-image checker before accepting the output.

Risk: Image artifacts may fail review if generated files drift from the requested format, resolution, style, or downstream document embedding.

Mitigation: Inspect existing artifacts first, regenerate downstream documents that embed the image, and validate the final output rather than only the source file.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated or revised image artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or refresh SVG, PNG, and WebP siblings for *.image.genai prompt files and can report validation status for generated image siblings.]

## Skill Version(s):

1.86.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
