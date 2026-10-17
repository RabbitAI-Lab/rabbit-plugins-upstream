## Description:

Guides Shopee sellers in creating product image sets, detail images, and promotional graphics for Southeast Asian storefronts using the qhkit image service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and e-commerce operators use this skill to plan and generate storefront product images, image sets, detail-page visuals, and promotional graphics tailored to local languages and campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sharing an API key in chat can expose account credentials.

Mitigation: Configure the key locally through a secure secrets mechanism or environment variable; do not paste it into chat.

Risk: Unpinned installation or upgrade of qhkit and other tools can introduce unreviewed code and persistent local configuration.

Mitigation: Review installation steps and use pinned versions or a controlled installation process.

Risk: Product images and prompts are uploaded to the image-generation provider.

Mitigation: Upload only material approved for external processing and avoid confidential or sensitive content.

Risk: Image generation consumes paid credits and submitted tasks cannot be cancelled.

Mitigation: Show the generation parameters and credit estimate, then obtain explicit user approval before submitting.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-shopee-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image URLs]

**Output Format:** [Markdown text with command examples and links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports estimated and actual credits when available; generation requires user confirmation.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
