## Description:

智能压缩图片体积，在保证画质的同时减少文件大小，支持批量处理与格式转换（JPG/PNG/WebP），提高网页加载及上传效率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to compress, resize, batch-process, and convert images for upload limits, web delivery, and smaller file sizes while keeping output quality and format choices explicit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Compression, resizing, or format conversion can alter image quality or produce files that differ from the original images.

Mitigation: Run commands on copies or a dedicated output directory, keep originals when quality matters, and report before/after file sizes and formats.

Risk: The skill may suggest installing and executing local image-conversion tools such as ImageMagick.

Mitigation: Confirm the toolchain source and review generated shell commands before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-compress)
- [Package homepage](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include target quality, maximum dimensions, output directory, converted format, and before/after file-size comparison.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
