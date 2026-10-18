## Description:

Helps Pinduoduo sellers and designers create product image sets, detail-page graphics, and promotional images with LinkPix.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Pinduoduo sellers, e-commerce operators, and designers use this skill to prepare product listings, image sets, detail pages, and promotional graphics from product images and copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or updating unpinned Node/npm tooling may introduce unreviewed code.

Mitigation: Review the packages and pin approved versions before installation.

Risk: A qhkit API token may be stored on the machine.

Mitigation: Prefer an environment-scoped token and avoid sharing it in chat or logs.

Risk: Product images are uploaded to qhkit for generation.

Mitigation: Confirm the images are approved for upload before submitting them.

Risk: Image-generation requests consume paid credits and cannot be canceled after submission.

Mitigation: Check the estimate and obtain explicit approval for the parameters and expected credits before submitting.

## Reference(s):

- [LinkPix Pinduoduo image skill on ClawHub](https://clawhub.ai/autoagc/skills/linkpix-pinduoduo-image)
- [qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [qhkit API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Images, Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with generated image links and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports generated image URLs and actual credit usage after user-approved submission.]

## Skill Version(s):

0.1.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
