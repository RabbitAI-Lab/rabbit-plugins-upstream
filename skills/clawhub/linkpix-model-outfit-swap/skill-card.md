## Description:

Generates e-commerce model try-on images from garment and optional model reference images using LinkPix through the qhkit CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers, content operators, and agents use this skill to create model-worn apparel product images from flat-lay, hanging, garment, or model reference images. It supports localized model descriptions such as age, body type, pose, country style, and studio context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update the qhkit CLI on the machine.

Mitigation: Review the npm package and installation path before use, and run installation in a managed environment when possible.

Risk: Local product and model reference images may be uploaded to the LinkPix/Qinghu service.

Mitigation: Use only images approved for third-party processing and avoid confidential or restricted assets.

Risk: API keys could be exposed if pasted into chat.

Mitigation: Configure credentials locally or through managed secrets, and avoid sharing raw tokens in conversation.

Risk: Generation can consume account credits after confirmation.

Mitigation: Run an estimate when supported and confirm model, image count, dimensions, references, and expected credits before submitting generation tasks.

Risk: Generated try-on images may slightly alter garment details such as text, logos, or structure.

Mitigation: Review generated outputs against the source product before using them in listings or customer-facing material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-model-outfit-swap)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key tutorial](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Files]

**Output Format:** [Markdown with inline bash and JSON examples, plus generated image URLs when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses qhkit image generation flows, may upload local image files to the LinkPix/Qinghu service, and may consume account credits after user confirmation.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
