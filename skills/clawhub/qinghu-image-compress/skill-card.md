## Description:

This skill helps agents compress local images with ImageMagick, including batch resizing, target-size reduction, and WebP conversion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need an agent to reduce image file sizes for upload limits, web loading performance, or format conversion while keeping the work local.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may install or use ImageMagick on selected local image files.

Mitigation: Confirm the user is comfortable with ImageMagick installation and local file processing before running commands.

Risk: Compressed outputs could replace originals before the user reviews quality or file-size changes.

Mitigation: Write outputs to a separate directory and review size and visual quality before replacing originals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-compress)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks and concise file-size comparison guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local image-processing commands and asks for target size, quality, format, and output directory before replacing originals.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
