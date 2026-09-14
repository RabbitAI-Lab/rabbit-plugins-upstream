## Description:

智能识别商品主体，根据一张产品图一键生成不同类型、不同电商平台风格的主图+轮播图套图，无需写提示词。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and agent users use this skill to generate e-commerce main image and carousel image sets from a product photo and optional marketing copy. It is intended for workflows such as marketplace listing images, SKU images, and platform-specific product hero images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade mutable global npm tooling for qhkit.

Mitigation: Review the @iqinghu/qhkit package before installation, prefer a pinned reviewed version, and use a local or least-privilege install path where practical.

Risk: The skill requires a production API token for the LinkPix service.

Mitigation: Avoid placing real tokens directly in shell commands; prefer environment variables or a secure configuration mechanism with limited token exposure.

Risk: Product images, prompts, and marketing copy may be uploaded to an external service.

Mitigation: Use the skill only when the user accepts external processing of the provided product assets and text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-main-image-set)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix login](https://www.iqinghu.com/workbench/login?type=1&urlCode=1788417429126)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit image generation, estimation, setup, and delivery of generated image URLs with actual credit usage.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
