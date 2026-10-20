## Description:

Guides Ozon sellers in creating product image sets, detail images, and promotional graphics using Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ozon sellers and cross-border commerce teams use this skill to plan and generate product image sets, Russian-language selling-point images, detail images, and campaign graphics.

### Deployment Geography for Use:

Global (focused on Ozon and the Russian market)

## Known Risks and Mitigations:

Risk: Installing or updating the third-party CLI may change the local toolchain or introduce supply-chain exposure.

Mitigation: Review the installation and PATH changes, and prefer a reviewed or pinned qhkit version.

Risk: Product images and an API key are used with Qinghu AI.

Mitigation: Upload only images approved for that service and protect the API key.

Risk: Image generation consumes credits and submitted tasks cannot be canceled.

Mitigation: Check the credit estimate and generation parameters, then obtain explicit approval before submission.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-ozon-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API key setup](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image links]

**Output Format:** [Markdown with command examples and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are delivered through a third-party service; generation may consume credits.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
