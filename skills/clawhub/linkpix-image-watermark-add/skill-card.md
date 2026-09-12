## Description:

为商品图片批量添加品牌 logo 或版权文字水印，并支持位置、透明度和大小调整。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and content operators use this skill to prepare product images with visible brand, logo, or copyright watermarks before publication or batch distribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch image processing can apply an incorrect watermark or route many outputs incorrectly if folders, watermark assets, or parameters are wrong.

Mitigation: Confirm the input folder, output folder, watermark asset or text, position, opacity, and size, then generate and review one sample before approving a batch run.

Risk: The skill may ask the agent to install ImageMagick and run local image-processing commands.

Mitigation: Install tooling from trusted package sources and approve only commands that operate on the intended local image files and output directory.

## Reference(s):

- [ClawHub Skill Release](https://clawhub.ai/autoagc/skills/linkpix-image-watermark-add)
- [qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Markdown with bash code blocks and concise output notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce watermarked image files in a local output directory when executed by the agent.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
