## Description:

Uses LinkPix/qhkit image generation to keep a product subject while replacing its background with specified ecommerce scene imagery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce operators use this skill through an agent to replace product image backgrounds, prepare marketing scene variants, estimate provider credits, and deliver generated image results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images may be uploaded to LinkPix/qhkit and generation can spend provider credits.

Mitigation: Confirm the model, image count, size, reference images, and estimated credits with the user before submitting generation.

Risk: API key setup can expose credentials if tokens are sent in chat or stored casually.

Mitigation: Prefer a secure secret store or the QHKIT_TOKEN environment variable, and avoid sharing raw API keys in conversation.

Risk: Generated background replacement may slightly change product details such as text, logos, or structure.

Mitigation: Have the user review generated images for product fidelity before publication or commercial use.

Risk: Installation may prompt for global npm, Node, Pillow, or sharp changes.

Mitigation: Use a managed qhkit installation where possible and review dependency installation prompts before approving them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-background-swap)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys console](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes qhkit command parameters, confirmation prompts, credit estimates, and generated image URLs.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
