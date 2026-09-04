## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation maintainers use this skill to create, revise, and validate generated images for Markdown, PDFs, DOCX files, web pages, merge requests, and release artifacts while preserving requested format and resolution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide an agent to edit generated image prompts, sibling image files, and downstream documents that embed those images.

Mitigation: Review changed prompts, image outputs, and rebuilt documents before release, confirming the requested format, dimensions, and embedding behavior.

Risk: The included checker recursively scans repositories for *.image.genai prompts and generated sibling freshness.

Mitigation: Run the checker only against repositories where recursive artifact checks are appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and file edit recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to generate or update .svg, .png, and .webp image siblings from *.image.genai prompt files and validate them with the included local checker.]

## Skill Version(s):

1.84.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
