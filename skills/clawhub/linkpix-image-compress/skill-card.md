## Description:

Compresses images locally while preserving practical visual quality, with support for batch processing, size targets, resizing, and JPG, PNG, or WebP conversion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to reduce image file sizes for upload limits, web performance, and format conversion workflows. It guides local ImageMagick or ffmpeg-based compression and asks for target size, quality, dimensions, and output directory before batch work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask the agent to install ImageMagick when it is not already available.

Mitigation: Review installation commands and use trusted package managers or preinstalled local tooling before running compression workflows.

Risk: Batch compression can overwrite or misplace image outputs if paths are not reviewed.

Mitigation: Use a separate output directory such as compressed/ and review input and output paths before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-compress)
- [npm package homepage](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compression settings, output directory guidance, and before-and-after file size comparisons.]

## Skill Version(s):

0.1.1 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
