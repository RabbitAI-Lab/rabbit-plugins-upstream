## Description:

LinkPix helps agents provide local ImageMagick or ffmpeg commands for adding logo or text watermarks to product images with controllable placement, opacity, and scale.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and content teams use this skill when they need an agent to provide repeatable local commands for watermarking one image or batches of product images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch watermarking commands can process every matching image in the current directory.

Mitigation: Confirm the working directory and run one sample image before processing a full batch.

Risk: Installing ImageMagick or ffmpeg can change the local system environment.

Mitigation: Use an approved package manager or preinstalled toolchain and verify installation before running watermark commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-watermark-add)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are intended for local image watermarking workflows and may include output directory and file-list guidance.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
