## Description:

为商品图片批量添加品牌 logo 或版权文字水印，支持控制位置、透明度和大小，以保护原创素材并提升品牌辨识度。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to apply logo or text watermarks to product images in single-image or batch workflows with local ImageMagick or ffmpeg commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch watermarking commands can modify many images or create many output files if run in the wrong directory.

Mitigation: Review generated commands before execution, run a single sample first, and write batch results to a dedicated output directory such as watermarked/.

Risk: The workflow depends on local ImageMagick or ffmpeg binaries supplied by the user's environment.

Mitigation: Install dependencies only from a trusted package manager and verify the selected command before processing user images.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-watermark-add)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks and concise file-delivery guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local watermarking command recipes and output-directory guidance; does not generate images itself.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
