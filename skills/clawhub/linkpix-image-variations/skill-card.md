## Description:

Generates multiple e-commerce product-image marketing variations from a reference image, using different backgrounds, layouts, and styles for ad creative production.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce marketers, designers, and agent users use this skill to turn a product photo into multiple campaign-ready image variants for A/B testing, platform-specific product sets, and advertising material production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install local tooling or Node.js dependencies.

Mitigation: Prefer preinstalling qhkit from the official npm package and review installation commands before execution.

Risk: The workflow may require API-key configuration.

Mitigation: Provision the token through a secure secret mechanism such as QHKIT_TOKEN rather than sending credentials in chat.

Risk: Image generation uses an external LinkPix/qhkit service and may upload user images or spend credits.

Mitigation: Confirm the input images, model or template, output count, quality, and estimated credits before running generation commands.

Risk: Generated image variants can alter product details, text, logos, or structure.

Mitigation: Review generated outputs for product accuracy and brand-sensitive details before publishing or using them in ads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-image-variations)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for image generation workflows; generated media URLs are returned by the external qhkit service after user confirmation.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
