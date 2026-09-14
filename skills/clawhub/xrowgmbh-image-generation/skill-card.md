## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, regenerate, and review generated images for documents, PDFs, web pages, merge requests, and release artifacts while preserving requested formats and validating downstream outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated image or document changes could be incorrect, misleading, or inconsistent with the requested format.

Mitigation: Review image and document changes before merging, and validate the actual downstream artifact rather than only the source file.

Risk: Workspace scans for *.image.genai files may touch repositories where that convention is not expected.

Mitigation: Use the skill on repositories where scanning for *.image.genai files is acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)
- [Publisher Profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with file changes and shell commands when validation is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update image assets and related generated files when requested.]

## Skill Version(s):

1.91.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
