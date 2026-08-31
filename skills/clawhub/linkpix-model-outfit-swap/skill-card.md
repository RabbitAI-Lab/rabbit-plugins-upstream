## Description:

Helps apparel sellers generate realistic model try-on images from clothing photos, with support for different model descriptions, body types, and country or market styling through LinkPix/qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and agent users use this skill to prepare LinkPix/qhkit commands for virtual apparel try-on images, estimate credits, confirm generation parameters, and return generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may handle a raw LinkPix/qhkit API key in chat or persistent CLI configuration.

Mitigation: Use a secure local secret mechanism such as QHKIT_TOKEN when possible, and avoid pasting API keys into chat.

Risk: Clothing and model reference images are uploaded to the LinkPix/qhkit service for generation.

Mitigation: Install and use the skill only when the user is comfortable sending those images to the service.

Risk: Generation jobs can consume credits and cannot be cancelled after submission.

Mitigation: Run an estimate when supported, show the model, image count, size, references, and expected credits, then wait for explicit user approval before generating.

Risk: Generated try-on images are generative redraws and may alter important product details such as text, logos, or structure.

Mitigation: Review generated images before use and check critical garment details against the source product.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-model-outfit-swap)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys page](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [LinkPix API key tutorial](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs and credit usage reported by qhkit after user-approved generation.]

## Skill Version(s):

0.1.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
