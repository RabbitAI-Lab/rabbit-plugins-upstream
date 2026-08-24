## Description:

自动将印花图案精准贴合到服装、帽子、杯子等商品上，随布料褶皱与透视自然变形，快速生成真实展示效果图（mockup）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and POD sellers use this skill to generate product mockup images by applying a supplied pattern to apparel, hats, mugs, or similar merchandise. The skill helps agents prepare qhkit image-generation commands, check model and size options, confirm credit use before submission, and deliver generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads selected image files to the Qinghu/LinkPix service.

Mitigation: Use it only with images approved for that service and review which local paths or URLs will be submitted before generation.

Risk: The skill stores or reuses a Qinghu API token for qhkit access.

Mitigation: Use an approved token storage method, avoid exposing the token in conversation, and rotate credentials if they are shared accidentally.

Risk: Image generation consumes credits and submitted jobs cannot be canceled.

Mitigation: Run an estimate where supported and confirm model, image count, size, reference images, and expected credits before executing generate commands.

Risk: Generated mockups may alter fine pattern details or color fidelity.

Mitigation: Review final images for key pattern elements, placement, distortion, and color accuracy before using them in commerce.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-apply)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu LinkPix service](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs returned by qhkit after user confirmation and credit-consuming generation.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
