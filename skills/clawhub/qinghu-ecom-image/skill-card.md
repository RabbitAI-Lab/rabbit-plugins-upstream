## Description:

Guides agents to generate e-commerce product image sets, detail-page graphics, and custom promotional images using Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers, marketers, and content creators use this skill to guide an agent in preparing product image sets, detail-page images, and promotional graphics from prompts or reference product photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running an external npm CLI adds a software dependency.

Mitigation: Use a reviewed or pinned package version in controlled environments before installation.

Risk: Product images and prompts are uploaded to the Qinghu service, and use requires an API token.

Mitigation: Confirm the upload is appropriate for the material and handle the API token as a secret.

Risk: Persistent changes to shell startup files can alter future command environments.

Mitigation: Avoid adding PATH changes to shell startup files unless persistence is intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-ecom-image)
- [Qinghu CLI package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image links]

**Output Format:** [Markdown with CLI examples and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports reference images and text prompts; image-generation results include credit usage.]

## Skill Version(s):

0.1.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
