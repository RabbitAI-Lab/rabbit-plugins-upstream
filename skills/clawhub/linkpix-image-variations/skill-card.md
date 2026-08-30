## Description:

基于一张商品图快速生成多种营销版本，支持不同背景、布局和设计风格，用于量产广告素材。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce or marketing teams use this skill to turn a product image into multiple LinkPix/qhkit-generated variants for ad creative, background and layout exploration, and A/B testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images are uploaded to the qhkit/LinkPix service during generation.

Mitigation: Use only images appropriate for that service and review generated outputs for brand, text, logo, and product-detail accuracy before publication.

Risk: The skill can prompt for qhkit credentials and install or upgrade command-line dependencies.

Mitigation: Configure API tokens through local secret storage or QHKIT_TOKEN instead of chat, and review dependency installation or upgrade commands before running them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-variations)
- [ClawHub publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce LinkPix image-generation task parameters, estimates, and generated image URLs through qhkit.]

## Skill Version(s):

0.1.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
