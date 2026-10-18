## Description:

Helps sellers enhance existing product images with LinkPix, improving composition, lighting, texture, and presentation through generative image editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and marketing teams use this skill to improve existing product listing images or generate a refreshed set of product visuals with LinkPix.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images are uploaded to the LinkPix/qhkit service.

Mitigation: Confirm which images may be shared with the service before uploading them.

Risk: Using the workflow requires an API token and may install or upgrade local npm packages or Node.

Mitigation: Obtain consent before software installation or upgrades, and handle the API token as a secret.

Risk: Generating images spends credits and may alter product text, logos, or structural details.

Mitigation: Check the credit estimate and obtain approval before generation; review the resulting image against the original product.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-main-image-optimize)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands and generated image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports generated image links and actual credits charged when available.]

## Skill Version(s):

0.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
