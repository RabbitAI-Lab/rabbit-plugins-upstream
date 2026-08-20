## Description:

LinkPix helps clothing sellers generate e-commerce model try-on images from clothing photos and optional model references through the qhkit CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers and agents use this skill to turn flat-lay, hanger, or product clothing photos into commercial model try-on images. It supports selecting model attributes, body type, country or skin tone, pose, scene, image size, and output count.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or upgrade qhkit and Node automatically.

Mitigation: Require explicit user approval before installing or upgrading tools, and prefer least-privilege install paths when global install permissions are unavailable.

Risk: The skill can reuse or configure a Qinghu/LinkPix token.

Mitigation: Require explicit approval before using stored credentials or setting a token, and avoid exposing token values in logs or responses.

Risk: The skill uploads selected local clothing or model images to the service.

Mitigation: Confirm the exact files with the user before each upload and warn that generated try-on results may differ from product details such as logos, text, or garment structure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-model-outfit-swap)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands, JSON command arguments, generated image URLs, and credit usage notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May install or upgrade qhkit/Node, configure a Qinghu/LinkPix token, upload selected local clothing or model images, and return generated image URLs.]

## Skill Version(s):

0.1.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
