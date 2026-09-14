## Description:

Helps Shopee sellers and Southeast Asia ecommerce operators generate product images, main-image carousel sets, detail-page images, and campaign graphics through LinkPix/qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, operators, and agent users use this skill to prepare Shopee-specific product visuals, including square main images, promotional sticker images, white-background variants, buyer-show style images, localized marketing graphics, detail pages, and activity posters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask users to provide an API key in chat.

Mitigation: Use a narrowly scoped, revocable API key and prefer a local secret mechanism such as an environment variable instead of sharing the key in chat or logs.

Risk: The skill installs mutable third-party command-line tooling.

Mitigation: Pin or review the qhkit CLI package version before installation, especially in sensitive or production environments.

Risk: Product images are uploaded to the qhkit service for generation.

Mitigation: Upload only assets approved for third-party processing and avoid confidential product imagery unless the service terms and data-handling posture are acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-shopee-image)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Markdown, Image URLs]

**Output Format:** [Markdown with qhkit CLI commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit CLI access and a configured Qinghu API key; product images may be uploaded to the qhkit service during generation.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
