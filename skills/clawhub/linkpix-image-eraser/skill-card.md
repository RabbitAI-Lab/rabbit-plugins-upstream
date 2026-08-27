## Description:

智能擦除商品图片中的人物、水印、文字及杂物，并自动补全背景，完成商品修图与素材优化。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to remove specified elements such as people, watermarks, text, and clutter from product images while filling the edited area with generated background content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images are sent to qhkit/LinkPix for editing.

Mitigation: Use the skill only with images that may be processed by qhkit/LinkPix.

Risk: Watermark or text removal can be misused on images the user is not authorized to edit.

Mitigation: Proceed only for images the user owns or is authorized to modify.

Risk: Paid generation consumes credits after task submission.

Mitigation: Review the confirmed parameters and credit estimate before approving generation.

Risk: Generative inpainting may slightly change product details, text, logos, or structure.

Mitigation: Inspect completed images and verify important product details before using the output.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-image-eraser)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit image option, estimate, configuration, and generation commands; generation returns image URLs from the qhkit service.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
